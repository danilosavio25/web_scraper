# Django Knowledge

> Category: frameworks

## Source: en_6.0.md

Django documentation | Django documentation | Django

Skip to main content

Django

The web framework for perfectionists with deadlines.

Search

Submit

Toggle theme (current theme: auto)

Toggle theme (current theme: light)

Toggle theme (current theme: dark)

Toggle Light / Dark / Auto color theme

Menu

Main navigation

* Overview
* Download
* Documentation
* News
* Code
* Issues
* Foundation
* ♥ Donate
* Search

  Submit
* Toggle theme (current theme: auto)

  Toggle theme (current theme: light)

  Toggle theme (current theme: dark)

  Toggle Light / Dark / Auto color theme

Documentation

Help us reach our 2025 fundraising goal!

Donate to the *Django Software Foundation* to fund Django's development, security, and community events!  
If you got value out of using Django this year, please consider making a donation ♥
Donate today

* Getting Help

* Language: **en**
* el
* es
* fr
* id
* it
* ja
* ko
* pl
* pt-br
* sv
* zh-hans

* Documentation version:
  **6.0**
* 1.8
* 1.10
* 1.11
* 2.0
* 2.1
* 2.2
* 3.0
* 3.1
* 3.2
* 4.0
* 4.1
* 4.2
* 5.0
* 5.1
* 5.2
* dev

# Django documentation¶

Everything you need to know about Django.

## First steps¶

Are you new to Django or to programming? This is the place to start!

* **From scratch:**
  Overview |
  Installation
* **Tutorial:**
  Part 1: Requests and responses |
  Part 2: Models and the admin site |
  Part 3: Views and templates |
  Part 4: Forms and generic views |
  Part 5: Testing |
  Part 6: Static files |
  Part 7: Customizing the admin site |
  Part 8: Adding third-party packages
* **Advanced Tutorials:**
  How to write reusable apps |
  Writing your first contribution to Django

## Getting help¶

Having trouble? We’d like to help!

* Try the FAQ – it’s got answers to many common questions.
* Looking for specific information? Try the Index, Module Index or
  the detailed table of contents.
* Not found anything? See FAQ: Getting Help for information on getting support
  and asking questions to the community.
* Report bugs with Django in our ticket tracker.

## How the documentation is organized¶

Django has a lot of documentation. A high-level overview of how it’s organized
will help you know where to look for certain things:

* Tutorials take you by the hand through a series of
  steps to create a web application. Start here if you’re new to Django or web
  application development. Also look at the “First steps”.
* Topic guides discuss key topics and concepts at a
  fairly high level and provide useful background information and explanation.
* Reference guides contain technical reference for APIs and
  other aspects of Django’s machinery. They describe how it works and how to
  use it but assume that you have a basic understanding of key concepts.
* How-to guides are recipes. They guide you through the
  steps involved in addressing key problems and use-cases. They are more
  advanced than tutorials and assume some knowledge of how Django works.

## The model layer¶

Django provides an abstraction layer (the “models”) for structuring and
manipulating the data of your web application. Learn more about it below:

* **Models:**
  Introduction to models |
  Field types |
  Indexes |
  Meta options |
  Model class
* **QuerySets:**
  Making queries |
  QuerySet method reference |
  Lookup expressions
* **Model instances:**
  Instance methods |
  Accessing related objects
* **Migrations:**
  Introduction to Migrations |
  Operations reference |
  SchemaEditor |
  Writing migrations
* **Advanced:**
  Managers |
  Raw SQL |
  Transactions |
  Aggregation |
  Search |
  Custom fields |
  Multiple databases |
  Custom lookups |
  Query Expressions |
  Conditional Expressions |
  Database Functions
* **Other:**
  Supported databases |
  Legacy databases |
  Providing initial data |
  Optimize database access |
  PostgreSQL specific features

## The view layer¶

Django has the concept of “views” to encapsulate the logic responsible for
processing a user’s request and for returning the response. Find all you need
to know about views via the links below:

* **The basics:**
  URLconfs |
  View functions |
  Shortcuts |
  Decorators |
  Asynchronous Support
* **Reference:**
  Built-in Views |
  Request/response objects |
  TemplateResponse objects
* **File uploads:**
  Overview |
  File objects |
  Storage API |
  Managing files |
  Custom storage
* **Class-based views:**
  Overview |
  Built-in display views |
  Built-in editing views |
  Using mixins |
  API reference |
  Flattened index
