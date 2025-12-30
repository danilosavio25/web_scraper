# Typescript Knowledge

> Category: languages

## Source: docs.md

TypeScript: The starting point for learning TypeScript

Skip to main content

TypeScript

* Download
* Docs
* Handbook
* Playground
* Tools

in En

# TypeScript Documentation

#### Get Started

Quick introductions based on your background or preference.

* TS for the New Programmer
* TypeScript for JS Programmers
* TS for Java/C# Programmers
* TS for Functional Programmers
* TypeScript Tooling in 5 minutes

#### Handbook

A great first read for your daily TS work.

* The TypeScript Handbook
* The Basics
* Everyday Types
* Narrowing
* More on Functions
* Object Types
* Type Manipulation
* + Creating Types from Types
  + Generics
  + Keyof Type Operator
  + Typeof Type Operator
  + Indexed Access Types
  + Conditional Types
  + Mapped Types
  + Template Literal Types
* Classes
* Modules

#### Reference

Deep dive reference materials.

* Utility Types
* Cheat Sheets
* Decorators
* Declaration Merging
* Enums
* Iterators and Generators
* JSX
* Mixins
* Namespaces
* Namespaces and Modules
* Symbols
* Triple-Slash Directives
* Type Compatibility
* Type Inference
* Variable Declaration

#### Modules Reference

How TypeScript models JavaScript modules.

* Introduction
* Theory
* Guides
* + Choosing Compiler Options
* Reference
* Appendices
* + ESM/CJS Interoperability

#### Tutorials

Using TypeScript in several environments.

* ASP.NET Core
* Gulp
* DOM Manipulation
* Migrating from JavaScript
* Using Babel with TypeScript

#### Declaration Files

Learn how to write declaration files to describe existing JavaScript. Important for DefinitelyTyped contributions.

* Introduction
* Declaration Reference
* Library Structures
* .d.ts Templates
* + Modules .d.ts
  + Module: Plugin
  + Module: Class
  + Module: Function
  + Global .d.ts
  + Global: Modifying Module
* Do's and Don'ts
* Deep Dive
* Publishing
* Consumption

#### JavaScript

How to use TypeScript-powered JavaScript tooling.

* JS Projects Utilizing TypeScript
* Type Checking JavaScript Files
* JSDoc Reference
* Creating .d.ts Files from .js files

#### Project Configuration

Compiler configuration reference.

* What is a tsconfig.json
* Compiler Options in MSBuild
* TSConfig Reference
* tsc CLI Options
* Project References
* Integrating with Build Tools
* Configuring Watch
* Nightly Builds

#### Cheat Sheets

Downloadable syntax reference pages for different parts of everyday TypeScript code.

* Control Flow Analysis
* Classes
* Interfaces
* Types
* Download PDFs and PNGs

## Learning Resources

#### Get Started

* JS to TS
* New to Programming
* OOP to JS
* Functional to JS
* Installation

#### Handbook

* Everyday Types
* Creating Types from Types
* Object Types
* Variable Declarations
* More on Functions

#### Tools

* Playground
* TSConfig Reference

#### Release Notes

* What's new in 5.9

#### Tutorials

* ASP.NET
* Migrating from JS
* Working with the DOM
* React & Webpack

### Customize

Site Colours:

SystemAlways LightAlways Dark

Code Font:

CascadiaCascadia (ligatures)ConsolasDank MonoFira CodeJetBrains MonoOpenDyslexicSF MonoSource Code Pro

### Popular Documentation Pages

* Everyday Types

  All of the common types in TypeScript
* Creating Types from Types

  Techniques to make more elegant types
* More on Functions

  How to provide types to functions in JavaScript
* More on Objects

  How to provide a type shape to JavaScript objects
* Narrowing

  How TypeScript infers types based on runtime behavior
* Variable Declarations

  How to create and type JavaScript variables
* TypeScript in 5 minutes

  An overview of building a TypeScript web app
* TSConfig Options

  All the configuration options for a project
