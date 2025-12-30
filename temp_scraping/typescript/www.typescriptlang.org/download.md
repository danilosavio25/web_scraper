TypeScript: How to set up TypeScript

[Skip to main content](#site-content)

[TypeScript](/)

* [Download](/download/)
* [Docs](/docs/)
* [Handbook](/docs/handbook/intro.html)
* [Community](/community/)
* [Playground](/play/)
* [Tools](/tools/)

in En

# Download TypeScript

TypeScript can be installed through three installation routes depending on how you intend to use it: an npm module, a NuGet package or a Visual Studio Extension.

If you are using Node.js, you want the npm version. If you are using MSBuild in your project, you want the NuGet package or Visual Studio extension.

## TypeScript in Your Project

Having TypeScript set up on a per-project basis lets you have many projects with many different versions of TypeScript, this keeps each project working consistently.

### via npm

TypeScript is available as a [package on the npm registry](https://www.npmjs.com/package/typescript) available as `"typescript"`.

You will need a copy of [Node.js](https://nodejs.org/en/ "Link to the node.js project") as an environment to run the package. Then you use a dependency manager like [npm](https://www.npmjs.com/ "Link to the npm package manager"), [yarn](https://yarnpkg.com/ "Link to the yarn package manager") or [pnpm](https://pnpm.js.org/ "Link to the pnpm package manager") to download TypeScript into your project.

`npm install typescript --save-dev`  
  
npm yarn pnpm

All of these dependency managers support lockfiles, ensuring that everyone on your team is using the same version of the language. You can then run the TypeScript compiler using one of the following commands:

`npx tsc`  
  
npm yarn pnpm

### with Visual Studio

For most project types, you can get TypeScript as a package in Nuget for your MSBuild projects, for example an ASP.NET Core app.

When using Nuget, you can [install TypeScript through Visual Studio](https://learn.microsoft.com/visualstudio/javascript/tutorial-aspnet-with-typescript) using:

* The Manage NuGet Packages window (which you can get to by right-clicking on a project node)
* The Nuget Package Manager Console (found in Tools > NuGet Package Manager > Package Manager Console) and then running:  
  `Install-Package Microsoft.TypeScript.MSBuild`

For project types which don't support Nuget, you can use the  [TypeScript Visual Studio extension](https://marketplace.visualstudio.com/items?itemName=TypeScriptTeam.typescript-593). You can [install the extension](https://learn.microsoft.com/visualstudio/ide/finding-and-using-visual-studio-extensions) using `Extensions > Manage Extensions` in Visual Studio.

The examples below are for more advanced use cases.

## Globally Installing TypeScript

It can be handy to have TypeScript available across all projects, often to test one-off ideas. Long-term, codebases should prefer a project-wide installation over a global install so that they can benefit from reproducible builds across different machines.

### via npm

You can use npm to install TypeScript globally, this means that you can use the `tsc` command anywhere in your terminal.

To do this, run `npm install -g typescript`. This will install the latest version (currently 5.9).

### via Visual Studio Marketplace

You can install TypeScript as a Visual Studio extension, which will allow you to use TypeScript across many MSBuild projects in Visual Studio.

The latest version is available [in the Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=TypeScriptTeam.typescript-593 "Link to the Visual Studio Marketplace for the TypeScript MSBuild extension").

## Working with TypeScript-compatible transpilers

There are other tools which convert TypeScript files to JavaScript files. You might use these tools for speed or consistency with your existing build tooling.

Each of these projects handle the file conversion, but do not handle the type-checking aspects of the TypeScript compiler. So it's likely that you will still need to keep the above TypeScript dependency around, and you will want to enable [`isolatedModules`](/tsconfig/#isolatedModules).

### Babel

[Babel](https://babeljs.io/) is a very popular JavaScript transpiler which supports TypeScript files via the plugin [@babel/plugin-transform-typescript](https://babeljs.io/docs/en/babel-preset-typescript#docsNav).

### swc

[swc](https://swc-project.github.io/docs/installation/) is a fast transpiler created in Rust which supports many of Babel's features including TypeScript.

### Sucrase

[Sucrase](https://github.com/alangpierce/sucrase#sucrase/) is a Babel fork focused on speed for using in development mode. Sucrase supports TypeScript natively.

## Next Steps

#### Get Started

* [JS to TS](/docs/handbook/typescript-in-5-minutes.html)
* [New to Programming](/docs/handbook/typescript-from-scratch.html)
* [OOP to JS](/docs/handbook/typescript-in-5-minutes-oop.html)
* [Functional to JS](/docs/handbook/typescript-in-5-minutes-func.html)
* [Installation](/download/)

#### Handbook

* [Everyday Types](/docs/handbook/2/everyday-types.html)
* [Creating Types from Types](/docs/handbook/2/types-from-types.html)
* [Object Types](/docs/handbook/2/objects.html)
* [Variable Declarations](/docs/handbook/variable-declarations.html)
* [More on Functions](/docs/handbook/2/functions.html)

#### Tools

* [Playground](/play/)
* [TSConfig Reference](/tsconfig/)

#### Release Notes

* [What's new in 5.9](/docs/handbook/release-notes/typescript-5-9.html)

#### Tutorials

* [ASP.NET](/docs/handbook/asp-net-core.html)
* [Migrating from JS](/docs/handbook/migrating-from-javascript.html)
* [Working with the DOM](/docs/handbook/dom-manipulation.html)
* [React & Webpack](/docs/handbook/react-&-webpack.html)

### Customize

Site Colours:

SystemAlways LightAlways Dark

Code Font:

CascadiaCascadia (ligatures)ConsolasDank MonoFira CodeJetBrains MonoOpenDyslexicSF MonoSource Code Pro

### Popular Documentation Pages

* [Everyday Types](/docs/handbook/2/everyday-types.html)

  All of the common types in TypeScript
* [Creating Types from Types](/docs/handbook/2/types-from-types.html)

  Techniques to make more elegant types
* [More on Functions](/docs/handbook/2/functions.html)

  How to provide types to functions in JavaScript
* [More on Objects](/docs/handbook/2/objects.html)

  How to provide a type shape to JavaScript objects
* [Narrowing](/docs/handbook/2/narrowing.html)

  How TypeScript infers types based on runtime behavior
* [Variable Declarations](/docs/handbook/variable-declarations.html)

  How to create and type JavaScript variables
* [TypeScript in 5 minutes](/docs/handbook/typescript-in-5-minutes.html)

  An overview of building a TypeScript web app
* [TSConfig Options](/tsconfig/)

  All the configuration options for a project
* [Classes](/docs/handbook/2/classes.html)

  How to provide types to JavaScript ES6 classes

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