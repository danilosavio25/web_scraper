# Nextjs Knowledge

> Category: frameworks

## Source: docs.md

Next.js Docs | Next.jsSkip to content

Search documentation...Search...`⌘K`

ShowcaseDocsBlogTemplatesEnterprise

Search documentation...Search...`⌘K`FeedbackLearn

Important

Security Advisory: React2Shell & two new vulnerabilities

Find out more

Menu

Using App Router

Features available in /app

Latest Version

16.1.1

* Getting Started

  + Installation
  + Project Structure
  + Layouts and Pages
  + Linking and Navigating
  + Server and Client Components
  + Cache Components
  + Fetching Data
  + Updating Data
  + Caching and Revalidating
  + Error Handling
  + CSS
  + Image Optimization
  + Font Optimization
  + Metadata and OG images
  + Route Handlers
  + Proxy
  + Deploying
  + Upgrading

* Guides

  + Analytics
  + Authentication
  + Backend for Frontend
  + Caching
  + CI Build Caching
  + Content Security Policy
  + CSS-in-JS
  + Custom Server
  + Data Security
  + Debugging
  + Draft Mode
  + Environment Variables
  + Forms
  + ISR
  + Instrumentation
  + Internationalization
  + JSON-LD
  + Lazy Loading
  + Development Environment
  + Next.js MCP Server
  + MDX
  + Memory Usage
  + Migrating

    - App Router
    - Create React App
    - Vite
  + Multi-tenant
  + Multi-zones
  + OpenTelemetry
  + Package Bundling
  + Prefetching
  + Production
  + PWAs
  + Redirecting
  + Sass
  + Scripts
  + Self-Hosting
  + SPAs
  + Static Exports
  + Tailwind CSS v3
  + Testing

    - Cypress
    - Jest
    - Playwright
    - Vitest
  + Third Party Libraries
  + Upgrading

    - Codemods
    - Version 14
    - Version 15
    - Version 16
  + Videos

* API Reference

  + Directives

    - use cache
    - use cache: private
    - use cache: remote
    - use client
    - use server
  + Components

    - Font
    - Form Component
    - Image Component
    - Link Component
    - Script Component
  + File-system conventions

    - default.js
    - Dynamic Segments
    - error.js
    - forbidden.js
    - instrumentation.js
    - instrumentation-client.js
    - Intercepting Routes
    - layout.js
    - loading.js
    - mdx-components.js
    - not-found.js
    - page.js
    - Parallel Routes
    - proxy.js
    - public
    - route.js
    - Route Groups
    - Route Segment Config
    - src
    - template.js
    - unauthorized.js
    - Metadata Files

      * favicon, icon, and apple-icon
      * manifest.json
      * opengraph-image and twitter-image
      * robots.txt
      * sitemap.xml
  + Functions

    - after
    - cacheLife
    - cacheTag
    - connection
    - cookies
    - draftMode
    - fetch
    - forbidden
    - generateImageMetadata
    - generateMetadata
    - generateSitemaps
    - generateStaticParams
    - generateViewport
    - headers
    - ImageResponse
    - NextRequest
    - NextResponse
    - notFound
    - permanentRedirect
    - redirect
    - refresh
    - revalidatePath
    - revalidateTag
    - unauthorized
    - unstable\_cache
    - unstable\_noStore
    - unstable\_rethrow
    - updateTag
    - useLinkStatus
    - useParams
    - usePathname
    - useReportWebVitals
    - useRouter
    - useSearchParams
    - useSelectedLayoutSegment
    - useSelectedLayoutSegments
    - userAgent
  + Configuration

    - next.config.js

      * experimental.adapterPath
      * allowedDevOrigins
      * appDir
      * assetPrefix
      * authInterrupts
      * basePath
      * browserDebugInfoInTerminal
      * cacheComponents
      * cacheHandlers
      * cacheLife
      * compress
      * crossOrigin
      * cssChunking
      * devIndicators
      * distDir
      * env
      * expireTime
      * exportPathMap
      * generateBuildId
      * generateEtags
      * headers
      * htmlLimitedBots
      * httpAgentOptions
      * images
      * cacheHandler
      * inlineCss
      * isolatedDevBuild
      * logging
      * mdxRs
      * onDemandEntries
      * optimizePackageImports
      * output
      * pageExtensions
      * poweredByHeader
      * productionBrowserSourceMaps
      * proxyClientMaxBodySize
      * reactCompiler
      * reactMaxHeadersLength
      * reactStrictMode
      * redirects
      * rewrites
      * sassOptions
      * serverActions
      * serverComponentsHmrCache
      * serverExternalPackages
      * staleTimes
      * staticGeneration\*
      * taint
      * trailingSlash
      * transpilePackages
      * turbopack
      * turbopackFileSystemCache
      * typedRoutes
      * typescript
      * urlImports
      * useLightningcss
      * viewTransition
      * webpack
      * webVitalsAttribution
    - TypeScript
    - ESLint
  + CLI

    - create-next-app
    - next CLI
  + Edge Runtime
  + Turbopack

