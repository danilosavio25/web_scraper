# Best_practices Knowledge

> Category: patterns_architecture

## Source: blog.md

The Twelve-Factor App 

# The Twelve-Factor Blog

## Why Intuit is Thrilled About the Evolution of the Twelve-Factor Model

###### 03 Apr, 2025

### Brett Weaver

## Evolving Twelve-Factor: Applications to Modern Cloud-Native Platforms

###### 10 Feb, 2025

### Brian Hammons

!Brian Hammons The recent **open sourcing of the Twelve-Factor App Methodology** comes at a transformative moment for cloud-native platforms. As organizations increasingly rely on cloud-native technologies to power mission-critical workloads, the principles behind Twelve-Factor offer timeless foundations that remain relevant for modern platform builders. ****

## December Monthly Updates

###### 3 Dec, 2024

### Vish Abrams

!Vish Abrams Welcome to our first monthly update! We’re excited to share our progress and what’s coming next.

#### What We’ve Been Working On

In addition to some minor formatting fixes, our initial focus has been on getting organized for larger updates. Here are the key activities: ****

## Twelve-Factor App Methodology is now Open Source

###### 12 Nov, 2024

### Yehuda Katz

!Yehuda Katz **Join us in modernizing the twelve-factor app manifesto together.** As a community of app, framework and platform developers, we’re working together to refresh this foundational document for the modern era. While it’s not software we’re working on, we’ll use familiar processes like pull requests, issues, and reviews to collaborate together in the twelve-factor project repo.

This initiative builds on a strong foundation laid by Heroku when they originally created “The Twelve-Factor App” all the way back in 2011, a time when container-based deployment was still just emerging. Back then, developers could get apps running on their local machines, but common development mistakes often made it challenging to deploy those apps to production. ****

## Narrow Conduits and the Application-Platform Interface

###### 12 Nov, 2024

### Vish Abrams

!Vish Abrams Welcome to the twelve-factor maintainters blog. As stated in our announcement, some of our posts will analyze the manifesto more generically. This is the first post in that vein, where we dive into the interface between the application and the platform.

It is well understood that defining a clear contract between parts of a system allows one to shed cognitive load on either side of the contract. This has been called the “narrow-waist” principle which has some unfortunate connotations, so we’ll refer to it as the “narrow-conduit” principle. This principle is especially valuable when the humans on either side of the conduit have dramatically different concerns. ****

---

## Source: codebase.md

The Twelve-Factor App 

# The Twelve-Factor App

## I. Codebase

### One codebase tracked in revision control, many deploys

A twelve-factor app is always tracked in a version control system, such as Git, Mercurial, or Subversion. A copy of the revision tracking database is known as a *code repository*, often shortened to *code repo* or just *repo*.

A *codebase* is any single repo (in a centralized revision control system like Subversion), or any set of repos who share a root commit (in a decentralized revision control system like Git).

There is always a one-to-one correlation between the codebase and the app:

* If there are multiple codebases, it’s not an app – it’s a distributed system. Each component in a distributed system is an app, and each can individually comply with twelve-factor.
* Multiple apps sharing the same code is a violation of twelve-factor. The solution here is to factor shared code into libraries which can be included through the dependency manager.

There is only one codebase per app, but there will be many deploys of the app. A *deploy* is a running instance of the app. This is typically a production site, and one or more staging sites. Additionally, every developer has a copy of the app running in their local development environment, each of which also qualifies as a deploy.

The codebase is the same across all deploys, although different versions may be active in each deploy. For example, a developer has some commits not yet deployed to staging; staging has some commits not yet deployed to production. But they all share the same codebase, thus making them identifiable as different deploys of the same app.

---

## Source: community.md

The Twelve-Factor App 

# The Twelve-Factor App

# Welcome to the Twelve-Factor community!

Thank you for your interest in the twelve-factor manifesto. Here are some suggestions for getting started with the community:

1. **Familiarize Yourself with the Project**

   * Begin by reviewing the Twelve-Factor Manifesto to see the current state.
   * Check out the Twelve-Factor Vision to understand the project’s goals and principles.
   * Take a look at the Twelve-Factor Governance document to familiarize yourself with how we operate.
2. **Join the Discussion**

   * Participate in discussions on open issues.
   * Broader discussions often happen on the mailing list
   * Near real-time collaboration happens on discord
   * Respectful dialogue and collaboration a key to our community’s success.
3. **Find an Area to Contribute**

   * Contributions come in many forms: documentation, bug fixes, new features, or participating in discussions.
   * Look for open issues on our GitHub repository that are tagged as good first issue for beginners, or explore areas where you feel you can provide value.
   * More details can be found in The Contributing document.

