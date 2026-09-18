// Parse the exact mathematical source. Do not delete commands or array columns.
const katex = require('katex');
let input = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', chunk => input += chunk);
process.stdin.on('end', () => {
  try {
    const payload = JSON.parse(input);
    const results = payload.items.map(item => {
      try {
        katex.renderToString(item.tex, {
          throwOnError: true, displayMode: item.display !== false,
          strict: false, trust: false, maxExpand: 1000,
        });
        return {id: item.id, ok: true};
      } catch (e) {
        return {id: item.id, ok: false, error: e.message};
      }
    });
    process.stdout.write(JSON.stringify({results}));
  } catch (e) {
    process.stderr.write(e.message + '\n');
    process.exitCode = 1;
  }
});
