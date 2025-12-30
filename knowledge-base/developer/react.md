# React Knowledge

> Category: frameworks

## Source: community.md

React Community – React

React

v19.2

Search`⌘``Ctrl``K`

Learn

Reference

Community

Blog

### GET INVOLVED

  + React Conferences
  + React Meetups
  + React Videos
  + Meet the Team
  + Docs Contributors
  + Translations
  + Acknowledgements
  + Versioning Policy

Is this page useful?

Community

# React Community

React has a community of millions of developers. On this page we’ve listed some React-related communities that you can be a part of; see the other pages in this section for additional online and in-person learning materials.

## Code of Conduct

Before participating in React’s communities, please read our Code of Conduct. We have adopted the Contributor Covenant and we expect that all community members adhere to the guidelines within.

## Stack Overflow

Stack Overflow is a popular forum to ask code-level questions or if you’re stuck with a specific error. Read through the existing questions tagged with **reactjs** or ask your own!

## Popular Discussion Forums

There are many online forums which are a great place for discussion about best practices and application architecture as well as the future of React. If you have an answerable code-level question, Stack Overflow is usually a better fit.

Each community consists of many thousands of React users.

* DEV’s React community
* Hashnode’s React community
* Reactiflux online chat
* Reddit’s React community

## News

For the latest news about React, follow **@reactjs** on Twitter, **@react.dev** on Bluesky and the official React blog on this website.

NextReact Conferences

---

Copyright © Meta Platforms, Inc

no uwu plz

uwu?

Logo by@sawaratsuki1004

Learn React

Quick Start

Installation

Describing the UI

Adding Interactivity

Managing State

Escape Hatches

API Reference

React APIs

React DOM APIs

Community

Code of Conduct

Meet the Team

Docs Contributors

Acknowledgements

More

Blog

React Native

Privacy

Terms

## On this page

* Overview
* Code of Conduct
* Stack Overflow
* Popular Discussion Forums
* News

---

## Source: index.md

React

React

v19.2

Search`⌘``Ctrl``K`

Learn

Reference

Community

Blog

# React

The library for web and native user interfaces

Learn ReactAPI Reference

## Create user interfaces from components

React lets you build user interfaces out of individual pieces called components. Create your own React components like `Thumbnail`, `LikeButton`, and `Video`. Then combine them into entire screens, pages, and apps.

### Video.js

```
function Video({ video }) {

return (

<div>

<Thumbnail video={video} />

<a href={video.url}>

<h3>{video.title}</h3>

<p>{video.description}</p>

</a>

<LikeButton video={video} />

</div>

);

}
```

### My video

Video description

Whether you work on your own or with thousands of other developers, using React feels the same. It is designed to let you seamlessly combine components written by independent people, teams, and organizations.

## Write components with code and markup

React components are JavaScript functions. Want to show some content conditionally? Use an `if` statement. Displaying a list? Try array `map()`. Learning React is learning programming.

### VideoList.js

```
function VideoList({ videos, emptyHeading }) {

const count = videos.length;

let heading = emptyHeading;

if (count > 0) {

const noun = count > 1 ? 'Videos' : 'Video';

heading = count + ' ' + noun;

}

return (

<section>

<h2>{heading}</h2>

{videos.map(video =>

<Video key={video.id} video={video} />

)}

</section>

);

}
```

## 3 Videos

### First video

Video description

### Second video

Video description

### Third video

Video description

This markup syntax is called JSX. It is a JavaScript syntax extension popularized by React. Putting JSX markup close to related rendering logic makes React components easy to create, maintain, and delete.

## Add interactivity wherever you need it

React components receive data and return what should appear on the screen. You can pass them new data in response to an interaction, like when the user types into an input. React will then update the screen to match the new data.

### SearchableVideoList.js

```
import { useState } from 'react';

function SearchableVideoList({ videos }) {

const [searchText, setSearchText] = useState('');

const foundVideos = filterVideos(videos, searchText);

return (

<>

<SearchInput

value={searchText}

onChange={newText => setSearchText(newText)} />

<VideoList

videos={foundVideos}

emptyHeading={`No matches for “${searchText}”`} />

</>

);

}
```

example.com/videos.html

# React Videos

A brief history of React

Search

## 5 Videos

### React: The Documentary

The origin story of React

### Rethinking Best Practices

Pete Hunt (2013)

### Introducing React Native

Tom Occhino (2015)

### Introducing React Hooks

Sophie Alpert and Dan Abramov (2018)

### Introducing Server Components

Dan Abramov and Lauren Tan (2020)

You don’t have to build your whole page in React. Add React to your existing HTML page, and render interactive React components anywhere on it.

Add React to your page

## Go full-stack with a framework

React is a library. It lets you put components together, but it doesn’t prescribe how to do routing and data fetching. To build an entire app with React, we recommend a full-stack React framework like Next.js or React Router.

### confs/[slug].js