* Getting Started

  + Installation
  + Project Structure
  + Images
  + Fonts
  + CSS
  + Deploying

* Guides

  + Analytics
  + Authentication
  + Babel
  + CI Build Caching
  + Content Security Policy
  + CSS-in-JS
  + Custom Server
  + Debugging
  + Draft Mode
  + Environment Variables
  + Forms
  + ISR
  + Instrumentation
  + Internationalization
  + Lazy Loading
  + MDX
  + Migrating

    - App Router
    - Create React App
    - Vite
  + Multi-Zones
  + OpenTelemetry
  + Package Bundling
  + PostCSS
  + Preview Mode
  + Production
  + Redirecting
  + Sass
  + Scripts
  + Self-Hosting
  + Static Exports
  + Tailwind CSS
  + Testing

    - Cypress
    - Jest
    - Playwright
    - Vitest
  + Third Party Libraries
  + Upgrading

    - Codemods
    - Version 10
    - Version 11
    - Version 12
    - Version 13
    - Version 14
    - Version 9

* Building Your Application

  + Routing

    - Pages and Layouts
    - Dynamic Routes
    - Linking and Navigating
    - Custom App
    - Custom Document
    - API Routes
    - Custom Errors
  + Rendering

    - Server-side Rendering (SSR)
    - Static Site Generation (SSG)
    - Automatic Static Optimization
    - Client-side Rendering (CSR)
  + Data Fetching

    - getStaticProps
    - getStaticPaths
    - Forms and Mutations
    - getServerSideProps
    - Client-side Fetching
  + Configuring

    - Error Handling

* API Reference

  + Components

    - Font
    - Form
    - Head
    - Image
    - Image (Legacy)
    - Link
    - Script
  + File-system conventions

    - instrumentation.js
    - Proxy
    - public
    - src Directory
  + Functions

    - getInitialProps
    - getServerSideProps
    - getStaticPaths
    - getStaticProps
    - NextRequest
    - NextResponse
    - useReportWebVitals
    - useRouter
    - userAgent
  + Configuration

    - next.config.js Options

      * experimental.adapterPath
      * allowedDevOrigins
      * assetPrefix
      * basePath
      * bundlePagesRouterDependencies
      * compress
      * crossOrigin
      * devIndicators
      * distDir
      * env
      * exportPathMap
      * generateBuildId
      * generateEtags
      * headers
      * httpAgentOptions
      * images
      * isolatedDevBuild
      * onDemandEntries
      * optimizePackageImports
      * output
      * pageExtensions
      * poweredByHeader
      * productionBrowserSourceMaps
      * experimental.proxyClientMaxBodySize
      * reactStrictMode
      * redirects
      * rewrites
      * serverExternalPackages
      * trailingSlash
      * transpilePackages
      * turbopack
      * typescript
      * urlImports
      * useLightningcss
      * webpack
      * webVitalsAttribution
    - TypeScript
    - ESLint
  + CLI

    - create-next-app CLI
    - next CLI
  + Edge Runtime
  + Turbopack

* Architecture

  + Accessibility
  + Fast Refresh
  + Next.js Compiler
  + Supported Browsers

  + Contribution Guide
  + Rspack

On this page

