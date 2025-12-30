# Django Knowledge

> Category: frameworks


## Source: en_6.0.md

Django documentation | Django documentation | Django


[Skip to main content](#main-content)


[Django](https://www.djangoproject.com/)

The web framework for perfectionists with deadlines.

Search




Submit

Toggle theme (current theme: auto)

Toggle theme (current theme: light)

Toggle theme (current theme: dark)

Toggle Light / Dark / Auto color theme

Menu

Main navigation

* [Overview](https://www.djangoproject.com/start/overview/)
* [Download](https://www.djangoproject.com/download/)
* [Documentation](https://docs.djangoproject.com/)
* [News](https://www.djangoproject.com/weblog/)
* [Code](https://github.com/django/django)
* [Issues](https://code.djangoproject.com/)
* [Community](https://www.djangoproject.com/community/)
* [Foundation](https://www.djangoproject.com/foundation/)
* [♥ Donate](https://www.djangoproject.com/fundraising/)
* Search




  Submit
* Toggle theme (current theme: auto)

  Toggle theme (current theme: light)

  Toggle theme (current theme: dark)

  Toggle Light / Dark / Auto color theme

[Documentation](https://docs.djangoproject.com/en/6.0/)

Help us reach our 2025 fundraising goal!

Donate to the *Django Software Foundation* to fund Django's development, security, and community events!  
If you got value out of using Django this year, please consider making a donation ♥
[Donate today](https://www.djangoproject.com/fundraising/)

* [Getting Help](https://docs.djangoproject.com/en/6.0/faq/help/)

* Language: **en**
* [el](https://docs.djangoproject.com/el/6.0/)
* [es](https://docs.djangoproject.com/es/6.0/)
* [fr](https://docs.djangoproject.com/fr/6.0/)
* [id](https://docs.djangoproject.com/id/6.0/)
* [it](https://docs.djangoproject.com/it/6.0/)
* [ja](https://docs.djangoproject.com/ja/6.0/)
* [ko](https://docs.djangoproject.com/ko/6.0/)
* [pl](https://docs.djangoproject.com/pl/6.0/)
* [pt-br](https://docs.djangoproject.com/pt-br/6.0/)
* [sv](https://docs.djangoproject.com/sv/6.0/)
* [zh-hans](https://docs.djangoproject.com/zh-hans/6.0/)

* Documentation version:
  **6.0**
* [1.8](https://docs.djangoproject.com/en/1.8/)
* [1.10](https://docs.djangoproject.com/en/1.10/)
* [1.11](https://docs.djangoproject.com/en/1.11/)
* [2.0](https://docs.djangoproject.com/en/2.0/)
* [2.1](https://docs.djangoproject.com/en/2.1/)
* [2.2](https://docs.djangoproject.com/en/2.2/)
* [3.0](https://docs.djangoproject.com/en/3.0/)
* [3.1](https://docs.djangoproject.com/en/3.1/)
* [3.2](https://docs.djangoproject.com/en/3.2/)
* [4.0](https://docs.djangoproject.com/en/4.0/)
* [4.1](https://docs.djangoproject.com/en/4.1/)
* [4.2](https://docs.djangoproject.com/en/4.2/)
* [5.0](https://docs.djangoproject.com/en/5.0/)
* [5.1](https://docs.djangoproject.com/en/5.1/)
* [5.2](https://docs.djangoproject.com/en/5.2/)
* [dev](https://docs.djangoproject.com/en/dev/)

# Django documentation[¶](#django-documentation "Link to this heading")

Everything you need to know about Django.

## First steps[¶](#first-steps "Link to this heading")

Are you new to Django or to programming? This is the place to start!

* **From scratch:**
  [Overview](intro/overview/) |
  [Installation](intro/install/)
* **Tutorial:**
  [Part 1: Requests and responses](intro/tutorial01/) |
  [Part 2: Models and the admin site](intro/tutorial02/) |
  [Part 3: Views and templates](intro/tutorial03/) |
  [Part 4: Forms and generic views](intro/tutorial04/) |
  [Part 5: Testing](intro/tutorial05/) |
  [Part 6: Static files](intro/tutorial06/) |
  [Part 7: Customizing the admin site](intro/tutorial07/) |
  [Part 8: Adding third-party packages](intro/tutorial08/)
* **Advanced Tutorials:**
  [How to write reusable apps](intro/reusable-apps/) |
  [Writing your first contribution to Django](intro/contributing/)

## Getting help[¶](#getting-help "Link to this heading")

Having trouble? We’d like to help!

* Try the [FAQ](faq/) – it’s got answers to many common questions.
* Looking for specific information? Try the [Index](genindex/), [Module Index](py-modindex/) or
  the [detailed table of contents](contents/).
* Not found anything? See [FAQ: Getting Help](faq/help/) for information on getting support
  and asking questions to the community.
* Report bugs with Django in our [ticket tracker](https://code.djangoproject.com/).

## How the documentation is organized[¶](#how-the-documentation-is-organized "Link to this heading")

Django has a lot of documentation. A high-level overview of how it’s organized
will help you know where to look for certain things:

* [Tutorials](intro/) take you by the hand through a series of
  steps to create a web application. Start here if you’re new to Django or web
  application development. Also look at the “[First steps](#index-first-steps)”.
* [Topic guides](topics/) discuss key topics and concepts at a
  fairly high level and provide useful background information and explanation.
* [Reference guides](ref/) contain technical reference for APIs and
  other aspects of Django’s machinery. They describe how it works and how to
  use it but assume that you have a basic understanding of key concepts.
* [How-to guides](howto/) are recipes. They guide you through the
  steps involved in addressing key problems and use-cases. They are more
  advanced than tutorials and assume some knowledge of how Django works.

## The model layer[¶](#the-model-layer "Link to this heading")

Django provides an abstraction layer (the “models”) for structuring and
manipulating the data of your web application. Learn more about it below:

* **Models:**
  [Introduction to models](topics/db/models/) |
  [Field types](ref/models/fields/) |
  [Indexes](ref/models/indexes/) |
  [Meta options](ref/models/options/) |
  [Model class](ref/models/class/)
* **QuerySets:**
  [Making queries](topics/db/queries/) |
  [QuerySet method reference](ref/models/querysets/) |
  [Lookup expressions](ref/models/lookups/)
* **Model instances:**
  [Instance methods](ref/models/instances/) |
  [Accessing related objects](ref/models/relations/)
* **Migrations:**
  [Introduction to Migrations](topics/migrations/) |
  [Operations reference](ref/migration-operations/) |
  [SchemaEditor](ref/schema-editor/) |
  [Writing migrations](howto/writing-migrations/)
* **Advanced:**
  [Managers](topics/db/managers/) |
  [Raw SQL](topics/db/sql/) |
  [Transactions](topics/db/transactions/) |
  [Aggregation](topics/db/aggregation/) |
  [Search](topics/db/search/) |
  [Custom fields](howto/custom-model-fields/) |
  [Multiple databases](topics/db/multi-db/) |
  [Custom lookups](howto/custom-lookups/) |
  [Query Expressions](ref/models/expressions/) |
  [Conditional Expressions](ref/models/conditional-expressions/) |
  [Database Functions](ref/models/database-functions/)
* **Other:**
  [Supported databases](ref/databases/) |
  [Legacy databases](howto/legacy-databases/) |
  [Providing initial data](howto/initial-data/) |
  [Optimize database access](topics/db/optimization/) |
  [PostgreSQL specific features](ref/contrib/postgres/)

## The view layer[¶](#the-view-layer "Link to this heading")

Django has the concept of “views” to encapsulate the logic responsible for
processing a user’s request and for returning the response. Find all you need
to know about views via the links below:

* **The basics:**
  [URLconfs](topics/http/urls/) |
  [View functions](topics/http/views/) |
  [Shortcuts](topics/http/shortcuts/) |
  [Decorators](topics/http/decorators/) |
  [Asynchronous Support](topics/async/)
* **Reference:**
  [Built-in Views](ref/views/) |
  [Request/response objects](ref/request-response/) |
  [TemplateResponse objects](ref/template-response/)
* **File uploads:**
  [Overview](topics/http/file-uploads/) |
  [File objects](ref/files/file/) |
  [Storage API](ref/files/storage/) |
  [Managing files](topics/files/) |
  [Custom storage](howto/custom-file-storage/)
* **Class-based views:**
  [Overview](topics/class-based-views/) |
  [Built-in display views](topics/class-based-views/generic-display/) |
  [Built-in editing views](topics/class-based-views/generic-editing/) |
  [Using mixins](topics/class-based-views/mixins/) |
  [API reference](ref/class-based-views/) |
  [Flattened index](ref/class-based-views/flattened-index/)
* **Advanced:**
  [Generating CSV](howto/outputting-csv/) |
  [Generating PDF](howto/outputting-pdf/)
* **Middleware:**
  [Overview](topics/http/middleware/) |
  [Built-in middleware classes](ref/middleware/)

## The template layer[¶](#the-template-layer "Link to this heading")

The template layer provides a designer-friendly syntax for rendering the
information to be presented to the user. Learn how this syntax can be used by
designers and how it can be extended by programmers:

* **The basics:**
  [Overview](topics/templates/)
* **For designers:**
  [Language overview](ref/templates/language/) |
  [Built-in tags and filters](ref/templates/builtins/) |
  [Humanization](ref/contrib/humanize/)
* **For programmers:**
  [Template API](ref/templates/api/) |
  [Custom tags and filters](howto/custom-template-tags/) |
  [Custom template backend](howto/custom-template-backend/)

## Forms[¶](#forms "Link to this heading")

Django provides a rich framework to facilitate the creation of forms and the
manipulation of form data.

* **The basics:**
  [Overview](topics/forms/) |
  [Form API](ref/forms/api/) |
  [Built-in fields](ref/forms/fields/) |
  [Built-in widgets](ref/forms/widgets/)
* **Advanced:**
  [Forms for models](topics/forms/modelforms/) |
  [Integrating media](topics/forms/media/) |
  [Formsets](topics/forms/formsets/) |
  [Customizing validation](ref/forms/validation/)

## The development process[¶](#the-development-process "Link to this heading")

Learn about the various components and tools to help you in the development and
testing of Django applications:

* **Settings:**
  [Overview](topics/settings/) |
  [Full list of settings](ref/settings/)
* **Applications:**
  [Overview](ref/applications/)
* **Exceptions:**
  [Overview](ref/exceptions/)
* **django-admin and manage.py:**
  [Overview](ref/django-admin/) |
  [Adding custom commands](howto/custom-management-commands/)
* **Testing:**
  [Introduction](topics/testing/) |
  [Writing and running tests](topics/testing/overview/) |
  [Included testing tools](topics/testing/tools/) |
  [Advanced topics](topics/testing/advanced/)
* **Deployment:**
  [Overview](howto/deployment/) |
  [WSGI servers](howto/deployment/wsgi/) |
  [ASGI servers](howto/deployment/asgi/) |
  [Deploying static files](howto/static-files/deployment/) |
  [Tracking code errors by email](howto/error-reporting/) |
  [Deployment checklist](howto/deployment/checklist/)

## The admin[¶](#the-admin "Link to this heading")

Find all you need to know about the automated admin interface, one of Django’s
most popular features:

* [Admin site](ref/contrib/admin/)
* [Admin actions](ref/contrib/admin/actions/)
* [Admin documentation generator](ref/contrib/admin/admindocs/)

## Security[¶](#security "Link to this heading")

Security is a topic of paramount importance in the development of web
applications and Django provides multiple protection tools and mechanisms:

* [Security overview](topics/security/)
* [Disclosed security issues in Django](releases/security/)
* [Clickjacking protection](ref/clickjacking/)
* [Cross Site Request Forgery protection](ref/csrf/)
* [Cryptographic signing](topics/signing/)
* [Security Middleware](ref/middleware/#security-middleware)
* [Content Security Policy](ref/csp/)

## Internationalization and localization[¶](#internationalization-and-localization "Link to this heading")

Django offers a robust internationalization and localization framework to
assist you in the development of applications for multiple languages and world
regions:

* [Overview](topics/i18n/) |
  [Internationalization](topics/i18n/translation/) |
  [Localization](topics/i18n/translation/#how-to-create-language-files) |
  [Localized web UI formatting and form input](topics/i18n/formatting/)
* [Time zones](topics/i18n/timezones/)

## Performance and optimization[¶](#performance-and-optimization "Link to this heading")

There are a variety of techniques and tools that can help get your code running
more efficiently - faster, and using fewer system resources.

* [Performance and optimization overview](topics/performance/)

## Geographic framework[¶](#geographic-framework "Link to this heading")

[GeoDjango](ref/contrib/gis/) intends to be a world-class
geographic web framework. Its goal is to make it as easy as possible to build
GIS web applications and harness the power of spatially enabled data.

## Common web application tools[¶](#common-web-application-tools "Link to this heading")

Django offers multiple tools commonly needed in the development of web
applications:

* **Authentication:**
  [Overview](topics/auth/) |
  [Using the authentication system](topics/auth/default/) |
  [Password management](topics/auth/passwords/) |
  [Customizing authentication](topics/auth/customizing/) |
  [API Reference](ref/contrib/auth/)
* [Caching](topics/cache/)
* [Logging](topics/logging/)
* [Tasks framework](topics/tasks/)
* [Sending emails](topics/email/)
* [Syndication feeds (RSS/Atom)](ref/contrib/syndication/)
* [Pagination](topics/pagination/)
* [Messages framework](ref/contrib/messages/)
* [Serialization](topics/serialization/)
* [Sessions](topics/http/sessions/)
* [Sitemaps](ref/contrib/sitemaps/)
* [Static files management](ref/contrib/staticfiles/)
* [Data validation](ref/validators/)

## Other core functionalities[¶](#other-core-functionalities "Link to this heading")

Learn about some other core functionalities of the Django framework:

* [Conditional content processing](topics/conditional-view-processing/)
* [Content types and generic relations](ref/contrib/contenttypes/)
* [Flatpages](ref/contrib/flatpages/)
* [Redirects](ref/contrib/redirects/)
* [Signals](topics/signals/)
* [System check framework](topics/checks/)
* [The sites framework](ref/contrib/sites/)
* [Unicode in Django](ref/unicode/)

## The Django open-source project[¶](#the-django-open-source-project "Link to this heading")

Learn about the development process for the Django project itself and about how
you can contribute:

* **Community:**
  [Contributing to Django](internals/contributing/) |
  [The release process](internals/release-process/) |
  [Team organization](internals/organization/) |
  [The Django source code repository](internals/git/) |
  [Security policies](internals/security/) |
  [Mailing lists and Forum](internals/mailing-lists/)
* **Design philosophies:**
  [Overview](misc/design-philosophies/)
* **Documentation:**
  [About this documentation](internals/contributing/writing-documentation/)
* **Third-party distributions:**
  [Overview](misc/distributions/)
* **Django over time:**
  [API stability](misc/api-stability/) |
  [Release notes and upgrading instructions](releases/) |
  [Deprecation Timeline](internals/deprecation/)

Previous page and next page

[Django documentation contents](contents/)

[Getting started](intro/)

 [Back to Top](#top)

## Additional Information

### Support Django!

![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)

* [Salsotto donated to the Django Software Foundation to support Django development. Donate today!](https://www.djangoproject.com/fundraising/)

### Browse

* Prev: [Django documentation contents](contents/)
* Next: [Getting started](intro/)
* [Table of contents](https://docs.djangoproject.com/en/6.0/contents/)
* [General Index](https://docs.djangoproject.com/en/6.0/genindex/)
* [Python Module Index](https://docs.djangoproject.com/en/6.0/py-modindex/)


### You are here:

* [Django 6.0 documentation](https://docs.djangoproject.com/en/6.0/)
  + Django documentation

### Getting help

[FAQ](https://docs.djangoproject.com/en/6.0/faq/)
:   Try the FAQ — it's got answers to many common questions.

[Index](https://docs.djangoproject.com/en/stable/genindex/), [Module Index](https://docs.djangoproject.com/en/stable/py-modindex/), or [Table of Contents](https://docs.djangoproject.com/en/stable/contents/)
:   Handy when looking for specific information.

[Django Discord Server](https://chat.djangoproject.com)
:   Join the Django Discord Community.

[Official Django Forum](https://forum.djangoproject.com/)
:   Join the community on the Django Forum.

[Ticket tracker](https://code.djangoproject.com/)
:   Report bugs with Django or Django documentation in our ticket tracker.

### Download:

Offline (Django 6.0):
[HTML](https://media.djangoproject.com/docs/django-docs-6.0-en.zip) |
[PDF](https://media.readthedocs.org/pdf/django/6.0.x/django.pdf) |
[ePub](https://media.readthedocs.org/epub/django/6.0.x/django.epub)
  

Provided by [Read the Docs](https://readthedocs.org/).

### Diamond and Platinum Members

[![Sentry](https://media.djangoproject.com/cache/7a/f9/7af9c770dc49465739a82c91a0eb3d51.png)](https://sentry.io/for/django/ "Sentry")

* **Sentry**
* [Monitor your Django Code
  Resolve performance bottlenecks and errors using monitoring, replays, logs and Seer an AI agent for debugging.](https://sentry.io/for/django/ "Sentry")

[![JetBrains](https://media.djangoproject.com/cache/c0/ea/c0ea128467983e64aab91cd27e7918c0.png)](https://jb.gg/ybja10 "JetBrains")

* **JetBrains**
* [JetBrains delivers intelligent software solutions that make developers more productive by simplifying their challenging tasks, automating the routine, and helping them adopt the best development practices. PyCharm is the Python IDE for Professional Developers by JetBrains providing a complete set of tools for productive Python, Web and scientific development.](https://jb.gg/ybja10 "JetBrains")









## Django Links

### Learn More

* [About Django](https://www.djangoproject.com/start/overview/)
* [Getting Started with Django](https://www.djangoproject.com/start/)
* [Team Organization](https://www.djangoproject.com/foundation/teams/)
* [Django Software Foundation](https://www.djangoproject.com/foundation/)
* [Code of Conduct](https://www.djangoproject.com/conduct/)
* [Diversity Statement](https://www.djangoproject.com/diversity/)

### Get Involved

* [Join a Group](https://www.djangoproject.com/community/)
* [Contribute
  to Django](https://docs.djangoproject.com/en/dev/internals/contributing/)
* [Submit
  a Bug](https://docs.djangoproject.com/en/dev/internals/contributing/bugs-and-features/)
* [Report
  a Security Issue](https://docs.djangoproject.com/en/dev/internals/security/#reporting-security-issues)
* [Individual membership](https://www.djangoproject.com/foundation/individual-members/)

### Get Help

* [Getting Help FAQ](https://docs.djangoproject.com/en/stable/faq/)
* [Django Discord](https://chat.djangoproject.com)
* [Official Django Forum](https://forum.djangoproject.com/)

### Follow Us

* [GitHub](https://github.com/django)
* [X](https://x.com/djangoproject)
* [Fediverse (Mastodon)](https://fosstodon.org/@django)
* [Bluesky](https://bsky.app/profile/djangoproject.com)
* [LinkedIn](https://www.linkedin.com/company/django-software-foundation)
* [News RSS](https://www.djangoproject.com/rss/weblog/)

### Support Us

* [Sponsor Django](https://www.djangoproject.com/fundraising/)
* [Corporate membership](https://www.djangoproject.com/foundation/corporate-members/)
* [Official merchandise store](https://django.threadless.com/)
* [Benevity Workplace Giving Program](https://www.djangoproject.com/fundraising/#benevity-giving)

[Django](https://www.djangoproject.com/)

* Hosting by [In-kind
  donors](https://www.djangoproject.com/fundraising/#in-kind-donors)
* Design by [Threespot](https://www.threespot.com)
  & [andrevv](http://andrevv.com/)

© 2005-2025
 [Django Software
Foundation](https://www.djangoproject.com/foundation/) and individual contributors. Django is a
[registered
trademark](https://www.djangoproject.com/trademarks/) of the Django Software Foundation.

---

## Source: en_6.0_faq_help.md

FAQ: Getting Help | Django documentation | Django


[Skip to main content](#main-content)


[Django](https://www.djangoproject.com/)

The web framework for perfectionists with deadlines.

Search




Submit

Toggle theme (current theme: auto)

Toggle theme (current theme: light)

Toggle theme (current theme: dark)

Toggle Light / Dark / Auto color theme

Menu

Main navigation

* [Overview](https://www.djangoproject.com/start/overview/)
* [Download](https://www.djangoproject.com/download/)
* [Documentation](https://docs.djangoproject.com/)
* [News](https://www.djangoproject.com/weblog/)
* [Code](https://github.com/django/django)
* [Issues](https://code.djangoproject.com/)
* [Community](https://www.djangoproject.com/community/)
* [Foundation](https://www.djangoproject.com/foundation/)
* [♥ Donate](https://www.djangoproject.com/fundraising/)
* Search




  Submit
* Toggle theme (current theme: auto)

  Toggle theme (current theme: light)

  Toggle theme (current theme: dark)

  Toggle Light / Dark / Auto color theme

[Documentation](https://docs.djangoproject.com/en/6.0/)

Help us reach our 2025 fundraising goal!

Donate to the *Django Software Foundation* to fund Django's development, security, and community events!  
If you got value out of using Django this year, please consider making a donation ♥
[Donate today](https://www.djangoproject.com/fundraising/)

* [Getting Help](https://docs.djangoproject.com/en/6.0/faq/help/)

* Language: **en**
* [el](https://docs.djangoproject.com/el/6.0/faq/help/)
* [es](https://docs.djangoproject.com/es/6.0/faq/help/)
* [fr](https://docs.djangoproject.com/fr/6.0/faq/help/)
* [id](https://docs.djangoproject.com/id/6.0/faq/help/)
* [it](https://docs.djangoproject.com/it/6.0/faq/help/)
* [ja](https://docs.djangoproject.com/ja/6.0/faq/help/)
* [ko](https://docs.djangoproject.com/ko/6.0/faq/help/)
* [pl](https://docs.djangoproject.com/pl/6.0/faq/help/)
* [pt-br](https://docs.djangoproject.com/pt-br/6.0/faq/help/)
* [sv](https://docs.djangoproject.com/sv/6.0/faq/help/)
* [zh-hans](https://docs.djangoproject.com/zh-hans/6.0/faq/help/)

* Documentation version:
  **6.0**
* [1.8](https://docs.djangoproject.com/en/1.8/faq/help/)
* [1.10](https://docs.djangoproject.com/en/1.10/faq/help/)
* [1.11](https://docs.djangoproject.com/en/1.11/faq/help/)
* [2.0](https://docs.djangoproject.com/en/2.0/faq/help/)
* [2.1](https://docs.djangoproject.com/en/2.1/faq/help/)
* [2.2](https://docs.djangoproject.com/en/2.2/faq/help/)
* [3.0](https://docs.djangoproject.com/en/3.0/faq/help/)
* [3.1](https://docs.djangoproject.com/en/3.1/faq/help/)
* [3.2](https://docs.djangoproject.com/en/3.2/faq/help/)
* [4.0](https://docs.djangoproject.com/en/4.0/faq/help/)
* [4.1](https://docs.djangoproject.com/en/4.1/faq/help/)
* [4.2](https://docs.djangoproject.com/en/4.2/faq/help/)
* [5.0](https://docs.djangoproject.com/en/5.0/faq/help/)
* [5.1](https://docs.djangoproject.com/en/5.1/faq/help/)
* [5.2](https://docs.djangoproject.com/en/5.2/faq/help/)
* [dev](https://docs.djangoproject.com/en/dev/faq/help/)

# FAQ: Getting Help[¶](#faq-getting-help "Link to this heading")

## How do I do X? Why doesn’t Y work? Where can I go to get help?[¶](#how-do-i-do-x-why-doesn-t-y-work-where-can-i-go-to-get-help "Link to this heading")

First, please check if your question is answered on the [FAQ](../). Also, search for answers using your favorite search engine, and
in [the forum](https://forum.djangoproject.com/).

If you can’t find an answer, please take a few minutes to formulate your
question well. Explaining the problems you are facing clearly will help others
help you. See the StackOverflow guide on [asking good questions](https://stackoverflow.com/help/how-to-ask).

Then, please post it in one of the following channels:

* The Django Forum section [“Using Django”](https://forum.djangoproject.com/c/users/6). This is for web-based
  discussions.
* The [Django Discord server](https://chat.djangoproject.com) for chat-based discussions.

In all these channels please abide by the [Django Code of Conduct](https://www.djangoproject.com/conduct/). In
summary, being friendly and patient, considerate, respectful, and careful in
your choice of words.

## Nobody answered my question! What should I do?[¶](#nobody-answered-my-question-what-should-i-do "Link to this heading")

Try making your question more specific, or provide a better example of your
problem.

As with most open-source projects, the folks on these channels are volunteers.
If nobody has answered your question, it may be because nobody knows the
answer, it may be because nobody can understand the question, or it may be that
everybody that can help is busy.

You can also try asking on a different channel. But please don’t post your
question in all three channels in quick succession.

## I think I’ve found a bug! What should I do?[¶](#i-think-i-ve-found-a-bug-what-should-i-do "Link to this heading")

Detailed instructions on how to handle a potential bug can be found in our
[Guide to contributing to Django](../../internals/contributing/bugs-and-features/#reporting-bugs).

## I think I’ve found a security problem! What should I do?[¶](#i-think-i-ve-found-a-security-problem-what-should-i-do "Link to this heading")

If you think you’ve found a security problem with Django, please send a message
to `security@djangoproject.com`. This is a private list only open to
long-time, highly trusted Django developers, and its archives are not publicly
readable.

Due to the sensitive nature of security issues, we ask that if you think you
have found a security problem, *please* don’t post a message on the forum, the
Discord server, IRC, or one of the public mailing lists. Django has a
[policy for handling security issues](../../internals/security/#reporting-security-issues);
while a defect is outstanding, we would like to minimize any damage that
could be inflicted through public knowledge of that defect.

Previous page and next page

[FAQ: Using Django](../usage/)

[FAQ: Databases and models](../models/)

 [Back to Top](#top)

## Additional Information

### Support Django!

![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)

* [Enix Yu donated to the Django Software Foundation to support Django development. Donate today!](https://www.djangoproject.com/fundraising/)

### Contents

* [FAQ: Getting Help](#)
  + [How do I do X? Why doesn’t Y work? Where can I go to get help?](#how-do-i-do-x-why-doesn-t-y-work-where-can-i-go-to-get-help)
  + [Nobody answered my question! What should I do?](#nobody-answered-my-question-what-should-i-do)
  + [I think I’ve found a bug! What should I do?](#i-think-i-ve-found-a-bug-what-should-i-do)
  + [I think I’ve found a security problem! What should I do?](#i-think-i-ve-found-a-security-problem-what-should-i-do)

### Browse

* Prev: [FAQ: Using Django](../usage/)
* Next: [FAQ: Databases and models](../models/)
* [Table of contents](https://docs.djangoproject.com/en/6.0/contents/)
* [General Index](https://docs.djangoproject.com/en/6.0/genindex/)
* [Python Module Index](https://docs.djangoproject.com/en/6.0/py-modindex/)


### You are here:

* [Django 6.0 documentation](https://docs.djangoproject.com/en/6.0/)
  + [Django FAQ](../)
    - FAQ: Getting Help

### Getting help

[FAQ](https://docs.djangoproject.com/en/6.0/faq/)
:   Try the FAQ — it's got answers to many common questions.

[Index](https://docs.djangoproject.com/en/stable/genindex/), [Module Index](https://docs.djangoproject.com/en/stable/py-modindex/), or [Table of Contents](https://docs.djangoproject.com/en/stable/contents/)
:   Handy when looking for specific information.

[Django Discord Server](https://chat.djangoproject.com)
:   Join the Django Discord Community.

[Official Django Forum](https://forum.djangoproject.com/)
:   Join the community on the Django Forum.

[Ticket tracker](https://code.djangoproject.com/)
:   Report bugs with Django or Django documentation in our ticket tracker.

### Download:

Offline (Django 6.0):
[HTML](https://media.djangoproject.com/docs/django-docs-6.0-en.zip) |
[PDF](https://media.readthedocs.org/pdf/django/6.0.x/django.pdf) |
[ePub](https://media.readthedocs.org/epub/django/6.0.x/django.epub)
  

Provided by [Read the Docs](https://readthedocs.org/).

### Diamond and Platinum Members

[![Sentry](https://media.djangoproject.com/cache/7a/f9/7af9c770dc49465739a82c91a0eb3d51.png)](https://sentry.io/for/django/ "Sentry")

* **Sentry**
* [Monitor your Django Code
  Resolve performance bottlenecks and errors using monitoring, replays, logs and Seer an AI agent for debugging.](https://sentry.io/for/django/ "Sentry")

[![JetBrains](https://media.djangoproject.com/cache/c0/ea/c0ea128467983e64aab91cd27e7918c0.png)](https://jb.gg/ybja10 "JetBrains")

* **JetBrains**
* [JetBrains delivers intelligent software solutions that make developers more productive by simplifying their challenging tasks, automating the routine, and helping them adopt the best development practices. PyCharm is the Python IDE for Professional Developers by JetBrains providing a complete set of tools for productive Python, Web and scientific development.](https://jb.gg/ybja10 "JetBrains")









## Django Links

### Learn More

* [About Django](https://www.djangoproject.com/start/overview/)
* [Getting Started with Django](https://www.djangoproject.com/start/)
* [Team Organization](https://www.djangoproject.com/foundation/teams/)
* [Django Software Foundation](https://www.djangoproject.com/foundation/)
* [Code of Conduct](https://www.djangoproject.com/conduct/)
* [Diversity Statement](https://www.djangoproject.com/diversity/)

### Get Involved

* [Join a Group](https://www.djangoproject.com/community/)
* [Contribute
  to Django](https://docs.djangoproject.com/en/dev/internals/contributing/)
* [Submit
  a Bug](https://docs.djangoproject.com/en/dev/internals/contributing/bugs-and-features/)
* [Report
  a Security Issue](https://docs.djangoproject.com/en/dev/internals/security/#reporting-security-issues)
* [Individual membership](https://www.djangoproject.com/foundation/individual-members/)

### Get Help

* [Getting Help FAQ](https://docs.djangoproject.com/en/stable/faq/)
* [Django Discord](https://chat.djangoproject.com)
* [Official Django Forum](https://forum.djangoproject.com/)

### Follow Us

* [GitHub](https://github.com/django)
* [X](https://x.com/djangoproject)
* [Fediverse (Mastodon)](https://fosstodon.org/@django)
* [Bluesky](https://bsky.app/profile/djangoproject.com)
* [LinkedIn](https://www.linkedin.com/company/django-software-foundation)
* [News RSS](https://www.djangoproject.com/rss/weblog/)

### Support Us

* [Sponsor Django](https://www.djangoproject.com/fundraising/)
* [Corporate membership](https://www.djangoproject.com/foundation/corporate-members/)
* [Official merchandise store](https://django.threadless.com/)
* [Benevity Workplace Giving Program](https://www.djangoproject.com/fundraising/#benevity-giving)

[Django](https://www.djangoproject.com/)

* Hosting by [In-kind
  donors](https://www.djangoproject.com/fundraising/#in-kind-donors)
* Design by [Threespot](https://www.threespot.com)
  & [andrevv](http://andrevv.com/)

© 2005-2025
 [Django Software
Foundation](https://www.djangoproject.com/foundation/) and individual contributors. Django is a
[registered
trademark](https://www.djangoproject.com/trademarks/) of the Django Software Foundation.

---

## Source: en_stable.md

Django documentation | Django documentation | Django


[Skip to main content](#main-content)


[Django](https://www.djangoproject.com/)

The web framework for perfectionists with deadlines.

Search




Submit

Toggle theme (current theme: auto)

Toggle theme (current theme: light)

Toggle theme (current theme: dark)

Toggle Light / Dark / Auto color theme

Menu

Main navigation

* [Overview](https://www.djangoproject.com/start/overview/)
* [Download](https://www.djangoproject.com/download/)
* [Documentation](https://docs.djangoproject.com/)
* [News](https://www.djangoproject.com/weblog/)
* [Code](https://github.com/django/django)
* [Issues](https://code.djangoproject.com/)
* [Community](https://www.djangoproject.com/community/)
* [Foundation](https://www.djangoproject.com/foundation/)
* [♥ Donate](https://www.djangoproject.com/fundraising/)
* Search




  Submit
* Toggle theme (current theme: auto)

  Toggle theme (current theme: light)

  Toggle theme (current theme: dark)

  Toggle Light / Dark / Auto color theme

[Documentation](https://docs.djangoproject.com/en/6.0/)

Help us reach our 2025 fundraising goal!

Donate to the *Django Software Foundation* to fund Django's development, security, and community events!  
If you got value out of using Django this year, please consider making a donation ♥
[Donate today](https://www.djangoproject.com/fundraising/)

* [Getting Help](https://docs.djangoproject.com/en/6.0/faq/help/)

* Language: **en**
* [el](https://docs.djangoproject.com/el/6.0/)
* [es](https://docs.djangoproject.com/es/6.0/)
* [fr](https://docs.djangoproject.com/fr/6.0/)
* [id](https://docs.djangoproject.com/id/6.0/)
* [it](https://docs.djangoproject.com/it/6.0/)
* [ja](https://docs.djangoproject.com/ja/6.0/)
* [ko](https://docs.djangoproject.com/ko/6.0/)
* [pl](https://docs.djangoproject.com/pl/6.0/)
* [pt-br](https://docs.djangoproject.com/pt-br/6.0/)
* [sv](https://docs.djangoproject.com/sv/6.0/)
* [zh-hans](https://docs.djangoproject.com/zh-hans/6.0/)

* Documentation version:
  **6.0**
* [1.8](https://docs.djangoproject.com/en/1.8/)
* [1.10](https://docs.djangoproject.com/en/1.10/)
* [1.11](https://docs.djangoproject.com/en/1.11/)
* [2.0](https://docs.djangoproject.com/en/2.0/)
* [2.1](https://docs.djangoproject.com/en/2.1/)
* [2.2](https://docs.djangoproject.com/en/2.2/)
* [3.0](https://docs.djangoproject.com/en/3.0/)
* [3.1](https://docs.djangoproject.com/en/3.1/)
* [3.2](https://docs.djangoproject.com/en/3.2/)
* [4.0](https://docs.djangoproject.com/en/4.0/)
* [4.1](https://docs.djangoproject.com/en/4.1/)
* [4.2](https://docs.djangoproject.com/en/4.2/)
* [5.0](https://docs.djangoproject.com/en/5.0/)
* [5.1](https://docs.djangoproject.com/en/5.1/)
* [5.2](https://docs.djangoproject.com/en/5.2/)
* [dev](https://docs.djangoproject.com/en/dev/)

# Django documentation[¶](#django-documentation "Link to this heading")

Everything you need to know about Django.

## First steps[¶](#first-steps "Link to this heading")

Are you new to Django or to programming? This is the place to start!

* **From scratch:**
  [Overview](intro/overview/) |
  [Installation](intro/install/)
* **Tutorial:**
  [Part 1: Requests and responses](intro/tutorial01/) |
  [Part 2: Models and the admin site](intro/tutorial02/) |
  [Part 3: Views and templates](intro/tutorial03/) |
  [Part 4: Forms and generic views](intro/tutorial04/) |
  [Part 5: Testing](intro/tutorial05/) |
  [Part 6: Static files](intro/tutorial06/) |
  [Part 7: Customizing the admin site](intro/tutorial07/) |
  [Part 8: Adding third-party packages](intro/tutorial08/)
* **Advanced Tutorials:**
  [How to write reusable apps](intro/reusable-apps/) |
  [Writing your first contribution to Django](intro/contributing/)

## Getting help[¶](#getting-help "Link to this heading")

Having trouble? We’d like to help!

* Try the [FAQ](faq/) – it’s got answers to many common questions.
* Looking for specific information? Try the [Index](genindex/), [Module Index](py-modindex/) or
  the [detailed table of contents](contents/).
* Not found anything? See [FAQ: Getting Help](faq/help/) for information on getting support
  and asking questions to the community.
* Report bugs with Django in our [ticket tracker](https://code.djangoproject.com/).

## How the documentation is organized[¶](#how-the-documentation-is-organized "Link to this heading")

Django has a lot of documentation. A high-level overview of how it’s organized
will help you know where to look for certain things:

* [Tutorials](intro/) take you by the hand through a series of
  steps to create a web application. Start here if you’re new to Django or web
  application development. Also look at the “[First steps](#index-first-steps)”.
* [Topic guides](topics/) discuss key topics and concepts at a
  fairly high level and provide useful background information and explanation.
* [Reference guides](ref/) contain technical reference for APIs and
  other aspects of Django’s machinery. They describe how it works and how to
  use it but assume that you have a basic understanding of key concepts.
* [How-to guides](howto/) are recipes. They guide you through the
  steps involved in addressing key problems and use-cases. They are more
  advanced than tutorials and assume some knowledge of how Django works.

## The model layer[¶](#the-model-layer "Link to this heading")

Django provides an abstraction layer (the “models”) for structuring and
manipulating the data of your web application. Learn more about it below:

* **Models:**
  [Introduction to models](topics/db/models/) |
  [Field types](ref/models/fields/) |
  [Indexes](ref/models/indexes/) |
  [Meta options](ref/models/options/) |
  [Model class](ref/models/class/)
* **QuerySets:**
  [Making queries](topics/db/queries/) |
  [QuerySet method reference](ref/models/querysets/) |
  [Lookup expressions](ref/models/lookups/)
* **Model instances:**
  [Instance methods](ref/models/instances/) |
  [Accessing related objects](ref/models/relations/)
* **Migrations:**
  [Introduction to Migrations](topics/migrations/) |
  [Operations reference](ref/migration-operations/) |
  [SchemaEditor](ref/schema-editor/) |
  [Writing migrations](howto/writing-migrations/)
* **Advanced:**
  [Managers](topics/db/managers/) |
  [Raw SQL](topics/db/sql/) |
  [Transactions](topics/db/transactions/) |
  [Aggregation](topics/db/aggregation/) |
  [Search](topics/db/search/) |
  [Custom fields](howto/custom-model-fields/) |
  [Multiple databases](topics/db/multi-db/) |
  [Custom lookups](howto/custom-lookups/) |
  [Query Expressions](ref/models/expressions/) |
  [Conditional Expressions](ref/models/conditional-expressions/) |
  [Database Functions](ref/models/database-functions/)
* **Other:**
  [Supported databases](ref/databases/) |
  [Legacy databases](howto/legacy-databases/) |
  [Providing initial data](howto/initial-data/) |
  [Optimize database access](topics/db/optimization/) |
  [PostgreSQL specific features](ref/contrib/postgres/)

## The view layer[¶](#the-view-layer "Link to this heading")

Django has the concept of “views” to encapsulate the logic responsible for
processing a user’s request and for returning the response. Find all you need
to know about views via the links below:

* **The basics:**
  [URLconfs](topics/http/urls/) |
  [View functions](topics/http/views/) |
  [Shortcuts](topics/http/shortcuts/) |
  [Decorators](topics/http/decorators/) |
  [Asynchronous Support](topics/async/)
* **Reference:**
  [Built-in Views](ref/views/) |
  [Request/response objects](ref/request-response/) |
  [TemplateResponse objects](ref/template-response/)
* **File uploads:**
  [Overview](topics/http/file-uploads/) |
  [File objects](ref/files/file/) |
  [Storage API](ref/files/storage/) |
  [Managing files](topics/files/) |
  [Custom storage](howto/custom-file-storage/)
* **Class-based views:**
  [Overview](topics/class-based-views/) |
  [Built-in display views](topics/class-based-views/generic-display/) |
  [Built-in editing views](topics/class-based-views/generic-editing/) |
  [Using mixins](topics/class-based-views/mixins/) |
  [API reference](ref/class-based-views/) |
  [Flattened index](ref/class-based-views/flattened-index/)
* **Advanced:**
  [Generating CSV](howto/outputting-csv/) |
  [Generating PDF](howto/outputting-pdf/)
* **Middleware:**
  [Overview](topics/http/middleware/) |
  [Built-in middleware classes](ref/middleware/)

## The template layer[¶](#the-template-layer "Link to this heading")

The template layer provides a designer-friendly syntax for rendering the
information to be presented to the user. Learn how this syntax can be used by
designers and how it can be extended by programmers:

* **The basics:**
  [Overview](topics/templates/)
* **For designers:**
  [Language overview](ref/templates/language/) |
  [Built-in tags and filters](ref/templates/builtins/) |
  [Humanization](ref/contrib/humanize/)
* **For programmers:**
  [Template API](ref/templates/api/) |
  [Custom tags and filters](howto/custom-template-tags/) |
  [Custom template backend](howto/custom-template-backend/)

## Forms[¶](#forms "Link to this heading")

Django provides a rich framework to facilitate the creation of forms and the
manipulation of form data.

* **The basics:**
  [Overview](topics/forms/) |
  [Form API](ref/forms/api/) |
  [Built-in fields](ref/forms/fields/) |
  [Built-in widgets](ref/forms/widgets/)
* **Advanced:**
  [Forms for models](topics/forms/modelforms/) |
  [Integrating media](topics/forms/media/) |
  [Formsets](topics/forms/formsets/) |
  [Customizing validation](ref/forms/validation/)

## The development process[¶](#the-development-process "Link to this heading")

Learn about the various components and tools to help you in the development and
testing of Django applications:

* **Settings:**
  [Overview](topics/settings/) |
  [Full list of settings](ref/settings/)
* **Applications:**
  [Overview](ref/applications/)
* **Exceptions:**
  [Overview](ref/exceptions/)
* **django-admin and manage.py:**
  [Overview](ref/django-admin/) |
  [Adding custom commands](howto/custom-management-commands/)
* **Testing:**
  [Introduction](topics/testing/) |
  [Writing and running tests](topics/testing/overview/) |
  [Included testing tools](topics/testing/tools/) |
  [Advanced topics](topics/testing/advanced/)
* **Deployment:**
  [Overview](howto/deployment/) |
  [WSGI servers](howto/deployment/wsgi/) |
  [ASGI servers](howto/deployment/asgi/) |
  [Deploying static files](howto/static-files/deployment/) |
  [Tracking code errors by email](howto/error-reporting/) |
  [Deployment checklist](howto/deployment/checklist/)

## The admin[¶](#the-admin "Link to this heading")

Find all you need to know about the automated admin interface, one of Django’s
most popular features:

* [Admin site](ref/contrib/admin/)
* [Admin actions](ref/contrib/admin/actions/)
* [Admin documentation generator](ref/contrib/admin/admindocs/)

## Security[¶](#security "Link to this heading")

Security is a topic of paramount importance in the development of web
applications and Django provides multiple protection tools and mechanisms:

* [Security overview](topics/security/)
* [Disclosed security issues in Django](releases/security/)
* [Clickjacking protection](ref/clickjacking/)
* [Cross Site Request Forgery protection](ref/csrf/)
* [Cryptographic signing](topics/signing/)
* [Security Middleware](ref/middleware/#security-middleware)
* [Content Security Policy](ref/csp/)

## Internationalization and localization[¶](#internationalization-and-localization "Link to this heading")

Django offers a robust internationalization and localization framework to
assist you in the development of applications for multiple languages and world
regions:

* [Overview](topics/i18n/) |
  [Internationalization](topics/i18n/translation/) |
  [Localization](topics/i18n/translation/#how-to-create-language-files) |
  [Localized web UI formatting and form input](topics/i18n/formatting/)
* [Time zones](topics/i18n/timezones/)

## Performance and optimization[¶](#performance-and-optimization "Link to this heading")

There are a variety of techniques and tools that can help get your code running
more efficiently - faster, and using fewer system resources.

* [Performance and optimization overview](topics/performance/)

## Geographic framework[¶](#geographic-framework "Link to this heading")

[GeoDjango](ref/contrib/gis/) intends to be a world-class
geographic web framework. Its goal is to make it as easy as possible to build
GIS web applications and harness the power of spatially enabled data.

## Common web application tools[¶](#common-web-application-tools "Link to this heading")

Django offers multiple tools commonly needed in the development of web
applications:

* **Authentication:**
  [Overview](topics/auth/) |
  [Using the authentication system](topics/auth/default/) |
  [Password management](topics/auth/passwords/) |
  [Customizing authentication](topics/auth/customizing/) |
  [API Reference](ref/contrib/auth/)
* [Caching](topics/cache/)
* [Logging](topics/logging/)
* [Tasks framework](topics/tasks/)
* [Sending emails](topics/email/)
* [Syndication feeds (RSS/Atom)](ref/contrib/syndication/)
* [Pagination](topics/pagination/)
* [Messages framework](ref/contrib/messages/)
* [Serialization](topics/serialization/)
* [Sessions](topics/http/sessions/)
* [Sitemaps](ref/contrib/sitemaps/)
* [Static files management](ref/contrib/staticfiles/)
* [Data validation](ref/validators/)

## Other core functionalities[¶](#other-core-functionalities "Link to this heading")

Learn about some other core functionalities of the Django framework:

* [Conditional content processing](topics/conditional-view-processing/)
* [Content types and generic relations](ref/contrib/contenttypes/)
* [Flatpages](ref/contrib/flatpages/)
* [Redirects](ref/contrib/redirects/)
* [Signals](topics/signals/)
* [System check framework](topics/checks/)
* [The sites framework](ref/contrib/sites/)
* [Unicode in Django](ref/unicode/)

## The Django open-source project[¶](#the-django-open-source-project "Link to this heading")

Learn about the development process for the Django project itself and about how
you can contribute:

* **Community:**
  [Contributing to Django](internals/contributing/) |
  [The release process](internals/release-process/) |
  [Team organization](internals/organization/) |
  [The Django source code repository](internals/git/) |
  [Security policies](internals/security/) |
  [Mailing lists and Forum](internals/mailing-lists/)
* **Design philosophies:**
  [Overview](misc/design-philosophies/)
* **Documentation:**
  [About this documentation](internals/contributing/writing-documentation/)
* **Third-party distributions:**
  [Overview](misc/distributions/)
* **Django over time:**
  [API stability](misc/api-stability/) |
  [Release notes and upgrading instructions](releases/) |
  [Deprecation Timeline](internals/deprecation/)

Previous page and next page

[Django documentation contents](contents/)

[Getting started](intro/)

 [Back to Top](#top)

## Additional Information

### Support Django!

![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)

* [Salsotto donated to the Django Software Foundation to support Django development. Donate today!](https://www.djangoproject.com/fundraising/)

### Browse

* Prev: [Django documentation contents](contents/)
* Next: [Getting started](intro/)
* [Table of contents](https://docs.djangoproject.com/en/6.0/contents/)
* [General Index](https://docs.djangoproject.com/en/6.0/genindex/)
* [Python Module Index](https://docs.djangoproject.com/en/6.0/py-modindex/)


### You are here:

* [Django 6.0 documentation](https://docs.djangoproject.com/en/6.0/)
  + Django documentation

### Getting help

[FAQ](https://docs.djangoproject.com/en/6.0/faq/)
:   Try the FAQ — it's got answers to many common questions.

[Index](https://docs.djangoproject.com/en/stable/genindex/), [Module Index](https://docs.djangoproject.com/en/stable/py-modindex/), or [Table of Contents](https://docs.djangoproject.com/en/stable/contents/)
:   Handy when looking for specific information.

[Django Discord Server](https://chat.djangoproject.com)
:   Join the Django Discord Community.

[Official Django Forum](https://forum.djangoproject.com/)
:   Join the community on the Django Forum.

[Ticket tracker](https://code.djangoproject.com/)
:   Report bugs with Django or Django documentation in our ticket tracker.

### Download:

Offline (Django 6.0):
[HTML](https://media.djangoproject.com/docs/django-docs-6.0-en.zip) |
[PDF](https://media.readthedocs.org/pdf/django/6.0.x/django.pdf) |
[ePub](https://media.readthedocs.org/epub/django/6.0.x/django.epub)
  

Provided by [Read the Docs](https://readthedocs.org/).

### Diamond and Platinum Members

[![Sentry](https://media.djangoproject.com/cache/7a/f9/7af9c770dc49465739a82c91a0eb3d51.png)](https://sentry.io/for/django/ "Sentry")

* **Sentry**
* [Monitor your Django Code
  Resolve performance bottlenecks and errors using monitoring, replays, logs and Seer an AI agent for debugging.](https://sentry.io/for/django/ "Sentry")

[![JetBrains](https://media.djangoproject.com/cache/c0/ea/c0ea128467983e64aab91cd27e7918c0.png)](https://jb.gg/ybja10 "JetBrains")

* **JetBrains**
* [JetBrains delivers intelligent software solutions that make developers more productive by simplifying their challenging tasks, automating the routine, and helping them adopt the best development practices. PyCharm is the Python IDE for Professional Developers by JetBrains providing a complete set of tools for productive Python, Web and scientific development.](https://jb.gg/ybja10 "JetBrains")









## Django Links

### Learn More

* [About Django](https://www.djangoproject.com/start/overview/)
* [Getting Started with Django](https://www.djangoproject.com/start/)
* [Team Organization](https://www.djangoproject.com/foundation/teams/)
* [Django Software Foundation](https://www.djangoproject.com/foundation/)
* [Code of Conduct](https://www.djangoproject.com/conduct/)
* [Diversity Statement](https://www.djangoproject.com/diversity/)

### Get Involved

* [Join a Group](https://www.djangoproject.com/community/)
* [Contribute
  to Django](https://docs.djangoproject.com/en/dev/internals/contributing/)
* [Submit
  a Bug](https://docs.djangoproject.com/en/dev/internals/contributing/bugs-and-features/)
* [Report
  a Security Issue](https://docs.djangoproject.com/en/dev/internals/security/#reporting-security-issues)
* [Individual membership](https://www.djangoproject.com/foundation/individual-members/)

### Get Help

* [Getting Help FAQ](https://docs.djangoproject.com/en/stable/faq/)
* [Django Discord](https://chat.djangoproject.com)
* [Official Django Forum](https://forum.djangoproject.com/)

### Follow Us

* [GitHub](https://github.com/django)
* [X](https://x.com/djangoproject)
* [Fediverse (Mastodon)](https://fosstodon.org/@django)
* [Bluesky](https://bsky.app/profile/djangoproject.com)
* [LinkedIn](https://www.linkedin.com/company/django-software-foundation)
* [News RSS](https://www.djangoproject.com/rss/weblog/)

### Support Us

* [Sponsor Django](https://www.djangoproject.com/fundraising/)
* [Corporate membership](https://www.djangoproject.com/foundation/corporate-members/)
* [Official merchandise store](https://django.threadless.com/)
* [Benevity Workplace Giving Program](https://www.djangoproject.com/fundraising/#benevity-giving)

[Django](https://www.djangoproject.com/)

* Hosting by [In-kind
  donors](https://www.djangoproject.com/fundraising/#in-kind-donors)
* Design by [Threespot](https://www.threespot.com)
  & [andrevv](http://andrevv.com/)

© 2005-2025
 [Django Software
Foundation](https://www.djangoproject.com/foundation/) and individual contributors. Django is a
[registered
trademark](https://www.djangoproject.com/trademarks/) of the Django Software Foundation.

---

## Source: index.md

Django documentation | Django documentation | Django


[Skip to main content](#main-content)


[Django](https://www.djangoproject.com/)

The web framework for perfectionists with deadlines.

Search




Submit

Toggle theme (current theme: auto)

Toggle theme (current theme: light)

Toggle theme (current theme: dark)

Toggle Light / Dark / Auto color theme

Menu

Main navigation

* [Overview](https://www.djangoproject.com/start/overview/)
* [Download](https://www.djangoproject.com/download/)
* [Documentation](https://docs.djangoproject.com/)
* [News](https://www.djangoproject.com/weblog/)
* [Code](https://github.com/django/django)
* [Issues](https://code.djangoproject.com/)
* [Community](https://www.djangoproject.com/community/)
* [Foundation](https://www.djangoproject.com/foundation/)
* [♥ Donate](https://www.djangoproject.com/fundraising/)
* Search




  Submit
* Toggle theme (current theme: auto)

  Toggle theme (current theme: light)

  Toggle theme (current theme: dark)

  Toggle Light / Dark / Auto color theme

[Documentation](https://docs.djangoproject.com/en/6.0/)

Help us reach our 2025 fundraising goal!

Donate to the *Django Software Foundation* to fund Django's development, security, and community events!  
If you got value out of using Django this year, please consider making a donation ♥
[Donate today](https://www.djangoproject.com/fundraising/)

* [Getting Help](https://docs.djangoproject.com/en/6.0/faq/help/)

* Language: **en**
* [el](https://docs.djangoproject.com/el/6.0/)
* [es](https://docs.djangoproject.com/es/6.0/)
* [fr](https://docs.djangoproject.com/fr/6.0/)
* [id](https://docs.djangoproject.com/id/6.0/)
* [it](https://docs.djangoproject.com/it/6.0/)
* [ja](https://docs.djangoproject.com/ja/6.0/)
* [ko](https://docs.djangoproject.com/ko/6.0/)
* [pl](https://docs.djangoproject.com/pl/6.0/)
* [pt-br](https://docs.djangoproject.com/pt-br/6.0/)
* [sv](https://docs.djangoproject.com/sv/6.0/)
* [zh-hans](https://docs.djangoproject.com/zh-hans/6.0/)

* Documentation version:
  **6.0**
* [1.8](https://docs.djangoproject.com/en/1.8/)
* [1.10](https://docs.djangoproject.com/en/1.10/)
* [1.11](https://docs.djangoproject.com/en/1.11/)
* [2.0](https://docs.djangoproject.com/en/2.0/)
* [2.1](https://docs.djangoproject.com/en/2.1/)
* [2.2](https://docs.djangoproject.com/en/2.2/)
* [3.0](https://docs.djangoproject.com/en/3.0/)
* [3.1](https://docs.djangoproject.com/en/3.1/)
* [3.2](https://docs.djangoproject.com/en/3.2/)
* [4.0](https://docs.djangoproject.com/en/4.0/)
* [4.1](https://docs.djangoproject.com/en/4.1/)
* [4.2](https://docs.djangoproject.com/en/4.2/)
* [5.0](https://docs.djangoproject.com/en/5.0/)
* [5.1](https://docs.djangoproject.com/en/5.1/)
* [5.2](https://docs.djangoproject.com/en/5.2/)
* [dev](https://docs.djangoproject.com/en/dev/)

# Django documentation[¶](#django-documentation "Link to this heading")

Everything you need to know about Django.

## First steps[¶](#first-steps "Link to this heading")

Are you new to Django or to programming? This is the place to start!

* **From scratch:**
  [Overview](intro/overview/) |
  [Installation](intro/install/)
* **Tutorial:**
  [Part 1: Requests and responses](intro/tutorial01/) |
  [Part 2: Models and the admin site](intro/tutorial02/) |
  [Part 3: Views and templates](intro/tutorial03/) |
  [Part 4: Forms and generic views](intro/tutorial04/) |
  [Part 5: Testing](intro/tutorial05/) |
  [Part 6: Static files](intro/tutorial06/) |
  [Part 7: Customizing the admin site](intro/tutorial07/) |
  [Part 8: Adding third-party packages](intro/tutorial08/)
* **Advanced Tutorials:**
  [How to write reusable apps](intro/reusable-apps/) |
  [Writing your first contribution to Django](intro/contributing/)

## Getting help[¶](#getting-help "Link to this heading")

Having trouble? We’d like to help!

* Try the [FAQ](faq/) – it’s got answers to many common questions.
* Looking for specific information? Try the [Index](genindex/), [Module Index](py-modindex/) or
  the [detailed table of contents](contents/).
* Not found anything? See [FAQ: Getting Help](faq/help/) for information on getting support
  and asking questions to the community.
* Report bugs with Django in our [ticket tracker](https://code.djangoproject.com/).

## How the documentation is organized[¶](#how-the-documentation-is-organized "Link to this heading")

Django has a lot of documentation. A high-level overview of how it’s organized
will help you know where to look for certain things:

* [Tutorials](intro/) take you by the hand through a series of
  steps to create a web application. Start here if you’re new to Django or web
  application development. Also look at the “[First steps](#index-first-steps)”.
* [Topic guides](topics/) discuss key topics and concepts at a
  fairly high level and provide useful background information and explanation.
* [Reference guides](ref/) contain technical reference for APIs and
  other aspects of Django’s machinery. They describe how it works and how to
  use it but assume that you have a basic understanding of key concepts.
* [How-to guides](howto/) are recipes. They guide you through the
  steps involved in addressing key problems and use-cases. They are more
  advanced than tutorials and assume some knowledge of how Django works.

## The model layer[¶](#the-model-layer "Link to this heading")

Django provides an abstraction layer (the “models”) for structuring and
manipulating the data of your web application. Learn more about it below:

* **Models:**
  [Introduction to models](topics/db/models/) |
  [Field types](ref/models/fields/) |
  [Indexes](ref/models/indexes/) |
  [Meta options](ref/models/options/) |
  [Model class](ref/models/class/)
* **QuerySets:**
  [Making queries](topics/db/queries/) |
  [QuerySet method reference](ref/models/querysets/) |
  [Lookup expressions](ref/models/lookups/)
* **Model instances:**
  [Instance methods](ref/models/instances/) |
  [Accessing related objects](ref/models/relations/)
* **Migrations:**
  [Introduction to Migrations](topics/migrations/) |
  [Operations reference](ref/migration-operations/) |
  [SchemaEditor](ref/schema-editor/) |
  [Writing migrations](howto/writing-migrations/)
* **Advanced:**
  [Managers](topics/db/managers/) |
  [Raw SQL](topics/db/sql/) |
  [Transactions](topics/db/transactions/) |
  [Aggregation](topics/db/aggregation/) |
  [Search](topics/db/search/) |
  [Custom fields](howto/custom-model-fields/) |
  [Multiple databases](topics/db/multi-db/) |
  [Custom lookups](howto/custom-lookups/) |
  [Query Expressions](ref/models/expressions/) |
  [Conditional Expressions](ref/models/conditional-expressions/) |
  [Database Functions](ref/models/database-functions/)
* **Other:**
  [Supported databases](ref/databases/) |
  [Legacy databases](howto/legacy-databases/) |
  [Providing initial data](howto/initial-data/) |
  [Optimize database access](topics/db/optimization/) |
  [PostgreSQL specific features](ref/contrib/postgres/)

## The view layer[¶](#the-view-layer "Link to this heading")

Django has the concept of “views” to encapsulate the logic responsible for
processing a user’s request and for returning the response. Find all you need
to know about views via the links below:

* **The basics:**
  [URLconfs](topics/http/urls/) |
  [View functions](topics/http/views/) |
  [Shortcuts](topics/http/shortcuts/) |
  [Decorators](topics/http/decorators/) |
  [Asynchronous Support](topics/async/)
* **Reference:**
  [Built-in Views](ref/views/) |
  [Request/response objects](ref/request-response/) |
  [TemplateResponse objects](ref/template-response/)
* **File uploads:**
  [Overview](topics/http/file-uploads/) |
  [File objects](ref/files/file/) |
  [Storage API](ref/files/storage/) |
  [Managing files](topics/files/) |
  [Custom storage](howto/custom-file-storage/)
* **Class-based views:**
  [Overview](topics/class-based-views/) |
  [Built-in display views](topics/class-based-views/generic-display/) |
  [Built-in editing views](topics/class-based-views/generic-editing/) |
  [Using mixins](topics/class-based-views/mixins/) |
  [API reference](ref/class-based-views/) |
  [Flattened index](ref/class-based-views/flattened-index/)
* **Advanced:**
  [Generating CSV](howto/outputting-csv/) |
  [Generating PDF](howto/outputting-pdf/)
* **Middleware:**
  [Overview](topics/http/middleware/) |
  [Built-in middleware classes](ref/middleware/)

## The template layer[¶](#the-template-layer "Link to this heading")

The template layer provides a designer-friendly syntax for rendering the
information to be presented to the user. Learn how this syntax can be used by
designers and how it can be extended by programmers:

* **The basics:**
  [Overview](topics/templates/)
* **For designers:**
  [Language overview](ref/templates/language/) |
  [Built-in tags and filters](ref/templates/builtins/) |
  [Humanization](ref/contrib/humanize/)
* **For programmers:**
  [Template API](ref/templates/api/) |
  [Custom tags and filters](howto/custom-template-tags/) |
  [Custom template backend](howto/custom-template-backend/)

## Forms[¶](#forms "Link to this heading")

Django provides a rich framework to facilitate the creation of forms and the
manipulation of form data.

* **The basics:**
  [Overview](topics/forms/) |
  [Form API](ref/forms/api/) |
  [Built-in fields](ref/forms/fields/) |
  [Built-in widgets](ref/forms/widgets/)
* **Advanced:**
  [Forms for models](topics/forms/modelforms/) |
  [Integrating media](topics/forms/media/) |
  [Formsets](topics/forms/formsets/) |
  [Customizing validation](ref/forms/validation/)

## The development process[¶](#the-development-process "Link to this heading")

Learn about the various components and tools to help you in the development and
testing of Django applications:

* **Settings:**
  [Overview](topics/settings/) |
  [Full list of settings](ref/settings/)
* **Applications:**
  [Overview](ref/applications/)
* **Exceptions:**
  [Overview](ref/exceptions/)
* **django-admin and manage.py:**
  [Overview](ref/django-admin/) |
  [Adding custom commands](howto/custom-management-commands/)
* **Testing:**
  [Introduction](topics/testing/) |
  [Writing and running tests](topics/testing/overview/) |
  [Included testing tools](topics/testing/tools/) |
  [Advanced topics](topics/testing/advanced/)
* **Deployment:**
  [Overview](howto/deployment/) |
  [WSGI servers](howto/deployment/wsgi/) |
  [ASGI servers](howto/deployment/asgi/) |
  [Deploying static files](howto/static-files/deployment/) |
  [Tracking code errors by email](howto/error-reporting/) |
  [Deployment checklist](howto/deployment/checklist/)

## The admin[¶](#the-admin "Link to this heading")

Find all you need to know about the automated admin interface, one of Django’s
most popular features:

* [Admin site](ref/contrib/admin/)
* [Admin actions](ref/contrib/admin/actions/)
* [Admin documentation generator](ref/contrib/admin/admindocs/)

## Security[¶](#security "Link to this heading")

Security is a topic of paramount importance in the development of web
applications and Django provides multiple protection tools and mechanisms:

* [Security overview](topics/security/)
* [Disclosed security issues in Django](releases/security/)
* [Clickjacking protection](ref/clickjacking/)
* [Cross Site Request Forgery protection](ref/csrf/)
* [Cryptographic signing](topics/signing/)
* [Security Middleware](ref/middleware/#security-middleware)
* [Content Security Policy](ref/csp/)

## Internationalization and localization[¶](#internationalization-and-localization "Link to this heading")

Django offers a robust internationalization and localization framework to
assist you in the development of applications for multiple languages and world
regions:

* [Overview](topics/i18n/) |
  [Internationalization](topics/i18n/translation/) |
  [Localization](topics/i18n/translation/#how-to-create-language-files) |
  [Localized web UI formatting and form input](topics/i18n/formatting/)
* [Time zones](topics/i18n/timezones/)

## Performance and optimization[¶](#performance-and-optimization "Link to this heading")

There are a variety of techniques and tools that can help get your code running
more efficiently - faster, and using fewer system resources.

* [Performance and optimization overview](topics/performance/)

## Geographic framework[¶](#geographic-framework "Link to this heading")

[GeoDjango](ref/contrib/gis/) intends to be a world-class
geographic web framework. Its goal is to make it as easy as possible to build
GIS web applications and harness the power of spatially enabled data.

## Common web application tools[¶](#common-web-application-tools "Link to this heading")

Django offers multiple tools commonly needed in the development of web
applications:

* **Authentication:**
  [Overview](topics/auth/) |
  [Using the authentication system](topics/auth/default/) |
  [Password management](topics/auth/passwords/) |
  [Customizing authentication](topics/auth/customizing/) |
  [API Reference](ref/contrib/auth/)
* [Caching](topics/cache/)
* [Logging](topics/logging/)
* [Tasks framework](topics/tasks/)
* [Sending emails](topics/email/)
* [Syndication feeds (RSS/Atom)](ref/contrib/syndication/)
* [Pagination](topics/pagination/)
* [Messages framework](ref/contrib/messages/)
* [Serialization](topics/serialization/)
* [Sessions](topics/http/sessions/)
* [Sitemaps](ref/contrib/sitemaps/)
* [Static files management](ref/contrib/staticfiles/)
* [Data validation](ref/validators/)

## Other core functionalities[¶](#other-core-functionalities "Link to this heading")

Learn about some other core functionalities of the Django framework:

* [Conditional content processing](topics/conditional-view-processing/)
* [Content types and generic relations](ref/contrib/contenttypes/)
* [Flatpages](ref/contrib/flatpages/)
* [Redirects](ref/contrib/redirects/)
* [Signals](topics/signals/)
* [System check framework](topics/checks/)
* [The sites framework](ref/contrib/sites/)
* [Unicode in Django](ref/unicode/)

## The Django open-source project[¶](#the-django-open-source-project "Link to this heading")

Learn about the development process for the Django project itself and about how
you can contribute:

* **Community:**
  [Contributing to Django](internals/contributing/) |
  [The release process](internals/release-process/) |
  [Team organization](internals/organization/) |
  [The Django source code repository](internals/git/) |
  [Security policies](internals/security/) |
  [Mailing lists and Forum](internals/mailing-lists/)
* **Design philosophies:**
  [Overview](misc/design-philosophies/)
* **Documentation:**
  [About this documentation](internals/contributing/writing-documentation/)
* **Third-party distributions:**
  [Overview](misc/distributions/)
* **Django over time:**
  [API stability](misc/api-stability/) |
  [Release notes and upgrading instructions](releases/) |
  [Deprecation Timeline](internals/deprecation/)

Previous page and next page

[Django documentation contents](contents/)

[Getting started](intro/)

 [Back to Top](#top)

## Additional Information

### Support Django!

![Support Django!](https://static.djangoproject.com/img/fundraising-heart.cd6bb84ffd33.svg)

* [Salsotto donated to the Django Software Foundation to support Django development. Donate today!](https://www.djangoproject.com/fundraising/)

### Browse

* Prev: [Django documentation contents](contents/)
* Next: [Getting started](intro/)
* [Table of contents](https://docs.djangoproject.com/en/6.0/contents/)
* [General Index](https://docs.djangoproject.com/en/6.0/genindex/)
* [Python Module Index](https://docs.djangoproject.com/en/6.0/py-modindex/)


### You are here:

* [Django 6.0 documentation](https://docs.djangoproject.com/en/6.0/)
  + Django documentation

### Getting help

[FAQ](https://docs.djangoproject.com/en/6.0/faq/)
:   Try the FAQ — it's got answers to many common questions.

[Index](https://docs.djangoproject.com/en/stable/genindex/), [Module Index](https://docs.djangoproject.com/en/stable/py-modindex/), or [Table of Contents](https://docs.djangoproject.com/en/stable/contents/)
:   Handy when looking for specific information.

[Django Discord Server](https://chat.djangoproject.com)
:   Join the Django Discord Community.

[Official Django Forum](https://forum.djangoproject.com/)
:   Join the community on the Django Forum.

[Ticket tracker](https://code.djangoproject.com/)
:   Report bugs with Django or Django documentation in our ticket tracker.

### Download:

Offline (Django 6.0):
[HTML](https://media.djangoproject.com/docs/django-docs-6.0-en.zip) |
[PDF](https://media.readthedocs.org/pdf/django/6.0.x/django.pdf) |
[ePub](https://media.readthedocs.org/epub/django/6.0.x/django.epub)
  

Provided by [Read the Docs](https://readthedocs.org/).

### Diamond and Platinum Members

[![Sentry](https://media.djangoproject.com/cache/7a/f9/7af9c770dc49465739a82c91a0eb3d51.png)](https://sentry.io/for/django/ "Sentry")

* **Sentry**
* [Monitor your Django Code
  Resolve performance bottlenecks and errors using monitoring, replays, logs and Seer an AI agent for debugging.](https://sentry.io/for/django/ "Sentry")

[![JetBrains](https://media.djangoproject.com/cache/c0/ea/c0ea128467983e64aab91cd27e7918c0.png)](https://jb.gg/ybja10 "JetBrains")

* **JetBrains**
* [JetBrains delivers intelligent software solutions that make developers more productive by simplifying their challenging tasks, automating the routine, and helping them adopt the best development practices. PyCharm is the Python IDE for Professional Developers by JetBrains providing a complete set of tools for productive Python, Web and scientific development.](https://jb.gg/ybja10 "JetBrains")









## Django Links

### Learn More

* [About Django](https://www.djangoproject.com/start/overview/)
* [Getting Started with Django](https://www.djangoproject.com/start/)
* [Team Organization](https://www.djangoproject.com/foundation/teams/)
* [Django Software Foundation](https://www.djangoproject.com/foundation/)
* [Code of Conduct](https://www.djangoproject.com/conduct/)
* [Diversity Statement](https://www.djangoproject.com/diversity/)

### Get Involved

* [Join a Group](https://www.djangoproject.com/community/)
* [Contribute
  to Django](https://docs.djangoproject.com/en/dev/internals/contributing/)
* [Submit
  a Bug](https://docs.djangoproject.com/en/dev/internals/contributing/bugs-and-features/)
* [Report
  a Security Issue](https://docs.djangoproject.com/en/dev/internals/security/#reporting-security-issues)
* [Individual membership](https://www.djangoproject.com/foundation/individual-members/)

### Get Help

* [Getting Help FAQ](https://docs.djangoproject.com/en/stable/faq/)
* [Django Discord](https://chat.djangoproject.com)
* [Official Django Forum](https://forum.djangoproject.com/)

### Follow Us

* [GitHub](https://github.com/django)
* [X](https://x.com/djangoproject)
* [Fediverse (Mastodon)](https://fosstodon.org/@django)
* [Bluesky](https://bsky.app/profile/djangoproject.com)
* [LinkedIn](https://www.linkedin.com/company/django-software-foundation)
* [News RSS](https://www.djangoproject.com/rss/weblog/)

### Support Us

* [Sponsor Django](https://www.djangoproject.com/fundraising/)
* [Corporate membership](https://www.djangoproject.com/foundation/corporate-members/)
* [Official merchandise store](https://django.threadless.com/)
* [Benevity Workplace Giving Program](https://www.djangoproject.com/fundraising/#benevity-giving)

[Django](https://www.djangoproject.com/)

* Hosting by [In-kind
  donors](https://www.djangoproject.com/fundraising/#in-kind-donors)
* Design by [Threespot](https://www.threespot.com)
  & [andrevv](http://andrevv.com/)

© 2005-2025
 [Django Software
Foundation](https://www.djangoproject.com/foundation/) and individual contributors. Django is a
[registered
trademark](https://www.djangoproject.com/trademarks/) of the Django Software Foundation.

---
