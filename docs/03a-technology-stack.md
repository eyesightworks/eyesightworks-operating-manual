# EyesightWorks Technologies Operating Manual

**Document:** 03A of 21

**Title:** Technology Stack

**Version:** 1.1

**Status:** Approved

**Owner:** EyesightWorks Technologies

**Last Updated:** 2026-09-21

---

# Revision History

| Version | Date       | Changes                                                                                                                                                         |
| ------- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.0     | 2026-08-05 | Initial Technology Stack                                                                                                                                        |
| 1.1     | 2026-09-21 | Updated approved stack, added Python/FastAPI and Flutter, clarified AI, cloud, payment, containerization, monitoring, testing, and deferred technology strategy |

---

# Technology Stack

## Executive Summary

This document defines the approved technology direction for EyesightWorks Technologies.

Its purpose is to standardize the primary technologies used across company products while allowing the platform to evolve as business requirements change.

Technology choices exist to support business objectives rather than personal preference.

Every approved technology should improve one or more of the following:

* Customer Value
* Engineering Productivity
* Platform Scalability
* Operational Reliability
* Security
* Long-Term Maintainability
* Cost Efficiency

This document defines **what technologies are approved, what role they serve, and when additional technologies may be introduced**.

It does not define:

* Business requirements
* Product requirements
* Application architecture
* Module organization
* Database schemas
* Coding standards
* Git workflows
* Testing processes
* Operational procedures

Those subjects are documented separately within the Operating Manual.

---

# Technology Philosophy

Technology supports business outcomes.

EyesightWorks Technologies follows these principles:

* Choose proven technologies over unnecessary experimentation.
* Prefer simplicity over unnecessary complexity.
* Build reusable capabilities where reuse creates value.
* Use cloud-ready and container-friendly technologies.
* Automate repetitive engineering work.
* Optimize for maintainability.
* Prioritize security.
* Introduce new technologies only when they solve a real problem.
* Prefer technologies the company can realistically operate and support.
* Avoid adopting technology simply because it is popular or trending.

Technology should serve the company rather than drive company strategy.

---

# Technology Selection Hierarchy

Technology selection should follow:

```text
Business Requirement
        ↓
Product Requirement
        ↓
Architecture Requirement
        ↓
Technology Selection
        ↓
Implementation
        ↓
Measurement
        ↓
Improvement
```

Technology should not determine what business problem the company solves.

---

# Approved Technology Structure

The technology stack is organized into:

```text
Web
 ↓
Backend
 ↓
Data
 ↓
Infrastructure
 ↓
AI / Specialized Services
 ↓
Mobile
 ↓
Payments
 ↓
Developer Tooling
 ↓
Testing
 ↓
Monitoring
```

Not every product is required to use every technology in this document.

A technology becomes relevant when the product or business requirement justifies it.

---

# Frontend

## Framework

**Next.js**

### Role

Primary framework for web applications.

### Reason

Provides:

* React-based development
* routing
* server-side rendering where appropriate
* static generation where appropriate
* application performance capabilities
* strong TypeScript support
* scalable project structure

Specific versions should be selected according to project requirements and supported releases.

---

# UI Library

**React**

### Role

Primary frontend UI library.

### Reason

Provides:

* component-based development
* reusable interfaces
* mature ecosystem
* strong compatibility with Next.js
* broad developer support

---

# Frontend Language

**TypeScript**

### Role

Primary frontend programming language.

### Reason

Provides:

* type safety
* maintainability
* safer refactoring
* improved developer productivity
* consistency across the primary technology stack

---

# Styling

**Tailwind CSS**

### Role

Primary utility-first styling framework.

### Reason

Supports:

* rapid interface development
* responsive design
* consistent styling
* reusable design patterns

---

# UI Components

**shadcn/ui**

### Role

Reusable and customizable UI component foundation.

### Reason

Provides accessible components while allowing the company to maintain control over implementation and visual design.

---

# Frontend Data Management

**TanStack Query**

### Role

Server-state management where client-side synchronization is required.

### Capabilities

* data fetching
* caching
* background updates
* synchronization
* request-state management