```
import { db } from './database.js';

import { Suspense } from 'react';

async function ConferencePage({ slug }) {

const conf = await db.Confs.find({ slug });

return (

<ConferenceLayout conf={conf}>

<Suspense fallback={<TalksLoading />}>

<Talks confId={conf.id} />

</Suspense>

</ConferenceLayout>

);

}

async function Talks({ confId }) {

const talks = await db.Talks.findAll({ confId });

const videos = talks.map(talk => talk.video);

return <SearchableVideoList videos={videos} />;

}
```

example.com/confs/react-conf-2021

React Conf 2021React Conf 2019

Search

## 19 Videos

React Conf]()### React 18 Keynote

The React Team

React Conf### React 18 for App Developers

Shruti Kapoor

React Conf### Streaming Server Rendering with Suspense

Shaundai Person

React Conf### The First React Working Group

Aakansha Doshi

React Conf### React Developer Tooling

Brian Vaughn

React Conf### React without memo

Xuan Huang (黄玄)

React Conf### React Docs Keynote

Rachel Nabors

React Conf### Things I Learnt from the New React Docs

Debbie O'Brien

React Conf### Learning in the Browser

Sarah Rainsberger

React Conf### The ROI of Designing with React

Linton Ye

React Conf### Interactive Playgrounds with React

Delba de Oliveira

React Conf### Re-introducing Relay

Robert Balicki

React Conf]()### React Native Desktop

Eric Rozell and Steven Moyes

React Conf### On-device Machine Learning for React Native

Roman Rädle

React Conf### React 18 for External Store Libraries

Daishi Kato

React Conf### Building Accessible Components with React 18

Diego Haz

React Conf### Accessible Japanese Form Components with React

Tafu Nakazaki

React Conf### UI Tools for Artists

Lyle Troxell

React Conf### Hydrogen + React 18

Helen Lin

React is also an architecture. Frameworks that implement it let you fetch data in asynchronous components that run on the server or even during the build. Read data from a file or a database, and pass it down to your interactive components.

Get started with a framework

## Use the best from every platform

People love web and native apps for different reasons. React lets you build both web apps and native apps using the same skills. It leans upon each platform’s unique strengths to let your interfaces feel just right on every platform.

example.com

#### Stay true to the web

People expect web app pages to load fast. On the server, React lets you start streaming HTML while you’re still fetching data, progressively filling in the remaining content before any JavaScript code loads. On the client, React can use standard web APIs to keep your UI responsive even in the middle of rendering.

1:08 AM

#### Go truly native

People expect native apps to look and feel like their platform. React Native and Expo let you build apps in React for Android, iOS, and more. They look and feel native because their UIs *are* truly native. It’s not a web view—your React components render real Android and iOS views provided by the platform.

With React, you can be a web *and* a native developer. Your team can ship to many platforms without sacrificing the user experience. Your organization can bridge the platform silos, and form teams that own entire features end-to-end.

Build for native platforms

## Upgrade when the future is ready

React approaches changes with care. Every React commit is tested on business-critical surfaces with over a billion users. Over 100,000 React components at Meta help validate every migration strategy.

The React team is always researching how to improve React. Some research takes years to pay off. React has a high bar for taking a research idea into production. Only proven approaches become a part of React.

Read more React news

Latest React News

## Additional Vulnerabilities in RSC

December 11, 2025

## Vulnerability in React Server Components

December 3, 2025

## React Conf 2025 Recap

October 16, 2025

## React Compiler v1.0

October 7, 2025

Read more React news

## Join a community of millions

You’re not alone. Two million developers from all over the world visit the React docs every month. React is something that people and teams can agree on.

!A hallway conversation between two people at React Conf

!A hallway conversation between two people at React Conf

This is why React is more than a library, an architecture, or even an ecosystem. React is a community. It’s a place where you can ask for help, find opportunities, and meet new friends. You will meet both developers and designers, beginners and experts, researchers and artists, teachers and students. Our backgrounds may be very different, but React lets us all create user interfaces together.

## Welcome to the React community

Get Started

Copyright © Meta Platforms, Inc

no uwu plz

uwu?

Logo by@sawaratsuki1004

Learn React

Quick Start

Installation

Describing the UI

Adding Interactivity

Managing State

Escape Hatches

API Reference

React APIs

React DOM APIs

Community

Code of Conduct

Meet the Team

Docs Contributors

Acknowledgements

More

Blog

React Native

Privacy

Terms

---

## Source: learn.md

Quick Start – React

React

v19.2

Search`⌘``Ctrl``K`

Learn

Reference

Community

Blog

### GET STARTED

* Quick Start

  + Tutorial: Tic-Tac-Toe
  + Thinking in React
* Installation

  + Creating a React App
  + Build a React App from Scratch
  + Add React to an Existing Project
* Setup

  + Editor Setup
  + Using TypeScript
  + React Developer Tools
