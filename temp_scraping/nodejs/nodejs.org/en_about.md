Node.js — About Node.js®

[New security releases to be made available Wednesday, January 7, 2026](https://nodejs.org/en/blog/vulnerability/december-2025-security-releases)

[Learn](/en/learn)[About](/en/about)[Download](/en/download)[Blog](/en/blog)[Docs](https://nodejs.org/docs/latest/api/)[Contribute](https://github.com/nodejs/node/blob/main/CONTRIBUTING.md)[Courses](https://training.linuxfoundation.org/openjs/)

Start typing...

⌘ K

Change pageAbout Node.js®

Change pageAbout Node.js®

About Node.js

[About Node.js®](/en/about)[Node.js Releases](/en/about/previous-releases)[Security Reporting](/en/about/security-reporting)[Project Governance](/en/about/governance)[Partners & Supporters](/en/about/partners)[Branding of Node.js](/en/about/branding)[End-of-Life (EOL)](/en/about/eol)

Get Involved

[Get Involved](/en/about/get-involved)[Collaboration Summit](/en/about/get-involved/collab-summit)[Upcoming Events](/en/about/get-involved/events)[Contribute to Node.js](https://github.com/nodejs/node/blob/main/CONTRIBUTING.md)[Code of Conduct](https://github.com/nodejs/admin/blob/main/CODE_OF_CONDUCT.md)

About Node.js

[About Node.js®](/en/about)[Node.js Releases](/en/about/previous-releases)[Security Reporting](/en/about/security-reporting)[Project Governance](/en/about/governance)[Partners & Supporters](/en/about/partners)[Branding of Node.js](/en/about/branding)[End-of-Life (EOL)](/en/about/eol)

Get Involved

[Get Involved](/en/about/get-involved)[Collaboration Summit](/en/about/get-involved/collab-summit)[Upcoming Events](/en/about/get-involved/events)[Contribute to Node.js](https://github.com/nodejs/node/blob/main/CONTRIBUTING.md)[Code of Conduct](https://github.com/nodejs/admin/blob/main/CODE_OF_CONDUCT.md)

# [About Node.js®](#about-nodejs)

As an asynchronous event-driven JavaScript runtime, Node.js is designed to build
scalable network applications. In the following "hello world" example, many
connections can be handled concurrently. Upon each connection, the callback is
fired, but if there is no work to be done, Node.js will sleep.

CJSESM

```
const { createServer } = require('node:http');

const hostname = '127.0.0.1';
const port = 3000;

const server = createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
```

JavaScriptCopy to clipboard

This is in contrast to today's more common concurrency model, in which OS threads
are employed. Thread-based networking is relatively inefficient and very
difficult to use. Furthermore, users of Node.js are free from worries of
dead-locking the process, since there are no locks. Almost no function in
Node.js directly performs I/O, so the process never blocks except when the I/O is performed using
synchronous methods of Node.js standard library. Because nothing blocks, scalable systems are very
reasonable to develop in Node.js.

If some of this language is unfamiliar, there is a full article on
[Blocking vs. Non-Blocking](/en/learn/asynchronous-work/overview-of-blocking-vs-non-blocking).

---

Node.js is similar in design to, and influenced by, systems like Ruby's
[Event Machine](https://github.com/eventmachine/eventmachine) and Python's [Twisted](https://twisted.org/). Node.js takes the event model a bit
further. It presents an event loop as a runtime construct instead of as a library. In other systems,
there is always a blocking call to start the event-loop.
Typically, behavior is defined through callbacks at the beginning of a script, and
at the end a server is started through a blocking call like `EventMachine::run()`.
In Node.js, there is no such start-the-event-loop call. Node.js simply enters the event loop after executing the input script. Node.js
exits the event loop when there are no more callbacks to perform. This behavior
is like browser JavaScript — the event loop is hidden from the user.

HTTP is a first-class citizen in Node.js, designed with streaming and low
latency in mind. This makes Node.js well suited for the foundation of a web
library or framework.

Node.js being designed without threads doesn't mean you can't take
advantage of multiple cores in your environment. Child processes can be spawned
by using our [`child_process.fork()`](https://nodejs.org/api/child_process.html) API, and are designed to be easy to
communicate with. Built upon that same interface is the [`cluster`](https://nodejs.org/api/cluster.html) module,
which allows you to share sockets between processes to enable load balancing
over your cores.

## [Official Node.js Resources](#official-nodejs-resources)

To ensure authenticity and security when working with Node.js, always use official sources. Avoid trusting emails,
binaries, or downloads from unofficial sources.

### [Official Node.js Domains](#official-nodejs-domains)

For downloading Node.js binaries and accessing official documentation, use only these domains:

* [nodejs.org](https://nodejs.org)
* [nodejs.dev](https://nodejs.dev) *(Redirects to <https://nodejs.org>)*
* [iojs.org](https://iojs.org) *(Redirects to <https://nodejs.org>)*

### [Official npm Packages](#official-npm-packages)

The Node.js team maintains the following official npm package scopes:

* [`@node-core`](https://npmjs.com/~node-core)
* [`@pkgjs`](https://npmjs.com/~pkgjs)

Additionally, the Node.js team maintains packages published by the [`nodejs-foundation`](https://npmjs.com/~nodejs-foundation) npm account,
though other Node.js-related packages (like [`undici`](https://www.npmjs.com/package/undici)) may also be maintained by contributors closely
tied to the project.

Using packages from the Node.js team guarantees that you are working with officially supported Node.js components.

### [Official GitHub Organizations](#official-github-organizations)

Node.js and related projects are maintained under these official GitHub organizations:

* [nodejs](https://github.com/nodejs)
* [pkgjs](https://github.com/pkgjs)

### [Official Communication Channels](#official-communication-channels)

Node.js and the OpenJS Foundation communicate through various official and community-supported channels. You can find details on
how to get involved on the [Get Involved](https://nodejs.org/en/about/get-involved) page.

### [Reporting Website Issues & Downtime](#reporting-website-issues--downtime)

If you encounter issues with the Node.js website, report them at the [Node.js website repository](https://github.com/nodejs/nodejs.org/issues).
For real-time updates on outages, visit the [Node.js Status Page](https://status.nodejs.org).

Reading Time
:   3 min

Contribute
:   [Edit this page](https://github.com/nodejs/nodejs.org/blob/main/apps/site/pages/en/about/index.mdx)

Table of Contents
:   1. [Official Node.js Resources](#official-nodejs-resources)
    2. [Official Node.js Domains](#official-nodejs-domains)
    3. [Official npm Packages](#official-npm-packages)
    4. [Official GitHub Organizations](#official-github-organizations)
    5. [Official Communication Channels](#official-communication-channels)
    6. [Reporting Website Issues & Downtime](#reporting-website-issues--downtime)

1. [Navigate to Home](/en)
2. About Node.js

[v24.12.0Latest LTS](/blog/release/v24.12.0)[v25.2.1Latest Release](/blog/release/v25.2.1)

[Trademark Policy](https://trademark-policy.openjsf.org/)[Privacy Policy](https://privacy-policy.openjsf.org/)[Code of Conduct](https://github.com/openjs-foundation/cross-project-council/blob/main/CODE_OF_CONDUCT.md)[Security Policy](https://github.com/nodejs/node/security/policy)

[© OpenJS Foundation](https://openjsf.org/)