It should be introduced where it creates meaningful value.

---

# Frontend Forms

**React Hook Form**

### Role

Form management.

### Reason

Provides efficient form handling with a suitable developer experience for TypeScript applications.

---

# Frontend Validation

**Zod**

### Role

Schema and runtime validation.

### Reason

Provides structured validation for application inputs and can support consistent validation concepts across frontend and backend systems.

---

# Backend

## Framework

**NestJS**

### Role

Primary backend application framework.

### Reason

Provides:

* modular architecture
* dependency injection
* TypeScript support
* structured application development
* scalable organization for business applications

---

# Backend Language

**TypeScript**

### Role

Primary backend programming language.

### Reason

Maintains consistency across the primary web technology stack and improves maintainability.

---

# API Standard

**REST API**

### Role

Default API architecture.

### Reason

REST is widely supported, understandable, and suitable for most EyesightWorks products.

---

# Optional API Technology

## GraphQL

GraphQL may be introduced when:

* clients require flexible data queries
* multiple clients need significantly different data shapes
* the benefits justify additional complexity

GraphQL is not the default API standard.

---

# Real-Time Communication

## WebSockets

WebSockets may be used for:

* real-time notifications
* chat
* live dashboards
* status updates
* collaborative workflows

They should only be introduced when real-time communication creates genuine product value.

---

# Specialized Backend Services

## Python

**Python** is an approved specialized engineering language.

### Role

Python should be used where it provides a meaningful advantage, especially for:

* AI
* automation
* data processing
* document processing
* search processing
* machine-learning workloads
* specialized backend services

Python is not intended to replace the primary NestJS backend platform.

---

# Python API Framework

## FastAPI

**FastAPI** is the preferred framework for specialized Python HTTP services.

### Use Cases

* AI services
* automation services
* document processing
* data-processing services
* specialized APIs
* services requiring Python-specific libraries

The service boundary should be justified by actual business or technical requirements.

---

# Primary Backend and Specialized Service Model

EyesightWorks may use:

```text
Main Product Backend
        |
        +---- NestJS / TypeScript
        |
        +---- Specialized Python / FastAPI Service
                     |
                     +---- AI
                     +---- Processing
                     +---- Automation
                     +---- Search
```

This allows the company to maintain a consistent primary backend while using Python where it provides additional value.

---

# Database

## Primary Database

**PostgreSQL**

### Role

Primary relational database technology.

### Reason

Provides:

* strong relational capabilities
* transactional integrity
* mature SQL support
* long-term scalability
* broad ecosystem support

---

# ORM

## Prisma

**Prisma ORM**

### Role

Primary ORM for TypeScript/NestJS applications using PostgreSQL.

### Capabilities

* type-safe database access
* schema management
* migrations
* query development

---

# Database Capabilities

Approved PostgreSQL capabilities may include:

* relational modeling
* indexes
* transactions
* migrations
* full-text search
* JSON capabilities where appropriate

Advanced database capabilities should be introduced only when requirements justify them.

---

# Search

Search should begin with the simplest approach capable of satisfying the actual requirement.

Possible approaches include:

* PostgreSQL search
* indexed queries
* application-level filtering
* Redis-assisted patterns where appropriate

Specialized search platforms should only be introduced when requirements exceed the capabilities of the existing stack.

---

# Caching

## Redis

**Redis**

### Role

Optional shared infrastructure capability.

### Use Cases

* caching
* temporary state
* rate limiting
* background job queues
* short-lived application data
* coordination where necessary

Redis is not required for every product.

It should be introduced when its capabilities create measurable value.

---

# Authentication and Security

## Authentication

Approved mechanisms may include:

* JWT
* refresh tokens
* secure session-based authentication where appropriate
* OAuth providers where required

The authentication model must match the product's security requirements.

---

# Authorization

## Role-Based Access Control

**RBAC**

### Role

Primary authorization model where role-based permissions are appropriate.

Authorization may also consider:

* resource ownership
* organization membership
* action-based permissions
* business rules

---

# Identity Providers

Potential identity integrations include:

* Google OAuth
* other OAuth providers where justified