* **Advanced:**
  Generating CSV |
  Generating PDF
* **Middleware:**
  Overview |
  Built-in middleware classes

## The template layer¶

The template layer provides a designer-friendly syntax for rendering the
information to be presented to the user. Learn how this syntax can be used by
designers and how it can be extended by programmers:

* **The basics:**
  Overview
* **For designers:**
  Language overview |
  Built-in tags and filters |
  Humanization
* **For programmers:**
  Template API |
  Custom tags and filters |
  Custom template backend

## Forms¶

Django provides a rich framework to facilitate the creation of forms and the
manipulation of form data.

* **The basics:**
  Overview |
  Form API |
  Built-in fields |
  Built-in widgets
* **Advanced:**
  Forms for models |
  Integrating media |
  Formsets |
  Customizing validation

## The development process¶

Learn about the various components and tools to help you in the development and
testing of Django applications:

* **Settings:**
  Overview |
  Full list of settings
* **Applications:**
  Overview
* **Exceptions:**
  Overview
* **django-admin and manage.py:**
  Overview |
  Adding custom commands
* **Testing:**
  Introduction |
  Writing and running tests |
  Included testing tools |
  Advanced topics
* **Deployment:**
  Overview |
  WSGI servers |
  ASGI servers |
  Deploying static files |
  Tracking code errors by email |
  Deployment checklist

## The admin¶

Find all you need to know about the automated admin interface, one of Django’s
most popular features:

* Admin site
* Admin actions
* Admin documentation generator

## Security¶

Security is a topic of paramount importance in the development of web
applications and Django provides multiple protection tools and mechanisms:

* Security overview
* Disclosed security issues in Django
* Clickjacking protection
* Cross Site Request Forgery protection
* Cryptographic signing
* Security Middleware
* Content Security Policy

## Internationalization and localization¶

Django offers a robust internationalization and localization framework to
assist you in the development of applications for multiple languages and world
regions:

* Overview |
  Internationalization |
  Localization |
  Localized web UI formatting and form input
* Time zones

## Performance and optimization¶

There are a variety of techniques and tools that can help get your code running
more efficiently - faster, and using fewer system resources.

* Performance and optimization overview

## Geographic framework¶

GeoDjango intends to be a world-class
geographic web framework. Its goal is to make it as easy as possible to build
GIS web applications and harness the power of spatially enabled data.

## Common web application tools¶

Django offers multiple tools commonly needed in the development of web
applications:

* **Authentication:**
  Overview |
  Using the authentication system |
  Password management |
  Customizing authentication |
  API Reference
* Caching
* Logging
* Tasks framework
* Sending emails
* Syndication feeds (RSS/Atom)
* Pagination
* Messages framework
* Serialization
* Sessions
* Sitemaps
* Static files management
* Data validation

## Other core functionalities¶

Learn about some other core functionalities of the Django framework:

* Conditional content processing
* Content types and generic relations
* Flatpages
* Redirects
* Signals
* System check framework
* The sites framework
* Unicode in Django

## The Django open-source project¶

Learn about the development process for the Django project itself and about how
you can contribute:

* **Community:**
  Contributing to Django |
  The release process |
  Team organization |
  The Django source code repository |
  Security policies |
  Mailing lists and Forum
* **Design philosophies:**
  Overview
* **Documentation:**
  About this documentation
* **Third-party distributions:**
  Overview
* **Django over time:**
  API stability |
  Release notes and upgrading instructions |
  Deprecation Timeline

Previous page and next page

Django documentation contents

Getting started

 Back to Top

## Additional Information

### Support Django!

* Salsotto donated to the Django Software Foundation to support Django development. Donate today!

### Browse

* Prev: Django documentation contents
* Next: Getting started
* Table of contents
* General Index
* Python Module Index

### You are here:

* Django 6.0 documentation
  + Django documentation

### Getting help

FAQ
:   Try the FAQ — it's got answers to many common questions.

Index, Module Index, or Table of Contents
:   Handy when looking for specific information.

Django Discord Server
:   Join the Django Discord Community.

Official Django Forum
:   Join the community on the Django Forum.

Ticket tracker
:   Report bugs with Django or Django documentation in our ticket tracker.

### Download:

Offline (Django 6.0):
HTML |
PDF |
ePub

Provided by Read the Docs.

### Diamond and Platinum Members