* React Compiler

  + Introduction
  + Installation
  + Incremental Adoption
  + Debugging and Troubleshooting

### LEARN REACT

* Describing the UI

  + Your First Component
  + Importing and Exporting Components
  + Writing Markup with JSX
  + JavaScript in JSX with Curly Braces
  + Passing Props to a Component
  + Conditional Rendering
  + Rendering Lists
  + Keeping Components Pure
  + Your UI as a Tree
* Adding Interactivity

  + Responding to Events
  + State: A Component's Memory
  + Render and Commit
  + State as a Snapshot
  + Queueing a Series of State Updates
  + Updating Objects in State
  + Updating Arrays in State
* Managing State

  + Reacting to Input with State
  + Choosing the State Structure
  + Sharing State Between Components
  + Preserving and Resetting State
  + Extracting State Logic into a Reducer
  + Passing Data Deeply with Context
  + Scaling Up with Reducer and Context
* Escape Hatches

  + Referencing Values with Refs
  + Manipulating the DOM with Refs
  + Synchronizing with Effects
  + You Might Not Need an Effect
  + Lifecycle of Reactive Effects
  + Separating Events from Effects
  + Removing Effect Dependencies
  + Reusing Logic with Custom Hooks

Is this page useful?

Learn React

# Quick Start

Welcome to the React documentation! This page will give you an introduction to 80% of the React concepts that you will use on a daily basis.

### You will learn

* How to create and nest components
* How to add markup and styles
* How to display data
* How to render conditions and lists
* How to respond to events and update the screen
* How to share data between components

## Creating and nesting components

React apps are made out of *components*. A component is a piece of the UI (user interface) that has its own logic and appearance. A component can be as small as a button, or as large as an entire page.

React components are JavaScript functions that return markup:

```
function MyButton() {

return (

<button>I'm a button</button>

);

}
```

Now that you’ve declared `MyButton`, you can nest it into another component:

```
export default function MyApp() {

return (

<div>

<h1>Welcome to my app</h1>

<MyButton />

</div>

);

}
```

Notice that `<MyButton />` starts with a capital letter. That’s how you know it’s a React component. React component names must always start with a capital letter, while HTML tags must be lowercase.

Have a look at the result:

App.js

App.js

ReloadClearFork

```
function MyButton() {
  return (
    <button>
      I'm a button
    </button>
  );
}

export default function MyApp() {
  return (
    <div>
      <h1>Welcome to my app</h1>
      <MyButton />
    </div>
  );
}
```

Show more

The `export default` keywords specify the main component in the file. If you’re not familiar with some piece of JavaScript syntax, MDN and javascript.info have great references.

## Writing markup with JSX

The markup syntax you’ve seen above is called *JSX*. It is optional, but most React projects use JSX for its convenience. All of the tools we recommend for local development support JSX out of the box.

JSX is stricter than HTML. You have to close tags like `<br />`. Your component also can’t return multiple JSX tags. You have to wrap them into a shared parent, like a `<div>...</div>` or an empty `<>...</>` wrapper:

```
function AboutPage() {

return (

<>

<h1>About</h1>

<p>Hello there.<br />How do you do?</p>

</>

);

}
```

If you have a lot of HTML to port to JSX, you can use an online converter.

## Adding styles

In React, you specify a CSS class with `className`. It works the same way as the HTML `class` attribute:

```
<img className="avatar" />
```

Then you write the CSS rules for it in a separate CSS file:

```
/* In your CSS */

.avatar {

border-radius: 50%;

}
```

React does not prescribe how you add CSS files. In the simplest case, you’ll add a `<link>` tag to your HTML. If you use a build tool or a framework, consult its documentation to learn how to add a CSS file to your project.

## Displaying data

JSX lets you put markup into JavaScript. Curly braces let you “escape back” into JavaScript so that you can embed some variable from your code and display it to the user. For example, this will display `user.name`:

```
return (

<h1>

{user.name}

</h1>

);
```

You can also “escape into JavaScript” from JSX attributes, but you have to use curly braces *instead of* quotes. For example, `className="avatar"` passes the `"avatar"` string as the CSS class, but `src={user.imageUrl}` reads the JavaScript `user.imageUrl` variable value, and then passes that value as the `src` attribute:

```
return (

<img

className="avatar"

src={user.imageUrl}

/>

);
```

You can put more complex expressions inside the JSX curly braces too, for example, string concatenation:

App.js

App.js

ReloadClearFork

```
const user = {
  name: 'Hedy Lamarr',
  imageUrl: '
  imageSize: 90,
};

export default function Profile() {
  return (
    <>
      <h1>{user.name}</h1>
      <img
        className="avatar"
        src={user.imageUrl}
        alt={'Photo of ' + user.name}
        style={{
          width: user.imageSize,
          height: user.imageSize
        }}
      />
    </>
  );
}
```

Show more

In the above example, `style={{}}` is not a special syntax, but a regular `{}` object inside the `style={ }` JSX curly braces. You can use the `style` attribute when your styles depend on JavaScript variables.

