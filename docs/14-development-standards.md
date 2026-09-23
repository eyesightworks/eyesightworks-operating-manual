# EyesightWorks Technologies Operating Manual

**Document:** 14 of 17

**Title:** Development Standards

**Version:** 1.0

**Status:** Draft

**Owner:** EyesightWorks Technologies

**Last Updated:** 2026-09-20

---

# Revision History

| Version | Date       | Changes                                 |
| ------- | ---------- | --------------------------------------- |
| 1.0     | 2026-09-20 | Initial Development Standards Framework |

---

# Development Standards

## Executive Summary

This document defines the engineering and software development standards used by EyesightWorks Technologies.

The purpose of the Development Standards is to ensure that software is developed consistently, safely, maintainably, and with appropriate attention to customer and business value.

Development standards should support:

* Reliable software
* Maintainable code
* Consistent engineering practices
* Secure development
* Effective collaboration
* Reproducible environments
* Testable systems
* Controlled releases
* Clear technical documentation

The company follows the principle:

**Business Need → Clear Requirements → Quality Implementation → Test → Deploy → Measure**

Development standards exist to support delivery, not to create unnecessary bureaucracy.

---

# Scope of This Document

This document defines:

* Development principles
* Code quality standards
* Repository standards
* Project structure
* Naming conventions
* Type safety
* API development standards
* Database development standards
* Configuration management
* Error handling
* Logging
* Security practices
* Dependency management
* Documentation standards
* Git standards
* Pull request standards
* Code review
* Testing expectations
* Environment consistency
* Technical debt management

This document does not define:

* Detailed product requirements
* Business strategy
* Customer feedback collection
* Product roadmaps
* Launch readiness
* Detailed architecture decisions
* Financial procedures

Those subjects are documented separately within the Operating Manual.

---

# Development Philosophy

Software should be developed to solve clearly understood business or customer problems.

The company should avoid building unnecessary complexity.

The development process should prioritize:

* Customer value
* Business value
* Simplicity
* Reliability
* Maintainability
* Security
* Testability
* Observability

Engineering decisions should be proportional to the importance and complexity of the problem being solved.

---

# Development Principles

## Understand Before Building

Developers should understand the requirement before implementation begins.

Before significant development work, the team should understand:

* What problem is being solved
* Who benefits from the solution
* What the expected outcome is
* What constraints exist
* What acceptance criteria apply

Unclear requirements should be clarified before significant implementation.

---

## Simplicity Before Complexity

The simplest solution that safely solves the problem should be preferred.

The company should avoid unnecessary:

* Abstractions
* Dependencies
* Services
* Infrastructure
* Design patterns
* Frameworks
* Configuration

Complexity should be introduced when there is a clear reason.

---

## Reuse Before Reinvention

Existing reliable components should be reused when appropriate.

Developers should evaluate whether an existing:

* Module
* Service
* Utility
* Component
* Library
* API
* Internal capability

can solve the problem before creating a new implementation.

---

## Quality Before Speed

Fast development should not create avoidable long-term problems.

Development speed should be balanced with:

* Correctness
* Security
* Maintainability
* Testing
* Documentation
* Operational reliability

---

## Small Changes Before Large Changes

Changes should be kept as focused as practical.

Smaller changes are generally easier to:

* Review
* Test
* Debug
* Deploy
* Roll back
* Understand

---

# Development Lifecycle

Development should generally follow:

```text id="m6e7by"
Business Requirement

↓

Product Requirement

↓

Technical Design

↓

Implementation

↓

Testing

↓

Code Review

↓

Deployment

↓

Monitoring

↓

Measurement

↓

Improvement
```

The level of documentation and review should match the size and risk of the change.

---

# Repository Standards

Every production repository should have a clear purpose.

A repository should normally contain:

* README
* Source code
* Tests
* Configuration templates where appropriate
* Documentation
* Git configuration
* Appropriate ignore files

Sensitive information must not be committed to source control.

Examples include:

* API keys
* Passwords
* Private credentials
* Production secrets
* Authentication secrets
* Payment credentials

---

# Recommended Project Structure

Project structure should be understandable and consistent.

A typical application may include:

```text id="lz4xil"
project/
├── src/
├── tests/
├── docs/
├── scripts/
├── public/
├── .env.example
├── .gitignore
├── README.md
└── package.json
```

The actual structure may differ according to technology and product requirements.

The structure should favor clarity over unnecessary complexity.

---

# Naming Conventions

Naming should be:

* Clear
* Consistent
* Descriptive
* Predictable

Names should communicate purpose.

Poor:

```text
data
thing
temp
x
helper2
```