External identity providers should only be introduced when they provide meaningful customer or operational value.

---

# Security Controls

Common security capabilities include:

* email verification
* password reset
* rate limiting
* input validation
* secure password hashing
* security headers
* secret management
* access control

Detailed security requirements are defined in:

**19-security-and-privacy.md**

---

# File and Media

## Cloudinary

**Cloudinary**

### Role

Primary media-management option for products requiring image and media storage.

### Capabilities

* image storage
* image transformation
* optimization
* CDN delivery
* media management

Other object-storage providers may be used where product requirements justify them.

---

# Payments

## Supported Providers

The company may use:

* Paystack
* Flutterwave
* Stripe

### Purpose

Support:

* African payment requirements
* international payments
* subscriptions
* transaction processing

Provider selection should depend on:

* customer location
* product requirements
* supported payment methods
* supported currencies
* fees
* reliability
* integration requirements

---

# Payment Architecture Principle

Payment provider-specific implementations should be isolated where practical.

This allows products to maintain a consistent internal payment model while supporting different providers.

Payment credentials and webhooks must follow the security standards defined in Document 19.

---

# Cloud Infrastructure

## Containerization

**Docker**

Docker is the standard containerization technology.

### Purpose

Provides:

* reproducible environments
* consistent application packaging
* development consistency
* deployment portability

---

# Docker Compose

**Docker Compose**

### Role

Primary local and small-environment multi-service orchestration technology.

### Use Cases

* local development
* PostgreSQL
* Redis
* backend services
* Python services
* development integrations

More advanced orchestration should only be introduced when justified.

---

# Cloud Platforms

Current and planned cloud platforms include:

* Vercel
* Render
* AWS
* GitHub

### Vercel

Primarily suitable for:

* Next.js applications
* frontend deployment
* web application hosting

### Render

Suitable for:

* backend services
* application services
* straightforward cloud deployment

### AWS

Long-term cloud platform option for products requiring more advanced infrastructure capabilities.

Potential services include:

* EC2
* RDS
* S3
* CloudFront
* IAM
* CloudWatch

AWS services should be introduced according to actual requirements.

---

# Cloud Portability

EyesightWorks should avoid unnecessary vendor lock-in.

Where practical:

* application logic should remain portable
* deployment procedures should be documented
* data should have appropriate export or recovery options
* provider-specific integrations should have clear boundaries

Vendor lock-in may be accepted when the provider creates clear business value.

---

# Mobile

## Flutter

**Flutter**

### Role

Primary cross-platform mobile development technology.

### Use Cases

* Android applications
* iOS applications
* shared mobile application codebases

Flutter should be introduced when validated customer demand or product strategy requires a mobile application.

Responsive web applications remain appropriate when they provide sufficient value.

---

# Mobile Architecture Principle

Mobile applications should follow:

```text
Validated Customer Need
        ↓
Mobile Requirement
        ↓
Flutter Application
        ↓
Shared Backend APIs
```

Mobile applications should reuse backend capabilities where appropriate rather than duplicate business logic unnecessarily.

---

# Continuous Integration

## Source Control

**Git**

Primary version-control technology.

---

# Repository Platform

**GitHub**

Primary source-code repository and collaboration platform.

---

# Automation

## GitHub Actions

GitHub Actions may be used for:

* automated testing
* builds
* linting
* deployment
* Docker image publishing
* security checks where appropriate

CI complexity should match project importance.

---

# Testing

## Unit Testing

**Jest**

Primary unit-testing option for TypeScript applications and services.

---

# Integration Testing

**Supertest**

Used for HTTP and API integration testing where appropriate.

---

# End-to-End Testing

**Playwright**

Used for browser-based end-to-end testing of important user workflows.

---

# Python Testing

Python services should use an appropriate testing strategy.

FastAPI services should include, where required:

* unit tests
* API tests
* integration tests

Testing depth should match service criticality.

---

# API Documentation

## Swagger / OpenAPI

Primary API documentation standard.

Documentation should remain aligned with meaningful API contract changes.

---

# API Testing Tools

Approved development tools include:

* Postman
* Thunder Client