## Meetings

The maintainers group meets weekly in our discord at 8:30 AM PST.

Invite links: (gcal) (ics)

# Maintainers

## Vish Abrams

### Heroku/Salesforce

## Evan Anderson

### Stacklok (independent)

!Evan Anderson Evan worked for about 15 years in Google’s cloud, with about 10 years in the public cloud. During that time, he was a founding member of the Google Compute Engine team, then worked on App Engine (control plane API), Cloud Functions, and Knative/Cloud Run. In 2019, he moved to VMware, where he spent 4 years on VMware Tandy, VMware’s cloud-native developer platform. He’s also the author of “Designing Serverless Applications with Knative”, and has held many leadership roles in Knative over the years.

## Brian Hammons

### AWS

!Brian Hammons Brian Hammons, a Principal Solutions Architect at AWS, is an original member of the launch team for Amazon EKS. He has held crucial roles in growing the service from its inception including co-founding projects such as eksworkshop.com, Data on EKS (DoEKS), and CNOE. Brian leads Application Modernization and Developer Productivity practice areas for AWS Strategic Industries as well as the Open Source Technical Field Community (TFC) of AWS Worldwide Specialists (WWSO).

## Yehuda Katz

### Heroku/Salesforce

!Yehuda Katz Yehuda is a True Believer in the power of the open web, especially when the web evolves as a collaboration between browser vendors, framework authors and application developers.

He is one of the creators of Ember.js, and a retired member of the Rust, the Ruby on Rails and jQuery Core Teams. He is an occasional member of ECMAScript’s TC39 standards committee, and a former member of the W3C’s TAG (Technical Architecture Group).

He was the co-author of the Extensible Web Manifesto, of which he is still very proud.

## Terence Lee

### Heroku/Salesforce

!Terence Lee Terence is an architect at Heroku where he helped create Classic Buildpacks and then later co-founded Cloud Native Buildpacks, a CNCF Incubation Project. In the Ruby community he’s been a maintainer on projects such as Ruby itself, Bundler, and Resque, but is mostly known for getting people together for #rubykaraoke. When he’s not going to an awesome event, he lives in Austin, TX where it’s acceptable to eat a taco for every meal of the day.

## Brett Weaver

### Intuit

!Brett Weaver Brett Weaver is a Distinguished Engineer at Intuit. He has spent the last twenty two odd years at Intuit in various software development and systems engineer roles. He has been focused on building distributed, scalable architectures for Intuit’s flagship products including Quickbooks and TurboTax. Most recently, Brett has been leading architecture for Intuit’s internal services platform.

# Emeritus

## Gail Frederick

### Heroku/Salesforce

!Gail Frederick As Heroku CTO, Gail is a Salesforce leader known for her technical excellence and drive to deliver. She stewards the opinionated magic that is Heroku’s developer platform. Prior to Heroku, Gail led engineering for Salesforce DX. Her values are integrity, impact, and joy. Previously, VP Engineering at eBay, where she was the 2019 winner of the John Donahoe Award, eBay’s highest leadership award, for building a new $3B annual GMB business by reinventing eBay’s developer ecosystem. Member of 2024 Curve Power List of 50 LGBTQ+ women and non-binary leaders. Formerly, executive advisory board member of Lesbians Who Tech, Business Governing Board member of OpenAPI Initiative at the Linux Foundation, and represented eBay at the founding of the Facebook-led Libra Initiative. Gail holds 9 software patents.

## Steren Giannini

### Google Cloud

!Steren Giannini Steren is an engineer turned product manager. He is leading product management for Google Cloud’s serverless portfolio (Cloud Run, Cloud Run functions, App Engine). He is a founding member of Cloud Run.

<

<

<

## Grace Jansen

### IBM

!Grace Jansen Grace is a Java Champion and Developer Advocate at IBM. She has been with IBM since graduating with a Degree in Biology. Grace enjoys bringing a varied perspective to her projects and using her knowledge of biological systems to simplify complex software patterns. As a developer advocate, Grace builds POC’s, demos, sample applications and tutorials. She is a regular presenter at international conferences and has authored a book on reactive systems.

## Joe Kutner

### Salesforce

!Joe Kutner Joe is co-founder of the Cloud Native Buildpacks project, which aims to make containerization more secure and developer friendly. He started the project in 2018 while working as DX Architect at Salesforce Heroku, and today is the DX Architect for Salesforce’s Hyperforce platform.

## James Ward

### AWS

