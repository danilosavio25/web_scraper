# Go Knowledge

> Category: languages

## Source: doc_tutorial_getting-started.md

Tutorial: Get started with Go - The Go Programming Language

Skip to Main Content

* Why Go *arrow\_drop\_down*

  Press Enter to activate/deactivate dropdown

  + Case Studies

    Common problems companies solve with Go
  + Use Cases

    Stories about how and why companies use Go
  + Security

    How Go can help keep you secure by default
* Learn

  Press Enter to activate/deactivate dropdown
* Docs *arrow\_drop\_down*

  Press Enter to activate/deactivate dropdown

  + Go Spec

    The official Go language specification
  + Go User Manual

    A complete introduction to building software with Go
  + Standard library

    Reference documentation for Go's standard library
  + Release Notes

    Learn what's new in each Go release
  + Effective Go

    Tips for writing clear, performant, and idiomatic Go code
* Packages

  Press Enter to activate/deactivate dropdown
* Community *arrow\_drop\_down*

  Press Enter to activate/deactivate dropdown

  + Recorded Talks

    Videos from prior events
  + Meetups
    *open\_in\_new*

    Meet other local Go developers
  + Conferences
    *open\_in\_new*

    Learn and network with Go developers from around the world
  + Go blog

    The Go project's official blog.
  + Go project

    Get help and stay informed from Go
  + Get connected

* Why Go *navigate\_next*

  *navigate\_before*Why Go

  + Case Studies
  + Use Cases
  + Security
* Learn
* Docs *navigate\_next*

  *navigate\_before*Docs

  + Go Spec
  + Go User Manual
  + Standard library
  + Release Notes
  + Effective Go
* Packages
* Community *navigate\_next*

  *navigate\_before*Community

  + Recorded Talks
  + Meetups
    *open\_in\_new*
  + Conferences
    *open\_in\_new*
  + Go blog
  + Go project
  + Get connected

1. Documentation
2. Tutorials
3. Tutorial: Get started with Go

# Tutorial: Get started with Go

In this tutorial, you'll get a brief introduction to Go programming. Along the
way, you will:

