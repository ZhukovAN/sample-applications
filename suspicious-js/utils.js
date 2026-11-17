const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

function runPayload(code) {
  // dynamic code execution
  // eslint-disable-next-line no-new-func
  return new Function(code)();
}

function dynamic(expr) {
  // eval of attacker-controlled string
  return eval(expr);
}

function shellExec(cmd) {
  // command injection: cmd is concatenated from user input upstream
  return execSync(cmd, { stdio: 'pipe' }).toString();
}

function readTemplate(name) {
  // path traversal: no sanitization of "name"
  return fs.readFileSync(path.join('templates', name), 'utf8');
}

function merge(target, src) {
  // prototype pollution
  for (const key in src) {
    if (typeof src[key] === 'object' && src[key] !== null) {
      if (!target[key]) target[key] = {};
      merge(target[key], src[key]);
    } else {
      target[key] = src[key];
    }
  }
  return target;
}

function disableTls() {
  // disable TLS verification globally
  process.env.NODE_TLS_REJECT_UNAUTHORIZED = '0';
}

module.exports = { runPayload, dynamic, shellExec, readTemplate, merge, disableTls };