!James Ward Professional software developer since 1997, with much of that time spent helping developers build software that doesn’t suck. A Typed Pure Functional Programming zealot who often compromises on his ideals to just get stuff done. Currently a Developer Advocate for AWS.

---

## Source: dependencies.md

The Twelve-Factor App 

# The Twelve-Factor App

## II. Dependencies

### Explicitly declare and isolate dependencies

Most programming languages offer a packaging system for distributing support libraries, such as CPAN for Perl or Rubygems for Ruby. Libraries installed through a packaging system can be installed system-wide (known as “site packages”) or scoped into the directory containing the app (known as “vendoring” or “bundling”).

**A twelve-factor app never relies on implicit existence of system-wide packages.** It declares all dependencies, completely and exactly, via a *dependency declaration* manifest. Furthermore, it uses a *dependency isolation* tool during execution to ensure that no implicit dependencies “leak in” from the surrounding system. The full and explicit dependency specification is applied uniformly to both production and development.

For example, Bundler for Ruby offers the `Gemfile` manifest format for dependency declaration and `bundle exec` for dependency isolation. In Python there are two separate tools for these steps – Pip is used for declaration and Virtualenv for isolation. Even C has Autoconf for dependency declaration, and static linking can provide dependency isolation. No matter what the toolchain, dependency declaration and isolation must always be used together – only one or the other is not sufficient to satisfy twelve-factor.

One benefit of explicit dependency declaration is that it simplifies setup for developers new to the app. The new developer can check out the app’s codebase onto their development machine, requiring only the language runtime and dependency manager installed as prerequisites. They will be able to set up everything needed to run the app’s code with a deterministic *build command*. For example, the build command for Ruby/Bundler is `bundle install`, while for Clojure/Leiningen it is `lein deps`.

Twelve-factor apps also do not rely on the implicit existence of any system tools. Examples include shelling out to ImageMagick or `curl`. While these tools may exist on many or even most systems, there is no guarantee that they will exist on all systems where the app may run in the future, or whether the version found on a future system will be compatible with the app. If the app needs to shell out to a system tool, that tool should be vendored into the app.

---

## Source: index.md

The Twelve-Factor App 

# The Twelve-Factor App

# Introduction

In the modern era, software is commonly delivered as a service: called *web apps*, or *software-as-a-service*. The twelve-factor app is a methodology for building software-as-a-service apps that:

* Use **declarative** formats for setup automation, to minimize time and cost for new developers joining the project;
* Have a **clean contract** with the underlying operating system, offering **maximum portability** between execution environments;
* Are suitable for **deployment** on modern **cloud platforms**, obviating the need for servers and systems administration;
* **Minimize divergence** between development and production, enabling **continuous deployment** for maximum agility;
* And can **scale up** without significant changes to tooling, architecture, or development practices.

The twelve-factor methodology can be applied to apps written in any programming language, and which use any combination of backing services (database, queue, memory cache, etc).

# Background

The contributors to this document have been directly involved in the development and deployment of hundreds of apps, and indirectly witnessed the development, operation, and scaling of hundreds of thousands of apps via our work on the Heroku platform.

This document synthesizes all of our experience and observations on a wide variety of software-as-a-service apps in the wild. It is a triangulation on ideal practices for app development, paying particular attention to the dynamics of the organic growth of an app over time, the dynamics of collaboration between developers working on the app’s codebase, and avoiding the cost of software erosion.

Our motivation is to raise awareness of some systemic problems we’ve seen in modern application development, to provide a shared vocabulary for discussing those problems, and to offer a set of broad conceptual solutions to those problems with accompanying terminology. The format is inspired by Martin Fowler’s books *Patterns of Enterprise Application Architecture* and *Refactoring*.

# Who should read this document?

Any developer building applications which run as a service. Ops engineers who deploy or manage such applications.

# The Twelve Factors

## I. Codebase

### One codebase tracked in revision control, many deploys

## II. Dependencies

### Explicitly declare and isolate dependencies

## III. Config

### Store config in the environment

## IV. Backing services

### Treat backing services as attached resources

## V. Build, release, run

### Strictly separate build and run stages

## VI. Processes

### Execute the app as one or more stateless processes

## VII. Port binding

### Export services via port binding

## VIII. Concurrency

### Scale out via the process model

## IX. Disposability

### Maximize robustness with fast startup and graceful shutdown

## X. Dev/prod parity

### Keep development, staging, and production as similar as possible

## XI. Logs

### Treat logs as event streams

## XII. Admin processes

### Run admin/management tasks as one-off processes

---