## Conditional rendering

In React, there is no special syntax for writing conditions. Instead, you’ll use the same techniques as you use when writing regular JavaScript code. For example, you can use an `if` statement to conditionally include JSX:

```
let content;

if (isLoggedIn) {

content = <AdminPanel />;

} else {

content = <LoginForm />;

}

return (

<div>

{content}

</div>

);
```

If you prefer more compact code, you can use the conditional `?` operator. Unlike `if`, it works inside JSX:

```
<div>

{isLoggedIn ? (

<AdminPanel />

) : (

<LoginForm />

)}

</div>
```

When you don’t need the `else` branch, you can also use a shorter logical `&&` syntax:

```
<div>

{isLoggedIn && <AdminPanel />}

</div>
```

All of these approaches also work for conditionally specifying attributes. If you’re unfamiliar with some of this JavaScript syntax, you can start by always using `if...else`.

## Rendering lists

You will rely on JavaScript features like `for` loop and the array `map()` function to render lists of components.

For example, let’s say you have an array of products:

```
const products = [

{ title: 'Cabbage', id: 1 },

{ title: 'Garlic', id: 2 },

{ title: 'Apple', id: 3 },

];
```

Inside your component, use the `map()` function to transform an array of products into an array of `<li>` items:

```
const listItems = products.map(product =>

<li key={product.id}>

{product.title}

</li>

);

return (

<ul>{listItems}</ul>

);
```

Notice how `<li>` has a `key` attribute. For each item in a list, you should pass a string or a number that uniquely identifies that item among its siblings. Usually, a key should be coming from your data, such as a database ID. React uses your keys to know what happened if you later insert, delete, or reorder the items.

App.js

App.js

ReloadClearFork

```
const products = [
  { title: 'Cabbage', isFruit: false, id: 1 },
  { title: 'Garlic', isFruit: false, id: 2 },
  { title: 'Apple', isFruit: true, id: 3 },
];

export default function ShoppingList() {
  const listItems = products.map(product =>
    <li
      key={product.id}
      style={{
        color: product.isFruit ? 'magenta' : 'darkgreen'
      }}
    >
      {product.title}
    </li>
  );

  return (
    <ul>{listItems}</ul>
  );
}
```

Show more

## Responding to events

You can respond to events by declaring *event handler* functions inside your components:

```
function MyButton() {

function handleClick() {

alert('You clicked me!');

}

return (

<button onClick={handleClick}>

Click me

</button>

);

}
```

Notice how `onClick={handleClick}` has no parentheses at the end! Do not *call* the event handler function: you only need to *pass it down*. React will call your event handler when the user clicks the button.

## Updating the screen

Often, you’ll want your component to “remember” some information and display it. For example, maybe you want to count the number of times a button is clicked. To do this, add *state* to your component.

First, import `useState` from React:

```
import { useState } from 'react';
```

Now you can declare a *state variable* inside your component:

```
function MyButton() {

const [count, setCount] = useState(0);

// ...
```

You’ll get two things from `useState`: the current state (`count`), and the function that lets you update it (`setCount`). You can give them any names, but the convention is to write `[something, setSomething]`.

The first time the button is displayed, `count` will be `0` because you passed `0` to `useState()`. When you want to change state, call `setCount()` and pass the new value to it. Clicking this button will increment the counter:

```
function MyButton() {

const [count, setCount] = useState(0);

function handleClick() {

setCount(count + 1);

}

return (

<button onClick={handleClick}>

Clicked {count} times

</button>

);

}
```

React will call your component function again. This time, `count` will be `1`. Then it will be `2`. And so on.

If you render the same component multiple times, each will get its own state. Click each button separately:

App.js

App.js

ReloadClearFork

```
import { useState } from 'react';

export default function MyApp() {
  return (
    <div>
      <h1>Counters that update separately</h1>
      <MyButton />
      <MyButton />
    </div>
  );
}

function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <button onClick={handleClick}>
      Clicked {count} times
    </button>
  );
}
```

Show more

Notice how each button “remembers” its own `count` state and doesn’t affect other buttons.

## Using Hooks

Functions starting with `use` are called *Hooks*. `useState` is a built-in Hook provided by React. You can find other built-in Hooks in the API reference. You can also write your own Hooks by combining the existing ones.

Hooks are more restrictive than other functions. You can only call Hooks *at the top* of your components (or other Hooks). If you want to use `useState` in a condition or a loop, extract a new component and put it there.

## Sharing data between components

In the previous example, each `MyButton` had its own independent `count`, and when each button was clicked, only the `count` for the button clicked changed:

!Diagram showing a tree of three components, one parent labeled MyApp and two children labeled MyButton. Both MyButton components contain a count with value zero.

!Diagram showing a tree of three components, one parent labeled MyApp and two children labeled MyButton. Both MyButton components contain a count with value zero.

