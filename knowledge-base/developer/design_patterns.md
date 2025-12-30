# Design_patterns Knowledge

> Category: patterns_architecture

## Source: design-patterns.md

Design Patterns

]

# Design Patterns

**Design patterns** are typical solutions to common problems
in software design. Each pattern is like a blueprint
that you can customize to solve a particular
design problem in your code.

What's a design pattern?

### Catalog of patterns

List of 22 classic design patterns,
grouped by their intent.

Look inside the catalog »

### Benefits of patterns

Patterns are a toolkit of solutions to common
problems in software design. They define
a common language that helps your team
communicate more efficiently.

More about the benefits »

### Classification

Design patterns differ by their complexity, level of
detail and scale of applicability. In addition,
they can be categorized by their intent
and divided into three groups.

More about the categories »

### History of patterns

Who invented patterns and when?
Can you use patterns outside software
development? How do you do that?

More about the history »

### Criticism of patterns

Are patterns as good as advertised?
Is it always possible to use them?
Can patterns sometimes be harmful?

More about the criticism »

### Dive Into Design Patterns

Check out our ebook on design
patterns and principles. It's available in
PDF/ePUB/MOBI formats and includes the
archive with code examples in
Java, C#, C++, PHP, Python, Ruby,
Go, Swift, & TypeScript.

Learn more about the book

* Premium Content
  + Design Patterns eBook
  + Refactoring Course
* Refactoring
  + What is Refactoring
    - Clean code
    - Technical debt
    - When to refactor
    - How to refactor
  + Catalog
  + Code Smells
    - Bloaters
      * Long Method
      * Large Class
      * Primitive Obsession
      * Long Parameter List
      * Data Clumps
    - Object-Orientation Abusers
      * Switch Statements
      * Temporary Field
      * Refused Bequest
      * Alternative Classes with Different Interfaces
    - Change Preventers
      * Divergent Change
      * Shotgun Surgery
      * Parallel Inheritance Hierarchies
    - Dispensables
      * Comments
      * Duplicate Code
      * Lazy Class
      * Data Class
      * Dead Code
      * Speculative Generality
    - Couplers
      * Feature Envy
      * Inappropriate Intimacy
      * Message Chains
      * Middle Man
    - Other Smells
      * Incomplete Library Class
  + Refactorings
    - Composing Methods
      * Extract Method
      * Inline Method
      * Extract Variable
      * Inline Temp
      * Replace Temp with Query
      * Split Temporary Variable
      * Remove Assignments to Parameters
      * Replace Method with Method Object
      * Substitute Algorithm
    - Moving Features between Objects
      * Move Method
      * Move Field
      * Extract Class
      * Inline Class
      * Hide Delegate
      * Remove Middle Man
      * Introduce Foreign Method
      * Introduce Local Extension
    - Organizing Data
      * Self Encapsulate Field
      * Replace Data Value with Object
      * Change Value to Reference
      * Change Reference to Value
      * Replace Array with Object
      * Duplicate Observed Data
      * Change Unidirectional Association to Bidirectional
      * Change Bidirectional Association to Unidirectional
      * Replace Magic Number with Symbolic Constant
      * Encapsulate Field
      * Encapsulate Collection
      * Replace Type Code with Class
      * Replace Type Code with Subclasses
      * Replace Type Code with State/Strategy
      * Replace Subclass with Fields
    - Simplifying Conditional Expressions
      * Decompose Conditional
      * Consolidate Conditional Expression
      * Consolidate Duplicate Conditional Fragments
      * Remove Control Flag
      * Replace Nested Conditional with Guard Clauses
      * Replace Conditional with Polymorphism
      * Introduce Null Object
      * Introduce Assertion
    - Simplifying Method Calls
      * Rename Method
      * Add Parameter
      * Remove Parameter
      * Separate Query from Modifier
      * Parameterize Method
      * Replace Parameter with Explicit Methods
      * Preserve Whole Object
      * Replace Parameter with Method Call
      * Introduce Parameter Object
      * Remove Setting Method
      * Hide Method
      * Replace Constructor with Factory Method
      * Replace Error Code with Exception
      * Replace Exception with Test
    - Dealing with Generalization
      * Pull Up Field
      * Pull Up Method
      * Pull Up Constructor Body
      * Push Down Method
      * Push Down Field
      * Extract Subclass
      * Extract Superclass
      * Extract Interface
      * Collapse Hierarchy
      * Form Template Method
      * Replace Inheritance with Delegation
      * Replace Delegation with Inheritance
