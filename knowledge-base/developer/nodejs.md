# Nodejs Knowledge

> Category: frameworks

## Source: en.md

Node.js — Run JavaScript Everywhere

New security releases to be made available Wednesday, January 7, 2026

LearnAboutDownloadBlogDocsContributeCourses

Start typing...

⌘ K

# Run JavaScript Everywhere

Node.js® is a free, open-source, cross-platform JavaScript runtime environment
that lets developers create servers, web apps, command line tools and scripts.

Get Node.js®Get Node.js®Get security support  
for EOL Node.js versionsNode.js is proudly supported by the partners above and more.

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

Learn more what Node.js is able to offer with our Learning materials.

v24.12.0Latest LTSv25.2.1Latest Release

Trademark PolicyPrivacy PolicyCode of ConductSecurity Policy

© OpenJS Foundation

---

## Source: en_about.md

Node.js — About Node.js®

New security releases to be made available Wednesday, January 7, 2026

LearnAboutDownloadBlogDocsContributeCourses

Start typing...

⌘ K

Change pageAbout Node.js®

Change pageAbout Node.js®

About Node.js

About Node.js®Node.js ReleasesSecurity ReportingProject GovernancePartners & SupportersBranding of Node.jsEnd-of-Life (EOL)

Get Involved

Get InvolvedCollaboration SummitUpcoming EventsContribute to Node.jsCode of Conduct

About Node.js

About Node.js®Node.js ReleasesSecurity ReportingProject GovernancePartners & SupportersBranding of Node.jsEnd-of-Life (EOL)

Get Involved

Get InvolvedCollaboration SummitUpcoming EventsContribute to Node.jsCode of Conduct

