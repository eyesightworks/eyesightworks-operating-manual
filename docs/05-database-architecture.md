# EyesightWorks Technologies Operating Manual

**Document:** 05 of 21

**Title:** Database Architecture

**Version:** 1.1

**Status:** Approved

**Owner:** EyesightWorks Technologies

**Last Updated:** 2026-09-21

---

# Revision History

| Version | Date       | Changes                                                                                                                                                            |
| ------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1.0     | 2026-08-05 | Initial Database Architecture                                                                                                                                      |
| 1.1     | 2026-09-21 | Updated database architecture standards, clarified data ownership, tenant isolation, security, backups, recovery, observability, scalability, and schema evolution |

---

# Database Architecture

## Executive Summary

This document defines the database architecture standards for EyesightWorks Technologies.

The purpose of the database architecture is to provide a secure, reliable, maintainable, and scalable data foundation for the company's products.

The database layer should support:

* reliable data management
* data integrity
* secure access
* predictable performance
* product scalability
* business reporting
* auditability
* recovery
* reusable platform capabilities

Database architecture exists to support:

**Business → Product → Architecture → Engineering**

Business requirements should determine what data exists.

Product requirements should determine how the data is used.

Architecture should determine how the data is organized and accessed.

Engineering should implement the approved model safely.

---

# Architecture Dependency

Database architecture must remain aligned with:

**02 — Business Architecture**

**03 — Backend Architecture**

**03A — Technology Stack**

**19 — Security and Privacy**

**20 — Business Continuity and Disaster Recovery**

**21 — Monitoring and Observability**

The relationship is:

```text id="t9i5h2"
Business Requirement
        ↓
Product Requirement
        ↓
Data Requirement
        ↓
Database Design
        ↓
Backend Access
        ↓
Application Behavior
        ↓
Measurement
        ↓
Improvement
```

Database design should not become the source of business strategy.

---

# Scope

This document defines:

* database architecture principles
* PostgreSQL standards
* Prisma usage
* schema organization
* data ownership
* relationships
* constraints
* indexing
* search
* tenant isolation
* migrations
* transactions
* caching considerations
* data security
* backup and recovery
* monitoring
* auditability
* retention
* scalability
* database governance

This document does not define:

* individual product schemas
* product-specific business entities
* API design
* frontend implementation
* detailed backend modules
* customer-specific database configurations

Those belong in the appropriate product and architecture documents.

---

# Database Architecture Principles

## Data Integrity Before Convenience

Correct data is more important than short-term implementation speed.

The database should protect important business rules through appropriate constraints and relationships.

---

## Security by Default

Data access should be restricted according to:

* identity
* role
* organization
* resource ownership
* business need

Sensitive data must receive appropriate protection.

---

## Business Requirements Drive Data Models

Database structures should represent actual business requirements rather than technical convenience.

A table should exist because the business or application needs the information.

---

## Simplicity Before Complexity

The company should prefer a simple reliable data architecture before adopting:

* multiple databases
* distributed databases
* sharding
* complex replication
* specialized data platforms

Additional complexity must be justified by evidence.

---

## Performance Through Good Design

Performance should come primarily from:

* appropriate schema design
* efficient queries
* suitable indexes
* pagination
* transaction design
* appropriate caching
* measured optimization

---

## Reuse Where Valuable

Shared platform data capabilities should be reused where this reduces unnecessary duplication.

However, forced centralization should be avoided when it creates excessive coupling.

---

## Recoverability

Important data must be recoverable.

Backup and restoration are part of database architecture rather than optional operational extras.

---

# Primary Database

## PostgreSQL

**PostgreSQL** is the primary relational database standard for EyesightWorks Technologies.

PostgreSQL provides:

* relational data modeling
* ACID transactions
* strong data integrity
* indexing
* full-text search
* JSON support
* mature tooling
* long-term scalability

PostgreSQL should be the default relational database unless an approved exception exists.

---

# ORM

## Prisma

**Prisma ORM** is the primary ORM for TypeScript/NestJS applications using PostgreSQL.