* Design Patterns
  + What is a Pattern
    - What's a design pattern?
    - History of patterns
    - Why should I learn patterns?
    - Criticism of patterns
    - Classification of patterns
  + Catalog
  + Creational Patterns
    - Factory Method
    - Abstract Factory
    - Builder
    - Prototype
    - Singleton
  + Structural Patterns
    - Adapter
    - Bridge
    - Composite
    - Decorator
    - Facade
    - Flyweight
    - Proxy
  + Behavioral Patterns
    - Chain of Responsibility
    - Command
    - Iterator
    - Mediator
    - Memento
    - Observer
    - State
    - Strategy
    - Template Method
    - Visitor
  + Code Examples
    - C
    - C++
    - Go
    - Java
    - PHP
    - Python
    - Ruby
    - Rust
    - Swift
    - TypeScript

Sign in
 Contact us

Shop Now!

* English

  English
  Español
  Français
  日本語
  한국어
  Polski
  Português Brasileiro
  Русский
  Українська
  中文
* Contact us
* Sign in

* Home
* Refactoring
* Design Patterns
* Premium Content
* Git Course
* Forum
* Contact us

2014-2025 Refactoring.Guru. All rights reserved.  
 Illustrations by Dmitry Zhart

* Terms & Conditions
* Privacy Policy
* Content Usage Policy
* About us

**Ukrainian office:**  

 Abolmasova 7  
Kyiv, Ukraine, 02002  
 Email: support@refactoring.guru

**Spanish office:**  

 Avda Pamplona 64  
Pamplona, Spain, 31009  
 Email: support@refactoring.guru

---

## Source: design-patterns_catalog.md

The Catalog of Design Patterns

]

# The Catalog of Design Patterns

### Creational patterns

These patterns provide various object creation mechanisms, which increase flexibility and reuse of existing code.

### Structural patterns

These patterns explain how to assemble objects and classes into larger structures while keeping these structures flexible and efficient.

### Behavioral patterns

These patterns are concerned with algorithms and the assignment of responsibilities between objects.

* Premium Content
  + Design Patterns eBook
  + Refactoring Course