* What is Next.js?
* How to use the docs
* App Router and Pages Router
* React version handling
* Pre-requisite knowledge
* Accessibility
* Join our Community
* Next Steps

Edit this page on GitHub Scroll to top

# Next.js Docs

Welcome to the Next.js documentation!

## What is Next.js?

Next.js is a React framework for building full-stack web applications. You use React Components to build user interfaces, and Next.js for additional features and optimizations.

It also automatically configures lower-level tools like bundlers and compilers. You can instead focus on building your product and shipping quickly.

Whether you're an individual developer or part of a larger team, Next.js can help you build interactive, dynamic, and fast React applications.

## How to use the docs

The docs are organized into 3 sections:

* Getting Started: Step-by-step tutorials to help you create a new application and learn the core Next.js features.
* Guides: Tutorials on specific use cases, choose what's relevant to you.
* API Reference: Detailed technical reference for every feature.

Use the sidebar to navigate through the sections, or search (`Ctrl+K` or `Cmd+K`) to quickly find a page.

## App Router and Pages Router

Next.js has two different routers:

* **App Router**: The newer router that supports new React features like Server Components.
* **Pages Router**: The original router, still supported and being improved.

At the top of the sidebar, you'll notice a dropdown menu that allows you to switch between the App Router and the Pages Router docs.

### React version handling

The App Router and Pages Router handle React versions differently:

* **App Router**: Uses React canary releases built-in, which include all the stable React 19 changes, as well as newer features being validated in frameworks, prior to a new React release.
* **Pages Router**: Uses the React version installed in your project's `package.json`.

This approach ensures new React features work reliably in the App Router while maintaining backwards compatibility for existing Pages Router applications.

## Pre-requisite knowledge

Our documentation assumes some familiarity with web development. Before getting started, it'll help if you're comfortable with:

* HTML
* CSS
* JavaScript
* React

If you're new to React or need a refresher, we recommend starting with our React Foundations course, and the Next.js Foundations course that has you building an application as you learn.

## Accessibility

For the best experience when using a screen reader, we recommend using Firefox and NVDA, or Safari and VoiceOver.

## Join our Community

If you have questions about anything related to Next.js, you're always welcome to ask our community on GitHub Discussions, Discord, X (Twitter), and Reddit.

## Next Steps

Create your first application and learn the core Next.js features.

### Getting Started

Learn how to create full-stack web applications with the Next.js App Router.

Previous

RspackNext

App Router

Was this helpful?

supported.

Send

---

---

#### Resources

DocsSupport PolicyLearnShowcaseBlogTeamAnalyticsNext.js ConfPreviewsEvals

#### More

Next.js CommerceContact SalesCommunityGitHubReleasesTelemetryGovernance

#### About Vercel

Next.js + VercelOpen Source SoftwareGitHubBlueskyX

#### Legal

Privacy Policy

#### Subscribe to our newsletter

Stay updated on new releases and features, guides, and case studies.

Subscribe

© 2025 Vercel, Inc.

---

---

---

## Source: index.md

Next.js by Vercel - The React FrameworkSkip to content

Search documentation...Search...`⌘K`

ShowcaseDocsBlogTemplatesEnterprise

Search documentation...Search...`⌘K`DeployLearn

Important

Security Advisory: React2Shell & two new vulnerabilities

Find out more

# The React Framework for the Web

Used by some of the world's largest companies, Next.js enables you to create **high-quality web applications** with the power of React components.

Get StartedLearn Next.js

▲ ~ npx create-next-app@latest

## What's in Next.js?

Everything you need to build great products on the web.

Data Fetching

Make your React component async and await your data. Next.js supports both server and client data fetching.Server Actions

Run server code by calling a function. Skip the API. Then, easily revalidate cached data and update your UI in one network roundtrip.Advanced Routing & Nested Layouts

Create routes using the file system, including support for more advanced routing patterns and UI layouts.

CSS Support

Style your application with your favorite tools, including support for CSS Modules, Tailwind CSS, and popular community libraries.Route Handlers

Build API endpoints to securely connect with third-party services for handling auth or listening for webhooks.Middleware

Take control of the incoming request. Use code to define routing and access rules for authentication, experimentation, and internationalization.