* **Sentry**
* Monitor your Django Code
  Resolve performance bottlenecks and errors using monitoring, replays, logs and Seer an AI agent for debugging.

* **JetBrains**
* JetBrains delivers intelligent software solutions that make developers more productive by simplifying their challenging tasks, automating the routine, and helping them adopt the best development practices. PyCharm is the Python IDE for Professional Developers by JetBrains providing a complete set of tools for productive Python, Web and scientific development.

## Django Links

### Learn More

* About Django
* Getting Started with Django
* Team Organization
* Django Software Foundation
* Code of Conduct
* Diversity Statement

### Get Involved

* Join a Group
* Contribute
  to Django
* Submit
  a Bug
* Report
  a Security Issue
* Individual membership

### Get Help

* Getting Help FAQ
* Django Discord
* Official Django Forum

### Follow Us

* X
* Fediverse (Mastodon)
* Bluesky
* LinkedIn
* News RSS

### Support Us

* Sponsor Django
* Corporate membership
* Official merchandise store
* Benevity Workplace Giving Program

Django

* Hosting by In-kind
  donors
* Design by Threespot
  & andrevv

© 2005-2025
 Django Software
Foundation and individual contributors. Django is a
registered
trademark of the Django Software Foundation.

---

## Source: en_6.0_faq_help.md

FAQ: Getting Help | Django documentation | Django

Skip to main content

Django

The web framework for perfectionists with deadlines.

Search

Submit

Toggle theme (current theme: auto)

Toggle theme (current theme: light)

Toggle theme (current theme: dark)

Toggle Light / Dark / Auto color theme

Menu

Main navigation

* Overview
* Download
* Documentation
* News
* Code
* Issues
* Foundation
* ♥ Donate
* Search

  Submit
* Toggle theme (current theme: auto)

  Toggle theme (current theme: light)

  Toggle theme (current theme: dark)

  Toggle Light / Dark / Auto color theme

Documentation

Help us reach our 2025 fundraising goal!

Donate to the *Django Software Foundation* to fund Django's development, security, and community events!  
If you got value out of using Django this year, please consider making a donation ♥
Donate today

* Getting Help

* Language: **en**
* el
* es
* fr
* id
* it
* ja
* ko
* pl
* pt-br
* sv
* zh-hans

* Documentation version:
  **6.0**
* 1.8
* 1.10
* 1.11
* 2.0
* 2.1
* 2.2
* 3.0
* 3.1
* 3.2
* 4.0
* 4.1
* 4.2
* 5.0
* 5.1
* 5.2
* dev

# FAQ: Getting Help¶

## How do I do X? Why doesn’t Y work? Where can I go to get help?¶

First, please check if your question is answered on the FAQ. Also, search for answers using your favorite search engine, and
in the forum.

If you can’t find an answer, please take a few minutes to formulate your
question well. Explaining the problems you are facing clearly will help others
help you. See the StackOverflow guide on asking good questions.

Then, please post it in one of the following channels:

* The Django Forum section “Using Django”. This is for web-based
  discussions.
* The Django Discord server for chat-based discussions.

In all these channels please abide by the Django Code of Conduct. In
summary, being friendly and patient, considerate, respectful, and careful in
your choice of words.

## Nobody answered my question! What should I do?¶

Try making your question more specific, or provide a better example of your
problem.

As with most open-source projects, the folks on these channels are volunteers.
If nobody has answered your question, it may be because nobody knows the
answer, it may be because nobody can understand the question, or it may be that
everybody that can help is busy.

You can also try asking on a different channel. But please don’t post your
question in all three channels in quick succession.

## I think I’ve found a bug! What should I do?¶

Detailed instructions on how to handle a potential bug can be found in our
Guide to contributing to Django.

## I think I’ve found a security problem! What should I do?¶

If you think you’ve found a security problem with Django, please send a message
to `security@djangoproject.com`. This is a private list only open to
long-time, highly trusted Django developers, and its archives are not publicly
readable.

Due to the sensitive nature of security issues, we ask that if you think you
have found a security problem, *please* don’t post a message on the forum, the
Discord server, IRC, or one of the public mailing lists. Django has a
policy for handling security issues;
while a defect is outstanding, we would like to minimize any damage that
could be inflicted through public knowledge of that defect.

Previous page and next page

FAQ: Using Django

FAQ: Databases and models

 Back to Top

## Additional Information

### Support Django!

* Enix Yu donated to the Django Software Foundation to support Django development. Donate today!

### Contents

