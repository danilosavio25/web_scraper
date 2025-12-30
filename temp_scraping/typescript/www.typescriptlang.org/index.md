TypeScript: JavaScript With Syntax For Types.

[Skip to main content](#site-content)

[TypeScript](/)

* [Download](/download/)
* [Docs](/docs/)
* [Handbook](/docs/handbook/intro.html)
* [Community](/community/)
* [Playground](/play/)
* [Tools](/tools/)

in En

# TypeScript is **JavaScript with syntax for types.**

TypeScript is a strongly typed programming language that builds on JavaScript, giving you better tooling at any scale.

[Try TypeScript Now

Online or via npm](/download)

* [Editor Checks](#)
* [Auto-complete](#)
* [Interfaces](#)
* [JSX](#)

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

[TypeScript 5.9](/docs/handbook/release-notes/typescript-5-9.html) is now available

## What is TypeScript?

### JavaScript and More

TypeScript adds additional syntax to JavaScript to support a **tighter integration with your editor**. Catch errors early in your editor.

### A Result You Can Trust

TypeScript code converts to JavaScript, which **runs anywhere JavaScript runs**: In a browser, on Node.js, Deno, Bun and in your apps.

### Safety at Scale

TypeScript understands JavaScript and uses **type inference to give you great tooling** without additional code.

## Get Started

[Handbook

Learn the language](/docs/handbook/intro.html)

[Playground

Try in your browser](/play)

[Download

Install TypeScript](/download/)

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

[Read](https://slack.engineering/typescript-at-slack-a81307fa288d)

### Open Source with TypeScript

[Angular](https://angular.io/)[Vue](https://vuejs.org/)[Jest](https://jestjs.io/)[Redux](https://redux.js.org/)[Ionic](https://ionicframework.com/)[Probot](https://probot.github.io/)[Deno](https://deno.land/)[Vercel](https://github.com/vercel/vercel)[Yarn](https://yarnpkg.com/)[GitHub  
Desktop](https://github.com/desktop/desktop/)

## Loved by Developers

![Image of the stack overflow logo, and a graph showing TypeScript as the 2nd most popular language](/images/index/stack-overflow.svg)

Voted **2nd most loved programming language** in the [Stack Overflow 2020 Developer survey](https://insights.stackoverflow.com/survey/2020#most-loved-dreaded-and-wanted)

![Logo of the State of JS survey](/images/index/state-of-js.svg)

TypeScript was **used by 78%** of the [2020 State of JS](https://2020.stateofjs.com/en-US/technologies/javascript-flavors/) respondents, with **93% saying they would use it again**.

TypeScript was given the award for **“Most Adopted Technology”** based on year-on-year growth.

## Get Started

[Handbook

Learn the language](/docs/handbook/intro.html)

[Playground

Try in your browser](/play)

[Download

Install TypeScript](/download/)

Made with ♥ in Redmond, Boston, SF & Dublin

![Microsoft Logo](data:image/png;base64,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)

© 2012-2025 Microsoft  
[Privacy](https://go.microsoft.com/fwlink/?LinkId=521839 "Microsoft Privacy Policy")[Terms of Use](https://go.microsoft.com/fwlink/?LinkID=206977)

### Using TypeScript

* [Get Started](/docs/)
* [Download](/download/)
* [Community](/community/)
* [Playground](/play/)
* [TSConfig Ref](/tsconfig/)
* [Code Samples](/play/#show-examples)
* [Why TypeScript](/why-create-typescript/)
* [Design](/branding/)

### Community

* [Get Help](/community)
* [Blog](https://devblogs.microsoft.com/typescript/)
* [GitHub Repo](https://github.com/microsoft/TypeScript/#readme)
* [Community Chat](https://discord.gg/typescript)
* [@TypeScript](https://twitter.com/TypeScript)
* [Mastodon](https://fosstodon.org/@TypeScript)
* [Stack Overflow](https://stackoverflow.com/questions/tagged/typescript)
* [Web Repo](https://github.com/microsoft/TypeScript-Website)

MSG