Better:

```text
customerProfile
propertySearch
paymentStatus
applicationService
```

Naming conventions should remain consistent within each technology.

---

# Type Safety

Where supported, typed programming should be preferred.

For TypeScript applications:

* Avoid unnecessary `any`
* Define interfaces or types where appropriate
* Validate external input
* Use explicit return types where they improve clarity
* Keep shared types consistent

For Python:

* Use type hints where practical
* Validate external data
* Use structured models for API data
* Avoid unvalidated dynamic data where practical

Type safety should improve correctness without creating unnecessary complexity.

---

# Frontend Development Standards

For web applications using React and Next.js:

* Components should have clear responsibilities
* UI logic should remain understandable
* Reusable components should be extracted when reuse is justified
* API communication should be centralized where appropriate
* Loading and error states should be handled
* User input should be validated
* Accessibility should be considered
* Sensitive information should not be exposed to the browser

Frontend code should prioritize usability, maintainability, and performance.

---

# Backend Development Standards

Backend services should have clear separation of responsibilities.

Typical responsibilities may include:

* Controllers or route handlers
* Business logic
* Data access
* Validation
* Authentication
* Authorization
* External integrations

Controllers should not contain excessive business logic.

Business rules should remain testable and maintainable.

---

# API Development Standards

APIs should be predictable and documented.

API development should consider:

* Consistent routes
* Appropriate HTTP methods
* Appropriate status codes
* Input validation
* Response consistency
* Error handling
* Authentication
* Authorization
* Pagination where appropriate
* Filtering where appropriate
* API documentation

Public APIs should avoid exposing internal implementation details unnecessarily.

---

# API Documentation

Important APIs should be documented.

Documentation should include:

* Endpoint
* HTTP method
* Authentication requirements
* Request format
* Response format
* Validation rules
* Error responses
* Example usage

OpenAPI or equivalent documentation should be used where practical.

---

# Database Development Standards

Database changes should be deliberate and reviewable.

Development should consider:

* Data integrity
* Relationships
* Constraints
* Indexes
* Query performance
* Migration safety
* Backup requirements
* Data consistency

Database changes should use controlled migrations where the technology supports them.

Production databases should not be modified casually through undocumented manual changes.

---

# Prisma Standards

Where Prisma is used:

* Schema changes should be reviewed
* Migrations should be tracked
* Generated client code should follow project conventions
* Database queries should remain understandable
* N+1 query problems should be avoided where practical
* Sensitive data should not be unnecessarily returned

Prisma should provide a consistent data-access layer rather than hiding poor database design.

---

# Python Development Standards

Where Python services are used:

* Use virtual environments during local development
* Maintain dependency requirements
* Use type hints where practical
* Validate API inputs
* Keep modules focused
* Handle exceptions appropriately
* Document service responsibilities

FastAPI services should use structured request and response models where appropriate.

Python services should exist for clear product or technical reasons rather than simply increasing technology count.

---

# Configuration Management

Environment-specific configuration should not be hard-coded into source code.

Use environment variables or approved configuration systems for:

* Database URLs
* API keys
* Authentication secrets
* External service credentials
* Environment-specific settings

A safe example configuration should be provided where useful:

```text id="j67m8v"
.env.example
```

Production secrets must remain outside source control.

---

# Environment Standards

Development, testing, staging, and production environments should be distinguishable.

Where practical:

```text id="g8etun"
Development
    ↓
Testing
    ↓
Staging
    ↓
Production
```

Changes should be tested in an environment appropriate to their risk before production release.

---

# Docker Standards

Docker should be used where containerization provides clear value.

When Docker is used:

* Images should have clear names
* Dockerfiles should be maintained with the service
* Secrets should not be embedded into images
* Unnecessary packages should be avoided
* Images should use appropriate base images
* Containers should run only the processes they require
* Development and production configurations should be clearly distinguished

Docker Compose may be used to manage local multi-service development environments.

A typical environment may include:

```text id="w6dbfa"
Docker Compose
│
├── Frontend
├── Backend
├── PostgreSQL
└── Redis
```

The actual services should reflect product requirements.

---

# Dependency Management

Dependencies should be selected deliberately.

Before adding a dependency, developers should consider:

* Security
* Maintenance
* License
* Community support
* Size
* Reliability
* Actual need

Unused dependencies should be removed.

Dependency versions should be controlled through the appropriate package-management system.

---

# Error Handling

Errors should be handled intentionally.

The application should:

* Return appropriate responses
* Provide useful logs
* Avoid exposing sensitive information
* Give users understandable messages where appropriate
* Preserve debugging information internally

