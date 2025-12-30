Node.js — Run JavaScript Everywhere

[New security releases to be made available Wednesday, January 7, 2026](https://nodejs.org/en/blog/vulnerability/december-2025-security-releases)

[Learn](/en/learn)[About](/en/about)[Download](/en/download)[Blog](/en/blog)[Docs](https://nodejs.org/docs/latest/api/)[Contribute](https://github.com/nodejs/node/blob/main/CONTRIBUTING.md)[Courses](https://training.linuxfoundation.org/openjs/)

Start typing...

⌘ K

# Run JavaScript Everywhere

Node.js® is a free, open-source, cross-platform JavaScript runtime environment
that lets developers create servers, web apps, command line tools and scripts.

[Get Node.js®](/en/download)[Get Node.js®](/en/download)[Get security support  
for EOL Node.js versions](/en/about/eol)Node.js is proudly supported by the partners above [and more](/en/about/partners).

Create an HTTP ServerWrite TestsRead and Hash a FileStreams PipelineWork with Threads

```
// server.mjs
import { createServer } from 'node:http';

const server = createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello World!\n');
});

// starts a simple http server locally on port 3000
server.listen(3000, '127.0.0.1', () => {
  console.log('Listening on 127.0.0.1:3000');
});

// run with `node server.mjs`
```

JavaScriptCopy to clipboard

Learn more what Node.js is able to offer with our [Learning materials](/en/learn).

[v24.12.0Latest LTS](/blog/release/v24.12.0)[v25.2.1Latest Release](/blog/release/v25.2.1)

[Trademark Policy](https://trademark-policy.openjsf.org/)[Privacy Policy](https://privacy-policy.openjsf.org/)[Code of Conduct](https://github.com/openjs-foundation/cross-project-council/blob/main/CODE_OF_CONDUCT.md)[Security Policy](https://github.com/nodejs/node/security/policy)

[© OpenJS Foundation](https://openjsf.org/)