* FAQ: Getting Help
  + How do I do X? Why doesn’t Y work? Where can I go to get help?
  + Nobody answered my question! What should I do?
  + I think I’ve found a bug! What should I do?
  + I think I’ve found a security problem! What should I do?

### Browse

* Prev: FAQ: Using Django
* Next: FAQ: Databases and models
* Table of contents
* General Index
* Python Module Index

### You are here:

* Django 6.0 documentation
  + Django FAQ
    - FAQ: Getting Help

### Getting help

FAQ
:   Try the FAQ — it's got answers to many common questions.

Index, Module Index, or Table of Contents
:   Handy when looking for specific information.

Django Discord Server
:   Join the Django Discord Community.

Official Django Forum
:   Join the community on the Django Forum.

Ticket tracker
:   Report bugs with Django or Django documentation in our ticket tracker.

### Download:

Offline (Django 6.0):
HTML |
PDF |
ePub

Provided by Read the Docs.

### Diamond and Platinum Members

* **Sentry**
* Monitor your Django Code
  Resolve performance bottlenecks and errors using monitoring, replays, logs and Seer an AI agent for debugging.

* **JetBrains**
* JetBrains delivers intelligent software solutions that make developers more productive by simplifying their challenging tasks, automating the routine, and helping them adopt the best development practices. PyCharm is the Python IDE for Professional Developers by JetBrains providing a complete set of tools for productive Python, Web and scientific development.

## Django Links

### Learn More

* About Django
* Getting Started with Django
* Team Organization
* Django Software Foundation
* Code of Conduct
* Diversity Statement

### Get Involved

* Join a Group
* Contribute
  to Django
* Submit
  a Bug
* Report
  a Security Issue
* Individual membership

### Get Help

* Getting Help FAQ
* Django Discord
* Official Django Forum

### Follow Us

* X
* Fediverse (Mastodon)
* Bluesky
* LinkedIn
* News RSS

### Support Us

* Sponsor Django
* Corporate membership
* Official merchandise store
* Benevity Workplace Giving Program

Django

* Hosting by In-kind
  donors
* Design by Threespot
  & andrevv

© 2005-2025
 Django Software
Foundation and individual contributors. Django is a
registered
trademark of the Django Software Foundation.

---

## Source: en_stable.md

Django documentation | Django documentation | Django

Skip to main content

Django

The web framework for perfectionists with deadlines.

Search

Submit

Toggle theme (current theme: auto)

Toggle theme (current theme: light)

Toggle theme (current theme: dark)

Toggle Light / Dark / Auto color theme

Menu

Main navigation

* Overview
* Download
* Documentation
* News
* Code
* Issues
* Foundation
* ♥ Donate
* Search

  Submit
* Toggle theme (current theme: auto)

  Toggle theme (current theme: light)

  Toggle theme (current theme: dark)

  Toggle Light / Dark / Auto color theme

Documentation

Help us reach our 2025 fundraising goal!

Donate to the *Django Software Foundation* to fund Django's development, security, and community events!  
If you got value out of using Django this year, please consider making a donation ♥
Donate today

* Getting Help

* Language: **en**
* el
* es
* fr
* id
* it
* ja
* ko
* pl
* pt-br
* sv
* zh-hans

* Documentation version:
  **6.0**
* 1.8
* 1.10
* 1.11
* 2.0
* 2.1
* 2.2
* 3.0
* 3.1
* 3.2
* 4.0
* 4.1
* 4.2
* 5.0
* 5.1
* 5.2
* dev

# Django documentation¶

Everything you need to know about Django.

## First steps¶

Are you new to Django or to programming? This is the place to start!

* **From scratch:**
  Overview |
  Installation
* **Tutorial:**
  Part 1: Requests and responses |
  Part 2: Models and the admin site |
  Part 3: Views and templates |
  Part 4: Forms and generic views |
  Part 5: Testing |
  Part 6: Static files |
  Part 7: Customizing the admin site |
  Part 8: Adding third-party packages
* **Advanced Tutorials:**
  How to write reusable apps |
  Writing your first contribution to Django

## Getting help¶

Having trouble? We’d like to help!

* Try the FAQ – it’s got answers to many common questions.
* Looking for specific information? Try the Index, Module Index or
  the detailed table of contents.
* Not found anything? See FAQ: Getting Help for information on getting support
  and asking questions to the community.
* Report bugs with Django in our ticket tracker.

## How the documentation is organized¶