Errors should not be silently ignored without justification.

---

# Logging Standards

Applications should produce useful logs.

Logs should help identify:

* Errors
* Failed operations
* Important state changes
* External integration failures
* Security-relevant events
* Performance problems

Logs should not contain sensitive information such as:

* Passwords
* Tokens
* Private keys
* Payment secrets

Logging volume should remain practical and useful.

---

# Security Standards

Security should be considered throughout development.

Developers should:

* Validate input
* Protect credentials
* Enforce authorization
* Use secure authentication
* Avoid exposing secrets
* Protect sensitive data
* Keep dependencies updated
* Review external integrations
* Minimize unnecessary permissions

Security-critical decisions should be documented where appropriate.

---

# Authentication and Authorization

Authentication determines who the user is.

Authorization determines what the user can do.

The system should keep these concepts separate.

Where role-based access control is used:

```text id="fwhqj5"
User
 ↓
Authentication
 ↓
Identity
 ↓
Role
 ↓
Permission
 ↓
Action
```

Authorization rules should be enforced on the backend.

Frontend checks should not be treated as a replacement for backend authorization.

---

# Input Validation

All external input should be treated as untrusted.

Input may originate from:

* Web forms
* API requests
* Mobile applications
* Query parameters
* Uploaded files
* External services

Validation should occur before data is processed or stored.

---

# File Upload Standards

File uploads should consider:

* File type
* File size
* Storage location
* Access control
* File naming
* Security
* Error handling

External storage services such as Cloudinary or other approved services may be used when appropriate.

---

# Payment Development Standards

When payment systems are integrated:

* Payment credentials must remain secure
* Payment status should be verified server-side
* Transactions should be recorded
* Webhooks should be validated
* Failed payments should be handled
* Duplicate payment processing should be considered
* Test and production credentials should remain separate

Payments should not be considered successful solely because a frontend request reports success.

---

# Testing Standards

Development should include appropriate testing.

Testing may include:

* Unit tests
* Integration tests
* API tests
* End-to-end tests
* Manual acceptance testing

Critical business logic should have appropriate automated coverage.

Testing requirements should be proportional to risk.

Detailed testing standards may be defined in a separate Operating Manual document.

---

# Code Review

Significant code changes should be reviewed before production deployment.

Code review should examine:

* Correctness
* Security
* Maintainability
* Performance
* Test coverage
* Error handling
* Naming
* Documentation
* Scope of change

Code review should improve the code rather than become a personal judgment of the developer.

---

# Pull Request Standards

Pull requests should be:

* Focused
* Understandable
* Small enough to review
* Properly described
* Linked to relevant work where applicable

A pull request description should explain:

* What changed
* Why it changed
* How it was tested
* Any important limitations
* Any deployment considerations

---

# Git Standards

Git should be used consistently for source control.

Branches should have clear purposes.

Examples:

```text id="9u7h5b"
main
develop
feature/*
fix/*
refactor/*
```

The exact branching strategy may vary by project.

Commit messages should communicate meaningful changes.

Good example:

```text
Add property search API
```

Poor example:

```text
update
changes
fix stuff
```

---

# Commit Standards

Commits should ideally be:

* Focused
* Understandable
* Reversible where practical
* Related to a meaningful change

Developers should avoid mixing unrelated changes into one commit.

---

# GitHub Standards

Repositories should maintain:

* Clear README
* Appropriate `.gitignore`
* Protected secrets
* Meaningful commit history
* Appropriate branch controls
* Issues or project tracking where useful

Repository access should follow least-privilege principles.

---

# Continuous Integration

Where appropriate, GitHub Actions or another CI system should automatically verify:

* Installation
* Build
* Tests
* Linting
* Formatting
* Important quality checks

A change that fails required checks should not be treated as production-ready.

---

# Code Formatting and Linting

Projects should use automated formatting and linting where supported.

For example:

* ESLint
* Prettier
* Python formatters
* Python linters

The project should define its formatting rules rather than relying on individual developer preferences.

---

# Documentation Standards

Important technical decisions and workflows should be documented.

Documentation may include:

* README
* Setup instructions
* Environment configuration
* API documentation
* Architecture documentation
* Deployment instructions
* Troubleshooting
* Known limitations

Documentation should be updated when significant implementation changes make it inaccurate.

---

# Technical Debt

Technical debt should be tracked rather than ignored.

Technical debt may include:

* Temporary workarounds
* Known performance limitations
* Outdated dependencies
* Duplicated code
* Incomplete testing
* Deferred refactoring
* Infrastructure limitations

Technical debt should be prioritized according to customer, business, security, and engineering impact.