Initially, each `MyButton`’s `count` state is `0`

!The same diagram as the previous, with the count of the first child MyButton component highlighted indicating a click with the count value incremented to one. The second MyButton component still contains value zero.

!The same diagram as the previous, with the count of the first child MyButton component highlighted indicating a click with the count value incremented to one. The second MyButton component still contains value zero.

The first `MyButton` updates its `count` to `1`

However, often you’ll need components to *share data and always update together*.

To make both `MyButton` components display the same `count` and update together, you need to move the state from the individual buttons “upwards” to the closest component containing all of them.

In this example, it is `MyApp`:

!Diagram showing a tree of three components, one parent labeled MyApp and two children labeled MyButton. MyApp contains a count value of zero which is passed down to both of the MyButton components, which also show value zero.

!Diagram showing a tree of three components, one parent labeled MyApp and two children labeled MyButton. MyApp contains a count value of zero which is passed down to both of the MyButton components, which also show value zero.

Initially, `MyApp`’s `count` state is `0` and is passed down to both children

!The same diagram as the previous, with the count of the parent MyApp component highlighted indicating a click with the value incremented to one. The flow to both of the children MyButton components is also highlighted, and the count value in each child is set to one indicating the value was passed down.

!The same diagram as the previous, with the count of the parent MyApp component highlighted indicating a click with the value incremented to one. The flow to both of the children MyButton components is also highlighted, and the count value in each child is set to one indicating the value was passed down.

On click, `MyApp` updates its `count` state to `1` and passes it down to both children

Now when you click either button, the `count` in `MyApp` will change, which will change both of the counts in `MyButton`. Here’s how you can express this in code.

First, *move the state up* from `MyButton` into `MyApp`:

```
export default function MyApp() {

const [count, setCount] = useState(0);

function handleClick() {

setCount(count + 1);

}

return (

<div>

<h1>Counters that update separately</h1>

<MyButton />

<MyButton />

</div>

);

}

function MyButton() {

// ... we're moving code from here ...

}
```

Then, *pass the state down* from `MyApp` to each `MyButton`, together with the shared click handler. You can pass information to `MyButton` using the JSX curly braces, just like you previously did with built-in tags like `<img>`:

```
export default function MyApp() {

const [count, setCount] = useState(0);

function handleClick() {

setCount(count + 1);

}

return (

<div>

<h1>Counters that update together</h1>

<MyButton count={count} onClick={handleClick} />

<MyButton count={count} onClick={handleClick} />

</div>

);

}
```

The information you pass down like this is called *props*. Now the `MyApp` component contains the `count` state and the `handleClick` event handler, and *passes both of them down as props* to each of the buttons.

Finally, change `MyButton` to *read* the props you have passed from its parent component:

```
function MyButton({ count, onClick }) {

return (

<button onClick={onClick}>

Clicked {count} times

</button>

);

}
```

When you click the button, the `onClick` handler fires. Each button’s `onClick` prop was set to the `handleClick` function inside `MyApp`, so the code inside of it runs. That code calls `setCount(count + 1)`, incrementing the `count` state variable. The new `count` value is passed as a prop to each button, so they all show the new value. This is called “lifting state up”. By moving state up, you’ve shared it between components.

App.js

App.js

ReloadClearFork

```
import { useState } from 'react';

export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Counters that update together</h1>
      <MyButton count={count} onClick={handleClick} />
      <MyButton count={count} onClick={handleClick} />
    </div>
  );
}

function MyButton({ count, onClick }) {
  return (
    <button onClick={onClick}>
      Clicked {count} times
    </button>
  );
}
```

Show more

## Next Steps

By now, you know the basics of how to write React code!

Check out the Tutorial to put them into practice and build your first mini-app with React.

NextTutorial: Tic-Tac-Toe

---

Copyright © Meta Platforms, Inc

no uwu plz

uwu?

Logo by@sawaratsuki1004

Learn React

Quick Start

Installation

Describing the UI

Adding Interactivity

Managing State

Escape Hatches

API Reference

React APIs

React DOM APIs

Community

Code of Conduct

Meet the Team

Docs Contributors

Acknowledgements

More

Blog

React Native

Privacy

Terms

## On this page

* Overview
* Creating and nesting components
* Writing markup with JSX
* Adding styles
* Displaying data
* Conditional rendering
* Rendering lists
* Responding to events
* Updating the screen
* Using Hooks
* Sharing data between components
* Next Steps

---

## Source: reference_react.md

React Reference Overview – React

React

v19.2

Search`⌘``Ctrl``K`

Learn

Reference

Community

Blog

### react@19.2

* Overview
* Hooks

  + useActionState
  + useCallback
  + useContext
  + useDebugValue
  + useDeferredValue
  + useEffect
  + useEffectEvent
  + useId
  + useImperativeHandle
  + useInsertionEffect
  + useLayoutEffect
  + useMemo
  + useOptimistic
  + useReducer
  + useRef
  + useState
  + useSyncExternalStore
  + useTransition