Django has a lot of documentation. A high-level overview of how it’s organized
will help you know where to look for certain things:

* Tutorials take you by the hand through a series of
  steps to create a web application. Start here if you’re new to Django or web
  application development. Also look at the “First steps”.
* Topic guides discuss key topics and concepts at a
  fairly high level and provide useful background information and explanation.
* Reference guides contain technical reference for APIs and
  other aspects of Django’s machinery. They describe how it works and how to
  use it but assume that you have a basic understanding of key concepts.
* How-to guides are recipes. They guide you through the
  steps involved in addressing key problems and use-cases. They are more
  advanced than tutorials and assume some knowledge of how Django works.

## The model layer¶

Django provides an abstraction layer (the “models”) for structuring and
manipulating the data of your web application. Learn more about it below:

* **Models:**
  Introduction to models |
  Field types |
  Indexes |
  Meta options |
  Model class
* **QuerySets:**
  Making queries |
  QuerySet method reference |
  Lookup expressions
* **Model instances:**
  Instance methods |
  Accessing related objects
* **Migrations:**
  Introduction to Migrations |
  Operations reference |
  SchemaEditor |
  Writing migrations
* **Advanced:**
  Managers |
  Raw SQL |
  Transactions |
  Aggregation |
  Search |
  Custom fields |
  Multiple databases |
  Custom lookups |
  Query Expressions |
  Conditional Expressions |
  Database Functions
* **Other:**
  Supported databases |
  Legacy databases |
  Providing initial data |
  Optimize database access |
  PostgreSQL specific features

## The view layer¶

Django has the concept of “views” to encapsulate the logic responsible for
processing a user’s request and for returning the response. Find all you need
to know about views via the links below:

* **The basics:**
  URLconfs |
  View functions |
  Shortcuts |
  Decorators |
  Asynchronous Support
* **Reference:**
  Built-in Views |
  Request/response objects |
  TemplateResponse objects
* **File uploads:**
  Overview |
  File objects |
  Storage API |
  Managing files |
  Custom storage
* **Class-based views:**
  Overview |
  Built-in display views |
  Built-in editing views |
  Using mixins |
  API reference |
  Flattened index
* **Advanced:**
  Generating CSV |
  Generating PDF
* **Middleware:**
  Overview |
  Built-in middleware classes

## The template layer¶

The template layer provides a designer-friendly syntax for rendering the
information to be presented to the user. Learn how this syntax can be used by
designers and how it can be extended by programmers:

* **The basics:**
  Overview
* **For designers:**
  Language overview |
  Built-in tags and filters |
  Humanization
* **For programmers:**
  Template API |
  Custom tags and filters |
  Custom template backend

## Forms¶

Django provides a rich framework to facilitate the creation of forms and the
manipulation of form data.

* **The basics:**
  Overview |
  Form API |
  Built-in fields |
  Built-in widgets
* **Advanced:**
  Forms for models |
  Integrating media |
  Formsets |
  Customizing validation

## The development process¶

Learn about the various components and tools to help you in the development and
testing of Django applications:

* **Settings:**
  Overview |
  Full list of settings
* **Applications:**
  Overview
* **Exceptions:**
  Overview
* **django-admin and manage.py:**
  Overview |
  Adding custom commands
* **Testing:**
  Introduction |
  Writing and running tests |
  Included testing tools |
  Advanced topics
* **Deployment:**
  Overview |
  WSGI servers |
  ASGI servers |
  Deploying static files |
  Tracking code errors by email |
  Deployment checklist

## The admin¶

Find all you need to know about the automated admin interface, one of Django’s
most popular features:

* Admin site
* Admin actions
* Admin documentation generator

## Security¶

Security is a topic of paramount importance in the development of web
applications and Django provides multiple protection tools and mechanisms:

* Security overview
* Disclosed security issues in Django
* Clickjacking protection
* Cross Site Request Forgery protection
* Cryptographic signing
* Security Middleware
* Content Security Policy

## Internationalization and localization¶

Django offers a robust internationalization and localization framework to
assist you in the development of applications for multiple languages and world
regions:

* Overview |
  Internationalization |
  Localization |
  Localized web UI formatting and form input
* Time zones

## Performance and optimization¶

There are a variety of techniques and tools that can help get your code running
more efficiently - faster, and using fewer system resources.

* Performance and optimization overview

## Geographic framework¶

