# suspicious-js

Test fixture only. Contains intentionally malicious patterns:

- `index.js` — entry point, runs base64-decoded payload via `Function`
- `auth.js` — hardcoded API tokens and signing secrets, weak crypto
- `utils.js` — `eval`, prototype pollution, path traversal
- `network.js` — exfiltrates env vars and `~/.ssh/id_rsa`; C2 beacon
- `postinstall.js` — invoked by `npm install`, downloads and runs remote code
- `package.json` — `postinstall` script, typosquatted dependencies

Do not execute. Do not run `npm install` in this directory.