Tool choice may vary between developers where it does not conflict with project standards.

---

# Code Quality

Approved development tools include:

* ESLint
* Prettier

These tools support:

* code consistency
* formatting
* maintainability
* quality checks

---

# Git Hooks

## Husky

Husky may be used for:

* pre-commit checks
* formatting
* linting
* lightweight quality controls

Git hooks should remain fast enough to preserve developer productivity.

---

# Artificial Intelligence

## AI Philosophy

Artificial intelligence is treated as a reusable capability for creating measurable customer or business value.

AI should help to:

* save customer time
* improve decisions
* automate repetitive work
* increase productivity

AI should not be added merely because it is fashionable.

---

# AI Providers

Approved provider options may include:

* OpenAI
* OpenRouter
* other providers when justified by product requirements

Provider selection should consider:

* capability
* reliability
* cost
* latency
* privacy
* data handling
* availability

---

# AI Capabilities

Approved AI capabilities may include:

* text generation
* structured generation
* document processing
* intelligent search
* classification
* summarization
* recommendations
* automation
* AI-assisted workflows

Advanced AI capabilities should be introduced only when they solve validated problems.

---

# AI Abstraction

Where multiple products use AI, a shared abstraction may be introduced to support:

* provider replacement
* model changes
* cost management
* centralized monitoring
* security controls

A shared abstraction should not create unnecessary complexity for smaller applications.

---

# AI Cost Monitoring

AI systems should monitor usage where relevant.

Potential measurements include:

* request volume
* token usage
* cost
* failure rate
* rate limits
* unusual usage patterns

Unexpected usage increases should be investigated.

---

# AI Security

AI integrations must:

* protect provider credentials
* keep privileged API keys server-side
* minimize unnecessary data sharing
* consider prompt injection
* validate important outputs
* handle provider failure
* follow privacy requirements

Detailed security requirements are defined in:

**19-security-and-privacy.md**

---

# Monitoring and Observability

The technology stack supports:

* structured logging
* health checks
* error tracking
* metrics
* service monitoring

Technologies such as:

* Prometheus
* Grafana
* Sentry

may be introduced when the product's operational complexity justifies them.

They are not mandatory for every early-stage application.

Detailed standards are defined in:

**21-monitoring-and-observability.md**

---

# Logging

Applications should use structured logging where practical.

Logging must avoid unnecessary exposure of:

* passwords
* API keys
* JWT secrets
* database credentials
* payment credentials
* sensitive personal information

---

# Deployment

The preferred deployment direction is:

```text
Source Code
    ↓
GitHub
    ↓
CI
    ↓
Build
    ↓
Container / Application Artifact
    ↓
Cloud Deployment
    ↓
Monitoring
```

The exact deployment process depends on product requirements.

---

# Environment Management

The company should maintain appropriate separation between:

```text
Development
   ↓
Testing
   ↓
Staging
   ↓
Production
```

Each environment should use appropriate configuration and credentials.

---

# Configuration and Secrets

Configuration should use:

* environment variables
* secure secret-management systems
* provider-specific secret storage where appropriate

The following must never be committed to source control:

* passwords
* API keys
* database credentials
* authentication secrets
* payment credentials
* cloud credentials
* AI provider credentials

---

# Approved Technology Categories

Technologies in this document fall into three categories.

## Core

Technologies intended to form the primary company engineering stack.

## Optional

Approved technologies used only when a product or system requirement justifies them.

## Deferred

Technologies intentionally postponed until evidence demonstrates that they are needed.

This distinction prevents the technology stack from becoming an obligation to use every listed tool.

---

# Core Technology Stack

The baseline company stack is:

```text
Next.js
React
TypeScript
NestJS
PostgreSQL
Prisma
Redis
Docker
Docker Compose
Git
GitHub
```

These technologies form the primary development direction.

---

# Specialized Technologies

Approved specialized technologies include:

```text
Python
FastAPI
Flutter
OpenAI
OpenRouter
Paystack
Flutterwave
Stripe
Cloudinary
AWS
GitHub Actions
```

They should be introduced according to actual product requirements.

---

# Optional Technologies