Prisma may provide:

* type-safe database access
* schema definitions
* migrations
* query access
* developer productivity

The use of Prisma should remain aligned with the backend architecture defined in Document 03.

---

# Specialized Python Services

Python/FastAPI services may access PostgreSQL where required.

Where multiple services access the same database, ownership and boundaries must remain clear.

A Python service should not bypass the established data model simply because it uses a different programming language.

---

# Database Organization

Data should be organized around meaningful business domains.

Possible domains include:

* identity
* organizations
* authentication
* customers
* products
* inventory
* bookings
* billing
* notifications
* files
* AI usage
* reporting
* audit
* product-specific business domains

Actual domains should be determined by product requirements.

---

# Domain Ownership

Every important business dataset should have a clearly understood owner.

The owning domain is responsible for:

* defining business meaning
* validating data
* managing data lifecycle
* maintaining data relationships
* controlling access
* handling relevant migrations

Other modules should interact through approved application or service boundaries rather than unrestricted direct access.

---

# Shared Platform Data

Potential shared platform data includes:

### Identity

* Users
* Organizations
* Roles
* Permissions

### Platform Services

* Notifications
* Files
* Billing
* AI Usage
* Settings
* Audit Records

These should become shared only when multiple products genuinely benefit from them.

---

# Product-Specific Data

Product-specific data should remain within the relevant product domain where practical.

Examples may include:

* real estate properties
* chemical suppliers
* pharmacy inventory
* bookings
* product listings
* orders

Shared platform architecture should not force unrelated product concepts into a single generic schema.

---

# Multi-Tenancy Strategy

EyesightWorks products may serve multiple businesses or organizations.

The preferred initial approach is:

**Shared database with logical tenant isolation**

Each organization-owned record should contain an appropriate relationship to its organization or tenant.

For example:

```text id="7o2u2w"
Organization
    ↓
Users
    ↓
Business Records
    ↓
Transactions
```

Tenant isolation must be enforced through application authorization and appropriate data-access controls.

---

# Tenant Isolation Principles

The system should ensure that:

* one organization cannot access another organization's private data
* authorization is enforced server-side
* ownership relationships are validated
* queries use appropriate tenant boundaries
* administrative access is controlled

Tenant identifiers should not be trusted merely because a client sends them.

---

# Future Multi-Tenancy Options

Depending on scale and requirements, EyesightWorks may later evaluate:

* database-per-tenant
* dedicated infrastructure
* regional isolation
* specialized enterprise environments

These approaches should only be introduced when customer requirements, scale, security, regulatory needs, or operational evidence justify them.

---

# Data Integrity

The database should enforce appropriate integrity using:

* primary keys
* foreign keys
* unique constraints
* check constraints
* not-null constraints
* referential integrity
* appropriate cascading rules

Where practical, critical data-consistency rules should not rely solely on frontend behavior.

---

# Primary Keys

Every persistent entity should have a stable primary key.

The specific identifier strategy should be selected according to the product requirements.

Possible approaches include:

* UUIDs
* database-generated numeric IDs
* other appropriate identifiers

The company should avoid changing identifier strategies without a justified reason.

---

# Relationships

Relationships should be:

* clearly defined
* based on business meaning
* appropriately indexed
* easy to maintain
* designed for expected query patterns

Many-to-many relationships should normally use explicit junction structures.

---

# Cascading Rules

Cascade behavior must be deliberate.

Deletion or update of a parent record should not unexpectedly remove or alter important business data.

Where cascading deletion could cause significant data loss, explicit deletion workflows should be preferred.

---

# Nullability

Fields should allow null values only when the absence of a value has a meaningful business interpretation.

Avoid using nullable fields simply because they are convenient during development.

---

# Unique Constraints

Unique constraints should be used when the business requires uniqueness.

Examples may include:

* email address within a defined scope
* external identifiers
* transaction references
* organization-specific identifiers

The uniqueness scope must reflect actual business rules.

---

# Database Naming

Database naming should be:

* consistent
* readable
* predictable
* aligned with project conventions

Names should communicate business meaning.

Avoid unexplained abbreviations where practical.

---

# Schema Evolution

Database schemas must evolve through version-controlled migrations.

The primary migration approach is:

**Prisma Migration System**

Migration files should be:

* version-controlled
* reviewable
* tested
* documented when significant
* applied consistently across environments

Direct production database modifications should be avoided except through controlled emergency procedures.

---

# Migration Principles

Migrations should:

* minimize downtime where practical
* preserve data
* consider existing records
* avoid unnecessary destructive changes
* support safe deployment sequencing
* be tested before production

Breaking migrations should be planned rather than performed casually.

---

# Backward-Compatible Changes

Where practical, database changes should follow a safe sequence such as:

```text id="v4p8q3"
Add New Structure
      ↓
Deploy Compatible Application
      ↓
Migrate / Backfill Data
      ↓
Switch Application Usage
      ↓
Remove Obsolete Structure
```

This reduces the chance that application and database versions become incompatible during deployment.

---

# Data Migration

Data migrations should be treated differently from schema migrations when necessary.

A migration that changes existing customer data should consider:

* data volume
* execution time
* failure recovery
* backups
* transaction behavior
* customer impact

Large data migrations should be tested before production.

---

# Transactions

Transactions should be used when multiple database operations must succeed or fail together.

Examples include:

* financial records
* inventory changes
* order creation
* booking confirmation
* payment state updates

Transactions should not be used unnecessarily for independent operations.

---

# Concurrency

Systems should consider concurrent updates to important records.

Where appropriate, use:

* database transactions
* constraints
* appropriate locking
* optimistic concurrency techniques
* idempotency

The approach should depend on the business operation.

---

# Idempotency

Operations that may be retried should consider idempotency.

This is especially important for:

* payments
* webhooks
* orders
* transaction processing
* external synchronization

Repeated execution should not unintentionally create duplicate business records.

---

# Indexing Strategy

Indexes should support common access patterns.

Potential indexes include:

* primary keys
* foreign keys
* frequently filtered fields
* frequently sorted fields
* search fields
* unique fields
* reporting access patterns

---

# Index Design

Indexes should be based on actual query patterns where possible.

The company should avoid adding indexes indiscriminately because indexes also:

* consume storage
* increase write cost
* increase maintenance cost

Indexes should be reviewed as query patterns change.

---

# Query Performance

Database performance should be measured through:

* slow-query analysis
* query plans
* response times
* database resource usage
* application-level performance

Performance optimization should be evidence-driven.

---

# Pagination

Large result sets should use appropriate pagination.

Pagination prevents:

* unnecessarily large responses
* excessive memory usage
* slow queries
* poor customer experiences

Pagination design should match the use case.

---

# Search Strategy

The initial search strategy is:

**PostgreSQL search capabilities**

This may include:

* indexed queries
* PostgreSQL full-text search
* filtering
* sorting

Specialized search platforms should only be introduced when actual requirements justify them.

---

# Deferred Search Technologies

Potential future technologies include:

* Elasticsearch
* OpenSearch
* Meilisearch
* other specialized search systems

These remain optional or deferred until:

* data scale
* search complexity
* relevance requirements
* performance requirements

justify the additional infrastructure.

---

# Caching

Caching may be used where repeated data access creates measurable performance or cost problems.

Possible caching technology:

**Redis**

Caching must consider:

* expiration
* invalidation
* stale data
* consistency
* memory usage

The database remains the authoritative source of persistent business data unless a deliberate architecture defines otherwise.

---

# Data Security

Database security must follow:

**19-security-and-privacy.md**

Controls should include, where appropriate:

* encryption in transit
* encryption at rest
* least-privilege access
* protected credentials
* access monitoring
* secure backups
* controlled administrative access

---

# Database Credentials

Database credentials must:

* remain secret
* never be committed to source control
* not be hardcoded
* use appropriate environment or secret-management systems
* be rotated when necessary