# About Node.js®

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
  console.log(`Server running at );
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
Blocking vs. Non-Blocking.

---

Node.js is similar in design to, and influenced by, systems like Ruby's
Event Machine and Python's Twisted. Node.js takes the event model a bit
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
by using our `child_process.fork()` API, and are designed to be easy to
communicate with. Built upon that same interface is the `cluster` module,
which allows you to share sockets between processes to enable load balancing
over your cores.

## Official Node.js Resources

To ensure authenticity and security when working with Node.js, always use official sources. Avoid trusting emails,
binaries, or downloads from unofficial sources.

### Official Node.js Domains

For downloading Node.js binaries and accessing official documentation, use only these domains:

* nodejs.org
* nodejs.dev *(Redirects to <)*
* iojs.org *(Redirects to <)*

### Official npm Packages

The Node.js team maintains the following official npm package scopes:

* `@node-core`
* `@pkgjs`

Additionally, the Node.js team maintains packages published by the `nodejs-foundation` npm account,
though other Node.js-related packages (like `undici`) may also be maintained by contributors closely
tied to the project.

Using packages from the Node.js team guarantees that you are working with officially supported Node.js components.

### Official GitHub Organizations

Node.js and related projects are maintained under these official GitHub organizations:

* nodejs
* pkgjs

### Official Communication Channels

Node.js and the OpenJS Foundation communicate through various official and community-supported channels. You can find details on
how to get involved on the Get Involved page.

### Reporting Website Issues & Downtime

If you encounter issues with the Node.js website, report them at the Node.js website repository.
For real-time updates on outages, visit the Node.js Status Page.

Reading Time
:   3 min

Contribute
:   Edit this page

Table of Contents
:   1. Official Node.js Resources
    2. Official Node.js Domains
    3. Official npm Packages
    4. Official GitHub Organizations
    5. Official Communication Channels
    6. Reporting Website Issues & Downtime

1. Navigate to Home
2. About Node.js

v24.12.0Latest LTSv25.2.1Latest Release

Trademark PolicyPrivacy PolicyCode of ConductSecurity Policy

© OpenJS Foundation

---

## Source: en_blog_vulnerability_december-2025-security-releases.md

Node.js — Wednesday, January 7, 2026 Security Releases

New security releases to be made available Wednesday, January 7, 2026

LearnAboutDownloadBlogDocsContributeCourses

Start typing...

⌘ K

Commercial support for versions past the Maintenance LTS phase is available through our OpenJS Ecosystem Sustainability Program partners

# Wednesday, January 7, 2026 Security Releases

TNJP

The Node.js Project

Wednesday, January 7, 2026 Security Releases

## (Update 17-Dec-2025) Security Release target January 7th

We have decided to delay the release further to Wednesday, January 7th, 2026. Many of the
downstream projects and users are on holiday break at the end of the year, and the security
release will disclose the vulnerabilities being fixed as soon as the patches are available.
We want to make sure that most users are no longer on holiday when they evaluate whether
they are affected and need to perform time-sensitive upgrades.

## (Update 15-Dec-2025) Security Release target December 18th

The team is still working on a particularly challenging patch, for this reason
the release is being postponed to Thursday, December 18th or shortly after.

# Summary

The Node.js project will release new versions of the 25.x, 24.x, 22.x, 20.x
releases lines on or shortly after, Monday, December 15, 2025 in order to address:

* 3 high severity issues.
* 1 low severity issue.
* 1 medium severity issue.

## Impact

The 25.x release line of Node.js is vulnerable to 3 high severity issues, 1 low severity issue.
The 24.x release line of Node.js is vulnerable to 3 high severity issues, 1 low severity issue, 1 medium severity issue.
The 22.x release line of Node.js is vulnerable to 3 high severity issues, 1 low severity issue, 1 medium severity issue.
The 20.x release line of Node.js is vulnerable to 3 high severity issues, 1 low severity issue, 1 medium severity issue.

It's important to note that End-of-Life versions are always affected when a security release occurs.
To ensure your system's security, please use an up-to-date version as outlined in our
Release Schedule.

## Release timing

Releases will be available on, or shortly after, Monday, December 15, 2025.

## Contact and future updates

The current Node.js security policy can be found at <
Please follow the process outlined in < if you wish to report a vulnerability in Node.js.

Subscribe to the low-volume announcement-only nodejs-sec mailing list at < to stay up to date on security vulnerabilities and security-related releases of Node.js and the projects maintained in the nodejs GitHub organization.

NextTuesday, July 15, 2025 Security Releases

Last Updated
:   Dec 08, 2025

Reading Time
:   2 min

Contribute
:   Edit this page

Table of Contents
:   1. (Update 17-Dec-2025) Security Release target January 7th
    2. (Update 15-Dec-2025) Security Release target December 18th
    3. Impact
    4. Release timing
    5. Contact and future updates

v24.12.0Latest LTSv25.2.1Latest Release

Trademark PolicyPrivacy PolicyCode of ConductSecurity Policy

© OpenJS Foundation

---

## Source: en_docs_guides.md

Node.js — Introduction to Node.js

New security releases to be made available Wednesday, January 7, 2026

LearnAboutDownloadBlogDocsContributeCourses

Start typing...

⌘ K

Change pageIntroduction to Node.js

Change pageIntroduction to Node.js

Getting Started

Introduction to Node.jsHow much JavaScript do you need to know to use Node.js?Differences between Node.js and the BrowserThe V8 JavaScript EngineAn introduction to the npm package managerECMAScript 2015 (ES6) and beyondDebugging Node.jsFetching data with Node.jsWebSocket client with Node.jsNode.js, the difference between development and productionProfiling Node.js ApplicationsNode.js with WebAssemblySecurity Best PracticesIntroduction to Userland Migrations

Command Line

Run Node.js scripts from the command lineHow to use the Node.js REPLOutput to the command line using Node.jsAccept input from the command line in Node.jsHow to read environment variables from Node.js

HTTP

Anatomy of an HTTP TransactionEnterprise Network Configuration

Manipulating Files

Node.js file statsNode.js File PathsReading files with Node.jsWriting files with Node.jsWorking with file descriptors in Node.jsWorking with folders in Node.jsHow to work with Different Filesystems

Asynchronous Work

JavaScript Asynchronous Programming and CallbacksAsynchronous flow controlDiscover Promises in Node.jsDiscover JavaScript TimersOverview of Blocking vs Non-BlockingThe Node.js Event LoopThe Node.js Event EmitterUnderstanding process.nextTick()Understanding setImmediate()Don't Block the Event Loop

TypeScript

Introduction to TypeScriptRunning TypeScript NativelyRunning TypeScript code using transpilationRunning TypeScript with a runnerPublishing a TypeScript package

Modules

How to use streamsBackpressuring in StreamsPublishing a packageHow to publish a Node-API packageABI Stability

Diagnostics

User JourneyMemoryLive DebuggingPoor PerformanceFlame Graphs

Test Runner

Discovering Node.js's test runnerUsing Node.js's test runnerMocking in testsCollecting code coverage in Node.js

Getting Started

Introduction to Node.jsHow much JavaScript do you need to know to use Node.js?Differences between Node.js and the BrowserThe V8 JavaScript EngineAn introduction to the npm package managerECMAScript 2015 (ES6) and beyondDebugging Node.jsFetching data with Node.jsWebSocket client with Node.jsNode.js, the difference between development and productionProfiling Node.js ApplicationsNode.js with WebAssemblySecurity Best PracticesIntroduction to Userland Migrations

Command Line

Run Node.js scripts from the command lineHow to use the Node.js REPLOutput to the command line using Node.jsAccept input from the command line in Node.jsHow to read environment variables from Node.js

HTTP

Anatomy of an HTTP TransactionEnterprise Network Configuration

Manipulating Files

Node.js file statsNode.js File PathsReading files with Node.jsWriting files with Node.jsWorking with file descriptors in Node.jsWorking with folders in Node.jsHow to work with Different Filesystems

Asynchronous Work

JavaScript Asynchronous Programming and CallbacksAsynchronous flow controlDiscover Promises in Node.jsDiscover JavaScript TimersOverview of Blocking vs Non-BlockingThe Node.js Event LoopThe Node.js Event EmitterUnderstanding process.nextTick()Understanding setImmediate()Don't Block the Event Loop

TypeScript

Introduction to TypeScriptRunning TypeScript NativelyRunning TypeScript code using transpilationRunning TypeScript with a runnerPublishing a TypeScript package

Modules

How to use streamsBackpressuring in StreamsPublishing a packageHow to publish a Node-API packageABI Stability

Diagnostics

User JourneyMemoryLive DebuggingPoor PerformanceFlame Graphs

Test Runner

Discovering Node.js's test runnerUsing Node.js's test runnerMocking in testsCollecting code coverage in Node.js

# Introduction to Node.js

Node.js is an open-source and cross-platform JavaScript runtime environment. It is a popular tool for almost any kind of project!

Node.js runs the V8 JavaScript engine, the core of Google Chrome, outside of the browser. This allows Node.js to be very performant.

A Node.js app runs in a single process, without creating a new thread for every request. Node.js provides a set of asynchronous I/O primitives in its standard library that prevent JavaScript code from blocking. In addition, libraries in Node.js are generally written using non-blocking paradigms. Accordingly, blocking behavior is the exception rather than the norm in Node.js.

When Node.js performs an I/O operation, like reading from the network, accessing a database or the filesystem, instead of blocking the thread and wasting CPU cycles waiting, Node.js will resume the operations when the response comes back.

This allows Node.js to handle thousands of concurrent connections with a single server without introducing the burden of managing thread concurrency, which could be a significant source of bugs.

Node.js has a unique advantage because millions of frontend developers that write JavaScript for the browser are now able to write the server-side code in addition to the client-side code without the need to learn a completely different language.

In Node.js the new ECMAScript standards can be used without problems, as you don't have to wait for all your users to update their browsers - you are in charge of deciding which ECMAScript version to use by changing the Node.js version, and you can also enable specific experimental features by running Node.js with flags.

## An Example Node.js Application

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
  console.log(`Server running at );
});
```

JavaScriptCopy to clipboard

To run this snippet, save it as a `server.js` file and run `node server.js` in your terminal.
If you use mjs version of the code, you should save it as a `server.mjs` file and run `node server.mjs` in your terminal.

This code first includes the Node.js `http` module.

Node.js has a fantastic standard library, including first-class support for networking.

The `createServer()` method of `http` creates a new HTTP server and returns it.

The server is set to listen on the specified port and host name. When the server is ready, the callback function is called, in this case informing us that the server is running.

Whenever a new request is received, the `request` event is called, providing two objects: a request (an `http.IncomingMessage` object) and a response (an `http.ServerResponse` object).

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

If you haven't already done so, download Node.js.

NextHow much JavaScript do you need to know to use Node.js?

Reading Time
:   3 min

Authors
:   FPMBRVTOOM+10

Contribute
:   Edit this page

Table of Contents
:   1. An Example Node.js Application

1. Navigate to Home
2. Getting Started
3. Introduction to Node.js

v24.12.0Latest LTSv25.2.1Latest Release

Trademark PolicyPrivacy PolicyCode of ConductSecurity Policy

© OpenJS Foundation

---

## Source: en_learn.md

Node.js — Introduction to Node.js

New security releases to be made available Wednesday, January 7, 2026

LearnAboutDownloadBlogDocsContributeCourses

Start typing...

⌘ K

Change pageIntroduction to Node.js

Change pageIntroduction to Node.js

Getting Started

Introduction to Node.jsHow much JavaScript do you need to know to use Node.js?Differences between Node.js and the BrowserThe V8 JavaScript EngineAn introduction to the npm package managerECMAScript 2015 (ES6) and beyondDebugging Node.jsFetching data with Node.jsWebSocket client with Node.jsNode.js, the difference between development and productionProfiling Node.js ApplicationsNode.js with WebAssemblySecurity Best PracticesIntroduction to Userland Migrations

Command Line

Run Node.js scripts from the command lineHow to use the Node.js REPLOutput to the command line using Node.jsAccept input from the command line in Node.jsHow to read environment variables from Node.js

HTTP

Anatomy of an HTTP TransactionEnterprise Network Configuration

Manipulating Files

Node.js file statsNode.js File PathsReading files with Node.jsWriting files with Node.jsWorking with file descriptors in Node.jsWorking with folders in Node.jsHow to work with Different Filesystems

Asynchronous Work

JavaScript Asynchronous Programming and CallbacksAsynchronous flow controlDiscover Promises in Node.jsDiscover JavaScript TimersOverview of Blocking vs Non-BlockingThe Node.js Event LoopThe Node.js Event EmitterUnderstanding process.nextTick()Understanding setImmediate()Don't Block the Event Loop

TypeScript

Introduction to TypeScriptRunning TypeScript NativelyRunning TypeScript code using transpilationRunning TypeScript with a runnerPublishing a TypeScript package

Modules

How to use streamsBackpressuring in StreamsPublishing a packageHow to publish a Node-API packageABI Stability

Diagnostics

User JourneyMemoryLive DebuggingPoor PerformanceFlame Graphs

Test Runner

Discovering Node.js's test runnerUsing Node.js's test runnerMocking in testsCollecting code coverage in Node.js

Getting Started

Introduction to Node.jsHow much JavaScript do you need to know to use Node.js?Differences between Node.js and the BrowserThe V8 JavaScript EngineAn introduction to the npm package managerECMAScript 2015 (ES6) and beyondDebugging Node.jsFetching data with Node.jsWebSocket client with Node.jsNode.js, the difference between development and productionProfiling Node.js ApplicationsNode.js with WebAssemblySecurity Best PracticesIntroduction to Userland Migrations

Command Line

Run Node.js scripts from the command lineHow to use the Node.js REPLOutput to the command line using Node.jsAccept input from the command line in Node.jsHow to read environment variables from Node.js

HTTP

Anatomy of an HTTP TransactionEnterprise Network Configuration

Manipulating Files

Node.js file statsNode.js File PathsReading files with Node.jsWriting files with Node.jsWorking with file descriptors in Node.jsWorking with folders in Node.jsHow to work with Different Filesystems

Asynchronous Work

JavaScript Asynchronous Programming and CallbacksAsynchronous flow controlDiscover Promises in Node.jsDiscover JavaScript TimersOverview of Blocking vs Non-BlockingThe Node.js Event LoopThe Node.js Event EmitterUnderstanding process.nextTick()Understanding setImmediate()Don't Block the Event Loop

TypeScript

Introduction to TypeScriptRunning TypeScript NativelyRunning TypeScript code using transpilationRunning TypeScript with a runnerPublishing a TypeScript package

Modules

How to use streamsBackpressuring in StreamsPublishing a packageHow to publish a Node-API packageABI Stability

Diagnostics

User JourneyMemoryLive DebuggingPoor PerformanceFlame Graphs

Test Runner

Discovering Node.js's test runnerUsing Node.js's test runnerMocking in testsCollecting code coverage in Node.js

# Introduction to Node.js

Node.js is an open-source and cross-platform JavaScript runtime environment. It is a popular tool for almost any kind of project!

Node.js runs the V8 JavaScript engine, the core of Google Chrome, outside of the browser. This allows Node.js to be very performant.

A Node.js app runs in a single process, without creating a new thread for every request. Node.js provides a set of asynchronous I/O primitives in its standard library that prevent JavaScript code from blocking. In addition, libraries in Node.js are generally written using non-blocking paradigms. Accordingly, blocking behavior is the exception rather than the norm in Node.js.

When Node.js performs an I/O operation, like reading from the network, accessing a database or the filesystem, instead of blocking the thread and wasting CPU cycles waiting, Node.js will resume the operations when the response comes back.

This allows Node.js to handle thousands of concurrent connections with a single server without introducing the burden of managing thread concurrency, which could be a significant source of bugs.

Node.js has a unique advantage because millions of frontend developers that write JavaScript for the browser are now able to write the server-side code in addition to the client-side code without the need to learn a completely different language.

In Node.js the new ECMAScript standards can be used without problems, as you don't have to wait for all your users to update their browsers - you are in charge of deciding which ECMAScript version to use by changing the Node.js version, and you can also enable specific experimental features by running Node.js with flags.

## An Example Node.js Application

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
  console.log(`Server running at );
});
```

JavaScriptCopy to clipboard

To run this snippet, save it as a `server.js` file and run `node server.js` in your terminal.
If you use mjs version of the code, you should save it as a `server.mjs` file and run `node server.mjs` in your terminal.

This code first includes the Node.js `http` module.

Node.js has a fantastic standard library, including first-class support for networking.

The `createServer()` method of `http` creates a new HTTP server and returns it.

The server is set to listen on the specified port and host name. When the server is ready, the callback function is called, in this case informing us that the server is running.

Whenever a new request is received, the `request` event is called, providing two objects: a request (an `http.IncomingMessage` object) and a response (an `http.ServerResponse` object).

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

If you haven't already done so, download Node.js.

NextHow much JavaScript do you need to know to use Node.js?

Reading Time
:   3 min

Authors
:   FPMBRVTOOM+10

Contribute
:   Edit this page

Table of Contents
:   1. An Example Node.js Application

1. Navigate to Home
2. Getting Started
3. Introduction to Node.js

v24.12.0Latest LTSv25.2.1Latest Release

Trademark PolicyPrivacy PolicyCode of ConductSecurity Policy

© OpenJS Foundation

---