Optional technologies may include:

```text
GraphQL
WebSockets
Prometheus
Grafana
Sentry
Playwright
Supertest
Postman
Thunder Client
Swagger / OpenAPI
Nginx
```

Their use should be determined by actual requirements.

---

# Deferred Technologies

The following technologies are deliberately deferred unless future evidence justifies them.

---

## Kubernetes

Kubernetes is not part of the baseline infrastructure.

### Review Trigger

Consider Kubernetes when:

* service count grows significantly
* deployment complexity becomes difficult to manage
* independent scaling becomes necessary
* operational requirements exceed current Docker-based infrastructure

---

## Kafka

Kafka is deferred until advanced event-streaming requirements become real.

### Review Trigger

Consider Kafka when:

* event volume becomes substantial
* distributed event processing becomes necessary
* reliable event streaming creates measurable value

---

## Specialized Search Platforms

Examples include:

* Elasticsearch
* OpenSearch
* other specialized search systems

### Review Trigger

Consider these when:

* search requirements exceed PostgreSQL capabilities
* scale requires specialized indexing
* advanced relevance requirements justify the added complexity

---

## Advanced AI Infrastructure

Examples include:

* Retrieval-Augmented Generation
* embeddings
* vector databases
* fine-tuned models
* multi-agent systems
* advanced model orchestration

### Review Trigger

Introduce these only when validated customer requirements demonstrate meaningful value beyond simpler AI approaches.

---

## Advanced Distributed Systems

Examples include:

* complex event-driven architectures
* distributed service meshes
* advanced messaging infrastructure
* large-scale worker systems

### Review Trigger

Adopt when business scale, reliability, or operational requirements justify the additional complexity.

---

# Technology Not Adopted by Default

EyesightWorks should not automatically adopt:

* Kubernetes
* Kafka
* Elasticsearch
* vector databases
* service meshes
* multiple databases
* multiple frontend frameworks
* advanced distributed infrastructure
* large observability platforms

Every additional technology creates:

* learning cost
* maintenance cost
* security considerations
* operational complexity
* dependency risk

The company should therefore maintain a deliberately controlled stack.

---

# Technology Decision Principles

Technology adoption should improve at least one of the following:

* Customer Value
* Engineering Productivity
* Platform Scalability
* Security
* Operational Reliability
* Maintainability
* Cost Efficiency

A technology that does not create meaningful value should not be adopted merely for experimentation.

---

# Technology Evaluation Questions

Before introducing a significant technology, ask:

1. What problem does it solve?
2. Who benefits?
3. Why is the current stack insufficient?
4. What measurable value will it create?
5. What complexity will it introduce?
6. What will it cost?
7. Can the team support it?
8. What security implications exist?
9. What privacy implications exist?
10. Is the decision reversible?
11. What operational burden will it create?
12. How will success be measured?

---

# Technology Replacement

A technology should be reconsidered when:

* it creates significant operational problems
* maintenance becomes unreasonable
* security risks increase
* business requirements change
* costs become disproportionate
* another technology provides materially better value

Existing technology should not be replaced simply because a newer tool exists.

---

# Technology Decision Record

A significant technology decision should document:

* Technology
* Problem
* Current approach
* Proposed approach
* Evidence
* Benefits
* Costs
* Risks
* Migration effort
* Operational impact
* Security implications
* Decision
* Owner
* Review trigger

Significant decisions should also be recorded in:

**08-decision-log.md**

---

# Technology Stack Review

The stack should be reviewed when:

* business strategy changes
* product requirements change
* major technical constraints appear
* security requirements change
* operational complexity increases
* significant cost problems emerge
* the current stack becomes insufficient
* a new technology creates measurable value

The technology stack should evolve deliberately rather than continuously.

---

# Technology Stack and Product Strategy

The technology stack supports the company's major product directions:

```text
AI Platform
      ↓
Business Hub
      ↓
ERP Platform
```

Shared technologies may be reused across these product groups where reuse creates meaningful value.

Products should remain independently understandable and deployable where appropriate.

---

# Technology Stack and Platform Reuse

Potential shared capabilities include:

