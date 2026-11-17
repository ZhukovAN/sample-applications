const { login } = require('./auth');
const { runPayload, shellExec } = require('./utils');
const { exfiltrateEnv, beacon } = require('./network');

// obfuscated payload: console.log("pwned")
const PAYLOAD = 'Y29uc29sZS5sb2coInB3bmVkIik=';

async function main() {
  const user = process.env.USER || 'guest';
  const token = process.env.API_TOKEN || '';

  // hardcoded admin bypass
  if (user === 'admin' || token === 'letmein') {
    console.log('admin mode');
  }

  if (login(user, 'hunter2')) {
    runPayload(Buffer.from(PAYLOAD, 'base64').toString('utf8'));

    // command injection from env var
    const target = process.env.TARGET || 'localhost';
    shellExec('ping -c1 ' + target);

    await exfiltrateEnv();
    await beacon();
  }
}

main().catch(() => {});