* Classes

  How to provide types to JavaScript ES6 classes

Made with ♥ in Redmond, Boston, SF & Dublin

© 2012-2025 Microsoft  
PrivacyTerms of Use

### Using TypeScript

* Get Started
* Download
* Playground
* TSConfig Ref
* Code Samples
* Why TypeScript
* Design

### Community

* Get Help
* GitHub Repo
* Community Chat
* @TypeScript
* Mastodon
* Stack Overflow
* Web Repo

MSG

---

## Source: docs_handbook_intro.html.md

TypeScript: Handbook - The TypeScript Handbook

Skip to main content

TypeScript

* Download
* Docs
* Handbook
* Playground
* Tools

in En

Was this page helpful?

* Get Started
  + TS for the New Programmer
  + TypeScript for JS Programmers
  + TS for Java/C# Programmers
  + TS for Functional Programmers
  + TypeScript Tooling in 5 minutes
* Handbook
  + The TypeScript Handbook
  + The Basics
  + Everyday Types
  + Narrowing
  + More on Functions
  + Object Types
  + Type Manipulation
    - Creating Types from Types
    - Generics
    - Keyof Type Operator
    - Typeof Type Operator
    - Indexed Access Types
    - Conditional Types
    - Mapped Types
    - Template Literal Types
  + Classes
  + Modules
* Reference
  + Utility Types
  + Cheat Sheets
  + Decorators
  + Declaration Merging
  + Enums
  + Iterators and Generators
  + JSX
  + Mixins
  + Namespaces
  + Namespaces and Modules
  + Symbols
  + Triple-Slash Directives
  + Type Compatibility
  + Type Inference
  + Variable Declaration
* Modules Reference
  + Introduction
  + Theory
  + Guides
    - Choosing Compiler Options
  + Reference
  + Appendices
    - ESM/CJS Interoperability
* Tutorials
  + ASP.NET Core
  + Gulp
  + DOM Manipulation
  + Migrating from JavaScript
  + Using Babel with TypeScript
* What's New
  + TypeScript 5.9
  + TypeScript 5.8
  + TypeScript 5.7
  + TypeScript 5.6
  + TypeScript 5.5
  + TypeScript 5.4
  + TypeScript 5.3
  + TypeScript 5.2
  + TypeScript 5.1
  + TypeScript 5.0
  + TypeScript 4.9
  + TypeScript 4.8
  + TypeScript 4.7
  + TypeScript 4.6
  + TypeScript 4.5
  + TypeScript 4.4
  + TypeScript 4.3
  + TypeScript 4.2
  + TypeScript 4.1
  + TypeScript 4.0
  + TypeScript 3.9
  + TypeScript 3.8
  + TypeScript 3.7
  + TypeScript 3.6
  + TypeScript 3.5
  + TypeScript 3.4
  + TypeScript 3.3
  + TypeScript 3.2
  + TypeScript 3.1
  + TypeScript 3.0
  + TypeScript 2.9
  + TypeScript 2.8
  + TypeScript 2.7
  + TypeScript 2.6
  + TypeScript 2.5
  + TypeScript 2.4
  + TypeScript 2.3
  + TypeScript 2.2
  + TypeScript 2.1
  + TypeScript 2.0
  + TypeScript 1.8
  + TypeScript 1.7
  + TypeScript 1.6
  + TypeScript 1.5
  + TypeScript 1.4
  + TypeScript 1.3
  + TypeScript 1.1
* Declaration Files
  + Introduction
  + Declaration Reference
  + Library Structures
  + .d.ts Templates
    - Modules .d.ts
    - Module: Plugin
    - Module: Class
    - Module: Function
    - Global .d.ts
    - Global: Modifying Module
  + Do's and Don'ts
  + Deep Dive
  + Publishing
  + Consumption
* JavaScript
  + JS Projects Utilizing TypeScript
  + Type Checking JavaScript Files
  + JSDoc Reference
  + Creating .d.ts Files from .js files
