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