Client and Server Rendering

Flexible rendering and caching options, including Incremental Static Regeneration (ISR), on a per-page level.

Data Fetching

Make your React component async and await your data. Next.js supports both server and client data fetching.Server Actions

Run server code by calling a function. Skip the API. Then, easily revalidate cached data and update your UI in one network roundtrip.Advanced Routing & Nested Layouts

Create routes using the file system, including support for more advanced routing patterns and UI layouts.

CSS Support

Style your application with your favorite tools, including support for CSS Modules, Tailwind CSS, and popular community libraries.Route Handlers

Build API endpoints to securely connect with third-party services for handling auth or listening for webhooks.Middleware

Take control of the incoming request. Use code to define routing and access rules for authentication, experimentation, and internationalization.Client and Server Rendering

Flexible rendering and caching options, including Incremental Static Regeneration (ISR), on a per-page level.

Data Fetching

Make your React component async and await your data. Next.js supports both server and client data fetching.Server Actions

Run server code by calling a function. Skip the API. Then, easily revalidate cached data and update your UI in one network roundtrip.Advanced Routing & Nested Layouts

Create routes using the file system, including support for more advanced routing patterns and UI layouts.CSS Support

Style your application with your favorite tools, including support for CSS Modules, Tailwind CSS, and popular community libraries.Route Handlers

Build API endpoints to securely connect with third-party services for handling auth or listening for webhooks.Middleware

Take control of the incoming request. Use code to define routing and access rules for authentication, experimentation, and internationalization.Client and Server Rendering

Flexible rendering and caching options, including Incremental Static Regeneration (ISR), on a per-page level.

Next.js 16

The power of full-stack to the frontend. Read the release notes.

## Built on a foundation of fast, production-grade tooling

Powered By

ReactThe library for web and native user interfaces. Next.js is built on the latest React features, including Server Components and Actions.TurbopackAn incremental bundler optimized for JavaScript and TypeScript, written in Rust 

, and built into Next.js.!SWC Logo

Speedy Web CompilerAn extensible Rust 

 based platform for the next generation of fast developer tools, and can be used for both compilation and minification.

## Get started in seconds

Deploy Next.js to Vercel

StarterEcommerceBlogAIPortfolioSaaSMulti-tenant AppsRealtime AppsDocumentationVirtual EventWeb3

Vercel is a frontend cloud from the creators of Next.js, making it easy to get started with Next.js quickly.

Jumpstart your Next.js development with pre-built solutions from Vercel and our community.

Deploy a Template on Vercel

Next.js Boilerplate

A Next.js starter from create-next-app.

!An image gallery built on Next.js and Cloudinary.

Image Gallery Starter

An image gallery built on Next.js and Cloudinary.

!An all-in-one starter kit for high-performance ecommerce sites.

Next.js Commerce

An all-in-one starter kit for high-performance ecommerce sites.

## The framework of choice when it matters

For **performance**, **efficiency** and **developer experience**. Next.js is trusted by some of the biggest names on the web.

View the Next.js Showcase

## Customer Testimonials

> ### “With Next.js, we now consistently average 0.09 or lower for Cumulative Layout Shift, placing our site in the top tier for user experience and Core Web Vitals.”

!notion Logo!notion LogoSenior Software Engineer, Frontend

> ### “Our UI for Frame.io responds to user input within 100ms and all animations run at a consistent 60fps with Next.js.”

!adobe Logo!adobe LogoCharlton Roberts, Product Engineering

> ### “Next.js has been a game-changer for our agency work and team collaboration. Its powerful features have allowed us to build high-performance websites quickly and efficiently like never before.”

Daniel Lopes, Frontend Developer

---

---

#### Resources

DocsSupport PolicyLearnShowcaseBlogTeamAnalyticsNext.js ConfPreviewsEvals

#### More

Next.js CommerceContact SalesCommunityGitHubReleasesTelemetryGovernance

#### About Vercel

Next.js + VercelOpen Source SoftwareGitHubBlueskyX

#### Legal

Privacy Policy

#### Subscribe to our newsletter

Stay updated on new releases and features, guides, and case studies.

Subscribe

© 2025 Vercel, Inc.