* Project Configuration
  + What is a tsconfig.json
  + Compiler Options in MSBuild
  + TSConfig Reference
  + tsc CLI Options
  + Project References
  + Integrating with Build Tools
  + Configuring Watch
  + Nightly Builds

# The TypeScript Handbook

## About this Handbook

Over 20 years after its introduction to the programming community, JavaScript is now one of the most widespread cross-platform languages ever created. Starting as a small scripting language for adding trivial interactivity to webpages, JavaScript has grown to be a language of choice for both frontend and backend applications of every size. While the size, scope, and complexity of programs written in JavaScript has grown exponentially, the ability of the JavaScript language to express the relationships between different units of code has not. Combined with JavaScript’s rather peculiar runtime semantics, this mismatch between language and program complexity has made JavaScript development a difficult task to manage at scale.

The most common kinds of errors that programmers write can be described as type errors: a certain kind of value was used where a different kind of value was expected. This could be due to simple typos, a failure to understand the API surface of a library, incorrect assumptions about runtime behavior, or other errors. The goal of TypeScript is to be a static typechecker for JavaScript programs - in other words, a tool that runs before your code runs (static) and ensures that the types of the program are correct (typechecked).

If you are coming to TypeScript without a JavaScript background, with the intention of TypeScript being your first language, we recommend you first start reading the documentation on either the Microsoft Learn JavaScript tutorial or read JavaScript at the Mozilla Web Docs.
If you have experience in other languages, you should be able to pick up JavaScript syntax quite quickly by reading the handbook.

## How is this Handbook Structured

The handbook is split into two sections:

* **The Handbook**

  The TypeScript Handbook is intended to be a comprehensive document that explains TypeScript to everyday programmers. You can read the handbook by going from top to bottom in the left-hand navigation.

  You should expect each chapter or page to provide you with a strong understanding of the given concepts. The TypeScript Handbook is not a complete language specification, but it is intended to be a comprehensive guide to all of the language’s features and behaviors.

  A reader who completes the walkthrough should be able to:

  + Read and understand commonly-used TypeScript syntax and patterns
  + Explain the effects of important compiler options
  + Correctly predict type system behavior in most cases

  In the interests of clarity and brevity, the main content of the Handbook will not explore every edge case or minutiae of the features being covered. You can find more details on particular concepts in the reference articles.
* **Reference Files**

  The reference section below the handbook in the navigation is built to provide a richer understanding of how a particular part of TypeScript works. You can read it top-to-bottom, but each section aims to provide a deeper explanation of a single concept - meaning there is no aim for continuity.

### Non-Goals

The Handbook is also intended to be a concise document that can be comfortably read in a few hours. Certain topics won’t be covered in order to keep things short.

Specifically, the Handbook does not fully introduce core JavaScript basics like functions, classes, and closures. Where appropriate, we’ll include links to background reading that you can use to read up on those concepts.

The Handbook also isn’t intended to be a replacement for a language specification. In some cases, edge cases or formal descriptions of behavior will be skipped in favor of high-level, easier-to-understand explanations. Instead, there are separate reference pages that more precisely and formally describe many aspects of TypeScript’s behavior. The reference pages are not intended for readers unfamiliar with TypeScript, so they may use advanced terminology or reference topics you haven’t read about yet.

Finally, the Handbook won’t cover how TypeScript interacts with other tools, except where necessary. Topics like how to configure TypeScript with webpack, rollup, parcel, react, babel, closure, lerna, rush, bazel, preact, vue, angular, svelte, jquery, yarn, or npm are out of scope - you can find these resources elsewhere on the web.

## Get Started

Before getting started with The Basics, we recommend reading one of the following introductory pages. These introductions are intended to highlight key similarities and differences between TypeScript and your favored programming language, and clear up common misconceptions specific to those languages.

* TypeScript for the New Programmer
* TypeScript for JavaScript Programmers
* TypeScript for Java/C# Programmers
* TypeScript for Functional Programmers

