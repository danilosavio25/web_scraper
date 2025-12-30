# Spring Knowledge

> Category: frameworks

## Source: ai.md

Spring | Generative AI

Skip to main content

Why Spring

* Overview
* Generative AI
* Microservices
* Reactive
* Event Driven
* Cloud
* Web Applications
* Serverless
* Batch

Learn

* Overview
* Quickstart
* Guides
* Security Advisories

Projects

* Overview
* Spring Boot
* Spring Framework
* Spring Cloud
* Spring Cloud Data Flow
* Spring Data
* Spring Integration
* Spring Batch
* Spring Security
* Spring AI
* Release Calendar
* Security advisories
* DEVELOPMENT TOOLS
* Spring Tools
* Spring Initializr

Academy

* Courses
* Get Certified

Community

* Overview
* Events
* Authors

Tanzu Spring

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

Get started with ChatClients

Portable Chat Models

# Tool Calling

Tool calling allows you to register your own functions to connect the LLMs to the APIs of external systems. These systems can provide LLMs with real-time data and perform data processing actions on their behalf. Spring AI greatly simplifies code you need to write to support function invocation. It handles the function invocation conversation for you. You can provide your function as a @Bean and then provide the bean name of the function in your prompt options to activate that function. Additionally, you can define and reference multiple functions in a single prompt.

Get started with Tool Calling

# Model Context Protocol (MCP)

Standardized protocol that enables AI models and Agents to interact with external tools and resources in a structured way. It supports multiple transport mechanisms to provide flexibility across different environments.

Get started with MCP

# Retrieval Augmented Generation

At its core, Spring AI addresses the fundamental challenge of AI integration - Connecting your enterprise Data and APIs with the AI Models. A technique termed Retrieval Augmented Generation (RAG) has emerged to address the challenge of incorporating relevant data into prompts for accurate AI model responses.Spring AI greatly simplifies code you need to write to support RAG pipelines.

Get started with RAG

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

TRY OUR QUICKSTART GUIDE

## More resources

!AI Powered Flight booking system!AI Powered Flight booking system

# AI Powered Flight booking system

Christian Tzolov

## Get ahead

VMware offers training and certification to turbo-charge your progress.

Learn more

## Get support

Tanzu Spring offers support and binaries for OpenJDK™, Spring, and Apache Tomcat® in one simple subscription.

Learn more

## Upcoming events

Check out all the upcoming events in the Spring community.

View all

Why Spring

Microservices

Reactive

Event Driven

Cloud

Web Applications

Serverless

Batch

Learn

Quickstart

Guides

Blog

Community

Events

Authors

Tanzu Spring

Spring Academy

Spring Advisories

Projects

Thank You

## Get the Spring newsletter

Stay connected with the Spring newsletter

Subscribe

Copyright © 2005 - 2025 Broadcom. All Rights Reserved. The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.   
Terms of Use • Privacy • Trademark Guidelines

Apache®, Apache Tomcat®, Apache Kafka®, Apache Cassandra™, and Apache Geode™ are trademarks or registered trademarks of the Apache Software Foundation in the United States and/or other countries. Java™, Java™ SE, Java™ EE, and OpenJDK™ are trademarks of Oracle and/or its affiliates. Kubernetes® is a registered trademark of the Linux Foundation in the United States and other countries. Linux® is the registered trademark of Linus Torvalds in the United States and other countries. Windows® and Microsoft® Azure are registered trademarks of Microsoft Corporation. “AWS” and “Amazon Web Services” are trademarks or registered trademarks of Amazon.com Inc. or its affiliates. All other trademarks and copyrights are property of their respective owners and are only mentioned for informative purposes. Other names may be trademarks of their respective owners.

---

## Source: guides.md

Spring | Guides

Skip to main content

Why Spring

* Overview
* Generative AI
* Microservices
* Reactive
* Event Driven
* Cloud
* Web Applications
* Serverless
* Batch

Learn

* Overview
* Quickstart
* Guides
* Security Advisories

Projects

* Overview
* Spring Boot
* Spring Framework
* Spring Cloud
* Spring Cloud Data Flow
* Spring Data
* Spring Integration
* Spring Batch
* Spring Security
* Spring AI
* Release Calendar
* Security advisories
* DEVELOPMENT TOOLS
* Spring Tools
* Spring Initializr

Academy

* Courses
* Get Certified

Community

* Overview
* Events
* Authors

Tanzu Spring

# Guides

Whatever you're building, these guides are designed to get you productive as
quickly as possible – using the latest Spring project releases and techniques
as recommended by the Spring team.

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

## Get ahead

VMware offers training and certification to turbo-charge your progress.

Learn more

## Get support

