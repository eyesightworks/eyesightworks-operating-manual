# EyesightWorks Technologies Operating Manual

**Document:** 06 of 21

**Title:** API Architecture

**Version:** 1.1

**Status:** Approved

**Owner:** EyesightWorks Technologies

**Last Updated:** 2026-09-21

---

# Revision History

| Version | Date       | Changes                                                                                                                                                                                      |
| ------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1.0     | 2026-08-05 | Initial API Architecture                                                                                                                                                                     |
| 1.1     | 2026-09-21 | Updated API architecture to align with the 01–21 Operating Manual, Product Roadmap, Product Requirements, platform reuse strategy, security, observability, and evidence-driven architecture |

---

# API Architecture

## 1. Executive Summary

This document defines the API architecture standards for EyesightWorks Technologies.

The purpose of the API architecture is to provide a secure, consistent, maintainable, and scalable interface layer through which company products, applications, services, and integrations communicate.

The API architecture supports the company's operating hierarchy:

**Business → Product → Architecture → Engineering → Operations → Governance**

APIs are therefore treated as **business interfaces**, not merely technical endpoints.

An API should expose a meaningful business capability that supports a validated product requirement or reusable platform capability.

The API architecture should support:

* Reliable communication between applications and services.
* Secure access to business capabilities.
* Consistent development standards.
* Reusable platform capabilities.
* Product-specific domain capabilities.
* External integrations where justified.
* AI services where required.
* Observability and operational monitoring.
* Controlled scalability.
* Long-term maintainability.

The API architecture should remain simple during the MVP stage and become more sophisticated only when customer, product, operational, or technical evidence justifies additional complexity.

---

# 2. Purpose

This document establishes company-wide API architecture standards.

It defines:

* API principles.
* API styles.
* API organization.
* Authentication.
* Authorization.
* Request standards.
* Response standards.
* Validation.
* Error handling.
* Versioning.
* Rate limiting.
* Security.
* Documentation.
* Monitoring.
* Scalability.
* Integration principles.
* Platform reuse.
* API governance.

This document provides the architectural foundation for product-specific APIs.

---

# 3. Scope

This document applies to APIs developed for EyesightWorks Technologies products and shared platform capabilities.

It covers APIs used by:

* Web applications.
* Mobile applications.
* Internal services.
* AI services.
* Administrative applications.
* External integrations.
* Partner integrations where strategically justified.

This document does not define:

* Individual product requirements.
* Individual database schemas.
* Frontend implementation details.
* Detailed UI workflows.
* Individual business policies.
* Complete endpoint specifications for every product.

Those details belong in the appropriate Product Requirements, Database Architecture, Application Architecture, or API specifications.

---

# 4. Relationship to Other Documents

API architecture must remain connected to the wider Operating Manual.

### Business Architecture

**Document 02 — Business Architecture**

Defines the business capabilities and company structure that APIs may need to support.

### Backend Architecture

**Document 03 — Backend Architecture**

Defines backend application architecture and implementation responsibilities.

### Technology Architecture

**Document 03A — Technology Architecture**

Defines the approved technology foundation used to implement the API layer.

### Database Architecture

**Document 05 — Database Architecture**

Defines data structures and persistence responsibilities.

### API Architecture

**Document 06 — API Architecture**

Defines how business capabilities are exposed and communicated through APIs.

### Product Roadmap

**Document 07 — Product Roadmap**

Defines product sequencing, MVP priorities, validation milestones, and staged investment.

API development should therefore follow product priorities rather than becoming an independent technical roadmap.

### Product Requirements

**Document 15 — Product Requirements**

Defines what individual products require.

Product-specific API requirements should originate from validated product requirements.

### Security

**Document 19 — Security**

Defines broader security requirements that APIs must follow.

### Monitoring

**Document 21 — Monitoring**

Defines broader operational monitoring requirements.

---

# 5. API Architecture Principles

## 5.1 Business Capability First

APIs should represent meaningful business capabilities rather than direct database operations.

For example:

**Preferred**

```text
POST /api/v1/properties
```

represents the business capability of creating a property.

The API should not simply expose database tables without considering the underlying business operation.

---

## 5.2 Product Requirement Before API Design

API capabilities should originate from:

**Customer Problem → Product Requirement → Business Workflow → API Capability**

API design should not lead product strategy.