Otherwise, jump to The Basics.

##### On this page

* About this Handbook
* How is this Handbook Structured
  + Non-Goals
* Get Started

##### Is this page helpful?

Yes No

Next

### The Basics

Step one in learning TypeScript: The basic types.

The TypeScript docs are an open source project. Help us improve these pages by sending a Pull Request ❤

Contributors to this page:  

OT!Orta Therox  (22)

MW!Maira Wenzel  (1)

M!MingYuan  (1)

N!navya9singh  (1)

谭!谭九鼎  (1)

5+

Last updated: Dec 29, 2025

### Customize

Site Colours:

SystemAlways LightAlways Dark

Code Font:

CascadiaCascadia (ligatures)ConsolasDank MonoFira CodeJetBrains MonoOpenDyslexicSF MonoSource Code Pro

### Popular Documentation Pages

* Everyday Types

  All of the common types in TypeScript
* Creating Types from Types

  Techniques to make more elegant types
* More on Functions

  How to provide types to functions in JavaScript
* More on Objects

  How to provide a type shape to JavaScript objects
* Narrowing

  How TypeScript infers types based on runtime behavior
* Variable Declarations

  How to create and type JavaScript variables
* TypeScript in 5 minutes

  An overview of building a TypeScript web app
* TSConfig Options

  All the configuration options for a project
* Classes

  How to provide types to JavaScript ES6 classes

Made with ♥ in Redmond, Boston, SF & Dublin

© 2012-2025 Microsoft  
PrivacyTerms of Use

### Using TypeScript

* Get Started
* Download
* Playground
* TSConfig Ref
* Code Samples
* Why TypeScript
* Design

### Community

* Get Help
* GitHub Repo
* Community Chat
* @TypeScript
* Mastodon
* Stack Overflow
* Web Repo

MSG

---

## Source: download.md

TypeScript: How to set up TypeScript

Skip to main content

TypeScript

* Download
* Docs
* Handbook
* Playground
* Tools

in En

# Download TypeScript

TypeScript can be installed through three installation routes depending on how you intend to use it: an npm module, a NuGet package or a Visual Studio Extension.

If you are using Node.js, you want the npm version. If you are using MSBuild in your project, you want the NuGet package or Visual Studio extension.

## TypeScript in Your Project

Having TypeScript set up on a per-project basis lets you have many projects with many different versions of TypeScript, this keeps each project working consistently.

### via npm

TypeScript is available as a package on the npm registry available as `"typescript"`.

You will need a copy of Node.js as an environment to run the package. Then you use a dependency manager like npm, yarn or pnpm to download TypeScript into your project.

`npm install typescript --save-dev`  
  
npm yarn pnpm

All of these dependency managers support lockfiles, ensuring that everyone on your team is using the same version of the language. You can then run the TypeScript compiler using one of the following commands:

`npx tsc`  
  
npm yarn pnpm

### with Visual Studio

For most project types, you can get TypeScript as a package in Nuget for your MSBuild projects, for example an ASP.NET Core app.

When using Nuget, you can install TypeScript through Visual Studio using:

* The Manage NuGet Packages window (which you can get to by right-clicking on a project node)
* The Nuget Package Manager Console (found in Tools > NuGet Package Manager > Package Manager Console) and then running:  
  `Install-Package Microsoft.TypeScript.MSBuild`

For project types which don't support Nuget, you can use the  TypeScript Visual Studio extension. You can install the extension using `Extensions > Manage Extensions` in Visual Studio.

The examples below are for more advanced use cases.

## Globally Installing TypeScript

It can be handy to have TypeScript available across all projects, often to test one-off ideas. Long-term, codebases should prefer a project-wide installation over a global install so that they can benefit from reproducible builds across different machines.

### via npm

You can use npm to install TypeScript globally, this means that you can use the `tsc` command anywhere in your terminal.

To do this, run `npm install -g typescript`. This will install the latest version (currently 5.9).

### via Visual Studio Marketplace