* Components

  + <Fragment> (<>)")
  + <Profiler>
  + <StrictMode>
  + <Suspense>
  + <Activity>
  + <ViewTransition>  - This feature is available in the latest Canary version of React
* APIs

  + act
  + addTransitionType  - This feature is available in the latest Canary version of React
  + cache
  + cacheSignal
  + captureOwnerStack
  + createContext
  + lazy
  + memo
  + startTransition
  + use
  + experimental\_taintObjectReference  - This feature is available in the latest Experimental version of React
  + experimental\_taintUniqueValue  - This feature is available in the latest Experimental version of React

### react-dom@19.2

* Hooks

  + useFormStatus
* Components

  + Common (e.g. <div>)")
  + <form>
  + <input>
  + <option>
  + <progress>
  + <select>
  + <textarea>
  + <link>
  + <meta>
  + <script>
  + <style>
  + <title>
* APIs

  + createPortal
  + flushSync
  + preconnect
  + prefetchDNS
  + preinit
  + preinitModule
  + preload
  + preloadModule
* Client APIs

  + createRoot
  + hydrateRoot
* Server APIs

  + renderToPipeableStream
  + renderToReadableStream
  + renderToStaticMarkup
  + renderToString
  + resume
  + resumeToPipeableStream
* Static APIs

  + prerender
  + prerenderToNodeStream
  + resumeAndPrerender
  + resumeAndPrerenderToNodeStream

### React Compiler

* Configuration

  + compilationMode
  + gating
  + logger
  + panicThreshold
  + target
* Directives

  + "use memo"
  + "use no memo"
* Compiling Libraries

### React DevTools

* React Performance tracks

### eslint-plugin-react-hooks

* Lints

  + exhaustive-deps
  + rules-of-hooks
  + component-hook-factories
  + config
  + error-boundaries
  + gating
  + globals
  + immutability
  + incompatible-library
  + preserve-manual-memoization
  + purity
  + refs
  + set-state-in-effect
  + set-state-in-render
  + static-components
  + unsupported-syntax
  + use-memo

### Rules of React

* Overview

  + Components and Hooks must be pure
  + React calls Components and Hooks
  + Rules of Hooks

### React Server Components

* Server Components
* Server Functions
* Directives

  + 'use client'
  + 'use server'

### Legacy APIs

* Legacy React APIs

  + Children
  + cloneElement
  + Component
  + createElement
  + createRef
  + forwardRef
  + isValidElement
  + PureComponent

Is this page useful?

API Reference

# React Reference Overview

This section provides detailed reference documentation for working with React. For an introduction to React, please visit the Learn section.

The React reference documentation is broken down into functional subsections:

## React

Programmatic React features:

* Hooks - Use different React features from your components.
* Components - Built-in components that you can use in your JSX.
* APIs - APIs that are useful for defining components.
* Directives - Provide instructions to bundlers compatible with React Server Components.

## React DOM

React DOM contains features that are only supported for web applications (which run in the browser DOM environment). This section is broken into the following:

* Hooks - Hooks for web applications which run in the browser DOM environment.
* Components - React supports all of the browser built-in HTML and SVG components.
* APIs - The `react-dom` package contains methods supported only in web applications.
* Client APIs - The `react-dom/client` APIs let you render React components on the client (in the browser).
* Server APIs - The `react-dom/server` APIs let you render React components to HTML on the server.
* Static APIs - The `react-dom/static` APIs let you generate static HTML for React components.

## React Compiler

The React Compiler is a build-time optimization tool that automatically memoizes your React components and values:

* Configuration - Configuration options for React Compiler.
* Directives - Function-level directives to control compilation.
* Compiling Libraries - Guide for shipping pre-compiled library code.

## ESLint Plugin React Hooks

The ESLint plugin for React Hooks helps enforce the Rules of React:

* Lints - Detailed documentation for each lint with examples.

## Rules of React

React has idioms — or rules — for how to express patterns in a way that is easy to understand and yields high-quality applications:

* Components and Hooks must be pure – Purity makes your code easier to understand, debug, and allows React to automatically optimize your components and hooks correctly.
* React calls Components and Hooks – React is responsible for rendering components and hooks when necessary to optimize the user experience.
* Rules of Hooks – Hooks are defined using JavaScript functions, but they represent a special type of reusable UI logic with restrictions on where they can be called.

## Legacy APIs

* Legacy APIs - Exported from the `react` package, but not recommended for use in newly written code.

NextHooks

---

Copyright © Meta Platforms, Inc

no uwu plz

uwu?

Logo by@sawaratsuki1004

Learn React

Quick Start

Installation

Describing the UI

Adding Interactivity

Managing State

Escape Hatches

API Reference

React APIs

React DOM APIs

Community

Code of Conduct

Meet the Team

Docs Contributors

Acknowledgements

More

Blog