---

---

Original

1440px

375px

Built-in Optimizations

Automatic Image, Font, and Script Optimizations for improved UX and Core Web Vitals.

Dynamic HTML Streaming

Instantly stream UI from the server, integrated with the App Router and React Suspense.

Next.js 16

The power of full-stack to the frontend. Read the release notes.

Dynamic HTML Streaming

Instantly stream UI from the server, integrated with the App Router and React Suspense.

Next.js 16

The power of full-stack to the frontend. Read the release notes.

Dynamic HTML Streaming

Instantly stream UI from the server, integrated with the App Router and React Suspense.

---

## Source: showcase.md

Showcase | Next.js by Vercel - The React FrameworkSkip to content

Search documentation...Search...`⌘K`

ShowcaseDocsBlogTemplatesEnterprise

Search documentation...Search...`⌘K`DeployLearn

Important

Security Advisory: React2Shell & two new vulnerabilities

Find out more

# The web framework for when it matters

Peerless performance, efficiency and developer experience. Next.js is trusted by some of the biggest names of the web.Peerless performance, efficiency and developer experience

Learn About Managed Next.jsContact Sales

  View the AI Chatbot Template template

  AI Chatbot Template

  A full-featured, hackable Next.js AI chatbot built by Vercel

  Deploy this template

  Read Stripe's customer story

  Architecting a live look at reliability: Stripe's viral Black Friday siteWith Vercel, Stripe's Black Friday site saw 100% uptime with over 17 million edge requests at launch

  100%

  Uptime

  17m+

  Edge requests at launch

  Read the customer story

  100%

  Uptime

  17m+

  Edge requests at launch

  Read Sonos's customer story

  Developing at the speed of sound: How Sonos amplified their DevExAfter migrating to Next.js and Vercel, Sonos had 75% faster build times and improved their performance scores by 10%

  75% faster

  Build times

  10% better

  Performance scores

  Read the customer story

  75% faster

  Build times

  10% better

  Performance scores

  View the Commerce Template template

  Commerce Template

  Starter kit for high-performance commerce with Shopify

  Deploy this template

14th

Largest   
 on GitHub

# 1

React   
 Framework

130,000

Stars   
 on GitHub

## Meet thousands of beautiful websites built with Next.js by Vercel

AllComposable CommerceWeb AppsAIMarketing & MediaPlatform Engineering

Sonos

Composable Commerce!

Nike

Composable Commerce!

OpenAI

AI!

Claude

AI!

NerdWallet

Web Apps!

Netflix Jobs

Web Apps

Load More

Powering the best frontend teams

StarterEcommerceBlogAIPortfolioSaaSMulti-tenant AppsRealtime AppsDocumentationVirtual EventWeb3

## Build like the best

Jumpstart your Next.js development with pre-built solutions from Vercel and our community.

Deploy a Template on Vercel

Next.js Boilerplate

A Next.js starter from create-next-app.

!An image gallery built on Next.js and Cloudinary.

Image Gallery Starter

An image gallery built on Next.js and Cloudinary.

!An all-in-one starter kit for high-performance ecommerce sites.

Next.js Commerce

An all-in-one starter kit for high-performance ecommerce sites.

## A powerful framework for building high-performance, server rendered web applications

### Superior Developer Experience

Deploy your Next.js site globally in seconds, with zero configuration just Git push to get started.

### Battle-tested in Production

All the features you need for production: hybrid static & server rendering, TypeScript support, smart bundling, route pre-fetching, and more.

### Performance-obsessed stack

Next.js brings years of experience in building and optimizing production applications.

Learn About Managed Next.jsContact Sales

---

---

#### Resources

DocsSupport PolicyLearnShowcaseBlogTeamAnalyticsNext.js ConfPreviewsEvals

#### More

Next.js CommerceContact SalesCommunityGitHubReleasesTelemetryGovernance

#### About Vercel

Next.js + VercelOpen Source SoftwareGitHubBlueskyX

#### Legal

Privacy Policy

#### Subscribe to our newsletter

Stay updated on new releases and features, guides, and case studies.

Subscribe

© 2025 Vercel, Inc.

---

---

---