You can install TypeScript as a Visual Studio extension, which will allow you to use TypeScript across many MSBuild projects in Visual Studio.

The latest version is available in the Visual Studio Marketplace.

## Working with TypeScript-compatible transpilers

There are other tools which convert TypeScript files to JavaScript files. You might use these tools for speed or consistency with your existing build tooling.

Each of these projects handle the file conversion, but do not handle the type-checking aspects of the TypeScript compiler. So it's likely that you will still need to keep the above TypeScript dependency around, and you will want to enable `isolatedModules`.

### Babel

Babel is a very popular JavaScript transpiler which supports TypeScript files via the plugin @babel/plugin-transform-typescript.

### swc

swc is a fast transpiler created in Rust which supports many of Babel's features including TypeScript.

### Sucrase

Sucrase is a Babel fork focused on speed for using in development mode. Sucrase supports TypeScript natively.

## Next Steps

#### Get Started

* JS to TS
* New to Programming
* OOP to JS
* Functional to JS
* Installation

#### Handbook

* Everyday Types
* Creating Types from Types
* Object Types
* Variable Declarations
* More on Functions

#### Tools

* Playground
* TSConfig Reference

#### Release Notes

* What's new in 5.9

#### Tutorials

* ASP.NET
* Migrating from JS
* Working with the DOM
* React & Webpack

### Customize

Site Colours:

SystemAlways LightAlways Dark

Code Font:

CascadiaCascadia (ligatures)ConsolasDank MonoFira CodeJetBrains MonoOpenDyslexicSF MonoSource Code Pro

### Popular Documentation Pages

* Everyday Types

  All of the common types in TypeScript
* Creating Types from Types

  Techniques to make more elegant types
* More on Functions

  How to provide types to functions in JavaScript
* More on Objects

  How to provide a type shape to JavaScript objects
* Narrowing

  How TypeScript infers types based on runtime behavior
* Variable Declarations

  How to create and type JavaScript variables
* TypeScript in 5 minutes

  An overview of building a TypeScript web app
* TSConfig Options

  All the configuration options for a project
* Classes

  How to provide types to JavaScript ES6 classes

Made with ♥ in Redmond, Boston, SF & Dublin

© 2012-2025 Microsoft  
PrivacyTerms of Use

### Using TypeScript

* Get Started
* Download
* Playground
* TSConfig Ref
* Code Samples
* Why TypeScript
* Design

### Community

* Get Help
* GitHub Repo
* Community Chat
* @TypeScript
* Mastodon
* Stack Overflow
* Web Repo

MSG

---

## Source: index.md

TypeScript: JavaScript With Syntax For Types.

Skip to main content

TypeScript

* Download
* Docs
* Handbook
* Playground
* Tools

in En

# TypeScript is **JavaScript with syntax for types.**

TypeScript is a strongly typed programming language that builds on JavaScript, giving you better tooling at any scale.

Try TypeScript Now

Online or via npm

* Editor Checks
* Auto-complete
* Interfaces
* JSX

```
ts

const user = {

firstName: "Angela",

lastName: "Davis",

role: "Professor",

}

console.log(user.name)

Property 'name' does not exist on type '{ firstName: string; lastName: string; role: string; }'.2339Property 'name' does not exist on type '{ firstName: string; lastName: string; role: string; }'.
```

```
ts

const user = {

firstName: "Angela",

lastName: "Davis",

role: "Professor",

}

console.log(user.name)

Property 'name' does not exist on type '{ firstName: string; lastName: string; role: string; }'.2339Property 'name' does not exist on type '{ firstName: string; lastName: string; role: string; }'.
```

TypeScript 5.9 is now available

## What is TypeScript?

### JavaScript and More

TypeScript adds additional syntax to JavaScript to support a **tighter integration with your editor**. Catch errors early in your editor.

### A Result You Can Trust

TypeScript code converts to JavaScript, which **runs anywhere JavaScript runs**: In a browser, on Node.js, Deno, Bun and in your apps.