---

# Development Standards for AI-Assisted Coding

AI tools may be used to support development.

However, developers remain responsible for:

* Understanding generated code
* Reviewing generated code
* Testing generated code
* Verifying security
* Checking dependencies
* Protecting confidential information
* Ensuring alignment with project requirements

AI-generated code should not be committed blindly.

The same engineering standards apply regardless of how code was produced.

---

# Performance Standards

Performance should be considered according to actual product requirements.

Developers should avoid premature optimization.

Performance work should be driven by:

* Measured bottlenecks
* Customer impact
* Infrastructure limitations
* Business requirements

Performance improvements should be measured where practical.

---

# Accessibility Standards

Products should consider accessibility during development.

Development should consider:

* Keyboard navigation
* Readable text
* Sufficient contrast
* Clear labels
* Accessible forms
* Meaningful error messages
* Appropriate semantic structure

Accessibility should be treated as part of product quality.

---

# Release Readiness

Before a production release, developers should verify:

* Code builds
* Required tests pass
* Critical bugs are addressed
* Configuration is correct
* Database changes are reviewed
* Security issues are reviewed
* Monitoring is available where required
* Deployment instructions are ready

Document 10 provides the broader Launch Checklist.

---

# Development Quality Checklist

Before considering significant development work complete:

* [ ] Requirement understood
* [ ] Appropriate design chosen
* [ ] Code implemented
* [ ] Input validation added
* [ ] Error handling considered
* [ ] Security reviewed
* [ ] Tests added or updated
* [ ] Code formatted
* [ ] Linting passed
* [ ] Documentation updated where necessary
* [ ] Code reviewed
* [ ] Deployment impact considered
* [ ] Technical debt documented where applicable

---

# Development Governance

Development standards should improve engineering consistency without creating unnecessary process.

The company should:

* Apply stronger controls to higher-risk changes
* Keep routine development lightweight
* Automate repetitive quality checks
* Review standards periodically
* Remove standards that no longer provide value

The goal is:

**High Quality Without Unnecessary Bureaucracy**

---

# Relationship With Other Operating Manual Documents

## Decision Log

Document 08 provides governance for significant technical and engineering decisions.

Technical decisions that materially affect the company should reference the appropriate Decision ID.

---

## Customer Feedback

Document 09 provides customer evidence that may influence development priorities.

Engineering work should connect to validated customer or business needs where appropriate.

---

## Launch Checklist

Document 10 defines broader launch readiness requirements.

Development should prepare the technical components required for launch.

---

## Metrics Dashboard

Document 11 defines engineering and operational metrics used to measure software and system performance.

---

## Business Value Score

Document 12 provides a framework for evaluating the business value of opportunities before significant engineering investment.

---

## Brand Guidelines

Document 13 provides standards for customer-facing brand and product presentation.

Development teams should preserve approved product branding where relevant.

---

# Development Records

Significant development standards, technical decisions, and exceptions should be documented where appropriate.

A development record may include:

| Field            | Description                    |
| ---------------- | ------------------------------ |
| Record ID        | Unique identifier              |
| Project          | Related project                |
| Date             | Date of record                 |
| Change           | Development change             |
| Reason           | Why the change was made        |
| Owner            | Responsible person             |
| Testing          | Validation performed           |
| Related Decision | Decision ID where applicable   |
| Status           | Active, Completed, or Archived |

---

# Decision Summary

## Approved

* Business-value-driven development
* Clear requirements before implementation
* Simplicity before unnecessary complexity
* Reuse before reinvention
* Small and focused changes
* Type-safe development
* Consistent project structure
* API standards
* Database standards
* Secure configuration management
* Error handling and logging
* Authentication and authorization standards
* Input validation
* Payment development standards
* Testing expectations
* Code review
* Git and GitHub standards
* CI practices
* Documentation standards
* Technical debt tracking
* AI-assisted development review
* Accessibility and performance awareness
* Development quality checklist
* Cross-document technical governance

---

## Open Questions

* Which branching strategy should become the company standard?
* What minimum automated checks should every repository require?
* Which testing coverage targets should be adopted?
* Which coding standards should be mandatory across all projects?
* Which development metrics should be included in the Metrics Dashboard?
* Which CI/CD requirements should apply to production repositories?
* What process should be used to approve exceptions to development standards?

---

# Operating Principle

EyesightWorks Technologies should build software that is understandable, maintainable, secure, testable, and valuable.

The company should follow:

**Understand → Design → Build → Test → Review → Deploy → Measure → Improve**

Development standards exist to make good engineering repeatable while keeping the focus on customer and business value.