Tanzu Spring offers support and binaries for OpenJDK™, Spring, and Apache Tomcat® in one simple subscription.

Learn more

## Upcoming events

Check out all the upcoming events in the Spring community.

View all

Why Spring

Microservices

Reactive

Event Driven

Cloud

Web Applications

Serverless

Batch

Learn

Quickstart

Guides

Blog

Community

Events

Authors

Tanzu Spring

Spring Academy

Spring Advisories

Projects

Thank You

## Get the Spring newsletter

Stay connected with the Spring newsletter

Subscribe

Copyright © 2005 - 2025 Broadcom. All Rights Reserved. The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.   
Terms of Use • Privacy • Trademark Guidelines

Apache®, Apache Tomcat®, Apache Kafka®, Apache Cassandra™, and Apache Geode™ are trademarks or registered trademarks of the Apache Software Foundation in the United States and/or other countries. Java™, Java™ SE, Java™ EE, and OpenJDK™ are trademarks of Oracle and/or its affiliates. Kubernetes® is a registered trademark of the Linux Foundation in the United States and other countries. Linux® is the registered trademark of Linus Torvalds in the United States and other countries. Windows® and Microsoft® Azure are registered trademarks of Microsoft Corporation. “AWS” and “Amazon Web Services” are trademarks or registered trademarks of Amazon.com Inc. or its affiliates. All other trademarks and copyrights are property of their respective owners and are only mentioned for informative purposes. Other names may be trademarks of their respective owners.

---

## Source: index.md

Spring | Home

Skip to main content

Why Spring

* Overview
* Generative AI
* Microservices
* Reactive
* Event Driven
* Cloud
* Web Applications
* Serverless
* Batch

Learn

* Overview
* Quickstart
* Guides
* Security Advisories

Projects

* Overview
* Spring Boot
* Spring Framework
* Spring Cloud
* Spring Cloud Data Flow
* Spring Data
* Spring Integration
* Spring Batch
* Spring Security
* Spring AI
* Release Calendar
* Security advisories
* DEVELOPMENT TOOLS
* Spring Tools
* Spring Initializr

Academy

* Courses
* Get Certified

Community

* Overview
* Events
* Authors

Tanzu Spring

# Spring makes Java simple. modern. productive. reactive. cloud-ready.

Why SpringQuickstart

# What Spring can do

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

With Spring Boot in your app, just a few lines of code is all you need to start building services like a boss.

New to Spring? Try our simple quickstart guide.

Most [of our] services today are all based on Spring Boot. I think the most important thing is that [Spring] has just been very well maintained over the years...that is important for us for the long term because we don’t want to be switching to a new framework every two years.

Paul Bakker, Senior Software Engineer, Netflix

Watch now

## Get ahead

VMware offers training and certification to turbo-charge your progress.

Learn more

## Get support

Tanzu Spring offers support and binaries for OpenJDK™, Spring, and Apache Tomcat® in one simple subscription.

Learn more

## Upcoming events

Check out all the upcoming events in the Spring community.

View all

Why Spring

Microservices

Reactive

Event Driven

Cloud

Web Applications

Serverless

Batch

Learn

Quickstart

Guides

Blog

Community

Events

Authors

Tanzu Spring

Spring Academy

Spring Advisories

Projects

Thank You

## Get the Spring newsletter

Stay connected with the Spring newsletter

Subscribe

Copyright © 2005 - 2025 Broadcom. All Rights Reserved. The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.   
Terms of Use • Privacy • Trademark Guidelines

Apache®, Apache Tomcat®, Apache Kafka®, Apache Cassandra™, and Apache Geode™ are trademarks or registered trademarks of the Apache Software Foundation in the United States and/or other countries. Java™, Java™ SE, Java™ EE, and OpenJDK™ are trademarks of Oracle and/or its affiliates. Kubernetes® is a registered trademark of the Linux Foundation in the United States and other countries. Linux® is the registered trademark of Linus Torvalds in the United States and other countries. Windows® and Microsoft® Azure are registered trademarks of Microsoft Corporation. “AWS” and “Amazon Web Services” are trademarks or registered trademarks of Amazon.com Inc. or its affiliates. All other trademarks and copyrights are property of their respective owners and are only mentioned for informative purposes. Other names may be trademarks of their respective owners.

---

## Source: why-spring.md

Spring | Why Spring

Skip to main content

Why Spring

* Overview
* Generative AI
* Microservices
* Reactive
* Event Driven
* Cloud
* Web Applications
* Serverless
* Batch

Learn

* Overview
* Quickstart
* Guides
* Security Advisories

Projects