React Native

Privacy

Terms

## On this page

* Overview
* React
* React DOM
* React Compiler
* ESLint Plugin React Hooks
* Rules of React
* Legacy APIs

---

## Source: versions.md

React Versions – React

React

v19.2

Search`⌘``Ctrl``K`

Learn

Reference

Community

Blog

### GET STARTED

* Quick Start
* Installation
* Setup
* React Compiler

### LEARN REACT

* Describing the UI
* Adding Interactivity
* Managing State
* Escape Hatches

### REACT API

* Hooks
* Components
* APIs
* Legacy APIs

### REACT DOM API

* Components
* APIs
* Client APIs
* Server APIs

### REACT COMPILER API

* Configuration
* Directives
* Compiling Libraries

### GET INVOLVED

* React Community

### STAY INFORMED

* React Blog

Is this page useful?

React Docs

# React Versions

The React docs at react.dev provide documentation for the latest version of React.

We aim to keep the docs updated within major versions, and do not publish versions for each minor or patch version. When a new major is released, we archive the docs for the previous version as `x.react.dev`. See our versioning policy for more info.

You can find an archive of previous major versions below.

## Latest version: 19.2

* react.dev

## Previous versions

* 18.react.dev
* 17.react.dev
* 16.react.dev
* 15.react.dev

### Note

#### Legacy Docs

In 2023, we launched our new docs for React 18 as react.dev. The legacy React 18 docs are available at legacy.reactjs.org. Versions 17 and below are hosted on legacy sites.

For versions older than React 15, see 15.react.dev.

## Changelog

### React 19

**Blog Posts**

* React v19
* React 19 Upgrade Guide
* React Compiler Beta Release
* React Compiler v1.0
* React 19.2

**Talks**

* React 19 Keynote
* A Roadmap to React 19
* What’s new in React 19
* React for Two Computers
* React Compiler Deep Dive
* React Compiler Case Studies
* React 19 Deep Dive: Coordinating HTML

**Releases**

* v19.2.1 (December, 2025)
* v19.2.1 (December, 2025)
* v19.2.0 (October, 2025)
* v19.1.3 (December, 2025)
* v19.1.2 (December, 2025)
* v19.1.1 (July, 2025)
* v19.1.0 (March, 2025)
* v19.0.2 (December, 2025)
* v19.0.1 (December, 2025)
* v19.0.0 (December, 2024)

### React 18

**Blog Posts**

* React v18.0
* How to Upgrade to React 18
* The Plan for React 18

**Talks**

* React 18 Keynote
* React 18 for app developers
* Streaming Server Rendering with Suspense
* React without memo
* React Docs Keynote
* React Developer Tooling
* The first React Working Group
* React 18 for External Store Libraries

**Releases**

* v18.3.1 (April, 2024)
* v18.3.0 (April, 2024)
* v18.2.0 (June, 2022)
* v18.1.0 (April, 2022)
* v18.0.0 (March 2022)

### React 17

**Blog Posts**

* React v17.0
* Introducing the New JSX Transform
* React v17.0 Release Candidate: No New Features

**Releases**

* v17.0.2 (March 2021)
* v17.0.1 (October 2020)
* v17.0.0 (October 2020)

### React 16

**Blog Posts**

* React v16.0
* DOM Attributes in React 16
* Error Handling in React 16
* React v16.2.0: Improved Support for Fragments
* React v16.4.0: Pointer Events
* React v16.4.2: Server-side vulnerability fix
* React v16.6.0: lazy, memo and contextType
* React v16.7: No, This Is Not the One With Hooks
* React v16.8: The One With Hooks
* React v16.9.0 and the Roadmap Update
* React v16.13.0

**Releases**

* v16.14.0 (October 2020)
* v16.13.1 (March 2020)
* v16.13.0 (February 2020)
* v16.12.0 (November 2019)
* v16.11.0 (October 2019)
* v16.10.2 (October 2019)
* v16.10.1 (September 2019)
* v16.10.0 (September 2019)
* v16.9.0 (August 2019)
* v16.8.6 (March 2019)
* v16.8.5 (March 2019)
* v16.8.4 (March 2019)
* v16.8.3 (February 2019)
* v16.8.2 (February 2019)
* v16.8.1 (February 2019)
* v16.8.0 (February 2019)
* v16.7.0 (December 2018)
* v16.6.3 (November 2018)
* v16.6.2 (November 2018)
* v16.6.1 (November 2018)
* v16.6.0 (October 2018)
* v16.5.2 (September 2018)
* v16.5.1 (September 2018)
* v16.5.0 (September 2018)
* v16.4.2 (August 2018)
* v16.4.1 (June 2018)
* v16.4.0 (May 2018)
* v16.3.3 (August 2018)
* v16.3.2 (April 2018)
* v16.3.1 (April 2018)
* v16.3.0 (March 2018)
* v16.2.1 (August 2018)
* v16.2.0 (November 2017)
* v16.1.2 (August 2018)
* v16.1.1 (November 2017)
* v16.1.0 (November 2017)
* v16.0.1 (August 2018)
* v16.0 (September 2017)

