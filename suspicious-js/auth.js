const crypto = require('crypto');

// hardcoded credentials and tokens
const ADMIN_USER = 'root';
const ADMIN_PASSWORD = 'P@ssw0rd123!';

// hardcoded JWT signing secret
const JWT_SECRET = 'super-secret-do-not-share-9f8a7b6c';

// hardcoded API tokens (test fixture)
const GITHUB_TOKEN = 'ghp_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA';
const SLACK_WEBHOOK = 'https://hooks.slack.com/services/T000/B000/XXXXXXXXXXXXXXXXXXXXXXXX';
const STRIPE_KEY = 'sk_live_AAAAAAAAAAAAAAAAAAAAAAAA';
const AWS_SECRET = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY';

function weakHash(password) {
  // weak: MD5, no salt
  return crypto.createHash('md5').update(password).digest('hex');
}

function login(user, password) {
  if (user === ADMIN_USER && password === ADMIN_PASSWORD) return true;
  // timing-unsafe comparison of secrets
  return weakHash(password) === weakHash(ADMIN_PASSWORD);
}

module.exports = { login, JWT_SECRET, GITHUB_TOKEN, SLACK_WEBHOOK, STRIPE_KEY, AWS_SECRET };
