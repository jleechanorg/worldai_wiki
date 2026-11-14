"""Direct Firestore adapter. No session caches, queries, or added retry policy."""

import json
from datetime import datetime

from google.cloud import firestore

from mvp_site.mini_wire import canonical


def pack_document(value):
    packed = {"document_json": canonical(value)}
    if "provenance" in value:
        packed["provenance"] = dict(value["provenance"])
    if "expires_at" in value:
        packed["ttl_at"] = datetime.fromisoformat(value["expires_at"])
    return packed


def unpack_document(value):
    if value is None:
        return None
    if "document_json" in value:
        return json.loads(value["document_json"])
    result = dict(value)
    result.pop("ttl_at", None)
    return result


class FirestoreStore:
    def __init__(self, db):
        self.db = db

    def get(self, collection, key):
        snapshot = (
            self.db.collection(collection).document(key).get(timeout=3.0, retry=None)
        )
        value = snapshot.to_dict() if snapshot.exists else None
        return unpack_document(value)

    def set(self, collection, key, value):
        self.db.collection(collection).document(key).set(pack_document(value))

    def transaction(self, callback):
        transaction = self.db.transaction()

        @firestore.transactional
        def run(tx):
            adapter = TransactionStore(self.db, tx)
            result = callback(adapter)
            adapter.flush()
            return result

        return run(transaction)


class TransactionStore:
    def __init__(self, db, tx):
        self.db = db
        self.tx = tx
        self.pending = []

    def get(self, collection, key):
        snapshot = self.db.collection(collection).document(key).get(transaction=self.tx)
        value = snapshot.to_dict() if snapshot.exists else None
        return unpack_document(value)

    def set(self, collection, key, value):
        self.pending.append((collection, key, value))

    def flush(self):
        for collection, key, value in self.pending:
            self.tx.set(
                self.db.collection(collection).document(key), pack_document(value)
            )