If a capability has no validated product or business purpose, it should not automatically become part of the platform.

---

## 5.3 Platform Before Duplication

Where the same business capability is required by multiple products, the company should prefer reusable platform capabilities.

Potential shared capabilities include:

* Identity.
* Organizations.
* Authentication.
* Authorization.
* File management.
* Notifications.
* AI services.
* Usage tracking.
* Reporting.
* Administration.

This supports the principle:

**Build once. Reuse where practical.**

Reuse should not create unnecessary coupling between products.

---

## 5.4 Simplicity Before Complexity

The company prefers simple APIs that are easy to understand, maintain, test, and operate.

Complex architecture should only be introduced when justified by:

* Customer demand.
* Product requirements.
* Traffic.
* Reliability requirements.
* Security requirements.
* Integration requirements.
* Measurable operational evidence.

---

## 5.5 Security by Default

API security must be considered from the beginning.

APIs should apply appropriate:

* Authentication.
* Authorization.
* Input validation.
* Rate limiting.
* Secure communication.
* Data protection.
* Logging.
* Monitoring.

Security should not be treated as a final deployment step.

---

## 5.6 Evidence-Driven Evolution

API architecture should evolve according to evidence.

New technologies, communication patterns, infrastructure, or services should not be introduced merely because they are technically interesting.

Architecture decisions should create measurable value in at least one of:

* Customer value.
* Product capability.
* Developer productivity.
* Security.
* Reliability.
* Maintainability.
* Scalability.
* Operational efficiency.

---

# 6. API Goals

The EyesightWorks API platform should provide:

## Product Integration

Enable reliable communication between:

* Frontend applications.
* Backend applications.
* Internal services.
* AI services.
* External systems.
* Partner integrations.

---

## Platform Reuse

Provide reusable capabilities that can support multiple products without unnecessarily duplicating the same implementation.

---

## Developer Experience

APIs should be:

* Predictable.
* Consistent.
* Well documented.
* Easy to test.
* Easy to integrate.
* Easy to maintain.

---

## Security

Protect customer information, business operations, and platform resources.

---

## Scalability

Support growth in:

* Users.
* Businesses.
* Products.
* Transactions.
* API requests.
* Integrations.

without requiring unnecessary architectural redesign.

---

# 7. Primary API Style

## REST API

**REST is the approved primary API architecture for EyesightWorks Technologies.**

REST is preferred because it provides:

* Simplicity.
* Broad industry adoption.
* Strong framework support.
* Strong tooling.
* Straightforward frontend integration.
* Good maintainability.
* Clear resource-oriented design.

REST should be the default unless a documented requirement justifies another approach.

---

# 8. API Data Format

The standard API data format is:

**JSON**

JSON should be used for normal API requests and responses.

It provides:

* Broad compatibility.
* Human readability.
* Simplicity.
* Strong ecosystem support.

Documented exceptions may exist for appropriate file, streaming, or specialized integrations.

---

# 9. Optional API Technologies

## 9.1 GraphQL

GraphQL is not part of the initial API standard.

It may be evaluated when validated requirements demonstrate meaningful value beyond REST.

Potential review triggers include:

* Complex client-driven data requirements.
* Highly interactive dashboards.
* Significant data aggregation requirements.
* Validated need to reduce multiple network requests.

GraphQL should not be introduced simply because it is technically available.

---

## 9.2 Event-Driven Architecture

Event-driven communication may be introduced later where asynchronous processing creates measurable value.

Potential use cases include:

* Background jobs.
* Notifications.
* AI processing.
* High-volume workflows.
* Integration events.
* Long-running processes.

Event-driven architecture should remain a staged capability rather than an MVP requirement unless a product specifically requires it.

---

# 10. API Organization

APIs should be organized around business capabilities and product domains.

Shared domains may include:

* Identity.
* Organizations.
* Users.
* Authentication.
* Authorization.
* File Management.
* Notifications.
* Artificial Intelligence.
* Reporting.
* Administration.
* Usage Tracking.

Product-specific domains may include:

* Properties.
* Chemical Products.
* Suppliers.
* Pharmacy Products.
* Inventory.
* Sales.
* Purchases.
* Jobs.
* Applications.

Product-specific APIs should remain aligned with their Product Requirements.

---

# 11. API Layer Structure

The API architecture should generally follow:

