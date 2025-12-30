The Twelve-Factor App 








# [The Twelve-Factor App](/ "The Twelve-Factor App")

* [Blog](/blog)
* [Community](/community)
* [![GitHub logo](/images/github-mark.svg)GitHub](https://github.com/twelve-factor/twelve-factor)

## II. Dependencies

### Explicitly declare and isolate dependencies

Most programming languages offer a packaging system for distributing support libraries, such as [CPAN](http://www.cpan.org/) for Perl or [Rubygems](http://rubygems.org/) for Ruby. Libraries installed through a packaging system can be installed system-wide (known as “site packages”) or scoped into the directory containing the app (known as “vendoring” or “bundling”).

**A twelve-factor app never relies on implicit existence of system-wide packages.** It declares all dependencies, completely and exactly, via a *dependency declaration* manifest. Furthermore, it uses a *dependency isolation* tool during execution to ensure that no implicit dependencies “leak in” from the surrounding system. The full and explicit dependency specification is applied uniformly to both production and development.

For example, [Bundler](https://bundler.io/) for Ruby offers the `Gemfile` manifest format for dependency declaration and `bundle exec` for dependency isolation. In Python there are two separate tools for these steps – [Pip](http://www.pip-installer.org/en/latest/) is used for declaration and [Virtualenv](http://www.virtualenv.org/en/latest/) for isolation. Even C has [Autoconf](http://www.gnu.org/s/autoconf/) for dependency declaration, and static linking can provide dependency isolation. No matter what the toolchain, dependency declaration and isolation must always be used together – only one or the other is not sufficient to satisfy twelve-factor.

One benefit of explicit dependency declaration is that it simplifies setup for developers new to the app. The new developer can check out the app’s codebase onto their development machine, requiring only the language runtime and dependency manager installed as prerequisites. They will be able to set up everything needed to run the app’s code with a deterministic *build command*. For example, the build command for Ruby/Bundler is `bundle install`, while for Clojure/[Leiningen](https://github.com/technomancy/leiningen#readme) it is `lein deps`.

Twelve-factor apps also do not rely on the implicit existence of any system tools. Examples include shelling out to ImageMagick or `curl`. While these tools may exist on many or even most systems, there is no guarantee that they will exist on all systems where the app may run in the future, or whether the version found on a future system will be compatible with the app. If the app needs to shell out to a system tool, that tool should be vendored into the app.

[Česky (cs)](/cs/dependencies) | [Deutsch (de)](/de/dependencies) | [Ελληνικά (el)](/el/dependencies) | English (en) | [Español (es)](/es/dependencies) | [فارسی (fa)](/fa/dependencies) | [Français (fr)](/fr/dependencies) | [Italiano (it)](/it/dependencies) | [日本語 (ja)](/ja/dependencies) | [한국어 (ko)](/ko/dependencies) | [Polski (pl)](/pl/dependencies) | [Português do Brasil (pt\_br)](/pt_br/dependencies) | [Русский (ru)](/ru/dependencies) | [Slovensky (sk)](/sk/dependencies) | [ภาษาไทย (th)](/th/dependencies) | [Türkçe (tr)](/tr/dependencies) | [Українська (uk)](/uk/dependencies) | [Tiếng Việt (vi)](/vi/dependencies) | [简体中文 (zh\_cn)](/zh_cn/dependencies)

[« Previous](./codebase)

[Next »](./config)

[Česky (cs)](/cs/dependencies) | [Deutsch (de)](/de/dependencies) | [Ελληνικά (el)](/el/dependencies) | English (en) | [Español (es)](/es/dependencies) | [فارسی (fa)](/fa/dependencies) | [Français (fr)](/fr/dependencies) | [Italiano (it)](/it/dependencies) | [日本語 (ja)](/ja/dependencies) | [한국어 (ko)](/ko/dependencies) | [Polski (pl)](/pl/dependencies) | [Português do Brasil (pt\_br)](/pt_br/dependencies) | [Русский (ru)](/ru/dependencies) | [Slovensky (sk)](/sk/dependencies) | [ภาษาไทย (th)](/th/dependencies) | [Türkçe (tr)](/tr/dependencies) | [Українська (uk)](/uk/dependencies) | [Tiếng Việt (vi)](/vi/dependencies) | [简体中文 (zh\_cn)](/zh_cn/dependencies)

Written by Adam Wiggins • Last updated 2017 • [Sourcecode](https://github.com/heroku/12factor) • [Download ePub Book](/12factor.epub)

© Copyright 2025 Salesforce, Inc. All rights reserved. Various trademarks held by their respective owners. Salesforce Tower, 415 Mission Street, 3rd Floor, San Francisco, CA 94105, United States

[Legal](https://www.salesforce.com/company/legal/) [Terms of Service](https://www.salesforce.com/company/legal/sfdc-website-terms-of-service/) [Privacy Information](https://www.salesforce.com/company/privacy/) [Responsible Disclosure](https://www.salesforce.com/company/disclosure/) [Trust](https://trust.salesforce.com/en/) [Contact](https://www.salesforce.com/form/contact/contactme/?d=70130000000EeYa) [![](/images/privacy.png "Privacy Icon")Your Privacy Choices](https://www.salesforce.com/form/other/privacy-request/) [Cookie Preferences](#)