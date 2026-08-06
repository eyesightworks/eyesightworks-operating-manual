# EyesightWorks Technologies Operating Manual

**Document:** 05 of 17

**Title:** Database Architecture

**Version:** 1.0

**Status:** Draft

**Owner:** EyesightWorks Technologies

**Last Updated:** 2026-08-05

---

# Revision History

| Version | Date       | Changes                       |
| ------- | ---------- | ----------------------------- |
| 1.0     | 2026-08-05 | Initial Database Architecture |

---

# Database Architecture

## Executive Summary

This document defines the database architecture standards for EyesightWorks Technologies.

The purpose of this document is to establish a secure, scalable, maintainable, and reusable data foundation that supports multiple software products across the company ecosystem.

The database architecture should enable:

* Reliable data management
* High performance
* Data integrity
* Secure data access
* Scalability
* Reusable platform capabilities
* Long-term maintainability

Database architecture exists to support the company's operating philosophy:

**Business → Product → Architecture → Engineering**

This document defines how company data should be organized, managed, and protected.

It does not define:

* Product-specific database schemas
* Individual business entities
* API design
* Backend modules
* Frontend implementation

Those subjects belong in their respective architecture documents.

---

# Database Architecture Principles

The database architecture follows these principles:

## Data Integrity Before Convenience

Data correctness is more important than short-term implementation speed.

The database should enforce rules that protect business data quality.

---

## Security by Default

Customer and company data must be protected through appropriate security controls.

---

## Performance Through Good Design

Performance should come from:

* Proper schema design
* Efficient queries
* Appropriate indexing
* Database optimization

---

## Reusability Before Duplication

Shared data capabilities should be created once and reused across products.

---

## Scalability Through Simplicity

The company prefers simple, reliable database solutions before introducing additional complexity.

---

## Business Requirements Drive Data Models

Database structures should represent real business requirements rather than technical preferences.

---

# Platform-First Database Architecture

The database architecture is designed around reusable platform capabilities shared across EyesightWorks Technologies products.

Product-specific data models should extend the platform rather than duplicate existing capabilities.

Shared platform data may include:

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
* Audit Logs
* System Configuration
This supports the company principle:

**Build once. Reuse everywhere.**

---

# Primary Database

## Approved Database

**PostgreSQL**

## Reason

PostgreSQL provides:

* Strong relational data modeling
* ACID compliance
* Reliable transactions
* Advanced indexing
* JSON support
* Full-text search capabilities
* Long-term scalability
* Mature ecosystem

PostgreSQL is the company's primary relational database standard.

---

# Database ORM

## Approved ORM

**Prisma ORM**

## Reason

Prisma provides:

* Type-safe database access
* Schema management
* Database migrations
* Developer productivity
* Consistency across projects

All backend applications should use Prisma unless an approved exception exists.

---

# Database Organization

The platform should organize data into logical business domains.

Examples include:

* Identity
* Organizations
* Authentication
* Billing
* Notifications
* AI Services
* File Management
* Reporting
* Audit
* * Business Domains

Each domain should maintain clear ownership and responsibilities.

Domains should remain independent where practical to reduce unnecessary coupling.

---

# Multi-Tenancy Strategy

EyesightWorks Technologies products are designed to support multiple organizations and business customers.

## Initial Strategy

The preferred initial approach is:

**Shared database with tenant isolation**

Tenant isolation should be enforced through both application logic and database access controls to prevent unauthorized access between organizations.

Each business record should belong to an organization or tenant where appropriate.

Benefits:

* Efficient infrastructure usage
* Lower operational cost
* Easier maintenance
* Faster product development
* Simplified deployment

## Future Consideration

Alternative strategies such as:

* Database-per-tenant
* Isolated customer infrastructure
* Regional database deployment

may be evaluated when customer scale, security requirements, compliance needs, or operational evidence justify additional complexity.

---

---

# Data Integrity

Data integrity is a fundamental responsibility of the database architecture.

The database should enforce:

- Primary keys
- Foreign keys
- Unique constraints
- Check constraints
- Referential integrity
- Appropriate cascading rules

Whenever practical, business rules that protect data consistency should be enforced at the database level rather than relying solely on application logic.

---

# Database Relationships

Relationships should be:

- Clearly defined
- Based on business requirements
- Properly indexed
- Designed for long-term maintainability

Many-to-many relationships should be implemented using junction tables.

Unnecessary relationships and excessive coupling should be avoided to maintain a clean and scalable data model.

---

# Indexing Strategy

Indexes should be designed to support:

- Primary keys
- Foreign keys
- Frequently searched fields
- Filtering
- Sorting
- Reporting queries
- Full-text search

Indexes should be reviewed periodically because excessive or unused indexes can negatively affect write performance and storage efficiency.

---

# Search Strategy

The approved search solution for the initial platform is:

**PostgreSQL Full-Text Search**

Dedicated search technologies will only be introduced when validated business requirements justify the additional operational complexity.

Deferred search technologies may include:

- Elasticsearch
- Meilisearch
- Other specialized search platforms

---

# Schema Evolution

Database schemas should evolve through version-controlled migrations.

Approved migration approach:

**Prisma Migration System**

Migration principles:

- Version controlled
- Reviewable
- Tested before deployment
- Documented
- Reversible where practical
- Backward compatible whenever practical

Direct modification of production databases should be avoided.

---

# Data Ownership

Every piece of business data should have a clearly defined owner.

Each business domain is responsible for:

- Creating its own data
- Validating its own business rules
- Managing its own lifecycle

Shared platform services should expose data through application services rather than unrestricted direct database access.

---

# Data Security

Sensitive data must be protected through appropriate security controls.

Security measures include:

- Encryption in transit
- Encryption at rest where appropriate
- Secure credential management
- Role-based access control
- Least-privilege access
- Secret management

Database access should be limited to authorized systems and approved personnel.

---

# Backup and Recovery

Production databases should support:

- Automated backups
- Backup verification
- Recovery testing
- Point-in-time recovery where available
- Backup monitoring

A backup strategy is not complete unless recovery procedures have been successfully tested.

Business continuity depends on both reliable backups and verified recovery processes.

---

# Performance Strategy

Database performance should primarily be achieved through:

- Efficient schema design
- Query optimization
- Appropriate indexing
- Pagination
- Connection pooling
- Caching where appropriate
- Continuous performance monitoring

Performance optimization should be driven by measured evidence rather than assumptions.

---

# Database Monitoring

Production databases should continuously monitor:

- Query performance
- Slow queries
- Connection utilization
- Storage growth
- Failed operations
- Database availability

Monitoring should provide early visibility into potential issues before they affect customers.

---

# Audit and Historical Data

Important business events should be recorded through audit logs.

Audit records may include:

- User activity
- Authentication events
- Permission changes
- Billing actions
- Administrative actions
- System events

Where practical, audit records should remain immutable to preserve historical accuracy and accountability.

---

# Data Lifecycle

Business data should follow an appropriate lifecycle.

Where business requirements permit, records should be archived or soft deleted rather than permanently removed.

Soft deletion supports:

- Data recovery
- Audit requirements
- Historical reporting

Permanent deletion should be limited to situations where it is operationally, contractually, or legally required.

---

# Data Retention

Data retention policies should balance:

- Business requirements
- Customer expectations
- Legal obligations
- Storage costs

Each product may define additional retention policies based on its operational and regulatory requirements.

---

# Scalability Strategy

Database scalability should evolve gradually as business needs grow.

## MVP Stage

Focus on:

- Simple architecture
- Reliable data storage
- Rapid product validation

## Growth Stage

Introduce:

- Query optimization
- Improved monitoring
- Performance tuning
- Infrastructure optimization

## Enterprise Stage

Evaluate:

- Read replicas
- Database partitioning
- Advanced database infrastructure
- Regional deployment strategies

Additional complexity should only be introduced when supported by measurable business or operational evidence.

---

# Database Decision Principles

Database decisions should improve one or more of the following:

- Reliability
- Security
- Performance
- Maintainability
- Scalability
- Data quality

Complexity should only be introduced when it delivers measurable customer, business, or operational value.

---

# Decision Summary

## Approved

- PostgreSQL as the primary database
- Prisma ORM
- Platform-first data architecture
- Shared database with tenant isolation
- Business domain organization
- Version-controlled schema migrations
- PostgreSQL Full-Text Search
- Strong relational data model
- Audit logging
- Evidence-driven scalability

---

## Open Questions

- When should read replicas be introduced?
- Under what conditions should database partitioning be adopted?
- What long-term archival strategy is appropriate for historical data?
- When is regional database deployment justified?
- What disaster recovery objectives are required for enterprise customers?

---

# Next Document

## 06-api-architecture.md

This document defines the API architecture standards used across EyesightWorks Technologies.

It will define:

- API design principles
- Endpoint organization
- Authentication and authorization
- API versioning
- Request and response standards
- Validation strategy
- Error handling
- Rate limiting
- API security
- API documentation
- API scalability