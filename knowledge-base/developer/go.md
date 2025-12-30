# Go Knowledge

> Category: languages


## Source: doc_tutorial_getting-started.md

Tutorial: Get started with Go - The Go Programming Language





[![Go](/images/go-logo-white.svg)](/)

[Skip to Main Content](#main-content)

* [Why Go *arrow\_drop\_down*](#)

  Press Enter to activate/deactivate dropdown

  + [Case Studies](/solutions/case-studies)

    Common problems companies solve with Go
  + [Use Cases](/solutions/use-cases)

    Stories about how and why companies use Go
  + [Security](/security/)

    How Go can help keep you secure by default
* [Learn](/learn/)

  Press Enter to activate/deactivate dropdown
* [Docs *arrow\_drop\_down*](#)

  Press Enter to activate/deactivate dropdown

  + [Go Spec](/ref/spec)

    The official Go language specification
  + [Go User Manual](/doc)

    A complete introduction to building software with Go
  + [Standard library](https://pkg.go.dev/std)

    Reference documentation for Go's standard library
  + [Release Notes](/doc/devel/release)

    Learn what's new in each Go release
  + [Effective Go](/doc/effective_go)

    Tips for writing clear, performant, and idiomatic Go code
* [Packages](https://pkg.go.dev)

  Press Enter to activate/deactivate dropdown
* [Community *arrow\_drop\_down*](#)

  Press Enter to activate/deactivate dropdown

  + [Recorded Talks](/talks/)

    Videos from prior events
  + [Meetups
    *open\_in\_new*](https://www.meetup.com/pro/go)

    Meet other local Go developers
  + [Conferences
    *open\_in\_new*](/wiki/Conferences)

    Learn and network with Go developers from around the world
  + [Go blog](/blog)

    The Go project's official blog.
  + [Go project](/help)

    Get help and stay informed from Go
  + Get connected

    [![](/images/logos/social/google-groups.svg)](https://groups.google.com/g/golang-nuts)
    [![](/images/logos/social/github.svg)](https://github.com/golang)
    [![](/images/logos/social/twitter.svg)](https://twitter.com/golang)
    [![](/images/logos/social/reddit.svg)](https://www.reddit.com/r/golang/)
    [![](/images/logos/social/slack.svg)](https://invite.slack.golangbridge.org/)
    [![](/images/logos/social/stack-overflow.svg)](https://stackoverflow.com/tags/go)




[![Go.](/images/go-logo-blue.svg)](/)

* [Why Go *navigate\_next*](#)

  [*navigate\_before*Why Go](#)

  + [Case Studies](/solutions/case-studies)
  + [Use Cases](/solutions/use-cases)
  + [Security](/security/)
* [Learn](/learn/)
* [Docs *navigate\_next*](#)

  [*navigate\_before*Docs](#)

  + [Go Spec](/ref/spec)
  + [Go User Manual](/doc)
  + [Standard library](https://pkg.go.dev/std)
  + [Release Notes](/doc/devel/release)
  + [Effective Go](/doc/effective_go)
* [Packages](https://pkg.go.dev)
* [Community *navigate\_next*](#)

  [*navigate\_before*Community](#)

  + [Recorded Talks](/talks/)
  + [Meetups
    *open\_in\_new*](https://www.meetup.com/pro/go)
  + [Conferences
    *open\_in\_new*](/wiki/Conferences)
  + [Go blog](/blog)
  + [Go project](/help)
  + Get connected

    [![](/images/logos/social/google-groups.svg)](https://groups.google.com/g/golang-nuts)
    [![](/images/logos/social/github.svg)](https://github.com/golang)
    [![](/images/logos/social/twitter.svg)](https://twitter.com/golang)
    [![](/images/logos/social/reddit.svg)](https://www.reddit.com/r/golang/)
    [![](/images/logos/social/slack.svg)](https://invite.slack.golangbridge.org/)
    [![](/images/logos/social/stack-overflow.svg)](https://stackoverflow.com/tags/go)

1. [Documentation](/doc/)
2. [Tutorials](/doc/tutorial/)
3. [Tutorial: Get started with Go](/doc/tutorial/getting-started)

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
[Tutorials](/doc/tutorial/index.html).

## Prerequisites

* **Some programming experience.** The code here is pretty
  simple, but it helps to know something about functions.
* **A tool to edit your code.** Any text editor you have will
  work fine. Most text editors have good support for Go. The most popular are
  VSCode (free), GoLand (paid), and Vim (free).
* **A command terminal.** Go works well using any terminal on
  Linux and Mac, and on PowerShell or cmd in Windows.

## Install Go

Just use the [Download and install](/doc/install) steps.

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
   [`go mod init`](/ref/mod#go-mod-init) command,
   giving it the name of the module your code will be in. The name is the
   module's module path.

   In actual development, the module path will typically be the repository
   location where your source code will be kept. For example, the module
   path might be `github.com/mymodule`. If you plan to publish
   your module for others to use, the module path *must* be a
   location from which Go tools can download your module. For more about
   naming a module with a module path, see
   [Managing
   dependencies](/doc/modules/managing-dependencies#naming_module).

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
     [`fmt` package](https://pkg.go.dev/fmt/),
     which contains functions for formatting text, including printing to the
     console. This package is one of the
     [standard library](https://pkg.go.dev/std) packages you got
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
   [`go run`](/cmd/go/#hdr-Compile_and_run_Go_program) command
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
      [search for a "quote" package](https://pkg.go.dev/search?q=quote).
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
   [Authenticating modules](/ref/mod#authenticating) in the Go
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
[Create a Go module](/doc/tutorial/create-module.html).



[Why Go](/solutions/)
[Use Cases](/solutions/use-cases)
[Case Studies](/solutions/case-studies)

[Get Started](/learn/)
[Playground](/play)
[Tour](/tour/)
[Stack Overflow](https://stackoverflow.com/questions/tagged/go?tab=Newest)
[Help](/help/)

[Packages](https://pkg.go.dev)
[Standard Library](/pkg/)
[About Go Packages](https://pkg.go.dev/about)

[About](/project)
[Download](/dl/)
[Blog](/blog/)
[Issue Tracker](https://github.com/golang/go/issues)
[Release Notes](/doc/devel/release)
[Brand Guidelines](/brand)
[Code of Conduct](/conduct)

[Connect](https://www.twitter.com/golang)
[Twitter](https://www.twitter.com/golang)
[GitHub](https://github.com/golang)
[Slack](https://invite.slack.golangbridge.org/)
[r/golang](https://reddit.com/r/golang)
[Meetup](https://www.meetup.com/pro/go)
[Golang Weekly](https://golangweekly.com/)

Opens in new window.

![The Go Gopher](/images/gophers/pilot-bust.svg)

* [Copyright](/copyright)
* [Terms of Service](/tos)
* [Privacy Policy](http://www.google.com/intl/en/policies/privacy/)
* [Report an Issue](/s/website-issue)
* ![System theme](/images/icons/brightness_6_gm_grey_24dp.svg)
  ![Dark theme](/images/icons/brightness_2_gm_grey_24dp.svg)
  ![Light theme](/images/icons/light_mode_gm_grey_24dp.svg)

[![Google logo](/images/google-white.png)](https://google.com)

go.dev uses cookies from Google to deliver and enhance the quality of its services and to
analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay

---

## Source: index.md

The Go Programming Language





[![Go](/images/go-logo-white.svg)](/)

[Skip to Main Content](#main-content)

* [Why Go *arrow\_drop\_down*](#)

  Press Enter to activate/deactivate dropdown

  + [Case Studies](/solutions/case-studies)

    Common problems companies solve with Go
  + [Use Cases](/solutions/use-cases)

    Stories about how and why companies use Go
  + [Security](/security/)

    How Go can help keep you secure by default
* [Learn](/learn/)

  Press Enter to activate/deactivate dropdown
* [Docs *arrow\_drop\_down*](#)

  Press Enter to activate/deactivate dropdown

  + [Go Spec](/ref/spec)

    The official Go language specification
  + [Go User Manual](/doc)

    A complete introduction to building software with Go
  + [Standard library](https://pkg.go.dev/std)

    Reference documentation for Go's standard library
  + [Release Notes](/doc/devel/release)

    Learn what's new in each Go release
  + [Effective Go](/doc/effective_go)

    Tips for writing clear, performant, and idiomatic Go code
* [Packages](https://pkg.go.dev)

  Press Enter to activate/deactivate dropdown
* [Community *arrow\_drop\_down*](#)

  Press Enter to activate/deactivate dropdown

  + [Recorded Talks](/talks/)

    Videos from prior events
  + [Meetups
    *open\_in\_new*](https://www.meetup.com/pro/go)

    Meet other local Go developers
  + [Conferences
    *open\_in\_new*](/wiki/Conferences)

    Learn and network with Go developers from around the world
  + [Go blog](/blog)

    The Go project's official blog.
  + [Go project](/help)

    Get help and stay informed from Go
  + Get connected

    [![](/images/logos/social/google-groups.svg)](https://groups.google.com/g/golang-nuts)
    [![](/images/logos/social/github.svg)](https://github.com/golang)
    [![](/images/logos/social/twitter.svg)](https://twitter.com/golang)
    [![](/images/logos/social/reddit.svg)](https://www.reddit.com/r/golang/)
    [![](/images/logos/social/slack.svg)](https://invite.slack.golangbridge.org/)
    [![](/images/logos/social/stack-overflow.svg)](https://stackoverflow.com/tags/go)




[![Go.](/images/go-logo-blue.svg)](/)

* [Why Go *navigate\_next*](#)

  [*navigate\_before*Why Go](#)

  + [Case Studies](/solutions/case-studies)
  + [Use Cases](/solutions/use-cases)
  + [Security](/security/)
* [Learn](/learn/)
* [Docs *navigate\_next*](#)

  [*navigate\_before*Docs](#)

  + [Go Spec](/ref/spec)
  + [Go User Manual](/doc)
  + [Standard library](https://pkg.go.dev/std)
  + [Release Notes](/doc/devel/release)
  + [Effective Go](/doc/effective_go)
* [Packages](https://pkg.go.dev)
* [Community *navigate\_next*](#)

  [*navigate\_before*Community](#)

  + [Recorded Talks](/talks/)
  + [Meetups
    *open\_in\_new*](https://www.meetup.com/pro/go)
  + [Conferences
    *open\_in\_new*](/wiki/Conferences)
  + [Go blog](/blog)
  + [Go project](/help)
  + Get connected

    [![](/images/logos/social/google-groups.svg)](https://groups.google.com/g/golang-nuts)
    [![](/images/logos/social/github.svg)](https://github.com/golang)
    [![](/images/logos/social/twitter.svg)](https://twitter.com/golang)
    [![](/images/logos/social/reddit.svg)](https://www.reddit.com/r/golang/)
    [![](/images/logos/social/slack.svg)](https://invite.slack.golangbridge.org/)
    [![](/images/logos/social/stack-overflow.svg)](https://stackoverflow.com/tags/go)

# Build simple, secure, scalable systems with Go

* An open-source programming language supported by Google
* Easy to learn and great for teams
* Built-in concurrency and a robust standard library
* Large ecosystem of partners, communities, and tools

[Get Started](/learn/)
[Download](/dl)

Opens a new window with the Get Started guide.

Opens a new window to download Go.

Download packages for
Windows 64-bit,
macOS,
Linux, and
[more](/dl/)

The `go` command by default downloads and authenticates
modules using the Go module mirror and Go checksum database run by
Google. [Learn more.](/dl)

Opens in new window.

![Go Gopher climbing a ladder.](/images/gophers/ladder.svg)

## Companies using Go

Organizations in every industry use Go to power their software and services
[View all stories](/solutions/)

* [![](/images/logos/google.svg)

  View case study](/solutions/google/)
* [![](/images/logos/paypal.svg)

  View case study](/solutions/paypal)
* [![](/images/logos/american-express.svg)

  View case study](/solutions/americanexpress)
* [![](/images/logos/mercadolibre_light.svg)

  View case study](/solutions/mercadolibre)
* [![](/images/logos/bitly.svg)](https://bitly.com/blog/why-we-write-everything-in-go/?utm_source=go-dev&utm_medium=referral&utm_campaign=go-dev&utm_content=case-study)
* [![](/images/logos/capitalone_light.svg)](https://medium.com/capital-one-tech/a-serverless-and-go-journey-credit-offers-api-74ef1f9fde7f)
* [![](/images/logos/cockroach.svg)](https://www.cockroachlabs.com/blog/why-go-was-the-right-choice-for-cockroachdb/)
* [![](/images/logos/dropbox.png)](https://dropbox.tech/infrastructure/open-sourcing-our-go-libraries)
* [![](/images/logos/cloudflare_light.svg)](https://blog.cloudflare.com/graceful-upgrades-in-go/)
* [![](/images/logos/meta_light.svg)](https://entgo.io/blog/2019/10/03/introducing-ent/)
* [![](/images/logos/microsoft_light.svg)](https://cloudblogs.microsoft.com/opensource/2018/02/21/go-lang-brian-ketelsen-explains-fast-growth/)
* [![](/images/logos/wildlife_light.svg)](https://medium.com/tech-at-wildlife-studios/pitaya-wildlifes-golang-go-af57865f7a11)
* [![](/images/logos/bytedance_light.svg)](https://www.cloudwego.io/)
* [![](/images/logos/netflix.svg)](https://medium.com/netflix-techblog/application-data-caching-using-ssds-5bf25df851ef)
* [![](/images/logos/riot_light.svg)](https://technology.riotgames.com/news/leveraging-golang-game-development-and-operations)
* [![](/images/logos/salesforce.svg)](https://www.zdnet.com/article/salesforce-why-we-ditched-python-for-googles-go-language-in-einstein-analytics/)
* [![](/images/logos/twitch.svg)](https://blog.twitch.tv/en/2016/07/05/gos-march-to-low-latency-gc-a6fa96f06eb7/)
* [![](/images/logos/uber_light.svg)](https://eng.uber.com/aresdb/)
* [![](/images/logos/x.png)](https://blog.x.com/engineering/en_us/a/2015/handling-five-billion-sessions-a-day-in-real-time.html)

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
[Tour](/tour/ "Tour Go from your browser")

## What’s possible with Go

Use Go for a variety of software development purposes

* ![Sphere](/images/icons/sphere-dark.svg)
  ![Sphere](/images/icons/sphere.svg)

  ### Cloud & Network Services

  With a strong ecosystem of tools and APIs on major cloud providers, it is easier than ever to build services with Go.

  ![Packages.](/images/icons/package.svg)
  Popular Packages:

  + [cloud.google.com/go](https://cloud.google.com/go/home)
  + [aws/client](https://aws.amazon.com/sdk-for-go/)
  + [Azure/azure-sdk-for-go](https://github.com/Azure/azure-sdk-for-go)

  [Learn More
  *arrow\_forward*](/solutions/cloud/)
* ![Command Line](/images/icons/command-folder-dark.svg)
  ![Command Line](/images/icons/command-folder.svg)

  ### Command-line Interfaces

  With popular open source packages and a robust standard library, use Go to create fast and elegant CLIs.

  ![Packages.](/images/icons/package.svg)
  Popular Packages:

  + [spf13/cobra](https://github.com/spf13/cobra)
  + [spf13/viper](https://github.com/spf13/viper)
  + [urfave/cli](https://github.com/urfave/cli)
  + [delve](https://github.com/go-delve/delve)
  + [chzyer/readline](https://github.com/chzyer/readline)

  [Learn More
  *arrow\_forward*](/solutions/clis/)
* ![Code](/images/icons/code-dark.svg)
  ![Code](/images/icons/code.svg)

  ### Web Development

  With enhanced memory performance and support for several IDEs, Go powers fast and scalable web applications.

  ![Packages.](/images/icons/package.svg)
  Popular Packages:

  + [net/http](/pkg/net/http/)
  + [html/template](/pkg/html/template/)
  + [flosch/pongo2](https://github.com/flosch/pongo2)
  + [database/sql](/pkg/database/sql/)
  + [elastic/go-elasticsearch](https://github.com/elastic/go-elasticsearch)

  [Learn More
  *arrow\_forward*](/solutions/webdev/)
* ![Sphere](/images/icons/gear-dark.svg)
  ![Sphere](/images/icons/gear.svg)

  ### DevOps & Site Reliability

  With fast build times, lean syntax, an automatic formatter and doc generator, Go is built to support both DevOps and SRE.

  ![Packages.](/images/icons/package.svg)
  Popular Packages:

  + [open-telemetry/opentelemetry-go](https://github.com/open-telemetry/opentelemetry-go)
  + [istio/istio](https://github.com/istio/istio)
  + [urfave/cli](https://github.com/urfave/cli)

  [Learn More
  *arrow\_forward*](/solutions/devops/)
* ![Go Gopher is skateboarding.](/images/gophers/biplane.svg)

  [More use cases
  *arrow\_forward*](/solutions/use-cases)

## Get started with Go

Explore a wealth of learning resources, including guided journeys, courses, books, and more.

[Get Started](/learn/)
[Download Go](/doc/install/)

* Resources to start on your own
* [Guided learning journeys](/learn#guided-learning-journeys)

  Step-by-step tutorials to get your feet wet
* [Online learning](/learn#online-learning)

  Browse resources and learn at your own pace
* [Featured books](/learn#featured-books)

  Read through structured chapters and theories
* [Cloud Self-paced labs](/learn#self-paced-labs)

  Jump in to deploying Go apps on GCP

* In-Person Trainings
* [Ardan Labs](https://www.ardanlabs.com/)

  Offering customized on-site live training classes.
* [Gopher Guides](https://www.gopherguides.com/)

  Customized In-person, remote, and online training classes. Training for Developers by Developers.
* [Boss Sauce Creative](https://bosssauce.it/services/training)

  Personalized or track-based Go training for teams.
* [Shiju Varghese](https://github.com/shijuvar/gokit/tree/master/training)

  On-site classroom training on Go and consulting on distributed systems architectures, in India.



[Why Go](/solutions/)
[Use Cases](/solutions/use-cases)
[Case Studies](/solutions/case-studies)

[Get Started](/learn/)
[Playground](/play)
[Tour](/tour/)
[Stack Overflow](https://stackoverflow.com/questions/tagged/go?tab=Newest)
[Help](/help/)

[Packages](https://pkg.go.dev)
[Standard Library](/pkg/)
[About Go Packages](https://pkg.go.dev/about)

[About](/project)
[Download](/dl/)
[Blog](/blog/)
[Issue Tracker](https://github.com/golang/go/issues)
[Release Notes](/doc/devel/release)
[Brand Guidelines](/brand)
[Code of Conduct](/conduct)

[Connect](https://www.twitter.com/golang)
[Twitter](https://www.twitter.com/golang)
[GitHub](https://github.com/golang)
[Slack](https://invite.slack.golangbridge.org/)
[r/golang](https://reddit.com/r/golang)
[Meetup](https://www.meetup.com/pro/go)
[Golang Weekly](https://golangweekly.com/)

Opens in new window.

![The Go Gopher](/images/gophers/pilot-bust.svg)

* [Copyright](/copyright)
* [Terms of Service](/tos)
* [Privacy Policy](http://www.google.com/intl/en/policies/privacy/)
* [Report an Issue](/s/website-issue)
* ![System theme](/images/icons/brightness_6_gm_grey_24dp.svg)
  ![Dark theme](/images/icons/brightness_2_gm_grey_24dp.svg)
  ![Light theme](/images/icons/light_mode_gm_grey_24dp.svg)

[![Google logo](/images/google-white.png)](https://google.com)

go.dev uses cookies from Google to deliver and enhance the quality of its services and to
analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay

---

## Source: solutions_case-studies.md

Case Studies - The Go Programming Language





[![Go](/images/go-logo-white.svg)](/)

[Skip to Main Content](#main-content)

* [Why Go *arrow\_drop\_down*](#)

  Press Enter to activate/deactivate dropdown

  + [Case Studies](/solutions/case-studies)

    Common problems companies solve with Go
  + [Use Cases](/solutions/use-cases)

    Stories about how and why companies use Go
  + [Security](/security/)

    How Go can help keep you secure by default
* [Learn](/learn/)

  Press Enter to activate/deactivate dropdown
* [Docs *arrow\_drop\_down*](#)

  Press Enter to activate/deactivate dropdown

  + [Go Spec](/ref/spec)

    The official Go language specification
  + [Go User Manual](/doc)

    A complete introduction to building software with Go
  + [Standard library](https://pkg.go.dev/std)

    Reference documentation for Go's standard library
  + [Release Notes](/doc/devel/release)

    Learn what's new in each Go release
  + [Effective Go](/doc/effective_go)

    Tips for writing clear, performant, and idiomatic Go code
* [Packages](https://pkg.go.dev)

  Press Enter to activate/deactivate dropdown
* [Community *arrow\_drop\_down*](#)

  Press Enter to activate/deactivate dropdown

  + [Recorded Talks](/talks/)

    Videos from prior events
  + [Meetups
    *open\_in\_new*](https://www.meetup.com/pro/go)

    Meet other local Go developers
  + [Conferences
    *open\_in\_new*](/wiki/Conferences)

    Learn and network with Go developers from around the world
  + [Go blog](/blog)

    The Go project's official blog.
  + [Go project](/help)

    Get help and stay informed from Go
  + Get connected

    [![](/images/logos/social/google-groups.svg)](https://groups.google.com/g/golang-nuts)
    [![](/images/logos/social/github.svg)](https://github.com/golang)
    [![](/images/logos/social/twitter.svg)](https://twitter.com/golang)
    [![](/images/logos/social/reddit.svg)](https://www.reddit.com/r/golang/)
    [![](/images/logos/social/slack.svg)](https://invite.slack.golangbridge.org/)
    [![](/images/logos/social/stack-overflow.svg)](https://stackoverflow.com/tags/go)




[![Go.](/images/go-logo-blue.svg)](/)

* [Why Go *navigate\_next*](#)

  [*navigate\_before*Why Go](#)

  + [Case Studies](/solutions/case-studies)
  + [Use Cases](/solutions/use-cases)
  + [Security](/security/)
* [Learn](/learn/)
* [Docs *navigate\_next*](#)

  [*navigate\_before*Docs](#)

  + [Go Spec](/ref/spec)
  + [Go User Manual](/doc)
  + [Standard library](https://pkg.go.dev/std)
  + [Release Notes](/doc/devel/release)
  + [Effective Go](/doc/effective_go)
* [Packages](https://pkg.go.dev)
* [Community *navigate\_next*](#)

  [*navigate\_before*Community](#)

  + [Recorded Talks](/talks/)
  + [Meetups
    *open\_in\_new*](https://www.meetup.com/pro/go)
  + [Conferences
    *open\_in\_new*](/wiki/Conferences)
  + [Go blog](/blog)
  + [Go project](/help)
  + Get connected

    [![](/images/logos/social/google-groups.svg)](https://groups.google.com/g/golang-nuts)
    [![](/images/logos/social/github.svg)](https://github.com/golang)
    [![](/images/logos/social/twitter.svg)](https://twitter.com/golang)
    [![](/images/logos/social/reddit.svg)](https://www.reddit.com/r/golang/)
    [![](/images/logos/social/slack.svg)](https://invite.slack.golangbridge.org/)
    [![](/images/logos/social/stack-overflow.svg)](https://stackoverflow.com/tags/go)

1. [Why Go](/solutions/)
2. [Case Studies](/solutions/case-studies)

* ![Using Go at Google](/images/go_google_case_study_carousel.png)

  RECENTLY UPDATED

  ## Using Go at Google

  Go was created at Google in 2007, and since then, engineering teams across Google have adopted Go to build products and services at massive scale.
  [Learn more
  *arrow\_forward*](/solutions/google/)
* ![PayPal Taps Go to Modernize and Scale](/images/go_paypal_case_study.png)

  RECENTLY UPDATED

  ## PayPal Taps Go to Modernize and Scale

  Go’s value in producing clean, efficient code that readily scales as software deployment scales made the language a strong fit to support PayPal’s goals.
  [Learn more
  *arrow\_forward*](/solutions/paypal)
* ![American Express Uses Go for Payments & Rewards](/images/go_amex_case_study.png)

  RECENTLY UPDATED

  ## American Express Uses Go for Payments & Rewards

  Go provides American Express with the speed and scalability it needs for both its payment and rewards networks.
  [Learn more
  *arrow\_forward*](/solutions/americanexpress)

Opens in new window.

*navigate\_before*

*navigate\_next*

* [![Allegro](/images/logos/allegro_dark.svg)
  ![Allegro](/images/logos/allegro_light.svg)

  ## Allegro – Writing a very fast cache service with millions of entries in Go

  “Finally, we sped up our application from more than 2.5 seconds to less than 250 milliseconds for the longest request.”

  View Case Study](https://blog.allegro.tech/2016/03/writing-fast-cache-service-in-go.html)
* [![American Express](/images/logos/american-express.svg)
  ![American Express](/images/logos/american-express.svg)

  ## American Express Uses Go for Payments & Rewards

  Go provides American Express with the speed and scalability it needs for both its payment and rewards networks.

  View Case Study](/solutions/americanexpress)
* [![Armut](/images/logos/armut_dark.png)
  ![Armut](/images/logos/armut_light.png)

  ## How Armut Labs use Go

  Learn about how Armut Labs reduced resource consumption and API response time after moving from C# and .net core to Go.

  View Case Study](https://labs.armut.com/how-we-decreased-one-of-our-apis-response-time-by-87-and-used-less-resources-ce847e83308)
* [![Bitly](/images/logos/bitly.svg)
  ![Bitly](/images/logos/bitly.svg)

  ## Bitly - Why We Write Everything in Go

  In 2014, we wrote a little open source project called NSQ (nsq.io) and put a promising new language called Go through its paces. We liked what we saw so much that we started writing everything new in Go, and soon thereafter we began porting all legacy services to Go as well.

  View Case Study](https://bitly.com/blog/why-we-write-everything-in-go/?utm_source=go-dev&utm_medium=referral&utm_campaign=go-dev&utm_content=case-study)
* [![ByteDance](/images/logos/bytedance_dark.svg)
  ![ByteDance](/images/logos/bytedance_light.svg)

  ## Massive practice in Go at ByteDance

  Go was introduced to ByteDance in 2014, and since then engineering teams across ByteDance have adopted Go to build products and services on a massive scale. As we went deeper, relatively mature microservice best practices under Go were developed and summarized, which then were open-sourced and named CloudWeGo since 2021. Now 70% of microservices within ByteDance are written by Go.

  View Case Study](https://www.cloudwego.io/)
* [![Capital One](/images/logos/capitalone_dark.svg)
  ![Capital One](/images/logos/capitalone_light.svg)

  ## Capital One - A Serverless and Go Journey

  At the time, no single team member knew Go, but within a month, everyone was writing in Go and we were building out the endpoints. It was the flexibility, how easy it was to use, and the really cool concept behind Go (how Go handles native concurrency, garbage collection, and of course safety+speed.) that helped engage us during the build. Also, who can beat that cute mascot!

  View Case Study](https://medium.com/capital-one-tech/a-serverless-and-go-journey-credit-offers-api-74ef1f9fde7f)
* [![Cloudflare](/images/logos/cloudflare_dark.svg)
  ![Cloudflare](/images/logos/cloudflare_light.svg)

  ## Graceful upgrades in Go

  Cloudflare speeds up and protects millions of websites, APIs, SaaS services, and other properties connected to the Internet. “Go is at the heart of CloudFlare’s services including handling compression for high-latency HTTP connections, our entire DNS infrastructure, SSL, load testing and more.”

  View Case Study](https://blog.cloudflare.com/graceful-upgrades-in-go/)
* [![Cockroach Labs](/images/logos/cockroach.svg)
  ![Cockroach Labs](/images/logos/cockroach.svg)

  ## Cockroach Labs - Why We Chose to Build Our Database with Go

  Go's performance benefits, garbage collection, and low barrier to entry made it a great fit for CockroachDB.

  View Case Study](https://www.cockroachlabs.com/blog/why-go-was-the-right-choice-for-cockroachdb/)
* [![Curve](/images/logos/curve.png)
  ![Curve](/images/logos/curve.png)

  ## How Curve is getting ahead with Golang

  Curve shares how Go's efficiency, standard library, and thriving community help them move banking to the cloud.

  View Case Study](https://jaxenter.com/golang-curve-163187.html)
* [![Dropbox](/images/logos/dropbox.png)
  ![Dropbox](/images/logos/dropbox.png)

  ## Dropbox - Open sourcing our Go libraries

  About a year ago, we decided to migrate our performance-critical backends from Python to Go to leverage better concurrency support and faster execution speed. ... At this point, we have successfully moved major parts of our infrastructure to Go.

  View Case Study](https://dropbox.tech/infrastructure/open-sourcing-our-go-libraries)
* [![Facebook](/images/logos/meta_dark.svg)
  ![Facebook](/images/logos/meta_light.svg)

  ## How Facebook built an entity framework in Go

  Learn about a Facebook engineering team's decision to write a new entity framework (ORM) in Go.

  View Case Study](https://entgo.io/blog/2019/10/03/introducing-ent/)
* [![Google](/images/logos/google.svg)
  ![Google](/images/logos/google.svg)

  ## Using Go at Google

  Go was created at Google in 2007, and since then, engineering teams across Google have adopted Go to build products and services at massive scale.

  View Case Study](/solutions/google/)
* [![GRAIL](/images/logos/grail_dark.png)
  ![GRAIL](/images/logos/grail_light.png)

  ## Bigslice - A cluster computing system in Go

  At GRAIL, we use the Go programming language for most of our bioinformatics, data processing, and machine learning tasks. Go’s simplicity makes it easy for newcomers to learn; its transparent runtime semantics makes it easy to reason about performance; and its ability to control data layout and allocation makes it possible to write highly performant data processing code.

  View Case Study](https://medium.com/grail-eng/bigslice-a-cluster-computing-system-for-go-7e03acd2419b)
* [![MercadoLibre](/images/logos/mercadolibre_dark.svg)
  ![MercadoLibre](/images/logos/mercadolibre_light.svg)

  ## MercadoLibre Grows with Go

  Go provides clean, efficient code that readily scales as MercadoLibre’s online commerce grows, and increases developer productivity by allowing their engineers to serve their ever-increasing audience while writing less code.

  View Case Study](/solutions/mercadolibre)
* [![Microsoft](/images/logos/microsoft_dark.svg)
  ![Microsoft](/images/logos/microsoft_light.svg)

  ## How Microsoft Embraces Go

  Learn about how Microsoft has helped support Go and how it uses Go to power pieces of its cloud infrastructure.

  View Case Study](https://cloudblogs.microsoft.com/opensource/2018/02/21/go-lang-brian-ketelsen-explains-fast-growth/)
* [![Monzo](/images/logos/monzo_dark.svg)
  ![Monzo](/images/logos/monzo_light.svg)

  ## Monzo – Building a Bank with Golang, Microservices and Containers

  “Go is a perfect language for creating microservice architectures, and the concurrency features, and the language in general, has allowed the easy creation of small and simple networked services at Monzo that are focused around the ‘single responsibility principle’.”

  View Case Study](https://www.infoq.com/news/2017/03/monzo-bank-golang/)
* [![Netflix](/images/logos/netflix.svg)
  ![Netflix](/images/logos/netflix.svg)

  ## Netflix - Application data caching using SSDs

  The decision to use Go was deliberate, because we needed something that had lower latency than Java (where garbage collection pauses are an issue) and is more productive for developers than C, while also handling tens of thousands of client connections. Go fits this space well.

  View Case Study](https://medium.com/netflix-techblog/application-data-caching-using-ssds-5bf25df851ef)
* [![PayPal](/images/logos/paypal.svg)
  ![PayPal](/images/logos/paypal.svg)

  ## PayPal Taps Go to Modernize and Scale

  Go’s value in producing clean, efficient code that readily scales as software deployment scales made the language a strong fit to support PayPal’s goals.

  View Case Study](/solutions/paypal)
* [![Riot Games](/images/logos/riot_dark.svg)
  ![Riot Games](/images/logos/riot_light.svg)

  ## Riot Games - Leveraging Golang for Game Development and Operations

  Learn how Riot uses Go to develop, deploy, and operate backend microservices at scale–globally. They share their experience across use cases, with specific examples, and speak to the value of the gopher community.

  View Case Study](https://technology.riotgames.com/news/leveraging-golang-game-development-and-operations)
* [![Salesforce](/images/logos/salesforce.svg)
  ![Salesforce](/images/logos/salesforce.svg)

  ## Salesforce - From Python/C to Go

  One of the big advantages is that Go's cross-platform features make porting code easy.

  View Case Study](https://www.zdnet.com/article/salesforce-why-we-ditched-python-for-googles-go-language-in-einstein-analytics/)
* [![SIXT](/images/logos/sixt_dark.svg)
  ![SIXT](/images/logos/sixt_light.svg)

  ## Find out more about Golang at SIXT

  “We have been doing Golang at SIXT since 2015. Back then there was not that many people here in our area which were doing Golang in production mode, mostly side projects. So it was really a bold move from our side but it proved to be quite successful. Fast forward to 2019 we have over 15 teams doing Golang. Many of the applications they have built are basically foundation for most of our mobility product offer including Rent, Ride and Share.”

  View Case Study](https://www.facebook.com/sixtkarriere/posts/find-out-more-about-golang-at-sixt-to-become-a-godeveloper-mfd-at-sixt-click-her/2049632898495842/)
* [![Stream](/images/logos/getstream_dark.svg)
  ![Stream](/images/logos/getstream_light.svg)

  ## Stream – Why We Switched from Python to Go

  Go’s combination of a great ecosystem, easy onboarding for new developers, fast performance, solid support for concurrency and a productive programming environment make it a great choice. It allowed a small development team at Stream to power feeds and chat for over 500 million end users.

  View Case Study](https://getstream.io/blog/switched-python-go/)
* [![Trivago](/images/logos/trivago_dark.svg)
  ![Trivago](/images/logos/trivago_light.svg)

  ## Trivago – Why We Chose Go

  “Go’s simplicity and its sophisticated tooling let us scale not only our service but more importantly, the process of software engineering itself. Reducing the friction of onboarding and training someone has a significant impact on the company’s productivity, even more so in a constantly moving environment like trivago.”

  View Case Study](https://tech.trivago.com/2020/03/02/why-we-chose-go/)
* [![Twitch](/images/logos/twitch.svg)
  ![Twitch](/images/logos/twitch.svg)

  ## Twitch - Go’s march to low latency GC

  We use Go at Twitch for many of our busiest systems. Its simplicity, safety, performance, and readability make it a good tool for the problems we encounter with serving live video and chat to our millions of users.

  View Case Study](https://blog.twitch.tv/en/2016/07/05/gos-march-to-low-latency-gc-a6fa96f06eb7/)
* [![Uber](/images/logos/uber_dark.svg)
  ![Uber](/images/logos/uber_light.svg)

  ## Uber - GPU-power analytics engine in Go

  AresDB [,written in Go,] is widely used at Uber to power our real-time data analytics dashboards, enabling us to make data-driven decisions at scale about myriad aspects of our business.

  View Case Study](https://eng.uber.com/aresdb/)
* [![Wildlife Studios](/images/logos/wildlife_dark.svg)
  ![Wildlife Studios](/images/logos/wildlife_light.svg)

  ## How Wildlife Studios builds backend systems in Go

  Wildlife is a Brazilian native global company focused on mobile gaming. We aim to develop games that will make billions of people happy. We have almost 40 million daily active users, and we rely on Go as the main language for our core platform, given its features to scale our backend services.

  View Case Study](https://medium.com/tech-at-wildlife-studios/pitaya-wildlifes-golang-go-af57865f7a11)
* [![X](/images/logos/x.png)
  ![X](/images/logos/x.png)

  ## X - 5 billion sessions a day in realtime

  We now see about five billion sessions per day, and growing. Hundreds of millions of devices send millions of events every second to the Answers endpoint. During the time that it took you to read to here, the Answers back-end will have received and processed about 10,000,000 analytics events.

  View Case Study](https://blog.x.com/engineering/en_us/a/2015/handling-five-billion-sessions-a-day-in-real-time.html)



[Why Go](/solutions/)
[Use Cases](/solutions/use-cases)
[Case Studies](/solutions/case-studies)

[Get Started](/learn/)
[Playground](/play)
[Tour](/tour/)
[Stack Overflow](https://stackoverflow.com/questions/tagged/go?tab=Newest)
[Help](/help/)

[Packages](https://pkg.go.dev)
[Standard Library](/pkg/)
[About Go Packages](https://pkg.go.dev/about)

[About](/project)
[Download](/dl/)
[Blog](/blog/)
[Issue Tracker](https://github.com/golang/go/issues)
[Release Notes](/doc/devel/release)
[Brand Guidelines](/brand)
[Code of Conduct](/conduct)

[Connect](https://www.twitter.com/golang)
[Twitter](https://www.twitter.com/golang)
[GitHub](https://github.com/golang)
[Slack](https://invite.slack.golangbridge.org/)
[r/golang](https://reddit.com/r/golang)
[Meetup](https://www.meetup.com/pro/go)
[Golang Weekly](https://golangweekly.com/)

Opens in new window.

![The Go Gopher](/images/gophers/pilot-bust.svg)

* [Copyright](/copyright)
* [Terms of Service](/tos)
* [Privacy Policy](http://www.google.com/intl/en/policies/privacy/)
* [Report an Issue](/s/website-issue)
* ![System theme](/images/icons/brightness_6_gm_grey_24dp.svg)
  ![Dark theme](/images/icons/brightness_2_gm_grey_24dp.svg)
  ![Light theme](/images/icons/light_mode_gm_grey_24dp.svg)

[![Google logo](/images/google-white.png)](https://google.com)

go.dev uses cookies from Google to deliver and enhance the quality of its services and to
analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay

---

## Source: solutions_use-cases.md

Use Cases - The Go Programming Language





[![Go](/images/go-logo-white.svg)](/)

[Skip to Main Content](#main-content)

* [Why Go *arrow\_drop\_down*](#)

  Press Enter to activate/deactivate dropdown

  + [Case Studies](/solutions/case-studies)

    Common problems companies solve with Go
  + [Use Cases](/solutions/use-cases)

    Stories about how and why companies use Go
  + [Security](/security/)

    How Go can help keep you secure by default
* [Learn](/learn/)

  Press Enter to activate/deactivate dropdown
* [Docs *arrow\_drop\_down*](#)

  Press Enter to activate/deactivate dropdown

  + [Go Spec](/ref/spec)

    The official Go language specification
  + [Go User Manual](/doc)

    A complete introduction to building software with Go
  + [Standard library](https://pkg.go.dev/std)

    Reference documentation for Go's standard library
  + [Release Notes](/doc/devel/release)

    Learn what's new in each Go release
  + [Effective Go](/doc/effective_go)

    Tips for writing clear, performant, and idiomatic Go code
* [Packages](https://pkg.go.dev)

  Press Enter to activate/deactivate dropdown
* [Community *arrow\_drop\_down*](#)

  Press Enter to activate/deactivate dropdown

  + [Recorded Talks](/talks/)

    Videos from prior events
  + [Meetups
    *open\_in\_new*](https://www.meetup.com/pro/go)

    Meet other local Go developers
  + [Conferences
    *open\_in\_new*](/wiki/Conferences)

    Learn and network with Go developers from around the world
  + [Go blog](/blog)

    The Go project's official blog.
  + [Go project](/help)

    Get help and stay informed from Go
  + Get connected

    [![](/images/logos/social/google-groups.svg)](https://groups.google.com/g/golang-nuts)
    [![](/images/logos/social/github.svg)](https://github.com/golang)
    [![](/images/logos/social/twitter.svg)](https://twitter.com/golang)
    [![](/images/logos/social/reddit.svg)](https://www.reddit.com/r/golang/)
    [![](/images/logos/social/slack.svg)](https://invite.slack.golangbridge.org/)
    [![](/images/logos/social/stack-overflow.svg)](https://stackoverflow.com/tags/go)




[![Go.](/images/go-logo-blue.svg)](/)

* [Why Go *navigate\_next*](#)

  [*navigate\_before*Why Go](#)

  + [Case Studies](/solutions/case-studies)
  + [Use Cases](/solutions/use-cases)
  + [Security](/security/)
* [Learn](/learn/)
* [Docs *navigate\_next*](#)

  [*navigate\_before*Docs](#)

  + [Go Spec](/ref/spec)
  + [Go User Manual](/doc)
  + [Standard library](https://pkg.go.dev/std)
  + [Release Notes](/doc/devel/release)
  + [Effective Go](/doc/effective_go)
* [Packages](https://pkg.go.dev)
* [Community *navigate\_next*](#)

  [*navigate\_before*Community](#)

  + [Recorded Talks](/talks/)
  + [Meetups
    *open\_in\_new*](https://www.meetup.com/pro/go)
  + [Conferences
    *open\_in\_new*](/wiki/Conferences)
  + [Go blog](/blog)
  + [Go project](/help)
  + Get connected

    [![](/images/logos/social/google-groups.svg)](https://groups.google.com/g/golang-nuts)
    [![](/images/logos/social/github.svg)](https://github.com/golang)
    [![](/images/logos/social/twitter.svg)](https://twitter.com/golang)
    [![](/images/logos/social/reddit.svg)](https://www.reddit.com/r/golang/)
    [![](/images/logos/social/slack.svg)](https://invite.slack.golangbridge.org/)
    [![](/images/logos/social/stack-overflow.svg)](https://stackoverflow.com/tags/go)

1. [Why Go](/solutions/)
2. [Use Cases](/solutions/use-cases)

# Use Cases

* [![cloud icon](/solutions/cloud-green.svg)
  ![cloud icon](/solutions/cloud-white.svg)

  ### Cloud & Network Services

  With a strong ecosystem of tools and APIs on major cloud providers, it is easier than ever to build services with Go.

  Learn More](/solutions/cloud)
* [![CLI icon](/solutions/clis-green.svg)
  ![CLI icon](/solutions/clis-white.svg)

  ### Command-line Interfaces (CLIs)

  With popular open source packages and a robust standard library, use Go to create fast and elegant CLIs.

  Learn More](/solutions/clis)
* [![web dev icon](/solutions/webdev-green.svg)
  ![web dev icon](/solutions/webdev-white.svg)

  ### Web Development

  With enhanced memory performance and support for several IDEs, Go powers fast and scalable web applications.

  Learn More](/solutions/webdev)
* [![ops icon](/solutions/devops-green.svg)
  ![ops icon](/solutions/devops-white.svg)

  ### Development Operations & Site Reliability Engineering

  With fast build times, lean syntax, an automatic formatter and doc generator, Go is built to support both DevOps and SRE.

  Learn More](/solutions/devops)

Opens in new window.



[Why Go](/solutions/)
[Use Cases](/solutions/use-cases)
[Case Studies](/solutions/case-studies)

[Get Started](/learn/)
[Playground](/play)
[Tour](/tour/)
[Stack Overflow](https://stackoverflow.com/questions/tagged/go?tab=Newest)
[Help](/help/)

[Packages](https://pkg.go.dev)
[Standard Library](/pkg/)
[About Go Packages](https://pkg.go.dev/about)

[About](/project)
[Download](/dl/)
[Blog](/blog/)
[Issue Tracker](https://github.com/golang/go/issues)
[Release Notes](/doc/devel/release)
[Brand Guidelines](/brand)
[Code of Conduct](/conduct)

[Connect](https://www.twitter.com/golang)
[Twitter](https://www.twitter.com/golang)
[GitHub](https://github.com/golang)
[Slack](https://invite.slack.golangbridge.org/)
[r/golang](https://reddit.com/r/golang)
[Meetup](https://www.meetup.com/pro/go)
[Golang Weekly](https://golangweekly.com/)

Opens in new window.

![The Go Gopher](/images/gophers/pilot-bust.svg)

* [Copyright](/copyright)
* [Terms of Service](/tos)
* [Privacy Policy](http://www.google.com/intl/en/policies/privacy/)
* [Report an Issue](/s/website-issue)
* ![System theme](/images/icons/brightness_6_gm_grey_24dp.svg)
  ![Dark theme](/images/icons/brightness_2_gm_grey_24dp.svg)
  ![Light theme](/images/icons/light_mode_gm_grey_24dp.svg)

[![Google logo](/images/google-white.png)](https://google.com)

go.dev uses cookies from Google to deliver and enhance the quality of its services and to
analyze traffic. [Learn more.](https://policies.google.com/technologies/cookies)

Okay

---