### React 15

**Blog Posts**

* React v15.0
* React v15.0 Release Candidate 2
* React v15.0 Release Candidate
* New Versioning Scheme
* Discontinuing IE 8 Support in React DOM
* Introducing React’s Error Code System
* React v15.0.1
* React v15.4.0
* React v15.5.0
* React v15.6.0
* React v15.6.2

**Releases**

* v15.7.0 (October 2017)
* v15.6.2 (September 2017)
* v15.6.1 (June 2017)
* v15.6.0 (June 2017)
* v15.5.4 (April 2017)
* v15.5.3 (April 2017)
* v15.5.2 (April 2017)
* v15.5.1 (April 2017)
* v15.5.0 (April 2017)
* v15.4.2 (January 2016)
* v15.4.1 (November 2016)
* v15.4.0 (November 2016)
* v15.3.2 (September 2016)
* v15.3.1 (August 2016)
* v15.3.0 (July 2016)
* v15.2.1 (July 2016)
* v15.2.0 (July 2016)
* v15.1.0 (May 2016)
* v15.0.2 (April 2016)
* v15.0.1 (April 2016)
* v15.0.0 (April 2016)

### React 0.14

**Blog Posts**

* React v0.14
* React v0.14 Release Candidate
* React v0.14 Beta 1
* New React Developer Tools
* New React Devtools Beta
* React v0.14.1
* React v0.14.2
* React v0.14.3
* React v0.14.4
* React v0.14.8

**Releases**

* v0.14.10 (October 2020)
* v0.14.8 (March 2016)
* v0.14.7 (January 2016)
* v0.14.6 (January 2016)
* v0.14.5 (December 2015)
* v0.14.4 (December 2015)
* v0.14.3 (November 2015)
* v0.14.2 (November 2015)
* v0.14.1 (October 2015)
* v0.14.0 (October 2015)

### React 0.13

**Blog Posts**

* React Native v0.4
* React v0.13
* React v0.13 RC2
* React v0.13 RC
* React v0.13.0 Beta 1
* Streamlining React Elements
* Introducing Relay and GraphQL
* Introducing React Native
* React v0.13.1
* React v0.13.2
* React v0.13.3

**Releases**

* v0.13.3 (May 2015)
* v0.13.2 (April 2015)
* v0.13.1 (March 2015)
* v0.13.0 (March 2015)

### React 0.12

**Blog Posts**

* React v0.12
* React v0.12 RC
* Introducing React Elements
* React v0.12.2

**Releases**

* v0.12.2 (December 2014)
* v0.12.1 (November 2014)
* v0.12.0 (October 2014)

### React 0.11

**Blog Posts**

* React v0.11
* React v0.11 RC
* One Year of Open-Source React
* The Road to 1.0
* React v0.11.1
* React v0.11.2
* Introducing the JSX Specificaion

**Releases**

* v0.11.2 (September 2014)
* v0.11.1 (July 2014)
* v0.11.0 (July 2014)

### React 0.10 and below

**Blog Posts**

* React v0.10
* React v0.10 RC
* React v0.9
* React v0.9 RC
* React Chrome Developer Tools
* React v0.8
* React v0.5.2, v0.4.2
* React v0.5.1
* React v0.5
* React v0.4.1
* React v0.4.0
* New in React v0.4: Prop Validation and Default Values
* New in React v0.4: Autobind by Default
* React v0.3.3

**Releases**

* v0.10.0 (March 2014)
* v0.9.0 (February 2014)
* v0.8.0 (December 2013)
* v0.5.2 (December 2013)
* v0.5.1 (October 2013)
* v0.5.0 (October 2013)
* v0.4.1 (July 2013)
* v0.4.0 (July 2013)
* v0.3.3 (June 2013)
* v0.3.2 (May 2013)
* v0.3.1 (May 2013)
* v0.3.0 (May 2013)

### Initial Commit

React was open-sourced on May 29, 2013. The initial commit is: `75897c`: Initial public release

See the first blog post: Why did we build React?

React was open sourced at Facebook Seattle in 2013:

---

Copyright © Meta Platforms, Inc

no uwu plz

uwu?

Logo by@sawaratsuki1004

Learn React

Quick Start

Installation

Describing the UI

Adding Interactivity

Managing State

Escape Hatches

API Reference

React APIs

React DOM APIs

Community

Code of Conduct

Meet the Team

Docs Contributors

Acknowledgements

More

Blog

React Native

Privacy

Terms

## On this page

* Overview
* Latest version: 19.2
* Previous versions
* Changelog
* React 19
* React 18
* React 17
* React 16
* React 15
* React 0.14
* React 0.13
* React 0.12
* React 0.11
* React 0.10 and below
* Initial Commit

---