Production database credentials must be separate from development credentials.

---

# Database Access

Database access should be limited according to actual requirements.

Application accounts should not automatically receive unrestricted administrative privileges.

Administrative database access should be:

* limited
* monitored where practical
* protected through strong authentication
* removed when no longer required

---

# Direct Database Access

Applications should normally access data through approved application services.

Unrestricted direct database access by unrelated modules or external clients should be avoided.

The database should not become an unofficial API.

---

# Personally Identifiable Information

Where databases contain personal information, the system should consider:

* purpose
* access
* retention
* encryption
* deletion
* auditability
* privacy requirements

Only necessary personal information should be stored.

---

# Sensitive Data

Highly sensitive information should receive stronger controls.

Examples may include:

* authentication secrets
* financial records
* sensitive customer data
* identity information
* security information

Secrets such as passwords and API keys should generally not be stored as ordinary database values in plaintext.

---

# Data Retention

Data should be retained according to:

* business requirements
* customer requirements
* legal obligations
* contractual obligations
* operational needs
* security considerations

Each product may require a more specific retention policy.

---

# Soft Deletion

Soft deletion may be used where historical records or recovery are important.

However, soft deletion should not be treated as a universal requirement.

It should be used when it provides meaningful business value.

---

# Permanent Deletion

Permanent deletion should be used when:

* legally required
* contractually required
* operationally appropriate
* requested by an authorized process
* data is no longer needed

Deletion should consider:

* primary records
* related records
* files
* backups
* logs
* external systems

---

# Audit Data

Important business events may require audit records.

Potential audit events include:

* authentication
* authorization changes
* administrative actions
* billing changes
* sensitive record changes
* configuration changes
* important workflow actions

Audit information should be protected from unauthorized modification.

---

# Audit Design

Audit records may contain:

* actor
* action
* affected resource
* timestamp
* result
* relevant request or correlation identifier

Audit records should avoid unnecessary sensitive data.

---

# Reporting Data

Operational databases may support application reporting.

However, as reporting requirements grow, the company may eventually separate operational and analytical workloads.

Advanced analytical infrastructure should only be introduced when reporting complexity justifies it.

---

# Data Export

Important business data should have appropriate export or recovery options where practical.

Exports may support:

* customer migration
* recovery
* analytics
* backups
* business continuity

Export capabilities should be controlled to protect sensitive information.

---

# Backup Strategy

Production databases should have appropriate backups.

Potential controls include:

* automated backups
* provider backups
* periodic logical exports
* snapshots
* point-in-time recovery where supported

The actual backup strategy must match system importance.

---

# Backup Verification

A backup should not be considered reliable solely because the backup job reports success.

Where practical, verify that:

* backups can be located
* backups are accessible
* backups can be restored
* restored data is usable

---

# Recovery Testing

Recovery should be tested periodically according to system criticality.

Testing should verify:

* restore procedure
* application connectivity
* data consistency
* recovery documentation
* recovery ownership

Detailed recovery requirements are defined in:

**20-business-continuity-and-disaster-recovery.md**

---

# Recovery Objectives

Critical databases may have defined:

**Recovery Time Objective (RTO)**

and:

**Recovery Point Objective (RPO)**

These should reflect actual business needs.

They should not be selected arbitrarily.

---

# Database Monitoring

Production databases should be monitored for:

* availability
* connections
* query performance
* slow queries
* storage growth
* errors
* resource consumption
* backup status

Detailed observability requirements are defined in:

**21-monitoring-and-observability.md**

---

# Capacity Monitoring

Database capacity should be monitored for:

* storage growth
* connection usage
* query workload
* resource limits
* increasing transaction volume

Capacity problems should ideally be identified before they become customer-impacting failures.

---

# Database Health

A healthy database environment should demonstrate:

* stable availability
* controlled resource use
* acceptable query performance
* reliable backups
* successful migrations
* controlled access
* monitored failures

---

# Performance Strategy

Database performance should primarily come from:

* good schema design
* efficient queries
* suitable indexing
* pagination
* transaction design
* connection management
* appropriate caching

Advanced infrastructure should only be introduced after simpler optimization methods are insufficient.

---

# Connection Management

Applications should use appropriate connection management.

The architecture should consider:

* connection limits
* pooling
* application scale
* deployment model
* provider constraints

Connection behavior should be monitored in production.

---

# Read Replicas

Read replicas may be introduced when:

* read load becomes substantial
* primary database resources are constrained
* workload patterns justify replication

They are not part of the baseline database architecture.

---

# Partitioning

Database partitioning may be introduced when:

* tables become very large
* query performance requires it
* retention patterns justify it
* operational evidence supports it

Partitioning should not be introduced simply for theoretical scalability.

---

# Geographic Database Deployment

Regional database deployment may become relevant when:

* customer distribution requires it
* latency becomes important
* compliance requires regional storage
* disaster recovery requirements justify it

The decision should consider substantial operational complexity.

---

# Database Scalability Strategy

Database architecture should evolve gradually.

## MVP Stage

Focus on:

* simple schema
* reliable PostgreSQL
* correct constraints
* migrations
* backups
* basic monitoring

---

## Growth Stage

Introduce where justified:

* query optimization
* stronger monitoring
* caching
* indexing improvements
* capacity planning

---

## Scale Stage

Evaluate:

* read replicas
* partitioning
* advanced caching
* dedicated analytical workloads
* stronger redundancy

---

## Enterprise Stage

Evaluate:

* regional deployment
* advanced high availability
* additional isolation
* specialized data infrastructure

The company should not implement advanced database infrastructure before actual requirements justify it.

---

# Database Architecture and Backend

Document 03 defines how backend services interact with the database.

The relationship is:

```text id="v5mym8"
Backend Module
      ↓
Data Access Layer
      ↓
Prisma
      ↓
PostgreSQL
```

Business logic should remain in appropriate application services.

Database logic should focus on persistence and data integrity.

---

# Database Architecture and Frontend

Frontend applications should never connect directly to the production database.

The standard path is:

```text id="zt7mza"
Frontend
   ↓
API
   ↓
Backend
   ↓
Data Access
   ↓
Database
```

This protects database credentials and centralizes authorization.

---

# Database Architecture and Business Architecture

Database structures should reflect actual business requirements.

Business changes may require:

* new entities
* new relationships
* new constraints
* new reporting
* new retention rules

Database changes should therefore be traceable to product or business requirements where significant.

---

# Database Architecture and Security

Security requirements are defined in Document 19.

The database must protect:

* customer data
* business data
* authentication-related information
* transaction records
* audit information

Security should be considered during schema and access design.

---

# Database Architecture and Disaster Recovery

Database recovery is part of Document 20.

Critical database systems should have:

* backup procedures
* recovery procedures
* ownership
* recovery expectations
* testing

---

# Database Architecture and Monitoring

Document 21 defines monitoring and observability.

Database monitoring should provide sufficient visibility to identify:

* outages
* performance degradation
* capacity constraints
* backup failures
* abnormal resource usage

---

# Data Architecture Exceptions

A product may require a database architecture exception.

Possible reasons include:

* specialized data requirements
* external integration constraints
* regulatory needs
* performance requirements
* customer infrastructure requirements

An exception should document:

* problem
* reason
* proposed approach
* risks
* owner
* review trigger

---

# Database Technology Exceptions

PostgreSQL is the primary relational database.

A different database technology may be introduced only when:

* PostgreSQL cannot reasonably satisfy the requirement
* the business need is clear
* the operational cost is understood
* security and recovery are understood
* ownership is clear

The introduction of another database creates additional:

* operational complexity
* backup requirements
* monitoring requirements
* developer knowledge requirements

---

# Multiple Database Strategy

Using multiple database technologies should not be the default.

Additional databases may be justified for:

* specialized workloads
* search
* analytics
* caching
* document storage
* unique technical requirements

Each additional datastore should have a clear purpose.

---

# Data Ownership Checklist