```text
Client
   ↓
API
   ↓
Authentication / Authorization
   ↓
Validation
   ↓
Controller / Route
   ↓
Application / Business Logic
   ↓
Domain Services
   ↓
Data Access
   ↓
Database / External Service
```

The exact implementation may vary according to the product and backend architecture.

The API layer should not contain unnecessary business logic that belongs in appropriate services.

---

# 12. Authentication

Protected APIs must use secure authentication.

Approved authentication mechanisms include:

* JWT access tokens.
* Refresh tokens where required.

Authentication should be implemented consistently across products where shared identity is appropriate.

Authentication should establish **who** is making the request.

---

# 13. Authorization

Authorization determines **what the authenticated user is allowed to do**.

The standard authorization approach is:

**Role-Based Access Control — RBAC**

Where necessary, authorization may also consider:

* Organization.
* Resource ownership.
* Business role.
* Product role.
* Administrative privileges.

A user should not gain access to a resource merely because they are authenticated.

---

# 14. API Versioning

Public and externally consumed APIs should use explicit versioning.

Example:

```text
/api/v1/
```

Versioning should protect consumers from unexpected breaking changes.

A new API version should normally be introduced only when a breaking change cannot reasonably be avoided.

Backward compatibility should be maintained whenever practical.

---

# 15. Request Standards

API requests should use consistent standards.

Requests should include appropriate:

* HTTP methods.
* Resource names.
* Parameters.
* Request bodies.
* Authentication.
* Validation.
* Pagination.
* Filtering.
* Sorting.

Common HTTP methods include:

```text
GET
POST
PATCH
PUT
DELETE
```

The selected method should accurately represent the intended operation.

---

# 16. Resource Naming

API resources should use clear, consistent naming.

Example:

```text
/api/v1/properties
/api/v1/products
/api/v1/suppliers
/api/v1/users
/api/v1/enquiries
```

Resource naming should represent business concepts rather than database implementation details.

---

# 17. Pagination

Large collections should support pagination.

Example:

```text
GET /api/v1/properties?page=1&limit=20
```

Pagination should protect API performance and prevent unnecessarily large responses.

The exact pagination strategy may be adjusted according to product requirements and scale.

---

# 18. Filtering and Sorting

Where useful, collection APIs should support filtering and sorting.

Example:

```text
GET /api/v1/properties?location=Ibadan
```

or:

```text
GET /api/v1/products?category=industrial&sort=name
```

Filtering should reflect validated product requirements.

The API should not introduce large numbers of filters without a meaningful business purpose.

---

# 19. Response Standards

API responses should be predictable and consistent.

Responses should provide:

* Appropriate HTTP status.
* Requested data.
* Metadata where appropriate.
* Error information where applicable.

Response structures should remain consistent across products wherever practical.

---

# 20. HTTP Status Standards

APIs should use appropriate HTTP status codes.

Examples include:

```text
200 OK
201 Created
204 No Content
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
409 Conflict
422 Unprocessable Entity
429 Too Many Requests
500 Internal Server Error
```

The exact status should reflect the actual API outcome.

---

# 21. Input Validation

All incoming requests must be validated before business logic executes.

Validation should check:

* Required fields.
* Data types.
* Accepted values.
* Input length.
* Data formats.
* Security-sensitive input.
* Business rules where appropriate.

Invalid requests should return clear validation errors.

Validation should occur at the API boundary and should not rely solely on frontend validation.

---

# 22. Error Handling

APIs should return standardized error responses.

Errors should provide:

* Appropriate HTTP status codes.
* Human-readable messages.
* Machine-readable error codes.
* Validation details where appropriate.

Internal implementation details should never be exposed to API consumers.

Examples of information that should not be exposed include:

* Database errors.
* Internal stack traces.
* Secrets.
* Internal infrastructure details.
* Sensitive implementation information.

---

# 23. Rate Limiting

Rate limiting protects platform reliability and helps prevent abuse.

Rate limits may vary according to:

* Anonymous users.
* Authenticated users.
* Product.
* Subscription plan.
* API endpoint.
* Administrative privileges.

AI-related APIs may require separate usage controls because AI operations can create variable infrastructure costs.

Limits should be monitored and adjusted using operational evidence.

---

# 24. API Security

Production APIs should implement appropriate:

* HTTPS.
* Security headers.
* Input validation.
* Input sanitization where applicable.
* Authentication.
* Authorization.
* Rate limiting.
* Audit logging.
* Secure secret management.
* Appropriate file validation.

Security requirements should align with Document 19 — Security.

---

# 25. File and Media APIs

Products that support media or document uploads should use controlled file-management APIs.

File APIs should consider:

* File type validation.
* File size limits.
* Secure storage.
* Access control.
* Malware/security controls where appropriate.
* Safe filenames and metadata.
* Deletion procedures.
* Provider dependency.

Products such as the AI Real Estate Suite may require these capabilities for property media.

---

# 26. AI APIs

AI capabilities should be exposed through controlled application interfaces.

AI APIs should consider:

* Authentication.
* Authorization.
* Input validation.
* Usage limits.
* Cost monitoring.
* Provider abstraction where practical.
* Output validation.
* Logging.
* Failure handling.
* Appropriate privacy controls.

AI should remain an application capability rather than being embedded directly throughout unrelated product code.

---

# 27. Integration Architecture

External integrations should be isolated behind appropriate service boundaries.

Potential integrations include:

* AI providers.
* Payment providers.
* Email providers.
* File storage providers.
* Notification services.
* Third-party business systems.

The API architecture should minimize unnecessary dependency on a single external provider where practical.

External provider failures should not expose internal implementation details to API consumers.

---

# 28. API Documentation

All production APIs should be documented.

Approved documentation standard:

**OpenAPI / Swagger**

Documentation should include:

* Endpoints.
* HTTP methods.
* Authentication requirements.
* Request schemas.
* Response schemas.
* Request examples.
* Response examples.
* Error responses.
* Parameters.
* Pagination/filtering behavior where applicable.

API documentation should remain synchronized with the implementation.

---

# 29. Testing Requirements

APIs should be tested at appropriate levels.

Testing may include:

* Unit tests.
* Integration tests.
* Authentication tests.
* Authorization tests.
* Validation tests.
* Error-handling tests.
* API endpoint tests.
* Security tests.
* Performance tests where justified.

Critical business APIs should not rely solely on manual testing.

---

# 30. Monitoring and Observability

Production APIs should provide appropriate observability.

The platform should monitor:

* Response times.
* Error rates.
* Request volume.
* Availability.
* Authentication failures.
* Authorization failures.
* Rate-limit events.
* Resource utilization where appropriate.
* External dependency failures.

Monitoring should connect to **Document 21 — Monitoring**.

---

# 31. Logging and Auditability

API logging should provide enough information to support:

* Debugging.
* Security investigation.
* Operational analysis.
* Customer support.
* Incident response.

Logs should not unnecessarily contain sensitive information.

Important administrative and security-sensitive actions should have appropriate audit records.

---

# 32. Scalability Strategy

API scalability should evolve gradually.

## MVP Stage

Focus on:

* Simple REST APIs.
* Reliable authentication.
* Clear validation.
* Clear documentation.
* Shared capabilities where reuse is justified.
* Reliable database access.
* Basic monitoring.

---

## Growth Stage

Introduce where justified:

* Performance optimization.
* Response caching.
* Background processing.
* Queue-based processing.
* Improved monitoring.
* More advanced rate limiting.

---

## Enterprise Stage

Evaluate when evidence requires:

* API Gateway.
* Service-to-service authentication.
* Advanced caching.
* Distributed event processing.
* Additional infrastructure.
* Additional API technologies.

Additional complexity must be justified by actual requirements.

---

# 33. API Reliability

APIs should be designed to fail safely.

The system should consider:

* Database failures.
* External service failures.
* AI provider failures.
* Network failures.
* Invalid requests.
* Authentication failures.
* Rate limiting.
* Timeouts.

Where appropriate, APIs should use:

* Timeouts.
* Retry strategies.
* Graceful failure.
* Health checks.
* Recovery mechanisms.

Retries should be used carefully to avoid duplicate operations.

---

# 34. API Performance

API performance should be measured rather than assumed.

Performance considerations include:

* Database query efficiency.
* Response size.
* Pagination.
* Caching.
* External service latency.
* AI provider latency.
* Background processing.

Optimization should be prioritized according to actual performance evidence.

---

# 35. API Governance

API architecture decisions should remain consistent with the Operating Manual.

Major architectural decisions should be:

* Documented.
* Justified.
* Reviewed where appropriate.
* Connected to relevant product requirements.
* Recorded in Document 08 — Decision Log when significant.

API changes should not bypass:

* Security requirements.
* Product requirements.
* Development standards.
* Monitoring requirements.
* Business continuity requirements.

---

# 36. Product API Relationship

Each product should define its API requirements based on its approved Product Requirement.

For example:

### AI Real Estate Suite

Potential API domains include:

```text
/auth
/businesses
/properties
/property-media
/ai
/enquiries
/search
/usage
```

### Nigeria Chemical Hub

Potential API domains include:

```text
/auth
/businesses
/products
/suppliers
/search
/enquiries
/quote-requests
/verification
/moderation
```

### Pharmacy ERP

Potential API domains include:

```text
/auth
/pharmacies
/products
/inventory
/suppliers
/customers
/sales
/purchases
/reports
```

These examples illustrate architectural organization.

They are not final endpoint specifications.

Final APIs should be derived from the approved product requirements and implementation decisions.

---

# 37. API and MVP Strategy

The API architecture must support the company's MVP-first strategy.

For each new product:

```text
Validated Problem
      ↓
Product Requirement
      ↓
MVP Workflow
      ↓
Required API Capabilities
      ↓
Implementation
      ↓
Testing
      ↓
Launch
      ↓
Measurement
      ↓
Improvement
```

The company should avoid building a large API platform before the corresponding product capabilities are validated.

Reusable infrastructure should grow alongside real product requirements.

---

# 38. API and Product Roadmap

Document 07 — Product Roadmap establishes product sequencing and staged investment.

API work should therefore follow the roadmap.

If a product is not prioritized for implementation, its complete API infrastructure should not automatically be built.

When a product enters MVP development:

1. Review its Product Requirement.
2. Identify required business capabilities.
3. Identify reusable platform capabilities.
4. Define product-specific APIs.
5. Implement only the required MVP APIs.
6. Measure usage.
7. Improve the API based on evidence.

This keeps technical work aligned with business priorities.

---

# 39. API Decision Principles

API decisions should improve one or more of:

* Customer value.
* Product capability.
* Developer productivity.
* Security.
* Reliability.
* Maintainability.
* Scalability.
* Operational efficiency.

If an architectural decision does not create meaningful value or solve a real requirement, it should not automatically be adopted.

---

# 40. Approved Standards

The following are approved company API standards:

* REST as the primary API style.
* JSON as the standard API data format.
* JWT access tokens.
* Refresh tokens where appropriate.
* Role-Based Access Control.
* Explicit API versioning.
* Request validation.
* Standardized errors.
* Rate limiting.
* HTTPS.
* OpenAPI / Swagger documentation.
* API monitoring.
* Appropriate audit logging.
* Evidence-driven API evolution.
* Reusable platform capabilities where justified.
* Product-specific APIs derived from Product Requirements.

---

# 41. Deferred / Conditional Technologies

The following are not required for the initial API platform:

* GraphQL.
* API Gateway.
* Distributed event architecture.
* Complex microservice infrastructure.
* Advanced service meshes.
* Large-scale distributed processing.

These technologies may be evaluated later when measurable requirements justify them.

---

# 42. Open Questions

The following remain controlled architectural questions:

* When should GraphQL be introduced?
* When is an API Gateway justified?
* When should external developer APIs be exposed?
* What rate limits should apply to different product plans?
* When should event-driven architecture be introduced?
* Which integrations create the greatest validated customer value?
* When should shared platform APIs become independently deployable services?

These questions should be resolved through evidence and recorded through the appropriate architecture and decision processes.

---

# 43. Next Document

## 07 — Product Roadmap

Document 07 defines:

* Product portfolio.
* Product lifecycle.
* MVP sequencing.
* Product prioritization.
* Validation milestones.
* Customer learning milestones.
* Release strategy.
* Roadmap governance.
* Product investment decisions.

API architecture should support the roadmap rather than independently determine product priorities.

---

# 44. Operating Principle

**Business Requirement → Product Requirement → API Capability → Secure Implementation → Measure → Improve**

The API architecture exists to turn validated business and product capabilities into reliable, secure, reusable interfaces.

**Build what the business needs. Reuse what creates value. Keep complexity proportional to evidence.**