* Install Go (if you haven't already).
* Write some simple "Hello, world" code.
* Use the `go` command to run your code.
* Use the Go package discovery tool to find packages you can use in your own
  code.
* Call functions of an external module.

**Note:** For other tutorials, see
Tutorials.

## Prerequisites

* **Some programming experience.** The code here is pretty
  simple, but it helps to know something about functions.
* **A tool to edit your code.** Any text editor you have will
  work fine. Most text editors have good support for Go. The most popular are
  VSCode (free), GoLand (paid), and Vim (free).
* **A command terminal.** Go works well using any terminal on
  Linux and Mac, and on PowerShell or cmd in Windows.

## Install Go

Just use the Download and install steps.

## Write some code

Get started with Hello, World.

1. Open a command prompt and cd to your home directory.

   On Linux or Mac:

   ```
   cd
   ```

   On Windows:

   ```
   cd %HOMEPATH%
   ```
2. Create a hello directory for your first Go source code.

   For example, use the following commands:

   ```
   mkdir hello
   cd hello
   ```
3. Enable dependency tracking for your code.

   When your code imports packages contained in other modules, you manage
   those dependencies through your code's own module. That module is defined
   by a go.mod file that tracks the modules that provide those packages. That
   go.mod file stays with your code, including in your source code
   repository.

   To enable dependency tracking for your code by creating a go.mod file, run
   the
   `go mod init` command,
   giving it the name of the module your code will be in. The name is the
   module's module path.

   In actual development, the module path will typically be the repository
   location where your source code will be kept. For example, the module
   path might be `github.com/mymodule`. If you plan to publish
   your module for others to use, the module path *must* be a
   location from which Go tools can download your module. For more about
   naming a module with a module path, see
   Managing
   dependencies.

   For the purposes of this tutorial, just use
   `example/hello`.

   ```
   $ go mod init example/hello
   go: creating new go.mod: module example/hello
   ```
4. In your text editor, create a file hello.go in which to write your code.
5. Paste the following code into your hello.go file and save the file.

   ```
   package main

   import "fmt"

   func main() {
       fmt.Println("Hello, World!")
   }
   ```

   This is your Go code. In this code, you:

   * Declare a `main` package (a package is a way to group
     functions, and it's made up of all the files in the same directory).
   * Import the popular
     `fmt` package,
     which contains functions for formatting text, including printing to the
     console. This package is one of the
     standard library packages you got
     when you installed Go.
   * Implement a `main` function to print a message to the
     console. A `main` function executes by default when you run
     the `main` package.
6. Run your code to see the greeting.

   ```
   $ go run .
   Hello, World!
   ```

   The
   `go run` command
   is one of many `go` commands you'll use to get things done with
   Go. Use the following command to get a list of the others:

   ```
   $ go help
   ```

## Call code in an external package

When you need your code to do something that might have been implemented by
someone else, you can look for a package that has functions you can use in
your code.

1. Make your printed message a little more interesting with a function from an
   external module.
   1. Visit pkg.go.dev and
      search for a "quote" package.
   2. In the search results, locate and click on the v1 of the `rsc.io/quote` package
      (it should be listed with the "Other major versions" of `rsc.io/quote/v4`).
   3. In the **Documentation** section, under **Index**, note the
      list of functions you can call from your code. You'll use the
      `Go` function.
   4. At the top of this page, note that package `quote` is
      included in the `rsc.io/quote` module.

   You can use the pkg.go.dev site to find published modules whose packages
   have functions you can use in your own code. Packages are published in
   modules -- like `rsc.io/quote` -- where others can use them.
   Modules are improved with new versions over time, and you can upgrade your
   code to use the improved versions.
2. In your Go code, import the `rsc.io/quote` package and add a call
   to its `Go` function.

   After adding the highlighted lines, your code should include the
   following:

   ```
   package main

   import "fmt"

   import "rsc.io/quote"

   func main() {
       fmt.Println(quote.Go())
   }
   ```
3. Add new module requirements and sums.

   Go will add the `quote` module as a requirement, as well as a
   go.sum file for use in authenticating the module. For more, see
   Authenticating modules in the Go
   Modules Reference.

   ```
   $ go mod tidy
   go: finding module for package rsc.io/quote
   go: found rsc.io/quote in rsc.io/quote v1.5.2
   ```
4. Run your code to see the message generated by the function you're calling.

   ```
   $ go run .
   Don't communicate by sharing memory, share memory by communicating.
   ```

   Notice that your code calls the `Go` function, printing a
   clever message about communication.

   When you ran `go mod tidy`, it located and downloaded the
   `rsc.io/quote` module that contains the package you imported.
   By default, it downloaded the latest version -- v1.5.2.

## Write more code

With this quick introduction, you got Go installed and learned some of the
basics. To write some more code with another tutorial, take a look at
Create a Go module.

Why Go
Use Cases
Case Studies

Get Started
Playground
Tour
Stack Overflow
Help

Packages
Standard Library
About Go Packages

About
Download
Blog
Issue Tracker
Release Notes
Brand Guidelines
Code of Conduct

Connect
Twitter
GitHub
Slack
r/golang
Meetup
Golang Weekly

Opens in new window.

* Copyright
* Terms of Service
* Privacy Policy
* Report an Issue

go.dev uses cookies from Google to deliver and enhance the quality of its services and to
analyze traffic. Learn more.

Okay

---

## Source: index.md

The Go Programming Language

Skip to Main Content

* Why Go *arrow\_drop\_down*

  Press Enter to activate/deactivate dropdown

  + Case Studies

    Common problems companies solve with Go
  + Use Cases

    Stories about how and why companies use Go
  + Security

    How Go can help keep you secure by default
* Learn

  Press Enter to activate/deactivate dropdown
* Docs *arrow\_drop\_down*

  Press Enter to activate/deactivate dropdown

  + Go Spec

    The official Go language specification
  + Go User Manual

    A complete introduction to building software with Go
  + Standard library

    Reference documentation for Go's standard library
  + Release Notes

    Learn what's new in each Go release
  + Effective Go

    Tips for writing clear, performant, and idiomatic Go code
* Packages

  Press Enter to activate/deactivate dropdown
* Community *arrow\_drop\_down*

  Press Enter to activate/deactivate dropdown

  + Recorded Talks

    Videos from prior events
  + Meetups
    *open\_in\_new*

    Meet other local Go developers
  + Conferences
    *open\_in\_new*

    Learn and network with Go developers from around the world
  + Go blog

    The Go project's official blog.
  + Go project

    Get help and stay informed from Go
  + Get connected

* Why Go *navigate\_next*

  *navigate\_before*Why Go

  + Case Studies
  + Use Cases
  + Security
* Learn
* Docs *navigate\_next*

  *navigate\_before*Docs

  + Go Spec
  + Go User Manual
  + Standard library
  + Release Notes
  + Effective Go
* Packages
* Community *navigate\_next*

  *navigate\_before*Community

  + Recorded Talks
  + Meetups
    *open\_in\_new*
  + Conferences
    *open\_in\_new*
  + Go blog
  + Go project
  + Get connected

# Build simple, secure, scalable systems with Go

* An open-source programming language supported by Google
* Easy to learn and great for teams
* Built-in concurrency and a robust standard library
* Large ecosystem of partners, communities, and tools

Get Started
Download

Opens a new window with the Get Started guide.

Opens a new window to download Go.

Download packages for
Windows 64-bit,
macOS,
Linux, and
more

The `go` command by default downloads and authenticates
modules using the Go module mirror and Go checksum database run by
Google. Learn more.

Opens in new window.

## Companies using Go

Organizations in every industry use Go to power their software and services
View all stories

* “At the time, no single team member knew Go, but
  **within a month, everyone was writing in Go** and we were
  building out the endpoints. It was the flexibility, how easy it was to use,
  and the really cool concept behind Go (how Go handles native concurrency,
  garbage collection, and of course safety+speed.) that helped engage us
  during the build. Also, who can beat that cute mascot!”

  — Jaime Enrique Garcia Lopez,
  Senior Software Development Manager
   at Capital One
* "**A small language that compiles fast makes for a happy developer.**
  The Go language is small, compiles really fast, and as a result it lets your
  mind focus on the actual problem and less on the tool you are using to solve
  it. Code, test, debug cycles are so quick that you forget you are not
  working with an interpreted language. Looking at our code, you see
  **less boilerplate and more business logic.**"

  — Clayton Coleman,
  Lead Engineer, Open Shift
   at RedHat
* “**Go has excellent characteristics for scalability and services
  written using it typically have very small memory footprints.**
  Because code is compiled into a single static binary, services can also be
  containerised with ease, making it much simpler to build and deploy. These
  attributes make **Go an ideal choice for companies building
  microservices**, as you can easily deploy into a highly available and
  scalable environment such as Kubernetes.”

  — Matt Boyle,
  Lead Software Engineer
   at Curve
* "In our tightly managed environments where we run Go code,
  **we have seen a CPU reduction of approximately 10%**
  with cleaner and maintainable code."

  — Bala Natarajan,
  Sr. Director of Engineering, Developer Experience
   at PayPal
* "Tooling has always been a problem with our legacy code base... but we have
  found that Go has excellent tooling, plus built-in testing, benchmarking,
  and profiling frameworks. It is easy to write efficient and resilient
  applications. **After working on Go, most of our developers don't want
  to go back to other languages.**"

  — Benjamin Cane,
  Vice President and Principal Engineer
   at American Express
* "...when a programming language is designed for exactly the environment most
  of us use right now—scalable, cloud-based servers that are optimized for
  performance—a lot can go right."

  — John Biggs and Ben Popper,
   at Stack Overflow

*navigate\_before*

*navigate\_next*

## Try Go

Press Esc to move out of the editor.

// You can edit this code!
// Click here and start typing.
package main
import "fmt"
func main() {
fmt.Println("Hello, 世界")
}

Press Esc to move out of the editor.

```
Hello, 世界
```

Hello, World!
Conway's Game of Life
Fibonacci Closure
Peano Integers
Concurrent pi
Concurrent Prime Sieve
Peg Solitaire Solver
Tree Comparison

Run

Share
Tour

## What’s possible with Go

Use Go for a variety of software development purposes

  ### Cloud & Network Services

  With a strong ecosystem of tools and APIs on major cloud providers, it is easier than ever to build services with Go.

  Popular Packages:

  + cloud.google.com/go
  + aws/client
  + Azure/azure-sdk-for-go

  Learn More
  *arrow\_forward*

  ### Command-line Interfaces

  With popular open source packages and a robust standard library, use Go to create fast and elegant CLIs.

  Popular Packages:

  + spf13/cobra
  + spf13/viper
  + urfave/cli
  + delve
  + chzyer/readline

  Learn More
  *arrow\_forward*

  ### Web Development

  With enhanced memory performance and support for several IDEs, Go powers fast and scalable web applications.

  Popular Packages:

  + net/http
  + html/template
  + flosch/pongo2
  + database/sql
  + elastic/go-elasticsearch

  Learn More
  *arrow\_forward*

  ### DevOps & Site Reliability

  With fast build times, lean syntax, an automatic formatter and doc generator, Go is built to support both DevOps and SRE.

  Popular Packages:

  + open-telemetry/opentelemetry-go
  + istio/istio
  + urfave/cli

  Learn More
  *arrow\_forward*

  More use cases
  *arrow\_forward*

## Get started with Go

Explore a wealth of learning resources, including guided journeys, courses, books, and more.

Get Started
Download Go

* Resources to start on your own
* Guided learning journeys

  Step-by-step tutorials to get your feet wet
* Online learning

  Browse resources and learn at your own pace
* Featured books

  Read through structured chapters and theories
* Cloud Self-paced labs

  Jump in to deploying Go apps on GCP

* In-Person Trainings
* Ardan Labs

  Offering customized on-site live training classes.
* Gopher Guides

  Customized In-person, remote, and online training classes. Training for Developers by Developers.
* Boss Sauce Creative

  Personalized or track-based Go training for teams.
* Shiju Varghese

  On-site classroom training on Go and consulting on distributed systems architectures, in India.

Why Go
Use Cases
Case Studies

Get Started
Playground
Tour
Stack Overflow
Help

Packages
Standard Library
About Go Packages

About
Download
Blog
Issue Tracker
Release Notes
Brand Guidelines
Code of Conduct

Connect
Twitter
GitHub
Slack
r/golang
Meetup
Golang Weekly

Opens in new window.

* Copyright
* Terms of Service
* Privacy Policy
* Report an Issue

go.dev uses cookies from Google to deliver and enhance the quality of its services and to
analyze traffic. Learn more.

Okay

---

## Source: solutions_case-studies.md

Case Studies - The Go Programming Language

Skip to Main Content

* Why Go *arrow\_drop\_down*

  Press Enter to activate/deactivate dropdown

  + Case Studies

    Common problems companies solve with Go
  + Use Cases

    Stories about how and why companies use Go
  + Security

    How Go can help keep you secure by default
* Learn

  Press Enter to activate/deactivate dropdown
* Docs *arrow\_drop\_down*

  Press Enter to activate/deactivate dropdown

  + Go Spec

    The official Go language specification
  + Go User Manual

    A complete introduction to building software with Go
  + Standard library

    Reference documentation for Go's standard library
  + Release Notes

    Learn what's new in each Go release
  + Effective Go

    Tips for writing clear, performant, and idiomatic Go code
* Packages

  Press Enter to activate/deactivate dropdown
* Community *arrow\_drop\_down*

  Press Enter to activate/deactivate dropdown

  + Recorded Talks

    Videos from prior events
  + Meetups
    *open\_in\_new*

    Meet other local Go developers
  + Conferences
    *open\_in\_new*

    Learn and network with Go developers from around the world
  + Go blog

    The Go project's official blog.
  + Go project

    Get help and stay informed from Go
  + Get connected

* Why Go *navigate\_next*

  *navigate\_before*Why Go

  + Case Studies
  + Use Cases
  + Security
* Learn
* Docs *navigate\_next*

  *navigate\_before*Docs

  + Go Spec
  + Go User Manual
  + Standard library
  + Release Notes
  + Effective Go
* Packages
* Community *navigate\_next*

  *navigate\_before*Community

  + Recorded Talks
  + Meetups
    *open\_in\_new*
  + Conferences
    *open\_in\_new*
  + Go blog
  + Go project
  + Get connected

1. Why Go
2. Case Studies

  RECENTLY UPDATED

  ## Using Go at Google

  Go was created at Google in 2007, and since then, engineering teams across Google have adopted Go to build products and services at massive scale.
  Learn more
  *arrow\_forward*

  RECENTLY UPDATED

  ## PayPal Taps Go to Modernize and Scale

  Go’s value in producing clean, efficient code that readily scales as software deployment scales made the language a strong fit to support PayPal’s goals.
  Learn more
  *arrow\_forward*
* !American Express Uses Go for Payments & Rewards

  RECENTLY UPDATED

  ## American Express Uses Go for Payments & Rewards

  Go provides American Express with the speed and scalability it needs for both its payment and rewards networks.
  Learn more
  *arrow\_forward*

Opens in new window.

*navigate\_before*

*navigate\_next*

  ## Allegro – Writing a very fast cache service with millions of entries in Go

  “Finally, we sped up our application from more than 2.5 seconds to less than 250 milliseconds for the longest request.”

  View Case Study

  ## How Armut Labs use Go

  Learn about how Armut Labs reduced resource consumption and API response time after moving from C# and .net core to Go.

  View Case Study

  ## Bitly - Why We Write Everything in Go

  In 2014, we wrote a little open source project called NSQ (nsq.io) and put a promising new language called Go through its paces. We liked what we saw so much that we started writing everything new in Go, and soon thereafter we began porting all legacy services to Go as well.

  View Case Study

  ## Massive practice in Go at ByteDance

  Go was introduced to ByteDance in 2014, and since then engineering teams across ByteDance have adopted Go to build products and services on a massive scale. As we went deeper, relatively mature microservice best practices under Go were developed and summarized, which then were open-sourced and named CloudWeGo since 2021. Now 70% of microservices within ByteDance are written by Go.

  View Case Study

  ## Capital One - A Serverless and Go Journey

  At the time, no single team member knew Go, but within a month, everyone was writing in Go and we were building out the endpoints. It was the flexibility, how easy it was to use, and the really cool concept behind Go (how Go handles native concurrency, garbage collection, and of course safety+speed.) that helped engage us during the build. Also, who can beat that cute mascot!

  View Case Study

  ## Graceful upgrades in Go

  Cloudflare speeds up and protects millions of websites, APIs, SaaS services, and other properties connected to the Internet. “Go is at the heart of CloudFlare’s services including handling compression for high-latency HTTP connections, our entire DNS infrastructure, SSL, load testing and more.”

  View Case Study

  ## Cockroach Labs - Why We Chose to Build Our Database with Go

  Go's performance benefits, garbage collection, and low barrier to entry made it a great fit for CockroachDB.

  View Case Study

  ## How Curve is getting ahead with Golang

  Curve shares how Go's efficiency, standard library, and thriving community help them move banking to the cloud.

  View Case Study

  ## Dropbox - Open sourcing our Go libraries

  About a year ago, we decided to migrate our performance-critical backends from Python to Go to leverage better concurrency support and faster execution speed. ... At this point, we have successfully moved major parts of our infrastructure to Go.

  View Case Study

  ## How Facebook built an entity framework in Go

  Learn about a Facebook engineering team's decision to write a new entity framework (ORM) in Go.

  View Case Study

  ## Bigslice - A cluster computing system in Go

  At GRAIL, we use the Go programming language for most of our bioinformatics, data processing, and machine learning tasks. Go’s simplicity makes it easy for newcomers to learn; its transparent runtime semantics makes it easy to reason about performance; and its ability to control data layout and allocation makes it possible to write highly performant data processing code.

  View Case Study

  ## How Microsoft Embraces Go

  Learn about how Microsoft has helped support Go and how it uses Go to power pieces of its cloud infrastructure.

  View Case Study

  ## Monzo – Building a Bank with Golang, Microservices and Containers

  “Go is a perfect language for creating microservice architectures, and the concurrency features, and the language in general, has allowed the easy creation of small and simple networked services at Monzo that are focused around the ‘single responsibility principle’.”

  View Case Study

  ## Netflix - Application data caching using SSDs

  The decision to use Go was deliberate, because we needed something that had lower latency than Java (where garbage collection pauses are an issue) and is more productive for developers than C, while also handling tens of thousands of client connections. Go fits this space well.

  View Case Study

  ## Riot Games - Leveraging Golang for Game Development and Operations

  Learn how Riot uses Go to develop, deploy, and operate backend microservices at scale–globally. They share their experience across use cases, with specific examples, and speak to the value of the gopher community.

  View Case Study

  ## Salesforce - From Python/C to Go

  One of the big advantages is that Go's cross-platform features make porting code easy.

  View Case Study

  ## Find out more about Golang at SIXT

  “We have been doing Golang at SIXT since 2015. Back then there was not that many people here in our area which were doing Golang in production mode, mostly side projects. So it was really a bold move from our side but it proved to be quite successful. Fast forward to 2019 we have over 15 teams doing Golang. Many of the applications they have built are basically foundation for most of our mobility product offer including Rent, Ride and Share.”

  View Case Study

  ## Stream – Why We Switched from Python to Go

  Go’s combination of a great ecosystem, easy onboarding for new developers, fast performance, solid support for concurrency and a productive programming environment make it a great choice. It allowed a small development team at Stream to power feeds and chat for over 500 million end users.

  View Case Study

  ## Trivago – Why We Chose Go

  “Go’s simplicity and its sophisticated tooling let us scale not only our service but more importantly, the process of software engineering itself. Reducing the friction of onboarding and training someone has a significant impact on the company’s productivity, even more so in a constantly moving environment like trivago.”

  View Case Study

  ## Twitch - Go’s march to low latency GC

  We use Go at Twitch for many of our busiest systems. Its simplicity, safety, performance, and readability make it a good tool for the problems we encounter with serving live video and chat to our millions of users.

  View Case Study

  ## Uber - GPU-power analytics engine in Go

  AresDB [,written in Go,] is widely used at Uber to power our real-time data analytics dashboards, enabling us to make data-driven decisions at scale about myriad aspects of our business.

  View Case Study

  ## How Wildlife Studios builds backend systems in Go

  Wildlife is a Brazilian native global company focused on mobile gaming. We aim to develop games that will make billions of people happy. We have almost 40 million daily active users, and we rely on Go as the main language for our core platform, given its features to scale our backend services.

  View Case Study

  ## X - 5 billion sessions a day in realtime

  We now see about five billion sessions per day, and growing. Hundreds of millions of devices send millions of events every second to the Answers endpoint. During the time that it took you to read to here, the Answers back-end will have received and processed about 10,000,000 analytics events.

  View Case Study

Why Go
Use Cases
Case Studies

Get Started
Playground
Tour
Stack Overflow
Help

Packages
Standard Library
About Go Packages

About
Download
Blog
Issue Tracker
Release Notes
Brand Guidelines
Code of Conduct

Connect
Twitter
GitHub
Slack
r/golang
Meetup
Golang Weekly

Opens in new window.

* Copyright
* Terms of Service
* Privacy Policy
* Report an Issue

go.dev uses cookies from Google to deliver and enhance the quality of its services and to
analyze traffic. Learn more.

Okay

---

## Source: solutions_use-cases.md

Use Cases - The Go Programming Language

Skip to Main Content

* Why Go *arrow\_drop\_down*

  Press Enter to activate/deactivate dropdown

  + Case Studies

    Common problems companies solve with Go
  + Use Cases

    Stories about how and why companies use Go
  + Security

    How Go can help keep you secure by default
* Learn

  Press Enter to activate/deactivate dropdown
* Docs *arrow\_drop\_down*

  Press Enter to activate/deactivate dropdown

  + Go Spec

    The official Go language specification
  + Go User Manual

    A complete introduction to building software with Go
  + Standard library

    Reference documentation for Go's standard library
  + Release Notes

    Learn what's new in each Go release
  + Effective Go

    Tips for writing clear, performant, and idiomatic Go code
* Packages

  Press Enter to activate/deactivate dropdown
* Community *arrow\_drop\_down*

  Press Enter to activate/deactivate dropdown

  + Recorded Talks

    Videos from prior events
  + Meetups
    *open\_in\_new*

    Meet other local Go developers
  + Conferences
    *open\_in\_new*

    Learn and network with Go developers from around the world
  + Go blog

    The Go project's official blog.
  + Go project

    Get help and stay informed from Go
  + Get connected

* Why Go *navigate\_next*

  *navigate\_before*Why Go

  + Case Studies
  + Use Cases
  + Security
* Learn
* Docs *navigate\_next*

  *navigate\_before*Docs

  + Go Spec
  + Go User Manual
  + Standard library
  + Release Notes
  + Effective Go
* Packages
* Community *navigate\_next*

  *navigate\_before*Community

  + Recorded Talks
  + Meetups
    *open\_in\_new*
  + Conferences
    *open\_in\_new*
  + Go blog
  + Go project
  + Get connected

1. Why Go
2. Use Cases

# Use Cases

Opens in new window.

Why Go
Use Cases
Case Studies

Get Started
Playground
Tour
Stack Overflow
Help

Packages
Standard Library
About Go Packages

About
Download
Blog
Issue Tracker
Release Notes
Brand Guidelines
Code of Conduct

Connect
Twitter
GitHub
Slack
r/golang
Meetup
Golang Weekly

Opens in new window.

* Copyright
* Terms of Service
* Privacy Policy
* Report an Issue

go.dev uses cookies from Google to deliver and enhance the quality of its services and to
analyze traffic. Learn more.

Okay

---