For each important data domain:

* [ ] Business owner identified
* [ ] Technical owner identified
* [ ] Data meaning documented
* [ ] Access rules defined
* [ ] Tenant boundaries defined where required
* [ ] Relationships defined
* [ ] Constraints defined
* [ ] Retention requirements considered
* [ ] Backup requirements considered
* [ ] Monitoring requirements considered
* [ ] Security requirements considered
* [ ] Recovery requirements considered

---

# Database Quality Checklist

Before approving a significant database design:

* [ ] Business requirement is clear
* [ ] Data entities are understood
* [ ] Relationships are defined
* [ ] Primary keys are appropriate
* [ ] Foreign keys are appropriate
* [ ] Unique constraints are considered
* [ ] Data validation is considered
* [ ] Indexes are based on expected access patterns
* [ ] Tenant isolation is clear where applicable
* [ ] Migration strategy is defined
* [ ] Backup strategy is understood
* [ ] Recovery expectations are understood
* [ ] Security requirements are addressed
* [ ] Monitoring is addressed
* [ ] Retention is considered
* [ ] Significant decisions are documented

---

# Database Architecture Maturity

EyesightWorks should evolve database architecture gradually.

## Stage 1 — Product MVP

Focus on:

* PostgreSQL
* correct data modeling
* Prisma
* constraints
* migrations
* backups
* basic monitoring

---

## Stage 2 — Growing Product

Introduce:

* query optimization
* better indexes
* improved monitoring
* caching where justified
* stronger backup practices

---

## Stage 3 — Multi-Product Platform

Introduce where appropriate:

* shared platform data capabilities
* clearer domain ownership
* reusable data models
* stronger governance

---

## Stage 4 — High Scale

Evaluate:

* read replicas
* partitioning
* advanced caching
* analytical infrastructure
* additional redundancy

---

# Database Decision Principles

Database decisions should improve one or more of:

* Reliability
* Security
* Performance
* Maintainability
* Scalability
* Data Quality
* Recoverability

Complexity should only be introduced when it provides measurable customer, business, or operational value.

---

# Decision Summary

## Approved

The following database standards are approved:

* PostgreSQL as the primary relational database
* Prisma as the primary ORM for TypeScript/PostgreSQL applications
* Business-driven data modeling
* Domain-oriented organization
* Strong relational integrity
* Version-controlled migrations
* PostgreSQL-based search as the initial search strategy
* Appropriate tenant isolation
* Least-privilege database access
* Backup and recovery planning
* Database monitoring
* Evidence-driven scalability

---

# Deferred / Conditional

The following are not baseline requirements and should be introduced only when justified:

* database-per-tenant
* read replicas
* partitioning
* regional database deployment
* specialized search engines
* multiple primary databases
* advanced distributed database systems

---

# Open Questions

The following questions may be resolved as EyesightWorks grows:

* When should read replicas be introduced?
* Under what conditions should database partitioning be adopted?
* What long-term archival strategy is appropriate for historical data?
* When is regional database deployment justified?
* What database isolation requirements will enterprise customers require?
* When should a separate analytical database become necessary?
* Which shared platform data capabilities should be centralized first?
* What database recovery targets should be required for critical products?

These decisions should be based on business requirements, customer needs, operational evidence, and documented architecture decisions.

---

# Next Document

**docs/06-api-architecture.md**

The API Architecture document defines the standards for how frontend applications, backend systems, mobile applications, and external integrations communicate.

It will define:

* API design principles
* endpoint organization
* request and response standards
* authentication
* authorization
* validation
* error handling
* API versioning
* rate limiting
* API security
* documentation
* integration standards
* scalability

---

# Document Status

**Status:** Approved v1.1

This document establishes the database architecture standards for EyesightWorks Technologies.

The database architecture should remain:

**Correct → Secure → Simple → Observable → Recoverable → Maintainable → Scalable**

The governing principle is:

> **Business Requirement → Data Requirement → Database Design → Secure Access → Reliable Operation → Continuous Improvement**
