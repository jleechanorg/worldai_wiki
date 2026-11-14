/* global firebase */
'use strict';
document.addEventListener('DOMContentLoaded', () => {
  const status = document.getElementById('status');
  const result = document.getElementById('result');
  let authGeneration = 0;
  let requestGeneration = 0;
  const current = context => context.authGeneration === authGeneration &&
    context.requestGeneration === requestGeneration &&
    firebase.auth().currentUser === context.user;
  const begin = () => ({ user: firebase.auth().currentUser, authGeneration, requestGeneration: ++requestGeneration });
  const check = context => { if (!current(context)) throw new Error('Account or request changed'); };
  const showError = context => { if (current(context)) status.textContent = 'Request failed. Check your verified sign-in and try deliberately. No campaign change is assumed.'; };
  async function call(context, action, body) {
    check(context);
    const user = context.user;
    if (!user || !user.emailVerified) throw new Error('Verified sign-in required');
    const token = await user.getIdToken();
    check(context);
    const response = await fetch('/api/mini-recovery/' + action, {
      method: 'POST', headers: { 'Content-Type': 'application/json', Authorization: 'Bearer ' + token },
      body: JSON.stringify(body), cache: 'no-store', credentials: 'same-origin',
    });
    check(context);
    if (!response.ok) throw new Error('Request rejected');
    const data = await response.json();
    check(context);
    return data;
  }
  async function list(context) {
    const data = await call(context, 'list', {});
    check(context);
    const root = document.getElementById('campaigns'); root.replaceChildren();
    for (const session of data.sessions) {
      const li = document.createElement('li');
      const title = document.createElement('span'); title.textContent = session.title || session.session_id;
      const button = document.createElement('button'); button.textContent = 'Recover new private capability';
      button.onclick = async () => {
        if (!current(context)) return;
        if (!window.confirm('Invalidate the old capability and issue a new one? Other chats using the old capability will stop working.')) return;
        const recovery = begin();
        button.disabled = true;
        try {
          const recovered = await call(recovery, 'recover', { session_id: session.session_id });
          check(recovery);
          result.hidden = false; result.textContent = 'Keep private. New resume capability:\n' + recovered.session_key + '\nSaved revision: ' + recovered.revision;
          status.textContent = 'Recovered. Old capability invalidated; story unchanged.';
        } catch (_) { showError(recovery); }
        finally { if (current(recovery)) button.disabled = false; }
      };
      li.append(title, button); root.append(li);
    }
    status.textContent = data.sessions.length ? 'Linked campaigns loaded.' : 'No linked campaigns for this verified account.';
  }
  document.getElementById('signin').onclick = async () => {
    const context = begin();
    try { await firebase.auth().signInWithPopup(new firebase.auth.GoogleAuthProvider()); } catch (_) { showError(context); }
  };
  firebase.auth().onAuthStateChanged(user => {
    authGeneration++; requestGeneration++;
    result.hidden = true; result.textContent = ''; document.getElementById('campaigns').replaceChildren(); document.getElementById('capability').value = ''; status.textContent = '';
    document.getElementById('account').textContent = user && user.emailVerified ? 'Signed in with verified account: ' + user.email : 'Sign in with a verified email account to link or recover.';
  });
  document.getElementById('signout').onclick = () => {
    authGeneration++;
    const context = begin();
    result.hidden = true; result.textContent = ''; document.getElementById('campaigns').replaceChildren();
    return firebase.auth().signOut().catch(() => showError(context));
  };
  document.getElementById('remove').onclick = async () => {
    if (!window.confirm('Remove your recovery email and all linked campaigns? Keep your private capability first. Campaigns and current capabilities are not deleted or changed.')) return;
    const context = begin();
    try {
      await call(context, 'remove', {}); check(context);
      result.hidden = true; result.textContent = ''; document.getElementById('campaigns').replaceChildren(); document.getElementById('consent').checked = false;
      status.textContent = 'Recovery email and links removed. Keep your private capability to continue anonymous play.';
    } catch (_) { showError(context); }
  };
  document.getElementById('refresh').onclick = () => { const context = begin(); return list(context).catch(() => showError(context)); };
  document.getElementById('link').onsubmit = async event => {
    event.preventDefault(); const field = document.getElementById('capability'); const context = begin();
    try { await call(context, 'link', { session_key: field.value, consent: document.getElementById('consent').checked }); check(context); field.value = ''; await list(context); }
    catch (_) { showError(context); }
  };
});