* Refactoring
  + What is Refactoring
    - Clean code
    - Technical debt
    - When to refactor
    - How to refactor
  + Catalog
  + Code Smells
    - Bloaters
      * Long Method
      * Large Class
      * Primitive Obsession
      * Long Parameter List
      * Data Clumps
    - Object-Orientation Abusers
      * Switch Statements
      * Temporary Field
      * Refused Bequest
      * Alternative Classes with Different Interfaces
    - Change Preventers
      * Divergent Change
      * Shotgun Surgery
      * Parallel Inheritance Hierarchies
    - Dispensables
      * Comments
      * Duplicate Code
      * Lazy Class
      * Data Class
      * Dead Code
      * Speculative Generality
    - Couplers
      * Feature Envy
      * Inappropriate Intimacy
      * Message Chains
      * Middle Man
    - Other Smells
      * Incomplete Library Class
  + Refactorings
    - Composing Methods
      * Extract Method
      * Inline Method
      * Extract Variable
      * Inline Temp
      * Replace Temp with Query
      * Split Temporary Variable
      * Remove Assignments to Parameters
      * Replace Method with Method Object
      * Substitute Algorithm
    - Moving Features between Objects
      * Move Method
      * Move Field
      * Extract Class
      * Inline Class
      * Hide Delegate
      * Remove Middle Man
      * Introduce Foreign Method
      * Introduce Local Extension
    - Organizing Data
      * Self Encapsulate Field
      * Replace Data Value with Object
      * Change Value to Reference
      * Change Reference to Value
      * Replace Array with Object
      * Duplicate Observed Data
      * Change Unidirectional Association to Bidirectional
      * Change Bidirectional Association to Unidirectional
      * Replace Magic Number with Symbolic Constant
      * Encapsulate Field
      * Encapsulate Collection
      * Replace Type Code with Class
      * Replace Type Code with Subclasses
      * Replace Type Code with State/Strategy
      * Replace Subclass with Fields
    - Simplifying Conditional Expressions
      * Decompose Conditional
      * Consolidate Conditional Expression
      * Consolidate Duplicate Conditional Fragments
      * Remove Control Flag
      * Replace Nested Conditional with Guard Clauses
      * Replace Conditional with Polymorphism
      * Introduce Null Object
      * Introduce Assertion
    - Simplifying Method Calls
      * Rename Method
      * Add Parameter
      * Remove Parameter
      * Separate Query from Modifier
      * Parameterize Method
      * Replace Parameter with Explicit Methods
      * Preserve Whole Object
      * Replace Parameter with Method Call
      * Introduce Parameter Object
      * Remove Setting Method
      * Hide Method
      * Replace Constructor with Factory Method
      * Replace Error Code with Exception
      * Replace Exception with Test
    - Dealing with Generalization
      * Pull Up Field
      * Pull Up Method
      * Pull Up Constructor Body
      * Push Down Method
      * Push Down Field
      * Extract Subclass
      * Extract Superclass
      * Extract Interface
      * Collapse Hierarchy
      * Form Template Method
      * Replace Inheritance with Delegation
      * Replace Delegation with Inheritance
* Design Patterns
  + What is a Pattern
    - What's a design pattern?
    - History of patterns
    - Why should I learn patterns?
    - Criticism of patterns
    - Classification of patterns
  + Catalog
  + Creational Patterns
    - Factory Method
    - Abstract Factory
    - Builder
    - Prototype
    - Singleton
  + Structural Patterns
    - Adapter
    - Bridge
    - Composite
    - Decorator
    - Facade
    - Flyweight
    - Proxy
  + Behavioral Patterns
    - Chain of Responsibility
    - Command
    - Iterator
    - Mediator
    - Memento
    - Observer
    - State
    - Strategy
    - Template Method
    - Visitor
  + Code Examples
    - C
    - C++
    - Go
    - Java
    - PHP
    - Python
    - Ruby
    - Rust
    - Swift
    - TypeScript

Sign in
 Contact us

Shop Now!

* English

  English
  Español
  Français
  日本語
  한국어
  Polski
  Português Brasileiro
  Русский
  Українська
  中文
* Contact us
* Sign in

* Home
* Refactoring
* Design Patterns
* Premium Content
* Git Course
* Forum
* Contact us

2014-2025 Refactoring.Guru. All rights reserved.  
 Illustrations by Dmitry Zhart

* Terms & Conditions
* Privacy Policy
* Content Usage Policy
* About us

**Ukrainian office:**  

 Abolmasova 7  
Kyiv, Ukraine, 02002  
 Email: support@refactoring.guru

**Spanish office:**  

 Avda Pamplona 64  
Pamplona, Spain, 31009  
 Email: support@refactoring.guru

---

## Source: design-patterns_what-is-pattern.md

What's a design pattern?

]

/ Design Patterns

# What's a design pattern?

**Design patterns** are typical solutions to commonly occurring problems in software design. They are like pre-made blueprints that you can customize to solve a recurring design problem in your code.