### Safety at Scale

TypeScript understands JavaScript and uses **type inference to give you great tooling** without additional code.

## Get Started

Handbook

Learn the language

Playground

Try in your browser

Download

Install TypeScript

## Adopt TypeScript Gradually

Apply types to your JavaScript project incrementally, **each step improves editor support** and improves your codebase.

Let's take this incorrect JavaScript code, and see how **TypeScript can catch mistakes in your editor**.

```
js

function compact(arr) {

if (orr.length > 10)

return arr.trim(0, 10)

return arr

}
```

No editor warnings in JavaScript files  
  
This code crashes at runtime!

JavaScript file

```
js

// @ts-check

function compact(arr) {

if (orr.length > 10)

Cannot find name 'orr'.2304Cannot find name 'orr'.

return arr.trim(0, 10)

return arr

}
```

Adding this to a JS file shows errors in your editor

the param is arr, not orr!

JavaScript with TS Check

```
js

// @ts-check

/** @param {any[]} arr */

function compact(arr) {

if (arr.length > 10)

return arr.trim(0, 10)

Property 'trim' does not exist on type 'any[]'.2339Property 'trim' does not exist on type 'any[]'.

return arr

}
```

Using JSDoc to give type information

Now TS has found a bad call. Arrays have slice, not trim.

JavaScript with JSDoc

```
ts

function compact(arr: string[]) {

if (arr.length > 10)

return arr.slice(0, 10)

return arr

}
```

TypeScript adds natural syntax for providing types

TypeScript file

### Describe Your Data

**Describe the shape of objects and functions** in your code.

Making it possible to see **documentation and issues in your editor**.

```
ts

interface Account {

id: number

displayName: string

version: 1

}

function welcome(user: Account) {

console.log(user.id)

}
```

```
ts

type Result = "pass" | "fail"

function verify(result: Result) {

if (result === "pass") {

console.log("Passed")

} else {

console.log("Failed")

}

}
```

## TypeScript becomes JavaScript via the delete key.

```
ts

type Result = "pass" | "fail"

function verify(result: Result) {

if (result === "pass") {

console.log("Passed")

} else {

console.log("Failed")

}

}
```

**TypeScript file**.

```
ts

type Result = "pass" | "fail"

function verify(result: Result) {

if (result === "pass") {

console.log("Passed")

} else {

console.log("Failed")

}

}
```

**Types are removed**.

```
js

function verify(result) {

if (result === "pass") {

console.log("Passed")

} else {

console.log("Failed")

}

}
```

**JavaScript file**.

## TypeScript Testimonials

**First**, we were surprised by the number of small bugs we found when converting our code.

**Second**, we underestimated how powerful the editor integration is.

TypeScript was such a boon to our stability and sanity that we started using it for all new code within days of starting the conversion.

Felix Rieseberg at Slack covered the transition of their desktop app from JavaScript to TypeScript in their blog

Read

### Open Source with TypeScript

AngularVueJestReduxIonicProbotDenoVercelYarnGitHub  
Desktop

## Loved by Developers

!Image of the stack overflow logo, and a graph showing TypeScript as the 2nd most popular language

Voted **2nd most loved programming language** in the Stack Overflow 2020 Developer survey

TypeScript was **used by 78%** of the 2020 State of JS respondents, with **93% saying they would use it again**.

TypeScript was given the award for **“Most Adopted Technology”** based on year-on-year growth.

## Get Started

Handbook

Learn the language

Playground

Try in your browser

Download

Install TypeScript

Made with ♥ in Redmond, Boston, SF & Dublin

© 2012-2025 Microsoft  
PrivacyTerms of Use

### Using TypeScript

* Get Started
* Download
* Playground
* TSConfig Ref
* Code Samples
* Why TypeScript
* Design

### Community

* Get Help
* GitHub Repo
* Community Chat
* @TypeScript
* Mastodon
* Stack Overflow
* Web Repo

MSG

---