GeoDjango intends to be a world-class
geographic web framework. Its goal is to make it as easy as possible to build
GIS web applications and harness the power of spatially enabled data.

## Common web application tools¶

Django offers multiple tools commonly needed in the development of web
applications:

* **Authentication:**
  Overview |
  Using the authentication system |
  Password management |
  Customizing authentication |
  API Reference
* Caching
* Logging
* Tasks framework
* Sending emails
* Syndication feeds (RSS/Atom)
* Pagination
* Messages framework
* Serialization
* Sessions
* Sitemaps
* Static files management
* Data validation

## Other core functionalities¶

Learn about some other core functionalities of the Django framework:

* Conditional content processing
* Content types and generic relations
* Flatpages
* Redirects
* Signals
* System check framework
* The sites framework
* Unicode in Django

## The Django open-source project¶

Learn about the development process for the Django project itself and about how
you can contribute:

* **Community:**
  Contributing to Django |
  The release process |
  Team organization |
  The Django source code repository |
  Security policies |
  Mailing lists and Forum
* **Design philosophies:**
  Overview
* **Documentation:**
  About this documentation
* **Third-party distributions:**
  Overview
* **Django over time:**
  API stability |
  Release notes and upgrading instructions |
  Deprecation Timeline

Previous page and next page

Django documentation contents

Getting started

 Back to Top

## Additional Information

### Support Django!

* Salsotto donated to the Django Software Foundation to support Django development. Donate today!

### Browse

* Prev: Django documentation contents
* Next: Getting started
* Table of contents
* General Index
* Python Module Index

### You are here:

* Django 6.0 documentation
  + Django documentation

### Getting help

FAQ
:   Try the FAQ — it's got answers to many common questions.

Index, Module Index, or Table of Contents
:   Handy when looking for specific information.

Django Discord Server
:   Join the Django Discord Community.

Official Django Forum
:   Join the community on the Django Forum.

Ticket tracker
:   Report bugs with Django or Django documentation in our ticket tracker.

### Download:

Offline (Django 6.0):
HTML |
PDF |
ePub

Provided by Read the Docs.

### Diamond and Platinum Members

* **Sentry**
* Monitor your Django Code
  Resolve performance bottlenecks and errors using monitoring, replays, logs and Seer an AI agent for debugging.

* **JetBrains**
* JetBrains delivers intelligent software solutions that make developers more productive by simplifying their challenging tasks, automating the routine, and helping them adopt the best development practices. PyCharm is the Python IDE for Professional Developers by JetBrains providing a complete set of tools for productive Python, Web and scientific development.

## Django Links

### Learn More

* About Django
* Getting Started with Django
* Team Organization
* Django Software Foundation
* Code of Conduct
* Diversity Statement

### Get Involved

* Join a Group
* Contribute
  to Django
* Submit
  a Bug
* Report
  a Security Issue
* Individual membership

### Get Help

* Getting Help FAQ
* Django Discord
* Official Django Forum

### Follow Us

* X
* Fediverse (Mastodon)
* Bluesky
* LinkedIn
* News RSS

### Support Us

* Sponsor Django
* Corporate membership
* Official merchandise store
* Benevity Workplace Giving Program

Django

* Hosting by In-kind
  donors
* Design by Threespot
  & andrevv

© 2005-2025
 Django Software
Foundation and individual contributors. Django is a
registered
trademark of the Django Software Foundation.

---

## Source: index.md

Django documentation | Django documentation | Django

Skip to main content

Django

The web framework for perfectionists with deadlines.

Search

Submit

Toggle theme (current theme: auto)

Toggle theme (current theme: light)

Toggle theme (current theme: dark)

Toggle Light / Dark / Auto color theme

Menu

Main navigation

* Overview
* Download
* Documentation
* News
* Code
* Issues
* Foundation
* ♥ Donate
* Search

  Submit
* Toggle theme (current theme: auto)

  Toggle theme (current theme: light)

  Toggle theme (current theme: dark)

  Toggle Light / Dark / Auto color theme

Documentation

Help us reach our 2025 fundraising goal!

Donate to the *Django Software Foundation* to fund Django's development, security, and community events!  
If you got value out of using Django this year, please consider making a donation ♥
Donate today

* Getting Help

* Language: **en**
* el
* es
* fr
* id
* it
* ja
* ko
* pl
* pt-br
* sv
* zh-hans

* Documentation version:
  **6.0**