You can’t just find a pattern and copy it into your program, the way you can with off-the-shelf functions or libraries. The pattern is not a specific piece of code, but a general concept for solving a particular problem. You can follow the pattern details and implement a solution that suits the realities of your own program.

Patterns are often confused with algorithms, because both concepts describe typical solutions to some known problems. While an algorithm always defines a clear set of actions that can achieve some goal, a pattern is a more high-level description of a solution. The code of the same pattern applied to two different programs may be different.

An analogy to an algorithm is a cooking recipe: both have clear steps to achieve a goal. On the other hand, a pattern is more like a blueprint: you can see what the result and its features are, but the exact order of implementation is up to you.

## What does the pattern consist of?

Most patterns are described very formally so people can reproduce them in many contexts. Here are the sections that are usually present in a pattern description:

* **Intent** of the pattern briefly describes both the problem and the solution.
* **Motivation** further explains the problem and the solution the pattern makes possible.
* **Structure** of classes shows each part of the pattern and how they are related.
* **Code example** in one of the popular programming languages makes it easier to grasp the idea behind the pattern.

Some pattern catalogs list other useful details, such as applicability of the pattern, implementation steps and relations with other patterns.

#### Read next

History of patterns

#### Return

Design Patterns

* Premium Content
  + Design Patterns eBook
  + Refactoring Course
* Refactoring
  + What is Refactoring
    - Clean code
    - Technical debt
    - When to refactor
    - How to refactor
  + Catalog
  + Code Smells
    - Bloaters
      * Long Method
      * Large Class
      * Primitive Obsession
      * Long Parameter List
      * Data Clumps
    - Object-Orientation Abusers
      * Switch Statements
      * Temporary Field
      * Refused Bequest
      * Alternative Classes with Different Interfaces
    - Change Preventers
      * Divergent Change
      * Shotgun Surgery
      * Parallel Inheritance Hierarchies
    - Dispensables
      * Comments
      * Duplicate Code
      * Lazy Class
      * Data Class
      * Dead Code
      * Speculative Generality
    - Couplers
      * Feature Envy
      * Inappropriate Intimacy
      * Message Chains
      * Middle Man
    - Other Smells
      * Incomplete Library Class
  + Refactorings
    - Composing Methods
      * Extract Method
      * Inline Method
      * Extract Variable
      * Inline Temp
      * Replace Temp with Query
      * Split Temporary Variable
      * Remove Assignments to Parameters
      * Replace Method with Method Object
      * Substitute Algorithm
    - Moving Features between Objects
      * Move Method
      * Move Field
      * Extract Class
      * Inline Class
      * Hide Delegate
      * Remove Middle Man
      * Introduce Foreign Method
      * Introduce Local Extension
    - Organizing Data
      * Self Encapsulate Field
      * Replace Data Value with Object
      * Change Value to Reference
      * Change Reference to Value
      * Replace Array with Object
      * Duplicate Observed Data
      * Change Unidirectional Association to Bidirectional
      * Change Bidirectional Association to Unidirectional
      * Replace Magic Number with Symbolic Constant
      * Encapsulate Field
      * Encapsulate Collection
      * Replace Type Code with Class
      * Replace Type Code with Subclasses
      * Replace Type Code with State/Strategy
      * Replace Subclass with Fields
    - Simplifying Conditional Expressions
      * Decompose Conditional
      * Consolidate Conditional Expression
      * Consolidate Duplicate Conditional Fragments
      * Remove Control Flag
      * Replace Nested Conditional with Guard Clauses
      * Replace Conditional with Polymorphism
      * Introduce Null Object
      * Introduce Assertion
    - Simplifying Method Calls
      * Rename Method
      * Add Parameter
      * Remove Parameter
      * Separate Query from Modifier
      * Parameterize Method
      * Replace Parameter with Explicit Methods
      * Preserve Whole Object
      * Replace Parameter with Method Call
      * Introduce Parameter Object
      * Remove Setting Method
      * Hide Method
      * Replace Constructor with Factory Method
      * Replace Error Code with Exception
      * Replace Exception with Test
    - Dealing with Generalization
      * Pull Up Field
      * Pull Up Method
      * Pull Up Constructor Body
      * Push Down Method
      * Push Down Field
      * Extract Subclass
      * Extract Superclass
      * Extract Interface
      * Collapse Hierarchy
      * Form Template Method
      * Replace Inheritance with Delegation
      * Replace Delegation with Inheritance
