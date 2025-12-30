# Spring Knowledge

> Category: frameworks


## Source: ai.md

Spring | Generative AI

[Skip to main content](#main)

Why Spring

* [Overview](/why-spring)
* [Generative AI](/ai)
* [Microservices](/microservices)
* [Reactive](/reactive)
* [Event Driven](/event-driven)
* [Cloud](/cloud)
* [Web Applications](/web-applications)
* [Serverless](/serverless)
* [Batch](/batch)

Learn

* [Overview](/learn)
* [Quickstart](/quickstart)
* [Guides](/guides)
* [Blog](/blog)
* [Security Advisories](/security)

Projects

* [Overview](/projects)
* [Spring Boot](/projects/spring-boot)
* [Spring Framework](/projects/spring-framework)
* [Spring Cloud](/projects/spring-cloud)
* [Spring Cloud Data Flow](/projects/spring-cloud-dataflow)
* [Spring Data](/projects/spring-data)
* [Spring Integration](/projects/spring-integration)
* [Spring Batch](/projects/spring-batch)
* [Spring Security](/projects/spring-security)
* [Spring AI](/projects/spring-ai)
* [Release Calendar](/projects#release-calendar)
* [Security advisories](/security)
* DEVELOPMENT TOOLS
* [Spring Tools](/tools)
* [Spring Initializr](https://start.spring.io/)

Academy

* [Courses](https://spring.academy/courses)
* [Get Certified](https://spring.academy/learning-path)

Community

* [Overview](/community)
* [Events](/events)
* [Authors](/authors)

[Tanzu Spring](https://enterprise.spring.io)

![](/img/extra/microservices-4.svg)

# Generative AI

Businesses everywhere are looking to transform their applications by adding Gen AI capabilities to them. Conversational chatbots, code assistance, healthcare diagnostics are some of the use cases for Gen AI.

### What is Generative AI?

Generative AI is a type of Artificial Intelligence that can create new content such as text, images, videos and more. Things that make Gen AI unique are human language as the interface, contextually relevant output, pre-trained models, and accessibility via Web APIs.

### Why Java developers should care?

Java remains one of the most popular programming languages in the enterprise. Its stability, security, and scalability are unmatched. However, integrating AI capabilities such as retrieval-augmented generation (RAG), multimodal use cases like image recognition, as well as predictive analytics, has often required that teams learn new skills or switch to different platforms.

# Generative AI with Spring

Spring AI is a robust extension of the Spring Framework. It’s designed to empower Java developers to create AI-capable applications without the need for extensive reskilling. By leveraging the familiarity and strengths of the Spring Framework, Spring AI democratizes access to sophisticated AI features, making it easier for developers to build intelligent apps.

```
@Service  
public class SpringAI {  
  


private final ChatClient chatClient;  
  
public SpringAI(ChatClient.Builder builder) {  


this.chatClient = builder.build();

}  
  
public String tellMeAJoke()  


return chatClient.prompt().user("Tell me a joke").call().content());

}

  
}
```

[Get started with ChatClients](https://docs.spring.io/spring-ai/reference/api/multimodality.html)

[Portable Chat Models](https://docs.spring.io/spring-ai/reference/api/chat/comparison.html)

# Tool Calling

Tool calling allows you to register your own functions to connect the LLMs to the APIs of external systems. These systems can provide LLMs with real-time data and perform data processing actions on their behalf. Spring AI greatly simplifies code you need to write to support function invocation. It handles the function invocation conversation for you. You can provide your function as a @Bean and then provide the bean name of the function in your prompt options to activate that function. Additionally, you can define and reference multiple functions in a single prompt.

[Get started with Tool Calling](https://docs.spring.io/spring-ai/reference/api/tools.html)

# Model Context Protocol (MCP)

Standardized protocol that enables AI models and Agents to interact with external tools and resources in a structured way. It supports multiple transport mechanisms to provide flexibility across different environments.

[Get started with MCP](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-overview.html)

# Retrieval Augmented Generation

At its core, Spring AI addresses the fundamental challenge of AI integration - Connecting your enterprise Data and APIs with the AI Models. A technique termed Retrieval Augmented Generation (RAG) has emerged to address the challenge of incorporating relevant data into prompts for accurate AI model responses.Spring AI greatly simplifies code you need to write to support RAG pipelines.

![](/img/extra/ai-1.png)![](/img/extra/ai-1-dark.png)

[Get started with RAG](https://docs.spring.io/spring-ai/reference/api/retrieval-augmented-generation.html)

# Spring AI supported patterns

Generative AI brings with it it's own set of challenges. Spring AI supports the following patterns to address these challenges.

| Challenges | Patterns |
| --- | --- |
| Align responses to goals | System prompt |
| No structured output | Output converters |
| Not trained on your data | Prompt Stuffing |
| Limited Context Size | RAG |
| Stateless APIs | Chat memory |
| Not aware of your APIs | Function calling |
| Hallucinations | Evaluators |

# Integration with common technologies

Spring AI provides abstractions that serve as the foundation for developing AI applications. These abstractions have multiple implementations, enabling easy component swapping with minimal code changes. Spring AI has support for all major Model providers such as OpenAI, Microsoft, Amazon, Google, and Hugging Face. It also supports all major Vector Database providers such as Apache Cassandra, Azure Vector Search, Chroma, Milvus, MongoDB Atlas, Neo4j, Oracle, PostgreSQL/PGVector, PineCone, Qdrant, Redis, and Weaviate.

## Ready to get started?

[TRY OUR QUICKSTART GUIDE](https://docs.spring.io/spring-ai/reference/getting-started.html)

## More resources

[![AI Powered Flight booking system](/img/extra/ai-2.svg)![AI Powered Flight booking system](/img/extra/ai-2-dark.svg)](https://github.com/tzolov/playground-flight-booking)

# [AI Powered Flight booking system](https://github.com/tzolov/playground-flight-booking)

Christian Tzolov

![](/img/extra/footer.svg)

## Get ahead

VMware offers training and certification to turbo-charge your progress.

[Learn more](https://spring.academy/)

## Get support

Tanzu Spring offers support and binaries for OpenJDK™, Spring, and Apache Tomcat® in one simple subscription.

[Learn more](/support)

## Upcoming events

Check out all the upcoming events in the Spring community.

[View all](/events)

[Why Spring](/why-spring)

[Microservices](/microservices)

[Reactive](/reactive)

[Event Driven](/event-driven)

[Cloud](/cloud)

[Web Applications](/web-applications)

[Serverless](/serverless)

[Batch](/batch)

[Learn](/learn)

[Quickstart](/quickstart)

[Guides](/guides)

[Blog](/blog)

[Community](/community)

[Events](/events)

[Authors](/authors)

[Tanzu Spring](https://enterprise.spring.io)

[Spring Academy](https://spring.academy/)

[Spring Advisories](/security)

[Projects](/projects)

[Thank You](/thank-you)

## Get the Spring newsletter

Stay connected with the Spring newsletter

[Subscribe](https://go-vmware.broadcom.com/tnz-spring-newsletter-subscribe)

Copyright © 2005 - 2025 Broadcom. All Rights Reserved. The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.   
[Terms of Use](https://www.broadcom.com/company/legal/terms-of-use) • [Privacy](https://www.broadcom.com/company/legal/privacy) • [Trademark Guidelines](/trademarks)

Apache®, Apache Tomcat®, Apache Kafka®, Apache Cassandra™, and Apache Geode™ are trademarks or registered trademarks of the Apache Software Foundation in the United States and/or other countries. Java™, Java™ SE, Java™ EE, and OpenJDK™ are trademarks of Oracle and/or its affiliates. Kubernetes® is a registered trademark of the Linux Foundation in the United States and other countries. Linux® is the registered trademark of Linus Torvalds in the United States and other countries. Windows® and Microsoft® Azure are registered trademarks of Microsoft Corporation. “AWS” and “Amazon Web Services” are trademarks or registered trademarks of Amazon.com Inc. or its affiliates. All other trademarks and copyrights are property of their respective owners and are only mentioned for informative purposes. Other names may be trademarks of their respective owners.

---

## Source: guides.md

Spring | Guides

[Skip to main content](#main)

Why Spring

* [Overview](/why-spring)
* [Generative AI](/ai)
* [Microservices](/microservices)
* [Reactive](/reactive)
* [Event Driven](/event-driven)
* [Cloud](/cloud)
* [Web Applications](/web-applications)
* [Serverless](/serverless)
* [Batch](/batch)

Learn

* [Overview](/learn)
* [Quickstart](/quickstart)
* [Guides](/guides)
* [Blog](/blog)
* [Security Advisories](/security)

Projects

* [Overview](/projects)
* [Spring Boot](/projects/spring-boot)
* [Spring Framework](/projects/spring-framework)
* [Spring Cloud](/projects/spring-cloud)
* [Spring Cloud Data Flow](/projects/spring-cloud-dataflow)
* [Spring Data](/projects/spring-data)
* [Spring Integration](/projects/spring-integration)
* [Spring Batch](/projects/spring-batch)
* [Spring Security](/projects/spring-security)
* [Spring AI](/projects/spring-ai)
* [Release Calendar](/projects#release-calendar)
* [Security advisories](/security)
* DEVELOPMENT TOOLS
* [Spring Tools](/tools)
* [Spring Initializr](https://start.spring.io/)

Academy

* [Courses](https://spring.academy/courses)
* [Get Certified](https://spring.academy/learning-path)

Community

* [Overview](/community)
* [Events](/events)
* [Authors](/authors)

[Tanzu Spring](https://enterprise.spring.io)

# Guides

Whatever you're building, these guides are designed to get you productive as
quickly as possible – using the latest Spring project releases and techniques
as recommended by the Spring team.

![](/img/guides.svg)![](/img/guides-dark.svg)

![](/img/extra/microservices-4.svg)

# Category

REST APIs

IO

Data Access

Security

Messaging

Ops

Batch Processing

Web

Caching

Microservices

Testing

Documentation

Cloud Platform

Streaming

GraphQL

Misc

# Estimated Time

30mn

1h

3h

No result found.

![](/img/extra/footer.svg)

## Get ahead

VMware offers training and certification to turbo-charge your progress.

[Learn more](https://spring.academy/)

## Get support

Tanzu Spring offers support and binaries for OpenJDK™, Spring, and Apache Tomcat® in one simple subscription.

[Learn more](/support)

## Upcoming events

Check out all the upcoming events in the Spring community.

[View all](/events)

[Why Spring](/why-spring)

[Microservices](/microservices)

[Reactive](/reactive)

[Event Driven](/event-driven)

[Cloud](/cloud)

[Web Applications](/web-applications)

[Serverless](/serverless)

[Batch](/batch)

[Learn](/learn)

[Quickstart](/quickstart)

[Guides](/guides)

[Blog](/blog)

[Community](/community)

[Events](/events)

[Authors](/authors)

[Tanzu Spring](https://enterprise.spring.io)

[Spring Academy](https://spring.academy/)

[Spring Advisories](/security)

[Projects](/projects)

[Thank You](/thank-you)

## Get the Spring newsletter

Stay connected with the Spring newsletter

[Subscribe](https://go-vmware.broadcom.com/tnz-spring-newsletter-subscribe)

Copyright © 2005 - 2025 Broadcom. All Rights Reserved. The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.   
[Terms of Use](https://www.broadcom.com/company/legal/terms-of-use) • [Privacy](https://www.broadcom.com/company/legal/privacy) • [Trademark Guidelines](/trademarks)

Apache®, Apache Tomcat®, Apache Kafka®, Apache Cassandra™, and Apache Geode™ are trademarks or registered trademarks of the Apache Software Foundation in the United States and/or other countries. Java™, Java™ SE, Java™ EE, and OpenJDK™ are trademarks of Oracle and/or its affiliates. Kubernetes® is a registered trademark of the Linux Foundation in the United States and other countries. Linux® is the registered trademark of Linus Torvalds in the United States and other countries. Windows® and Microsoft® Azure are registered trademarks of Microsoft Corporation. “AWS” and “Amazon Web Services” are trademarks or registered trademarks of Amazon.com Inc. or its affiliates. All other trademarks and copyrights are property of their respective owners and are only mentioned for informative purposes. Other names may be trademarks of their respective owners.

---

## Source: index.md

Spring | Home

[Skip to main content](#main)

Why Spring

* [Overview](/why-spring)
* [Generative AI](/ai)
* [Microservices](/microservices)
* [Reactive](/reactive)
* [Event Driven](/event-driven)
* [Cloud](/cloud)
* [Web Applications](/web-applications)
* [Serverless](/serverless)
* [Batch](/batch)

Learn

* [Overview](/learn)
* [Quickstart](/quickstart)
* [Guides](/guides)
* [Blog](/blog)
* [Security Advisories](/security)

Projects

* [Overview](/projects)
* [Spring Boot](/projects/spring-boot)
* [Spring Framework](/projects/spring-framework)
* [Spring Cloud](/projects/spring-cloud)
* [Spring Cloud Data Flow](/projects/spring-cloud-dataflow)
* [Spring Data](/projects/spring-data)
* [Spring Integration](/projects/spring-integration)
* [Spring Batch](/projects/spring-batch)
* [Spring Security](/projects/spring-security)
* [Spring AI](/projects/spring-ai)
* [Release Calendar](/projects#release-calendar)
* [Security advisories](/security)
* DEVELOPMENT TOOLS
* [Spring Tools](/tools)
* [Spring Initializr](https://start.spring.io/)

Academy

* [Courses](https://spring.academy/courses)
* [Get Certified](https://spring.academy/learning-path)

Community

* [Overview](/community)
* [Events](/events)
* [Authors](/authors)

[Tanzu Spring](https://enterprise.spring.io)

# Spring makes Java simple. modern. productive. reactive. cloud-ready.

[Why Spring](/why-spring)[Quickstart](/quickstart)

# What Spring can do

[![Generative AI](/img/icons/ai.svg)

## Generative AI

Integrate AI into your Spring applications without reinventing the wheel.](/ai)

[![Microservices](/img/icons/microservices.svg)

## Microservices

Quickly deliver production‑grade features with independently evolvable microservices.](/microservices)

[![Reactive](/img/icons/reactive.svg)

## Reactive

Spring's asynchronous, nonblocking architecture means you can get more from your computing resources.](/reactive)

[![Cloud](/img/icons/cloud.svg)

## Cloud

Your code, any cloud—we’ve got you covered. Connect and scale your services, whatever your platform.](/cloud)

[![Web apps](/img/icons/web-apps.svg)

## Web apps

Frameworks for fast, secure, and responsive web applications connected to any data store.](/web-applications)

[![Serverless](/img/icons/serverless.svg)

## Serverless

The ultimate flexibility. Scale up on demand and scale to zero when there’s no demand.](/serverless)

[![Event Driven](/img/icons/event-driven.svg)

## Event Driven

Integrate with your enterprise. React to business events. Act on your streaming data in realtime.](/event-driven)

[![Batch](/img/icons/batch.svg)

## Batch

Automated tasks. Offline processing of data at a time to suit you.](/batch)

```
@SpringBootApplication  
@RestController  
public class DemoApplication {  


@GetMapping("/helloworld")  
public String hello() {

return"Hello World!";

}

}
```

## Level up your Java™ code

With [Spring Boot](/projects/spring-boot) in your app, just a few lines of code is all you need to start building services like a boss.

New to Spring? Try our simple [quickstart guide](/quickstart).

![Quote](/img/extra/quote.svg)

Most [of our] services today are all based on Spring Boot. I think the most important thing is that [Spring] has just been very well maintained over the years...that is important for us for the long term because we don’t want to be switching to a new framework every two years.

![Paul Bakker, Senior Software Engineer, Netflix](https://spring.io/img/extra/bakker-120.jpg)

Paul Bakker, Senior Software Engineer, Netflix

[Watch now](https://www.youtube.com/watch?v=mln3_o6qlBo?autoplay=1&autohide=1&showinfo=0&controls=1)

![](/img/extra/footer.svg)

## Get ahead

VMware offers training and certification to turbo-charge your progress.

[Learn more](https://spring.academy/)

## Get support

Tanzu Spring offers support and binaries for OpenJDK™, Spring, and Apache Tomcat® in one simple subscription.

[Learn more](/support)

## Upcoming events

Check out all the upcoming events in the Spring community.

[View all](/events)

[Why Spring](/why-spring)

[Microservices](/microservices)

[Reactive](/reactive)

[Event Driven](/event-driven)

[Cloud](/cloud)

[Web Applications](/web-applications)

[Serverless](/serverless)

[Batch](/batch)

[Learn](/learn)

[Quickstart](/quickstart)

[Guides](/guides)

[Blog](/blog)

[Community](/community)

[Events](/events)

[Authors](/authors)

[Tanzu Spring](https://enterprise.spring.io)

[Spring Academy](https://spring.academy/)

[Spring Advisories](/security)

[Projects](/projects)

[Thank You](/thank-you)

## Get the Spring newsletter

Stay connected with the Spring newsletter

[Subscribe](https://go-vmware.broadcom.com/tnz-spring-newsletter-subscribe)

Copyright © 2005 - 2025 Broadcom. All Rights Reserved. The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.   
[Terms of Use](https://www.broadcom.com/company/legal/terms-of-use) • [Privacy](https://www.broadcom.com/company/legal/privacy) • [Trademark Guidelines](/trademarks)

Apache®, Apache Tomcat®, Apache Kafka®, Apache Cassandra™, and Apache Geode™ are trademarks or registered trademarks of the Apache Software Foundation in the United States and/or other countries. Java™, Java™ SE, Java™ EE, and OpenJDK™ are trademarks of Oracle and/or its affiliates. Kubernetes® is a registered trademark of the Linux Foundation in the United States and other countries. Linux® is the registered trademark of Linus Torvalds in the United States and other countries. Windows® and Microsoft® Azure are registered trademarks of Microsoft Corporation. “AWS” and “Amazon Web Services” are trademarks or registered trademarks of Amazon.com Inc. or its affiliates. All other trademarks and copyrights are property of their respective owners and are only mentioned for informative purposes. Other names may be trademarks of their respective owners.

---

## Source: why-spring.md

Spring | Why Spring

[Skip to main content](#main)

Why Spring

* [Overview](/why-spring)
* [Generative AI](/ai)
* [Microservices](/microservices)
* [Reactive](/reactive)
* [Event Driven](/event-driven)
* [Cloud](/cloud)
* [Web Applications](/web-applications)
* [Serverless](/serverless)
* [Batch](/batch)

Learn

* [Overview](/learn)
* [Quickstart](/quickstart)
* [Guides](/guides)
* [Blog](/blog)
* [Security Advisories](/security)

Projects

* [Overview](/projects)
* [Spring Boot](/projects/spring-boot)
* [Spring Framework](/projects/spring-framework)
* [Spring Cloud](/projects/spring-cloud)
* [Spring Cloud Data Flow](/projects/spring-cloud-dataflow)
* [Spring Data](/projects/spring-data)
* [Spring Integration](/projects/spring-integration)
* [Spring Batch](/projects/spring-batch)
* [Spring Security](/projects/spring-security)
* [Spring AI](/projects/spring-ai)
* [Release Calendar](/projects#release-calendar)
* [Security advisories](/security)
* DEVELOPMENT TOOLS
* [Spring Tools](/tools)
* [Spring Initializr](https://start.spring.io/)

Academy

* [Courses](https://spring.academy/courses)
* [Get Certified](https://spring.academy/learning-path)

Community

* [Overview](/community)
* [Events](/events)
* [Authors](/authors)

[Tanzu Spring](https://enterprise.spring.io)

![](/img/extra/why-spring.svg)![](/img/extra/why-spring-dark.svg)

# Why Spring?

Spring makes programming Java quicker, easier, and safer for everybody. Spring’s
focus on speed, simplicity, and productivity has made it the
[world's most popular](https://www.jetbrains.com/lp/devecosystem-2023/java/)
Java framework.

![](/img/extra/quote-2.svg)![](/img/extra/quote-2-dark.svg)

“We use a lot of the tools that come with the Spring framework and reap the benefits of having a lot of the out of the box solutions, and not having to worry about writing a ton of additional code—so that really saves us some time and energy.”

SEAN GRAHAM, APPLICATION TRANSFORMATION LEAD, DICK’S SPORTING GOODS

[Watch now](https://www.youtube.com/watch?v=J66S0qP7DO4)

# Spring is everywhere

![](/img/icons/spring-is-everywhere.svg)![](/img/icons/spring-is-everywhere-dark.svg)

Spring’s flexible libraries are trusted by developers all over the world. Spring delivers delightful experiences to millions of end-users every day—whether that’s [streaming TV](https://medium.com/netflix-techblog/netflix-oss-and-spring-boot-coming-full-circle-4855947713a0), [online shopping](https://tech.target.com/2018/12/18/spring-feign.html), or countless other innovative solutions. Spring also has contributions from all the big names in tech, including Alibaba, Amazon, Google, Microsoft, and more.

# Spring is flexible

![](/img/icons/spring-is-flexible.svg)![](/img/icons/spring-is-flexible-dark.svg)

Spring’s flexible and comprehensive set of extensions and third-party libraries let developers build almost any application imaginable. At its core, Spring Framework’s [Inversion of Control (IoC)](https://en.wikipedia.org/wiki/Inversion_of_control) and [Dependency Injection (DI)](https://en.wikipedia.org/wiki/Dependency_injection) features provide the foundation for a wide-ranging set of features and functionality. Whether you’re building secure, reactive, cloud-based microservices for the web, or complex streaming data flows for the enterprise, Spring has the tools to help.

# Spring is productive

![](/img/icons/spring-is-productive.svg)![](/img/icons/spring-is-productive-dark.svg)

[Spring Boot](/guides/gs/spring-boot/) transforms how you approach Java programming tasks, radically streamlining your experience. Spring Boot combines necessities such as an application context and an auto-configured, embedded web server to make [microservice](/microservices) development a cinch. To go even faster, you can combine Spring Boot with Spring Cloud’s rich set of supporting libraries, servers, patterns, and templates, to safely deploy entire microservices-based architectures into the [cloud](/cloud), in record time.

# Spring is fast

![](/img/icons/spring-is-fast.svg)![](/img/icons/spring-is-fast-dark.svg)

Our engineers care deeply about performance. With Spring, you’ll notice fast startup, fast shutdown, and optimized execution, by default. Increasingly, Spring projects also support the [reactive](/reactive) (nonblocking) programming model for even greater efficiency. Developer productivity is Spring’s superpower. Spring Boot helps developers build applications with ease and with far less toil than other competing paradigms. Embedded web servers, auto-configuration, and “fat jars” help you get started quickly, and innovations like [LiveReload in Spring DevTools](https://docs.spring.io/spring-boot/docs/current/reference/html/using-spring-boot.html#using-boot-devtools-livereload) mean developers can iterate faster than ever before. You can even start a new Spring project in seconds, with the Spring Initializr at [start.spring.io](https://start.spring.io/).

# Spring is secure

![](/img/icons/spring-is-secure.svg)![](/img/icons/spring-is-secure-dark.svg)

Spring has a proven track record of dealing with security issues quickly and responsibly. The Spring committers work with security professionals to patch and test any reported vulnerabilities. Third-party dependencies are also monitored closely, and regular updates are issued to help keep your data and applications as safe as possible. In addition, [Spring Security](/projects/spring-security) makes it easier for you to integrate with industry-standard security schemes and deliver trustworthy solutions that are secure by default.

# Spring is supportive

![](/img/icons/spring-is-supportive.svg)![](/img/icons/spring-is-supportive-dark.svg)

The [Spring community](/community) is enormous, global, diverse, and spans folks of all ages and capabilities, from complete beginners to seasoned pros. No matter where you are on your journey, you can find the support and resources you need to get you to the next level: [quickstarts](/quickstart), [videos](/guides>guides & tutorials</a>, <a href=), [meetups](/events), [support](/support), or even formal [training and certification.](/training)

# What Spring can do?

[![Generative AI](/img/icons/ai.svg)

## Generative AI

Integrate AI into your Spring applications without reinventing the wheel.](/ai)

[![Microservices](/img/icons/microservices.svg)

## Microservices

Quickly deliver production‑grade features with independently evolvable microservices.](/microservices)

[![Reactive](/img/icons/reactive.svg)

## Reactive

Spring's asynchronous, nonblocking architecture means you can get more from your computing resources.](/reactive)

[![Cloud](/img/icons/cloud.svg)

## Cloud

Your code, any cloud—we’ve got you covered. Connect and scale your services, whatever your platform.](/cloud)

[![Web apps](/img/icons/web-apps.svg)

## Web apps

Frameworks for fast, secure, and responsive web applications connected to any data store.](/web-applications)

[![Serverless](/img/icons/serverless.svg)

## Serverless

The ultimate flexibility. Scale up on demand and scale to zero when there’s no demand.](/serverless)

[![Event Driven](/img/icons/event-driven.svg)

## Event Driven

Integrate with your enterprise. React to business events. Act on your streaming data in realtime.](/event-driven)

[![Batch](/img/icons/batch.svg)

## Batch

Automated tasks. Offline processing of data at a time to suit you.](/batch)

![](/img/extra/footer.svg)

## Get ahead

VMware offers training and certification to turbo-charge your progress.

[Learn more](https://spring.academy/)

## Get support

Tanzu Spring offers support and binaries for OpenJDK™, Spring, and Apache Tomcat® in one simple subscription.

[Learn more](/support)

## Upcoming events

Check out all the upcoming events in the Spring community.

[View all](/events)

[Why Spring](/why-spring)

[Microservices](/microservices)

[Reactive](/reactive)

[Event Driven](/event-driven)

[Cloud](/cloud)

[Web Applications](/web-applications)

[Serverless](/serverless)

[Batch](/batch)

[Learn](/learn)

[Quickstart](/quickstart)

[Guides](/guides)

[Blog](/blog)

[Community](/community)

[Events](/events)

[Authors](/authors)

[Tanzu Spring](https://enterprise.spring.io)

[Spring Academy](https://spring.academy/)

[Spring Advisories](/security)

[Projects](/projects)

[Thank You](/thank-you)

## Get the Spring newsletter

Stay connected with the Spring newsletter

[Subscribe](https://go-vmware.broadcom.com/tnz-spring-newsletter-subscribe)

Copyright © 2005 - 2025 Broadcom. All Rights Reserved. The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.   
[Terms of Use](https://www.broadcom.com/company/legal/terms-of-use) • [Privacy](https://www.broadcom.com/company/legal/privacy) • [Trademark Guidelines](/trademarks)

Apache®, Apache Tomcat®, Apache Kafka®, Apache Cassandra™, and Apache Geode™ are trademarks or registered trademarks of the Apache Software Foundation in the United States and/or other countries. Java™, Java™ SE, Java™ EE, and OpenJDK™ are trademarks of Oracle and/or its affiliates. Kubernetes® is a registered trademark of the Linux Foundation in the United States and other countries. Linux® is the registered trademark of Linus Torvalds in the United States and other countries. Windows® and Microsoft® Azure are registered trademarks of Microsoft Corporation. “AWS” and “Amazon Web Services” are trademarks or registered trademarks of Amazon.com Inc. or its affiliates. All other trademarks and copyrights are property of their respective owners and are only mentioned for informative purposes. Other names may be trademarks of their respective owners.

---
