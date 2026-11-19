"""Mini-only bounded dice primitives, extracted from WorldAI shared dice."""

import random

import re

_DICE_RNG = random

_MAX_DICE_COUNT = 100
_MAX_DIE_SIZE = 1000
_MAX_DICE_MODIFIER_ABS = 1_000_000
_MAX_DICE_NOTATION_LENGTH = 64
# Bounds the number of additive "NdM" dice-pool terms a single notation string
# may contain (e.g. "1d8+3+2d8" has 2 terms). Defense-in-depth alongside
# _MAX_DICE_NOTATION_LENGTH, which already limits how many terms can fit.
_MAX_DICE_TERMS = 10

# Matches one signed dice-pool term ("+2d8", "-1d4") or one signed integer
# modifier term ("+3", "-2") within a normalized (lowercased, space-stripped)
# notation string. Consumed left-to-right by _parse_bounded_dice_notation so
# terms can appear in any order, matching how models actually compose
# compound damage (e.g. weapon dice, then a flat modifier, then bonus dice).
_DICE_TERM_PATTERN = re.compile(r"([+-]?)(\d+)d(\d+)|([+-]?)(\d+)(?!d)")

# Matches a leading "roll N times" multiplier prefix (e.g. "4x 1d20+7",
# "2x1d8+4", "4x1d20"). D&D models emit this when executing multiple attacks
# in a single turn. The multiplier is captured and returned as a 3rd element
# so the audit pipeline can route multi-attack rolls to the compound bucket
# (skipping per-die impossible-face checks on the mixed result inventory).
_ROLL_MULTIPLIER_PREFIX = re.compile(r"^(\d+)x[\s\t]*(?=\d)", re.IGNORECASE)


def _parse_bounded_dice_notation(  # noqa: PLR0911, PLR0912
    notation: object,
) -> tuple[list[tuple[int, int]], int, int] | None:
    """Parse one or more additive dice-pool terms plus one aggregate modifier.

    Supports both a single dice group ("2d6+3", the historical case) and
    multiple additive dice-pool terms combined with weapon/spell damage, e.g.
    "1d8+3+2d8" for a longsword attack (1d8+3) plus Divine Smite (+2d8) - a
    real D&D 5e mechanic that the single-term-only parser used to reject
    outright (rev-euebc), aborting the whole AGY turn. Returns
    (pools, modifier, multiplier) where pools is a list of (num_dice, die_size) pairs,
    modifier is the scalar bonus/penalty, and multiplier is the number of times
    the roll is repeated (1 by default, >1 for "Nx <notation>"), or None if the
    notation is malformed or exceeds resource bounds. Subtracting a whole dice pool
    (e.g. "2d6-1d4") is not a supported D&D mechanic and is rejected.
    """
    if not isinstance(notation, str):
        return None
    # Bound the raw string before normalization/lowering touches it, not just
    # after, so an arbitrarily large input can't be fully copied first.
    if len(notation) > _MAX_DICE_NOTATION_LENGTH:
        return None
    normalized = notation.lower().replace(" ", "")
    if not normalized or len(normalized) > _MAX_DICE_NOTATION_LENGTH:
        return None

    # Detect a leading "roll N times" prefix (e.g. "4x 1d20+7", "2x1d8+4").
    # The prefix is matched against the original notation so it does not
    # collide with dice terms like "1d20" that happen to start with digits
    # (the "x" in "1d20" is not preceded by a leading digit, so the prefix
    # regex won't match). A multiplier < 2 is treated as no prefix so
    # "1x 1d20+7" preserves the historical "1d20" contract.
    multiplier = 1
    raw_match = _ROLL_MULTIPLIER_PREFIX.match(notation.lower().lstrip())
    if raw_match:
        try:
            parsed_multiplier = int(raw_match.group(1))
        except (ValueError, OverflowError):
            return None
        if parsed_multiplier < 2:
            multiplier = 1
        else:
            multiplier = parsed_multiplier
            # Strip the prefix (including any optional whitespace between
            # the "x" and the dice term) from the RAW notation before
            # normalization. We then re-run the lower() + space-strip so
            # the term loop sees only the inner dice notation. Slicing
            # `normalized` directly is unsafe because spaces in the prefix
            # were already removed — slicing would land mid-dice-term
            # (e.g. "4x 1d20+7" → normalized "4x1d20+7" → strip 3 chars
            # → "d20+7", which is an unparseable dice-less tail).
            stripped_raw = notation[raw_match.end() :].lstrip()
            if not stripped_raw or len(stripped_raw) > _MAX_DICE_NOTATION_LENGTH:
                return None
            normalized = stripped_raw.lower().replace(" ", "")
            if not normalized or len(normalized) > _MAX_DICE_NOTATION_LENGTH:
                return None

    pools: list[tuple[int, int]] = []
    modifier = 0
    pos = 0
    while pos < len(normalized):
        match = _DICE_TERM_PATTERN.match(normalized, pos)
        if not match or match.start() != pos:
            return None
        dice_sign, dice_count, dice_size, mod_sign, mod_value = match.groups()
        try:
            if dice_count is not None:
                if dice_sign == "-":
                    # Subtracting a dice pool isn't a supported mechanic.
                    return None
                if len(pools) >= _MAX_DICE_TERMS:
                    return None
                pools.append((int(dice_count), int(dice_size)))
            else:
                sign = -1 if mod_sign == "-" else 1
                modifier += sign * int(mod_value)
        except (ValueError, OverflowError):
            return None
        pos = match.end()

    if not pools:
        return None
    total_dice = sum(num_dice for num_dice, _ in pools)
    if (
        not 1 <= total_dice <= _MAX_DICE_COUNT
        or any(not 1 <= die_size <= _MAX_DIE_SIZE for _, die_size in pools)
        or any(num_dice < 1 for num_dice, _ in pools)
        or abs(modifier) > _MAX_DICE_MODIFIER_ABS
    ):
        return None
    return pools, modifier, multiplier


def roll_bounded_pools(pools, modifier, *, advantage=False, rng=None):
    """Execute already validated shared pools without logging caller content.

    Mini uses this narrow primitive, never the provider/tool dispatcher.
    """
    source = rng or _DICE_RNG
    actual = [(2, 20)] if advantage else pools
    rolled_pools = [
        {
            "count": count,
            "sides": sides,
            "faces": [source.randint(1, sides) for _ in range(count)],
        }
        for count, sides in actual
    ]
    faces = [face for pool in rolled_pools for face in pool["faces"]]
    return {
        "raw_faces": faces,
        "pools": rolled_pools,
        "modifier": modifier,
        "total": sum(faces) + modifier,
    }