* Design Patterns
  + What is a Pattern
    - What's a design pattern?
    - History of patterns
    - Why should I learn patterns?
    - Criticism of patterns
    - Classification of patterns
  + Catalog
  + Creational Patterns
    - Factory Method
    - Abstract Factory
    - Builder
    - Prototype
    - Singleton
  + Structural Patterns
    - Adapter
    - Bridge
    - Composite
    - Decorator
    - Facade
    - Flyweight
    - Proxy
  + Behavioral Patterns
    - Chain of Responsibility
    - Command
    - Iterator
    - Mediator
    - Memento
    - Observer
    - State
    - Strategy
    - Template Method
    - Visitor
  + Code Examples
    - C
    - C++
    - Go
    - Java
    - PHP
    - Python
    - Ruby
    - Rust
    - Swift
    - TypeScript

Sign in
 Contact us

Shop Now!

* English

  English
  Español
  Français
  日本語
  한국어
  Polski
  Português Brasileiro
  Русский
  Українська
  中文
* Contact us
* Sign in

* Home
* Refactoring
* Design Patterns
* Premium Content
* Git Course
* Forum
* Contact us

2014-2025 Refactoring.Guru. All rights reserved.  
 Illustrations by Dmitry Zhart

* Terms & Conditions
* Privacy Policy
* Content Usage Policy
* About us

**Ukrainian office:**  

 Abolmasova 7  
Kyiv, Ukraine, 02002  
 Email: support@refactoring.guru

**Spanish office:**  

 Avda Pamplona 64  
Pamplona, Spain, 31009  
 Email: support@refactoring.guru

---

## Source: store.md

Premium products

]

# Meet our products!

New! A volume discount is available when buying 5 copies or more.
  
You can now order the products as a gift to someone else, schedule the delivery, etc.
  
You can also easily order for your entire team. This will allow you to track their progress.

R$229,00
Christmas SALER$79,95

plus local tax

including local tax

 Buy now

Learn more

R$169,00
Christmas SALER$49,95

plus local tax

including local tax

 Buy now

Learn more

## GitByBit PRO

My new creation, GitByBit is a unique course that teaches you Git through practice right in your code editor (VS Code or Cursor). It's beautiful, fun and engaging.

The core version is free. However, you can upgrade to the PRO version to practice advanced Git skills essential for teamwork, including merging, rebasing, pull requests, and more.

*The course is currently available only in English. If there’s enough interest, translations are planned for 2026 as a free update.*

R$229,00
Christmas SALER$79,95

plus local tax

including local tax

 Buy now

Learn more

* Premium Content
  + Design Patterns eBook
  + Refactoring Course