* Overview
* Spring Boot
* Spring Framework
* Spring Cloud
* Spring Cloud Data Flow
* Spring Data
* Spring Integration
* Spring Batch
* Spring Security
* Spring AI
* Release Calendar
* Security advisories
* DEVELOPMENT TOOLS
* Spring Tools
* Spring Initializr

Academy

* Courses
* Get Certified

Community

* Overview
* Events
* Authors

Tanzu Spring

# Why Spring?

Spring makes programming Java quicker, easier, and safer for everybody. Spring’s
focus on speed, simplicity, and productivity has made it the
world's most popular
Java framework.

“We use a lot of the tools that come with the Spring framework and reap the benefits of having a lot of the out of the box solutions, and not having to worry about writing a ton of additional code—so that really saves us some time and energy.”

SEAN GRAHAM, APPLICATION TRANSFORMATION LEAD, DICK’S SPORTING GOODS

Watch now

# Spring is everywhere

Spring’s flexible libraries are trusted by developers all over the world. Spring delivers delightful experiences to millions of end-users every day—whether that’s streaming TV, online shopping, or countless other innovative solutions. Spring also has contributions from all the big names in tech, including Alibaba, Amazon, Google, Microsoft, and more.

# Spring is flexible

Spring’s flexible and comprehensive set of extensions and third-party libraries let developers build almost any application imaginable. At its core, Spring Framework’s Inversion of Control (IoC) and Dependency Injection (DI) features provide the foundation for a wide-ranging set of features and functionality. Whether you’re building secure, reactive, cloud-based microservices for the web, or complex streaming data flows for the enterprise, Spring has the tools to help.

# Spring is productive

Spring Boot transforms how you approach Java programming tasks, radically streamlining your experience. Spring Boot combines necessities such as an application context and an auto-configured, embedded web server to make microservice development a cinch. To go even faster, you can combine Spring Boot with Spring Cloud’s rich set of supporting libraries, servers, patterns, and templates, to safely deploy entire microservices-based architectures into the cloud, in record time.

# Spring is fast

Our engineers care deeply about performance. With Spring, you’ll notice fast startup, fast shutdown, and optimized execution, by default. Increasingly, Spring projects also support the reactive (nonblocking) programming model for even greater efficiency. Developer productivity is Spring’s superpower. Spring Boot helps developers build applications with ease and with far less toil than other competing paradigms. Embedded web servers, auto-configuration, and “fat jars” help you get started quickly, and innovations like LiveReload in Spring DevTools mean developers can iterate faster than ever before. You can even start a new Spring project in seconds, with the Spring Initializr at start.spring.io.

# Spring is secure

Spring has a proven track record of dealing with security issues quickly and responsibly. The Spring committers work with security professionals to patch and test any reported vulnerabilities. Third-party dependencies are also monitored closely, and regular updates are issued to help keep your data and applications as safe as possible. In addition, Spring Security makes it easier for you to integrate with industry-standard security schemes and deliver trustworthy solutions that are secure by default.

# Spring is supportive

The Spring community is enormous, global, diverse, and spans folks of all ages and capabilities, from complete beginners to seasoned pros. No matter where you are on your journey, you can find the support and resources you need to get you to the next level: quickstarts, videos, meetups, support, or even formal training and certification.

# What Spring can do?

## Get ahead

VMware offers training and certification to turbo-charge your progress.

Learn more

## Get support

Tanzu Spring offers support and binaries for OpenJDK™, Spring, and Apache Tomcat® in one simple subscription.

Learn more

## Upcoming events

Check out all the upcoming events in the Spring community.

View all

Why Spring

Microservices

Reactive

Event Driven

Cloud

Web Applications

Serverless

Batch

Learn

Quickstart

Guides

Blog

Community

Events

Authors

Tanzu Spring

Spring Academy

Spring Advisories

Projects

Thank You

## Get the Spring newsletter

Stay connected with the Spring newsletter

Subscribe

Copyright © 2005 - 2025 Broadcom. All Rights Reserved. The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.   
Terms of Use • Privacy • Trademark Guidelines

Apache®, Apache Tomcat®, Apache Kafka®, Apache Cassandra™, and Apache Geode™ are trademarks or registered trademarks of the Apache Software Foundation in the United States and/or other countries. Java™, Java™ SE, Java™ EE, and OpenJDK™ are trademarks of Oracle and/or its affiliates. Kubernetes® is a registered trademark of the Linux Foundation in the United States and other countries. Linux® is the registered trademark of Linus Torvalds in the United States and other countries. Windows® and Microsoft® Azure are registered trademarks of Microsoft Corporation. “AWS” and “Amazon Web Services” are trademarks or registered trademarks of Amazon.com Inc. or its affiliates. All other trademarks and copyrights are property of their respective owners and are only mentioned for informative purposes. Other names may be trademarks of their respective owners.

---