* authentication
* authorization
* billing
* AI services
* notifications
* file management
* analytics
* reporting
* shared UI components
* design system

Shared technology should be introduced when multiple products benefit from it.

---

# Technology Stack and Security

Every technology decision should consider:

* credential management
* dependency security
* access control
* data protection
* provider security
* secret handling
* logging
* infrastructure configuration

Detailed requirements are maintained in:

**19-security-and-privacy.md**

---

# Technology Stack and Business Continuity

Critical technology choices should support recovery through:

* source control
* reproducible builds
* containerization
* database backups
* deployment documentation
* provider documentation
* recovery procedures

Detailed requirements are maintained in:

**20-business-continuity-and-disaster-recovery.md**

---

# Technology Stack and Monitoring

Production technologies should provide an appropriate level of visibility.

Monitoring may include:

* availability
* errors
* performance
* resource usage
* dependency health
* business workflow health

Detailed requirements are maintained in:

**21-monitoring-and-observability.md**

---

# Technology Standards Checklist

Before adopting a significant new technology:

* [ ] Business problem identified
* [ ] Product requirement identified
* [ ] Current-stack limitation documented
* [ ] Expected value defined
* [ ] Cost considered
* [ ] Security impact considered
* [ ] Privacy impact considered
* [ ] Operational impact considered
* [ ] Team capability considered
* [ ] Maintenance burden considered
* [ ] Vendor dependency considered
* [ ] Recovery implications considered
* [ ] Monitoring requirements considered
* [ ] Decision owner identified
* [ ] Review trigger defined

---

# Decision Summary

## Approved Core Stack

The following form the primary EyesightWorks engineering stack:

* Next.js
* React
* TypeScript
* Tailwind CSS
* shadcn/ui
* TanStack Query
* React Hook Form
* Zod
* NestJS
* REST APIs
* PostgreSQL
* Prisma
* Redis
* Docker
* Docker Compose
* Git
* GitHub

---

## Approved Specialized Stack

The following are approved for appropriate use cases:

* Python
* FastAPI
* Flutter
* OpenAI
* OpenRouter
* Paystack
* Flutterwave
* Stripe
* Cloudinary
* AWS
* GitHub Actions

---

## Approved Optional Technologies

The following may be used when requirements justify them:

* GraphQL
* WebSockets
* Prometheus
* Grafana
* Sentry
* Playwright
* Supertest
* Postman
* Thunder Client
* Swagger / OpenAPI
* Nginx

---

## Deferred

The following remain deferred until evidence justifies adoption:

* Kubernetes
* Kafka
* Specialized search platforms
* Vector databases
* Advanced RAG infrastructure
* Fine-tuned models
* Multi-agent systems
* Advanced distributed infrastructure
* Other high-complexity technologies

---

# Open Questions

The following questions may be resolved as the company grows:

* When should AWS become the primary cloud platform for specific products?
* When should Kubernetes replace simpler Docker-based deployment?
* When will advanced event streaming become necessary?
* When should specialized search infrastructure be introduced?
* Which AI provider mix provides the best long-term balance of quality, cost, and reliability?
* Which shared platform services should be centralized first?
* When should Flutter become the standard mobile solution for selected products?
* Which observability tools should become company-wide standards?
* When should infrastructure-as-code become mandatory?

These questions should be resolved through business needs, customer evidence, technical evidence, and documented decisions.

---

# Next Document

**docs/03-backend-architecture.md**

The Backend Architecture document defines how the approved technologies are organized into backend systems, including:

* backend structure
* module boundaries
* API architecture
* authentication
* authorization
* database access
* AI services
* payments
* file management
* background processing
* security
* deployment
* scalability
* reliability
* monitoring

---

# Document Status

**Status:** Approved v1.1

This document establishes the current technology direction for EyesightWorks Technologies.

The technology stack should remain:

**Simple → Practical → Secure → Maintainable → Reusable → Scalable**

The governing principle is:

> **Business Need → Product Requirement → Architecture → Technology → Implementation**

New technologies should be introduced only when evidence demonstrates that the value they create justifies the complexity, cost, and operational responsibility they add.