* Refactoring
  + What is Refactoring
    - Clean code
    - Technical debt
    - When to refactor
    - How to refactor
  + Catalog
  + Code Smells
    - Bloaters
      * Long Method
      * Large Class
      * Primitive Obsession
      * Long Parameter List
      * Data Clumps
    - Object-Orientation Abusers
      * Switch Statements
      * Temporary Field
      * Refused Bequest
      * Alternative Classes with Different Interfaces
    - Change Preventers
      * Divergent Change
      * Shotgun Surgery
      * Parallel Inheritance Hierarchies
    - Dispensables
      * Comments
      * Duplicate Code
      * Lazy Class
      * Data Class
      * Dead Code
      * Speculative Generality
    - Couplers
      * Feature Envy
      * Inappropriate Intimacy
      * Message Chains
      * Middle Man
    - Other Smells
      * Incomplete Library Class
  + Refactorings
    - Composing Methods
      * Extract Method
      * Inline Method
      * Extract Variable
      * Inline Temp
      * Replace Temp with Query
      * Split Temporary Variable
      * Remove Assignments to Parameters
      * Replace Method with Method Object
      * Substitute Algorithm
    - Moving Features between Objects
      * Move Method
      * Move Field
      * Extract Class
      * Inline Class
      * Hide Delegate
      * Remove Middle Man
      * Introduce Foreign Method
      * Introduce Local Extension
    - Organizing Data
      * Self Encapsulate Field
      * Replace Data Value with Object
      * Change Value to Reference
      * Change Reference to Value
      * Replace Array with Object
      * Duplicate Observed Data
      * Change Unidirectional Association to Bidirectional
      * Change Bidirectional Association to Unidirectional
      * Replace Magic Number with Symbolic Constant
      * Encapsulate Field
      * Encapsulate Collection
      * Replace Type Code with Class
      * Replace Type Code with Subclasses
      * Replace Type Code with State/Strategy
      * Replace Subclass with Fields
    - Simplifying Conditional Expressions
      * Decompose Conditional
      * Consolidate Conditional Expression
      * Consolidate Duplicate Conditional Fragments
      * Remove Control Flag
      * Replace Nested Conditional with Guard Clauses
      * Replace Conditional with Polymorphism
      * Introduce Null Object
      * Introduce Assertion
    - Simplifying Method Calls
      * Rename Method
      * Add Parameter
      * Remove Parameter
      * Separate Query from Modifier
      * Parameterize Method
      * Replace Parameter with Explicit Methods
      * Preserve Whole Object
      * Replace Parameter with Method Call
      * Introduce Parameter Object
      * Remove Setting Method
      * Hide Method
      * Replace Constructor with Factory Method
      * Replace Error Code with Exception
      * Replace Exception with Test
    - Dealing with Generalization
      * Pull Up Field
      * Pull Up Method
      * Pull Up Constructor Body
      * Push Down Method
      * Push Down Field
      * Extract Subclass
      * Extract Superclass
      * Extract Interface
      * Collapse Hierarchy
      * Form Template Method
      * Replace Inheritance with Delegation
      * Replace Delegation with Inheritance
* Design Patterns
  + What is a Pattern
    - What's a design pattern?
    - History of patterns
    - Why should I learn patterns?
    - Criticism of patterns
    - Classification of patterns
  + Catalog
  + Creational Patterns
    - Factory Method
    - Abstract Factory
    - Builder
    - Prototype
    - Singleton
  + Structural Patterns
    - Adapter
    - Bridge
    - Composite
    - Decorator
    - Facade
    - Flyweight
    - Proxy
  + Behavioral Patterns
    - Chain of Responsibility
    - Command
    - Iterator
    - Mediator
    - Memento
    - Observer
    - State
    - Strategy
    - Template Method
    - Visitor
  + Code Examples
    - C
    - C++
    - Go
    - Java
    - PHP
    - Python
    - Ruby
    - Rust
    - Swift
    - TypeScript

Sign in
 Contact us

Shop Now!

* English

  English
  Español
  Français
  日本語
  한국어
  Polski
  Português Brasileiro
  Русский
  Українська
  中文
* Contact us
* Sign in

* Home
* Refactoring
* Design Patterns
* Premium Content
* Git Course
* Forum
* Contact us

2014-2025 Refactoring.Guru. All rights reserved.  
 Illustrations by Dmitry Zhart

* Terms & Conditions
* Privacy Policy
* Content Usage Policy
* About us

**Ukrainian office:**  

 Abolmasova 7  
Kyiv, Ukraine, 02002  
 Email: support@refactoring.guru

**Spanish office:**  

 Avda Pamplona 64  
Pamplona, Spain, 31009  
 Email: support@refactoring.guru

---