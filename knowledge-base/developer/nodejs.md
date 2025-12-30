# Nodejs Knowledge

> Category: frameworks


## Source: en.md

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

---

## Source: en_about.md

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

---

## Source: en_blog_vulnerability_december-2025-security-releases.md

Node.js — Wednesday, January 7, 2026 Security Releases

[New security releases to be made available Wednesday, January 7, 2026](https://nodejs.org/en/blog/vulnerability/december-2025-security-releases)

[Learn](/en/learn)[About](/en/about)[Download](/en/download)[Blog](/en/blog)[Docs](https://nodejs.org/docs/latest/api/)[Contribute](https://github.com/nodejs/node/blob/main/CONTRIBUTING.md)[Courses](https://training.linuxfoundation.org/openjs/)

Start typing...

⌘ K

Commercial support for versions past the Maintenance LTS phase is available through our [OpenJS Ecosystem Sustainability Program partners](/en/about/eol)

# Wednesday, January 7, 2026 Security Releases

[TNJP](https://github.com/nodejs)

The Node.js Project

Wednesday, January 7, 2026 Security Releases

## [(Update 17-Dec-2025) Security Release target January 7th](#update-17-dec-2025-security-release-target-january-7th)

We have decided to delay the release further to Wednesday, January 7th, 2026. Many of the
downstream projects and users are on holiday break at the end of the year, and the security
release will disclose the vulnerabilities being fixed as soon as the patches are available.
We want to make sure that most users are no longer on holiday when they evaluate whether
they are affected and need to perform time-sensitive upgrades.

## [(Update 15-Dec-2025) Security Release target December 18th](#update-15-dec-2025-security-release-target-december-18th)

The team is still working on a particularly challenging patch, for this reason
the release is being postponed to Thursday, December 18th or shortly after.

# [Summary](#summary)

The Node.js project will release new versions of the 25.x, 24.x, 22.x, 20.x
releases lines on or shortly after, Monday, December 15, 2025 in order to address:

* 3 high severity issues.
* 1 low severity issue.
* 1 medium severity issue.

## [Impact](#impact)

The 25.x release line of Node.js is vulnerable to 3 high severity issues, 1 low severity issue.
The 24.x release line of Node.js is vulnerable to 3 high severity issues, 1 low severity issue, 1 medium severity issue.
The 22.x release line of Node.js is vulnerable to 3 high severity issues, 1 low severity issue, 1 medium severity issue.
The 20.x release line of Node.js is vulnerable to 3 high severity issues, 1 low severity issue, 1 medium severity issue.

It's important to note that End-of-Life versions are always affected when a security release occurs.
To ensure your system's security, please use an up-to-date version as outlined in our
[Release Schedule](https://github.com/nodejs/release#release-schedule).

## [Release timing](#release-timing)

Releases will be available on, or shortly after, Monday, December 15, 2025.

## [Contact and future updates](#contact-and-future-updates)

The current Node.js security policy can be found at <https://nodejs.org/en/security/>.
Please follow the process outlined in <https://github.com/nodejs/node/blob/master/SECURITY.md> if you wish to report a vulnerability in Node.js.

Subscribe to the low-volume announcement-only nodejs-sec mailing list at <https://groups.google.com/forum/#!forum/nodejs-sec> to stay up to date on security vulnerabilities and security-related releases of Node.js and the projects maintained in the nodejs GitHub organization.

[NextTuesday, July 15, 2025 Security Releases](/en/blog/vulnerability/july-2025-security-releases)

Last Updated
:   Dec 08, 2025

Reading Time
:   2 min

Contribute
:   [Edit this page](https://github.com/nodejs/nodejs.org/blob/main/apps/site/pages/en/blog/vulnerability/december-2025-security-releases.md)

Table of Contents
:   1. [(Update 17-Dec-2025) Security Release target January 7th](#update-17-dec-2025-security-release-target-january-7th)
    2. [(Update 15-Dec-2025) Security Release target December 18th](#update-15-dec-2025-security-release-target-december-18th)
    3. [Impact](#impact)
    4. [Release timing](#release-timing)
    5. [Contact and future updates](#contact-and-future-updates)

[v24.12.0Latest LTS](/blog/release/v24.12.0)[v25.2.1Latest Release](/blog/release/v25.2.1)

[Trademark Policy](https://trademark-policy.openjsf.org/)[Privacy Policy](https://privacy-policy.openjsf.org/)[Code of Conduct](https://github.com/openjs-foundation/cross-project-council/blob/main/CODE_OF_CONDUCT.md)[Security Policy](https://github.com/nodejs/node/security/policy)

[© OpenJS Foundation](https://openjsf.org/)

---

## Source: en_docs_guides.md

Node.js — Introduction to Node.js

[New security releases to be made available Wednesday, January 7, 2026](https://nodejs.org/en/blog/vulnerability/december-2025-security-releases)

[Learn](/en/learn)[About](/en/about)[Download](/en/download)[Blog](/en/blog)[Docs](https://nodejs.org/docs/latest/api/)[Contribute](https://github.com/nodejs/node/blob/main/CONTRIBUTING.md)[Courses](https://training.linuxfoundation.org/openjs/)

Start typing...

⌘ K

Change pageIntroduction to Node.js

Change pageIntroduction to Node.js

Getting Started

[Introduction to Node.js](/en/learn/getting-started/introduction-to-nodejs)[How much JavaScript do you need to know to use Node.js?](/en/learn/getting-started/how-much-javascript-do-you-need-to-know-to-use-nodejs)[Differences between Node.js and the Browser](/en/learn/getting-started/differences-between-nodejs-and-the-browser)[The V8 JavaScript Engine](/en/learn/getting-started/the-v8-javascript-engine)[An introduction to the npm package manager](/en/learn/getting-started/an-introduction-to-the-npm-package-manager)[ECMAScript 2015 (ES6) and beyond](/en/learn/getting-started/ecmascript-2015-es6-and-beyond)[Debugging Node.js](/en/learn/getting-started/debugging)[Fetching data with Node.js](/en/learn/getting-started/fetch)[WebSocket client with Node.js](/en/learn/getting-started/websocket)[Node.js, the difference between development and production](/en/learn/getting-started/nodejs-the-difference-between-development-and-production)[Profiling Node.js Applications](/en/learn/getting-started/profiling)[Node.js with WebAssembly](/en/learn/getting-started/nodejs-with-webassembly)[Security Best Practices](/en/learn/getting-started/security-best-practices)[Introduction to Userland Migrations](/en/learn/getting-started/userland-migrations)

Command Line

[Run Node.js scripts from the command line](/en/learn/command-line/run-nodejs-scripts-from-the-command-line)[How to use the Node.js REPL](/en/learn/command-line/how-to-use-the-nodejs-repl)[Output to the command line using Node.js](/en/learn/command-line/output-to-the-command-line-using-nodejs)[Accept input from the command line in Node.js](/en/learn/command-line/accept-input-from-the-command-line-in-nodejs)[How to read environment variables from Node.js](/en/learn/command-line/how-to-read-environment-variables-from-nodejs)

HTTP

[Anatomy of an HTTP Transaction](/en/learn/http/anatomy-of-an-http-transaction)[Enterprise Network Configuration](/en/learn/http/enterprise-network-configuration)

Manipulating Files

[Node.js file stats](/en/learn/manipulating-files/nodejs-file-stats)[Node.js File Paths](/en/learn/manipulating-files/nodejs-file-paths)[Reading files with Node.js](/en/learn/manipulating-files/reading-files-with-nodejs)[Writing files with Node.js](/en/learn/manipulating-files/writing-files-with-nodejs)[Working with file descriptors in Node.js](/en/learn/manipulating-files/working-with-file-descriptors-in-nodejs)[Working with folders in Node.js](/en/learn/manipulating-files/working-with-folders-in-nodejs)[How to work with Different Filesystems](/en/learn/manipulating-files/working-with-different-filesystems)

Asynchronous Work

[JavaScript Asynchronous Programming and Callbacks](/en/learn/asynchronous-work/javascript-asynchronous-programming-and-callbacks)[Asynchronous flow control](/en/learn/asynchronous-work/asynchronous-flow-control)[Discover Promises in Node.js](/en/learn/asynchronous-work/discover-promises-in-nodejs)[Discover JavaScript Timers](/en/learn/asynchronous-work/discover-javascript-timers)[Overview of Blocking vs Non-Blocking](/en/learn/asynchronous-work/overview-of-blocking-vs-non-blocking)[The Node.js Event Loop](/en/learn/asynchronous-work/event-loop-timers-and-nexttick)[The Node.js Event Emitter](/en/learn/asynchronous-work/the-nodejs-event-emitter)[Understanding process.nextTick()](/en/learn/asynchronous-work/understanding-processnexttick)[Understanding setImmediate()](/en/learn/asynchronous-work/understanding-setimmediate)[Don't Block the Event Loop](/en/learn/asynchronous-work/dont-block-the-event-loop)

TypeScript

[Introduction to TypeScript](/en/learn/typescript/introduction)[Running TypeScript Natively](/en/learn/typescript/run-natively)[Running TypeScript code using transpilation](/en/learn/typescript/transpile)[Running TypeScript with a runner](/en/learn/typescript/run)[Publishing a TypeScript package](/en/learn/typescript/publishing-a-ts-package)

Modules

[How to use streams](/en/learn/modules/how-to-use-streams)[Backpressuring in Streams](/en/learn/modules/backpressuring-in-streams)[Publishing a package](/en/learn/modules/publishing-a-package)[How to publish a Node-API package](/en/learn/modules/publishing-node-api-modules)[ABI Stability](/en/learn/modules/abi-stability)

Diagnostics

[User Journey](/en/learn/diagnostics/user-journey)[Memory](/en/learn/diagnostics/memory)[Live Debugging](/en/learn/diagnostics/live-debugging)[Poor Performance](/en/learn/diagnostics/poor-performance)[Flame Graphs](/en/learn/diagnostics/flame-graphs)

Test Runner

[Discovering Node.js's test runner](/en/learn/test-runner/introduction)[Using Node.js's test runner](/en/learn/test-runner/using-test-runner)[Mocking in tests](/en/learn/test-runner/mocking)[Collecting code coverage in Node.js](/en/learn/test-runner/collecting-code-coverage)

Getting Started

[Introduction to Node.js](/en/learn/getting-started/introduction-to-nodejs)[How much JavaScript do you need to know to use Node.js?](/en/learn/getting-started/how-much-javascript-do-you-need-to-know-to-use-nodejs)[Differences between Node.js and the Browser](/en/learn/getting-started/differences-between-nodejs-and-the-browser)[The V8 JavaScript Engine](/en/learn/getting-started/the-v8-javascript-engine)[An introduction to the npm package manager](/en/learn/getting-started/an-introduction-to-the-npm-package-manager)[ECMAScript 2015 (ES6) and beyond](/en/learn/getting-started/ecmascript-2015-es6-and-beyond)[Debugging Node.js](/en/learn/getting-started/debugging)[Fetching data with Node.js](/en/learn/getting-started/fetch)[WebSocket client with Node.js](/en/learn/getting-started/websocket)[Node.js, the difference between development and production](/en/learn/getting-started/nodejs-the-difference-between-development-and-production)[Profiling Node.js Applications](/en/learn/getting-started/profiling)[Node.js with WebAssembly](/en/learn/getting-started/nodejs-with-webassembly)[Security Best Practices](/en/learn/getting-started/security-best-practices)[Introduction to Userland Migrations](/en/learn/getting-started/userland-migrations)

Command Line

[Run Node.js scripts from the command line](/en/learn/command-line/run-nodejs-scripts-from-the-command-line)[How to use the Node.js REPL](/en/learn/command-line/how-to-use-the-nodejs-repl)[Output to the command line using Node.js](/en/learn/command-line/output-to-the-command-line-using-nodejs)[Accept input from the command line in Node.js](/en/learn/command-line/accept-input-from-the-command-line-in-nodejs)[How to read environment variables from Node.js](/en/learn/command-line/how-to-read-environment-variables-from-nodejs)

HTTP

[Anatomy of an HTTP Transaction](/en/learn/http/anatomy-of-an-http-transaction)[Enterprise Network Configuration](/en/learn/http/enterprise-network-configuration)

Manipulating Files

[Node.js file stats](/en/learn/manipulating-files/nodejs-file-stats)[Node.js File Paths](/en/learn/manipulating-files/nodejs-file-paths)[Reading files with Node.js](/en/learn/manipulating-files/reading-files-with-nodejs)[Writing files with Node.js](/en/learn/manipulating-files/writing-files-with-nodejs)[Working with file descriptors in Node.js](/en/learn/manipulating-files/working-with-file-descriptors-in-nodejs)[Working with folders in Node.js](/en/learn/manipulating-files/working-with-folders-in-nodejs)[How to work with Different Filesystems](/en/learn/manipulating-files/working-with-different-filesystems)

Asynchronous Work

[JavaScript Asynchronous Programming and Callbacks](/en/learn/asynchronous-work/javascript-asynchronous-programming-and-callbacks)[Asynchronous flow control](/en/learn/asynchronous-work/asynchronous-flow-control)[Discover Promises in Node.js](/en/learn/asynchronous-work/discover-promises-in-nodejs)[Discover JavaScript Timers](/en/learn/asynchronous-work/discover-javascript-timers)[Overview of Blocking vs Non-Blocking](/en/learn/asynchronous-work/overview-of-blocking-vs-non-blocking)[The Node.js Event Loop](/en/learn/asynchronous-work/event-loop-timers-and-nexttick)[The Node.js Event Emitter](/en/learn/asynchronous-work/the-nodejs-event-emitter)[Understanding process.nextTick()](/en/learn/asynchronous-work/understanding-processnexttick)[Understanding setImmediate()](/en/learn/asynchronous-work/understanding-setimmediate)[Don't Block the Event Loop](/en/learn/asynchronous-work/dont-block-the-event-loop)

TypeScript

[Introduction to TypeScript](/en/learn/typescript/introduction)[Running TypeScript Natively](/en/learn/typescript/run-natively)[Running TypeScript code using transpilation](/en/learn/typescript/transpile)[Running TypeScript with a runner](/en/learn/typescript/run)[Publishing a TypeScript package](/en/learn/typescript/publishing-a-ts-package)

Modules

[How to use streams](/en/learn/modules/how-to-use-streams)[Backpressuring in Streams](/en/learn/modules/backpressuring-in-streams)[Publishing a package](/en/learn/modules/publishing-a-package)[How to publish a Node-API package](/en/learn/modules/publishing-node-api-modules)[ABI Stability](/en/learn/modules/abi-stability)

Diagnostics

[User Journey](/en/learn/diagnostics/user-journey)[Memory](/en/learn/diagnostics/memory)[Live Debugging](/en/learn/diagnostics/live-debugging)[Poor Performance](/en/learn/diagnostics/poor-performance)[Flame Graphs](/en/learn/diagnostics/flame-graphs)

Test Runner

[Discovering Node.js's test runner](/en/learn/test-runner/introduction)[Using Node.js's test runner](/en/learn/test-runner/using-test-runner)[Mocking in tests](/en/learn/test-runner/mocking)[Collecting code coverage in Node.js](/en/learn/test-runner/collecting-code-coverage)

# [Introduction to Node.js](#introduction-to-nodejs)

Node.js is an open-source and cross-platform JavaScript runtime environment. It is a popular tool for almost any kind of project!

Node.js runs the V8 JavaScript engine, the core of Google Chrome, outside of the browser. This allows Node.js to be very performant.

A Node.js app runs in a single process, without creating a new thread for every request. Node.js provides a set of asynchronous I/O primitives in its standard library that prevent JavaScript code from blocking. In addition, libraries in Node.js are generally written using non-blocking paradigms. Accordingly, blocking behavior is the exception rather than the norm in Node.js.

When Node.js performs an I/O operation, like reading from the network, accessing a database or the filesystem, instead of blocking the thread and wasting CPU cycles waiting, Node.js will resume the operations when the response comes back.

This allows Node.js to handle thousands of concurrent connections with a single server without introducing the burden of managing thread concurrency, which could be a significant source of bugs.

Node.js has a unique advantage because millions of frontend developers that write JavaScript for the browser are now able to write the server-side code in addition to the client-side code without the need to learn a completely different language.

In Node.js the new ECMAScript standards can be used without problems, as you don't have to wait for all your users to update their browsers - you are in charge of deciding which ECMAScript version to use by changing the Node.js version, and you can also enable specific experimental features by running Node.js with flags.

## [An Example Node.js Application](#an-example-nodejs-application)

The most common example Hello World of Node.js is a web server:

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

To run this snippet, save it as a `server.js` file and run `node server.js` in your terminal.
If you use mjs version of the code, you should save it as a `server.mjs` file and run `node server.mjs` in your terminal.

This code first includes the Node.js [`http` module](https://nodejs.org/api/http.html).

Node.js has a fantastic [standard library](https://nodejs.org/api/), including first-class support for networking.

The `createServer()` method of `http` creates a new HTTP server and returns it.

The server is set to listen on the specified port and host name. When the server is ready, the callback function is called, in this case informing us that the server is running.

Whenever a new request is received, the [`request` event](https://nodejs.org/api/http.html#http_event_request) is called, providing two objects: a request (an [`http.IncomingMessage`](https://nodejs.org/api/http.html#http_class_http_incomingmessage) object) and a response (an [`http.ServerResponse`](https://nodejs.org/api/http.html#http_class_http_serverresponse) object).

Those 2 objects are essential to handle the HTTP call.

The first provides the request details. In this simple example, this is not used, but you could access the request headers and request data.

The second is used to return data to the caller.

In this case with:

```
res.statusCode = 200;
```

JavaScriptCopy to clipboard

we set the `statusCode` property to `200`, to indicate a successful response.

We set the `Content-Type` header:

```
res.setHeader('Content-Type', 'text/plain');
```

JavaScriptCopy to clipboard

and we close the response, adding the content as an argument to `end()`:

```
res.end('Hello World\n');
```

JavaScriptCopy to clipboard

If you haven't already done so, [download](https://nodejs.org/en/download) Node.js.

[NextHow much JavaScript do you need to know to use Node.js?](/en/learn/getting-started/how-much-javascript-do-you-need-to-know-to-use-nodejs)

Reading Time
:   3 min

Authors
:   [F](https://github.com/flaviocopes)[P](https://github.com/potch)[MB](https://github.com/mylesborins)[R](https://github.com/RomainLanz)[V](https://github.com/virkt25)[T](https://github.com/Trott)[O](https://github.com/onel0p3z)[O](https://github.com/ollelauribostrom)[M](https://github.com/MarkPieszak)+10

Contribute
:   [Edit this page](https://github.com/nodejs/nodejs.org/blob/main/apps/site/pages/en/learn/getting-started/introduction-to-nodejs.md)

Table of Contents
:   1. [An Example Node.js Application](#an-example-nodejs-application)

1. [Navigate to Home](/en)
2. Getting Started
3. [Introduction to Node.js](/en/learn/getting-started/introduction-to-nodejs)

[v24.12.0Latest LTS](/blog/release/v24.12.0)[v25.2.1Latest Release](/blog/release/v25.2.1)

[Trademark Policy](https://trademark-policy.openjsf.org/)[Privacy Policy](https://privacy-policy.openjsf.org/)[Code of Conduct](https://github.com/openjs-foundation/cross-project-council/blob/main/CODE_OF_CONDUCT.md)[Security Policy](https://github.com/nodejs/node/security/policy)

[© OpenJS Foundation](https://openjsf.org/)

---

## Source: en_learn.md

Node.js — Introduction to Node.js

[New security releases to be made available Wednesday, January 7, 2026](https://nodejs.org/en/blog/vulnerability/december-2025-security-releases)

[Learn](/en/learn)[About](/en/about)[Download](/en/download)[Blog](/en/blog)[Docs](https://nodejs.org/docs/latest/api/)[Contribute](https://github.com/nodejs/node/blob/main/CONTRIBUTING.md)[Courses](https://training.linuxfoundation.org/openjs/)

Start typing...

⌘ K

Change pageIntroduction to Node.js

Change pageIntroduction to Node.js

Getting Started

[Introduction to Node.js](/en/learn/getting-started/introduction-to-nodejs)[How much JavaScript do you need to know to use Node.js?](/en/learn/getting-started/how-much-javascript-do-you-need-to-know-to-use-nodejs)[Differences between Node.js and the Browser](/en/learn/getting-started/differences-between-nodejs-and-the-browser)[The V8 JavaScript Engine](/en/learn/getting-started/the-v8-javascript-engine)[An introduction to the npm package manager](/en/learn/getting-started/an-introduction-to-the-npm-package-manager)[ECMAScript 2015 (ES6) and beyond](/en/learn/getting-started/ecmascript-2015-es6-and-beyond)[Debugging Node.js](/en/learn/getting-started/debugging)[Fetching data with Node.js](/en/learn/getting-started/fetch)[WebSocket client with Node.js](/en/learn/getting-started/websocket)[Node.js, the difference between development and production](/en/learn/getting-started/nodejs-the-difference-between-development-and-production)[Profiling Node.js Applications](/en/learn/getting-started/profiling)[Node.js with WebAssembly](/en/learn/getting-started/nodejs-with-webassembly)[Security Best Practices](/en/learn/getting-started/security-best-practices)[Introduction to Userland Migrations](/en/learn/getting-started/userland-migrations)

Command Line

[Run Node.js scripts from the command line](/en/learn/command-line/run-nodejs-scripts-from-the-command-line)[How to use the Node.js REPL](/en/learn/command-line/how-to-use-the-nodejs-repl)[Output to the command line using Node.js](/en/learn/command-line/output-to-the-command-line-using-nodejs)[Accept input from the command line in Node.js](/en/learn/command-line/accept-input-from-the-command-line-in-nodejs)[How to read environment variables from Node.js](/en/learn/command-line/how-to-read-environment-variables-from-nodejs)

HTTP

[Anatomy of an HTTP Transaction](/en/learn/http/anatomy-of-an-http-transaction)[Enterprise Network Configuration](/en/learn/http/enterprise-network-configuration)

Manipulating Files

[Node.js file stats](/en/learn/manipulating-files/nodejs-file-stats)[Node.js File Paths](/en/learn/manipulating-files/nodejs-file-paths)[Reading files with Node.js](/en/learn/manipulating-files/reading-files-with-nodejs)[Writing files with Node.js](/en/learn/manipulating-files/writing-files-with-nodejs)[Working with file descriptors in Node.js](/en/learn/manipulating-files/working-with-file-descriptors-in-nodejs)[Working with folders in Node.js](/en/learn/manipulating-files/working-with-folders-in-nodejs)[How to work with Different Filesystems](/en/learn/manipulating-files/working-with-different-filesystems)

Asynchronous Work

[JavaScript Asynchronous Programming and Callbacks](/en/learn/asynchronous-work/javascript-asynchronous-programming-and-callbacks)[Asynchronous flow control](/en/learn/asynchronous-work/asynchronous-flow-control)[Discover Promises in Node.js](/en/learn/asynchronous-work/discover-promises-in-nodejs)[Discover JavaScript Timers](/en/learn/asynchronous-work/discover-javascript-timers)[Overview of Blocking vs Non-Blocking](/en/learn/asynchronous-work/overview-of-blocking-vs-non-blocking)[The Node.js Event Loop](/en/learn/asynchronous-work/event-loop-timers-and-nexttick)[The Node.js Event Emitter](/en/learn/asynchronous-work/the-nodejs-event-emitter)[Understanding process.nextTick()](/en/learn/asynchronous-work/understanding-processnexttick)[Understanding setImmediate()](/en/learn/asynchronous-work/understanding-setimmediate)[Don't Block the Event Loop](/en/learn/asynchronous-work/dont-block-the-event-loop)

TypeScript

[Introduction to TypeScript](/en/learn/typescript/introduction)[Running TypeScript Natively](/en/learn/typescript/run-natively)[Running TypeScript code using transpilation](/en/learn/typescript/transpile)[Running TypeScript with a runner](/en/learn/typescript/run)[Publishing a TypeScript package](/en/learn/typescript/publishing-a-ts-package)

Modules

[How to use streams](/en/learn/modules/how-to-use-streams)[Backpressuring in Streams](/en/learn/modules/backpressuring-in-streams)[Publishing a package](/en/learn/modules/publishing-a-package)[How to publish a Node-API package](/en/learn/modules/publishing-node-api-modules)[ABI Stability](/en/learn/modules/abi-stability)

Diagnostics

[User Journey](/en/learn/diagnostics/user-journey)[Memory](/en/learn/diagnostics/memory)[Live Debugging](/en/learn/diagnostics/live-debugging)[Poor Performance](/en/learn/diagnostics/poor-performance)[Flame Graphs](/en/learn/diagnostics/flame-graphs)

Test Runner

[Discovering Node.js's test runner](/en/learn/test-runner/introduction)[Using Node.js's test runner](/en/learn/test-runner/using-test-runner)[Mocking in tests](/en/learn/test-runner/mocking)[Collecting code coverage in Node.js](/en/learn/test-runner/collecting-code-coverage)

Getting Started

[Introduction to Node.js](/en/learn/getting-started/introduction-to-nodejs)[How much JavaScript do you need to know to use Node.js?](/en/learn/getting-started/how-much-javascript-do-you-need-to-know-to-use-nodejs)[Differences between Node.js and the Browser](/en/learn/getting-started/differences-between-nodejs-and-the-browser)[The V8 JavaScript Engine](/en/learn/getting-started/the-v8-javascript-engine)[An introduction to the npm package manager](/en/learn/getting-started/an-introduction-to-the-npm-package-manager)[ECMAScript 2015 (ES6) and beyond](/en/learn/getting-started/ecmascript-2015-es6-and-beyond)[Debugging Node.js](/en/learn/getting-started/debugging)[Fetching data with Node.js](/en/learn/getting-started/fetch)[WebSocket client with Node.js](/en/learn/getting-started/websocket)[Node.js, the difference between development and production](/en/learn/getting-started/nodejs-the-difference-between-development-and-production)[Profiling Node.js Applications](/en/learn/getting-started/profiling)[Node.js with WebAssembly](/en/learn/getting-started/nodejs-with-webassembly)[Security Best Practices](/en/learn/getting-started/security-best-practices)[Introduction to Userland Migrations](/en/learn/getting-started/userland-migrations)

Command Line

[Run Node.js scripts from the command line](/en/learn/command-line/run-nodejs-scripts-from-the-command-line)[How to use the Node.js REPL](/en/learn/command-line/how-to-use-the-nodejs-repl)[Output to the command line using Node.js](/en/learn/command-line/output-to-the-command-line-using-nodejs)[Accept input from the command line in Node.js](/en/learn/command-line/accept-input-from-the-command-line-in-nodejs)[How to read environment variables from Node.js](/en/learn/command-line/how-to-read-environment-variables-from-nodejs)

HTTP

[Anatomy of an HTTP Transaction](/en/learn/http/anatomy-of-an-http-transaction)[Enterprise Network Configuration](/en/learn/http/enterprise-network-configuration)

Manipulating Files

[Node.js file stats](/en/learn/manipulating-files/nodejs-file-stats)[Node.js File Paths](/en/learn/manipulating-files/nodejs-file-paths)[Reading files with Node.js](/en/learn/manipulating-files/reading-files-with-nodejs)[Writing files with Node.js](/en/learn/manipulating-files/writing-files-with-nodejs)[Working with file descriptors in Node.js](/en/learn/manipulating-files/working-with-file-descriptors-in-nodejs)[Working with folders in Node.js](/en/learn/manipulating-files/working-with-folders-in-nodejs)[How to work with Different Filesystems](/en/learn/manipulating-files/working-with-different-filesystems)

Asynchronous Work

[JavaScript Asynchronous Programming and Callbacks](/en/learn/asynchronous-work/javascript-asynchronous-programming-and-callbacks)[Asynchronous flow control](/en/learn/asynchronous-work/asynchronous-flow-control)[Discover Promises in Node.js](/en/learn/asynchronous-work/discover-promises-in-nodejs)[Discover JavaScript Timers](/en/learn/asynchronous-work/discover-javascript-timers)[Overview of Blocking vs Non-Blocking](/en/learn/asynchronous-work/overview-of-blocking-vs-non-blocking)[The Node.js Event Loop](/en/learn/asynchronous-work/event-loop-timers-and-nexttick)[The Node.js Event Emitter](/en/learn/asynchronous-work/the-nodejs-event-emitter)[Understanding process.nextTick()](/en/learn/asynchronous-work/understanding-processnexttick)[Understanding setImmediate()](/en/learn/asynchronous-work/understanding-setimmediate)[Don't Block the Event Loop](/en/learn/asynchronous-work/dont-block-the-event-loop)

TypeScript

[Introduction to TypeScript](/en/learn/typescript/introduction)[Running TypeScript Natively](/en/learn/typescript/run-natively)[Running TypeScript code using transpilation](/en/learn/typescript/transpile)[Running TypeScript with a runner](/en/learn/typescript/run)[Publishing a TypeScript package](/en/learn/typescript/publishing-a-ts-package)

Modules

[How to use streams](/en/learn/modules/how-to-use-streams)[Backpressuring in Streams](/en/learn/modules/backpressuring-in-streams)[Publishing a package](/en/learn/modules/publishing-a-package)[How to publish a Node-API package](/en/learn/modules/publishing-node-api-modules)[ABI Stability](/en/learn/modules/abi-stability)

Diagnostics

[User Journey](/en/learn/diagnostics/user-journey)[Memory](/en/learn/diagnostics/memory)[Live Debugging](/en/learn/diagnostics/live-debugging)[Poor Performance](/en/learn/diagnostics/poor-performance)[Flame Graphs](/en/learn/diagnostics/flame-graphs)

Test Runner

[Discovering Node.js's test runner](/en/learn/test-runner/introduction)[Using Node.js's test runner](/en/learn/test-runner/using-test-runner)[Mocking in tests](/en/learn/test-runner/mocking)[Collecting code coverage in Node.js](/en/learn/test-runner/collecting-code-coverage)

# [Introduction to Node.js](#introduction-to-nodejs)

Node.js is an open-source and cross-platform JavaScript runtime environment. It is a popular tool for almost any kind of project!

Node.js runs the V8 JavaScript engine, the core of Google Chrome, outside of the browser. This allows Node.js to be very performant.

A Node.js app runs in a single process, without creating a new thread for every request. Node.js provides a set of asynchronous I/O primitives in its standard library that prevent JavaScript code from blocking. In addition, libraries in Node.js are generally written using non-blocking paradigms. Accordingly, blocking behavior is the exception rather than the norm in Node.js.

When Node.js performs an I/O operation, like reading from the network, accessing a database or the filesystem, instead of blocking the thread and wasting CPU cycles waiting, Node.js will resume the operations when the response comes back.

This allows Node.js to handle thousands of concurrent connections with a single server without introducing the burden of managing thread concurrency, which could be a significant source of bugs.

Node.js has a unique advantage because millions of frontend developers that write JavaScript for the browser are now able to write the server-side code in addition to the client-side code without the need to learn a completely different language.

In Node.js the new ECMAScript standards can be used without problems, as you don't have to wait for all your users to update their browsers - you are in charge of deciding which ECMAScript version to use by changing the Node.js version, and you can also enable specific experimental features by running Node.js with flags.

## [An Example Node.js Application](#an-example-nodejs-application)

The most common example Hello World of Node.js is a web server:

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

To run this snippet, save it as a `server.js` file and run `node server.js` in your terminal.
If you use mjs version of the code, you should save it as a `server.mjs` file and run `node server.mjs` in your terminal.

This code first includes the Node.js [`http` module](https://nodejs.org/api/http.html).

Node.js has a fantastic [standard library](https://nodejs.org/api/), including first-class support for networking.

The `createServer()` method of `http` creates a new HTTP server and returns it.

The server is set to listen on the specified port and host name. When the server is ready, the callback function is called, in this case informing us that the server is running.

Whenever a new request is received, the [`request` event](https://nodejs.org/api/http.html#http_event_request) is called, providing two objects: a request (an [`http.IncomingMessage`](https://nodejs.org/api/http.html#http_class_http_incomingmessage) object) and a response (an [`http.ServerResponse`](https://nodejs.org/api/http.html#http_class_http_serverresponse) object).

Those 2 objects are essential to handle the HTTP call.

The first provides the request details. In this simple example, this is not used, but you could access the request headers and request data.

The second is used to return data to the caller.

In this case with:

```
res.statusCode = 200;
```

JavaScriptCopy to clipboard

we set the `statusCode` property to `200`, to indicate a successful response.

We set the `Content-Type` header:

```
res.setHeader('Content-Type', 'text/plain');
```

JavaScriptCopy to clipboard

and we close the response, adding the content as an argument to `end()`:

```
res.end('Hello World\n');
```

JavaScriptCopy to clipboard

If you haven't already done so, [download](https://nodejs.org/en/download) Node.js.

[NextHow much JavaScript do you need to know to use Node.js?](/en/learn/getting-started/how-much-javascript-do-you-need-to-know-to-use-nodejs)

Reading Time
:   3 min

Authors
:   [F](https://github.com/flaviocopes)[P](https://github.com/potch)[MB](https://github.com/mylesborins)[R](https://github.com/RomainLanz)[V](https://github.com/virkt25)[T](https://github.com/Trott)[O](https://github.com/onel0p3z)[O](https://github.com/ollelauribostrom)[M](https://github.com/MarkPieszak)+10

Contribute
:   [Edit this page](https://github.com/nodejs/nodejs.org/blob/main/apps/site/pages/en/learn/getting-started/introduction-to-nodejs.md)

Table of Contents
:   1. [An Example Node.js Application](#an-example-nodejs-application)

1. [Navigate to Home](/en)
2. Getting Started
3. [Introduction to Node.js](/en/learn/getting-started/introduction-to-nodejs)

[v24.12.0Latest LTS](/blog/release/v24.12.0)[v25.2.1Latest Release](/blog/release/v25.2.1)

[Trademark Policy](https://trademark-policy.openjsf.org/)[Privacy Policy](https://privacy-policy.openjsf.org/)[Code of Conduct](https://github.com/openjs-foundation/cross-project-council/blob/main/CODE_OF_CONDUCT.md)[Security Policy](https://github.com/nodejs/node/security/policy)

[© OpenJS Foundation](https://openjsf.org/)

---