* 1.8
* 1.10
* 1.11
* 2.0
* 2.1
* 2.2
* 3.0
* 3.1
* 3.2
* 4.0
* 4.1
* 4.2
* 5.0
* 5.1
* 5.2
* dev

# Django documentation¶

Everything you need to know about Django.

## First steps¶

Are you new to Django or to programming? This is the place to start!

* **From scratch:**
  Overview |
  Installation
* **Tutorial:**
  Part 1: Requests and responses |
  Part 2: Models and the admin site |
  Part 3: Views and templates |
  Part 4: Forms and generic views |
  Part 5: Testing |
  Part 6: Static files |
  Part 7: Customizing the admin site |
  Part 8: Adding third-party packages
* **Advanced Tutorials:**
  How to write reusable apps |
  Writing your first contribution to Django

## Getting help¶

Having trouble? We’d like to help!

* Try the FAQ – it’s got answers to many common questions.
* Looking for specific information? Try the Index, Module Index or
  the detailed table of contents.
* Not found anything? See FAQ: Getting Help for information on getting support
  and asking questions to the community.
* Report bugs with Django in our ticket tracker.

## How the documentation is organized¶

Django has a lot of documentation. A high-level overview of how it’s organized
will help you know where to look for certain things:

* Tutorials take you by the hand through a series of
  steps to create a web application. Start here if you’re new to Django or web
  application development. Also look at the “First steps”.
* Topic guides discuss key topics and concepts at a
  fairly high level and provide useful background information and explanation.
* Reference guides contain technical reference for APIs and
  other aspects of Django’s machinery. They describe how it works and how to
  use it but assume that you have a basic understanding of key concepts.
* How-to guides are recipes. They guide you through the
  steps involved in addressing key problems and use-cases. They are more
  advanced than tutorials and assume some knowledge of how Django works.

## The model layer¶

Django provides an abstraction layer (the “models”) for structuring and
manipulating the data of your web application. Learn more about it below:

* **Models:**
  Introduction to models |
  Field types |
  Indexes |
  Meta options |
  Model class
* **QuerySets:**
  Making queries |
  QuerySet method reference |
  Lookup expressions
* **Model instances:**
  Instance methods |
  Accessing related objects
* **Migrations:**
  Introduction to Migrations |
  Operations reference |
  SchemaEditor |
  Writing migrations
* **Advanced:**
  Managers |
  Raw SQL |
  Transactions |
  Aggregation |
  Search |
  Custom fields |
  Multiple databases |
  Custom lookups |
  Query Expressions |
  Conditional Expressions |
  Database Functions
* **Other:**
  Supported databases |
  Legacy databases |
  Providing initial data |
  Optimize database access |
  PostgreSQL specific features

## The view layer¶

Django has the concept of “views” to encapsulate the logic responsible for
processing a user’s request and for returning the response. Find all you need
to know about views via the links below:

* **The basics:**
  URLconfs |
  View functions |
  Shortcuts |
  Decorators |
  Asynchronous Support
* **Reference:**
  Built-in Views |
  Request/response objects |
  TemplateResponse objects
* **File uploads:**
  Overview |
  File objects |
  Storage API |
  Managing files |
  Custom storage
* **Class-based views:**
  Overview |
  Built-in display views |
  Built-in editing views |
  Using mixins |
  API reference |
  Flattened index
* **Advanced:**
  Generating CSV |
  Generating PDF
* **Middleware:**
  Overview |
  Built-in middleware classes

## The template layer¶

The template layer provides a designer-friendly syntax for rendering the
information to be presented to the user. Learn how this syntax can be used by
designers and how it can be extended by programmers:

* **The basics:**
  Overview
* **For designers:**
  Language overview |
  Built-in tags and filters |
  Humanization
* **For programmers:**
  Template API |
  Custom tags and filters |
  Custom template backend

## Forms¶

Django provides a rich framework to facilitate the creation of forms and the
manipulation of form data.

* **The basics:**
  Overview |
  Form API |
  Built-in fields |
  Built-in widgets
* **Advanced:**
  Forms for models |
  Integrating media |
  Formsets |
  Customizing validation

## The development process¶

Learn about the various components and tools to help you in the development and
testing of Django applications:

* **Settings:**
  Overview |
  Full list of settings
* **Applications:**
  Overview
* **Exceptions:**
  Overview
* **django-admin and manage.py:**
  Overview |
  Adding custom commands
* **Testing:**
  Introduction |
  Writing and running tests |
  Included testing tools |
  Advanced topics
