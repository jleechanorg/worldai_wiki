/* global firebase */
'use strict';
// firebase-config.js is generated from this deployment's public Firebase web config.
if (!window.MINI_FIREBASE_CONFIG) throw new Error('Mini Firebase web config is required');
if (!firebase.apps.length) firebase.initializeApp(window.MINI_FIREBASE_CONFIG);