* **Deployment:**
  Overview |
  WSGI servers |
  ASGI servers |
  Deploying static files |
  Tracking code errors by email |
  Deployment checklist

## The admin¶

Find all you need to know about the automated admin interface, one of Django’s
most popular features:

* Admin site
* Admin actions
* Admin documentation generator

## Security¶

Security is a topic of paramount importance in the development of web
applications and Django provides multiple protection tools and mechanisms:

* Security overview
* Disclosed security issues in Django
* Clickjacking protection
* Cross Site Request Forgery protection
* Cryptographic signing
* Security Middleware
* Content Security Policy

## Internationalization and localization¶

Django offers a robust internationalization and localization framework to
assist you in the development of applications for multiple languages and world
regions:

* Overview |
  Internationalization |
  Localization |
  Localized web UI formatting and form input
* Time zones

## Performance and optimization¶

There are a variety of techniques and tools that can help get your code running
more efficiently - faster, and using fewer system resources.

* Performance and optimization overview

## Geographic framework¶

GeoDjango intends to be a world-class
geographic web framework. Its goal is to make it as easy as possible to build
GIS web applications and harness the power of spatially enabled data.

## Common web application tools¶

Django offers multiple tools commonly needed in the development of web
applications:

* **Authentication:**
  Overview |
  Using the authentication system |
  Password management |
  Customizing authentication |
  API Reference
* Caching
* Logging
* Tasks framework
* Sending emails
* Syndication feeds (RSS/Atom)
* Pagination
* Messages framework
* Serialization
* Sessions
* Sitemaps
* Static files management
* Data validation

## Other core functionalities¶

Learn about some other core functionalities of the Django framework:

* Conditional content processing
* Content types and generic relations
* Flatpages
* Redirects
* Signals
* System check framework
* The sites framework
* Unicode in Django

## The Django open-source project¶

Learn about the development process for the Django project itself and about how
you can contribute:

* **Community:**
  Contributing to Django |
  The release process |
  Team organization |
  The Django source code repository |
  Security policies |
  Mailing lists and Forum
* **Design philosophies:**
  Overview
* **Documentation:**
  About this documentation
* **Third-party distributions:**
  Overview
* **Django over time:**
  API stability |
  Release notes and upgrading instructions |
  Deprecation Timeline

Previous page and next page

Django documentation contents

Getting started

 Back to Top

## Additional Information

### Support Django!

* Salsotto donated to the Django Software Foundation to support Django development. Donate today!

### Browse

* Prev: Django documentation contents
* Next: Getting started
* Table of contents
* General Index
* Python Module Index

### You are here:

* Django 6.0 documentation
  + Django documentation

### Getting help

FAQ
:   Try the FAQ — it's got answers to many common questions.

Index, Module Index, or Table of Contents
:   Handy when looking for specific information.

Django Discord Server
:   Join the Django Discord Community.

Official Django Forum
:   Join the community on the Django Forum.

Ticket tracker
:   Report bugs with Django or Django documentation in our ticket tracker.

### Download:

Offline (Django 6.0):
HTML |
PDF |
ePub

Provided by Read the Docs.

### Diamond and Platinum Members

* **Sentry**
* Monitor your Django Code
  Resolve performance bottlenecks and errors using monitoring, replays, logs and Seer an AI agent for debugging.

* **JetBrains**
* JetBrains delivers intelligent software solutions that make developers more productive by simplifying their challenging tasks, automating the routine, and helping them adopt the best development practices. PyCharm is the Python IDE for Professional Developers by JetBrains providing a complete set of tools for productive Python, Web and scientific development.

## Django Links

### Learn More

* About Django
* Getting Started with Django
* Team Organization
* Django Software Foundation
* Code of Conduct
* Diversity Statement

### Get Involved

* Join a Group
* Contribute
  to Django
* Submit
  a Bug
* Report
  a Security Issue
* Individual membership

### Get Help

* Getting Help FAQ
* Django Discord
* Official Django Forum

### Follow Us

* X
* Fediverse (Mastodon)
* Bluesky
* LinkedIn
* News RSS

### Support Us

* Sponsor Django
* Corporate membership
* Official merchandise store
* Benevity Workplace Giving Program

Django

* Hosting by In-kind
  donors
* Design by Threespot
  & andrevv

© 2005-2025
 Django Software
Foundation and individual contributors. Django is a
registered
trademark of the Django Software Foundation.

---