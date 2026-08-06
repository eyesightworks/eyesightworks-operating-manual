# EyesightWorks Technologies Operating Manual

**Document:** 03A of 17

**Title:** Technology Stack

**Version:** 1.0

**Status:** Draft

**Owner:** EyesightWorks Technologies

**Last Updated:** 2026-08-05

---

# Revision History

| Version | Date | Changes |
|---------|------------|----------------------------|
| 1.0 | 2026-08-05 | Initial Technology Stack |

---

# Technology Stack

## Executive Summary

This document defines the approved technology stack for EyesightWorks Technologies.

Its purpose is to standardize the technologies used across company products while allowing the platform to evolve as business requirements change.

Technology choices exist to support business objectives rather than personal preference.

Every approved technology should improve one or more of the following:

- Customer Value
- Engineering Productivity
- Platform Scalability
- Operational Reliability
- Long-Term Maintainability

This document defines **what technologies are approved and why they have been selected.**

It does **not** define application architecture, module organization, coding standards, Git workflows, testing procedures, or engineering processes.

Those subjects are documented separately within the operating manual.

---

# Technology Philosophy

Technology supports business outcomes.

Engineering decisions follow these principles:

- Choose proven technologies over experimental ones.
- Prefer simplicity over unnecessary complexity.
- Build reusable platform capabilities.
- Adopt cloud-native engineering practices.
- Automate repetitive engineering tasks.
- Optimize for maintainability and long-term scalability.
- Introduce new technologies only when they provide measurable value.

Technology should never be adopted solely because it is popular or trending.

---

# Approved Technology Stack

The following technologies are approved for use across EyesightWorks Technologies products.

---

# Frontend

## Framework

- Next.js 15

**Reason**

Provides server-side rendering, static site generation, routing, performance optimization, and an excellent developer experience.

---

## UI Library

- React

**Reason**

Provides a mature component-based architecture with a large ecosystem and long-term stability.

---

## Programming Language

- TypeScript

**Reason**

Improves maintainability, developer productivity, and application scalability through static typing.

---

## Styling

- Tailwind CSS

**Reason**

Accelerates development through utility-first styling while maintaining consistency.

---

## UI Components

- Shadcn UI

**Reason**

Provides accessible, reusable, and customizable interface components.

---

## Data Fetching

- TanStack Query (React Query)

**Reason**

Provides caching, synchronization, background updates, and efficient server-state management.

---

## Forms

- React Hook Form

**Reason**

Provides high-performance form handling with minimal re-rendering.

---

## Validation

- Zod

**Reason**

Allows shared validation logic between frontend and backend.

---

# Backend

## Framework

- NestJS

**Reason**

Provides a modular architecture suitable for scalable business applications.

---

## Programming Language

- TypeScript

**Reason**

Maintains consistency across the entire technology stack.

---

## API Standard

Primary

- REST API

Optional

- GraphQL

**Reason**

REST remains the default API approach.

GraphQL may be adopted only when client flexibility provides measurable business or engineering value.

---

## Real-Time Communication

- WebSockets

**Reason**

Supports real-time user experiences such as notifications, dashboards, and live updates.

---

## Background Processing

- Cron Jobs
- Background Workers

**Reason**

Supports scheduled tasks, asynchronous processing, reporting, email delivery, and AI workloads.

---

# Database

## Primary Database

- PostgreSQL

**Reason**

Provides reliability, strong relational capabilities, and excellent long-term scalability.

---

## ORM

- Prisma ORM

**Reason**

Provides type-safe database access, schema management, and migration support.

---

## Database Features

- Database Migrations
- Index Optimization
- Full-Text Search

---

# Authentication & Security

## Authentication

- JWT
- Refresh Tokens

---

## Authorization

- Role-Based Access Control (RBAC)

---

## Identity Providers

- Google OAuth

---

## Security Standards

- Email Verification
- Password Reset
- Rate Limiting
- Input Validation
- Security Headers

---

# File & Media

## Media Platform

- Cloudinary

**Reason**

Provides optimized media storage, image transformation, CDN delivery, and document management.

---

# Payments

## Supported Providers

- Stripe
- Paystack
- Flutterwave

**Reason**

Supports international and African payment requirements while reducing vendor dependency.

Payment providers may vary depending on customer location and business requirements.

---

# Caching

## Primary Cache

- Redis

**Reason**

Provides caching, session storage, background job queues, and improved application performance.

---

# Cloud Infrastructure

## Containerization

- Docker
- Docker Compose

---

## Reverse Proxy

- Nginx

---

## Configuration

- Environment Variables
- Secret Management

---

## Hosting

Current platforms

- Vercel
- Render
- GitHub

Future cloud providers

- AWS EC2
- AWS RDS
- AWS S3
- AWS CloudFront
- AWS IAM
- AWS CloudWatch

**Guiding Principle**

The platform should remain cloud-portable and avoid unnecessary vendor lock-in.

---

# Continuous Integration

## Source Control

- Git
- GitHub

---

## Automation

- GitHub Actions

**Objectives**

- Automated Testing
- Automated Builds
- Automated Deployment
- Docker Image Publishing

---

# Testing

## Unit Testing

- Jest

---

## Integration Testing

- Supertest

---

## End-to-End Testing

- Playwright

**Guiding Principle**

Testing coverage should increase as products mature.

---

# Monitoring

## Monitoring

- Prometheus
- Grafana

---

## Error Tracking

- Sentry

---

## Logging

- Structured Logging

---

# Artificial Intelligence

## AI Philosophy

Artificial intelligence is treated as a reusable platform capability rather than a product dependency.

AI providers are implementation choices and may change over time without affecting platform architecture.

Applications should interact with AI through a shared abstraction layer that allows provider replacement, cost optimization, and future expansion.

---

## Approved AI Providers

- OpenRouter
- OpenAI

---

## Approved AI Capabilities

- Prompt Management
- Prompt Templates
- AI Usage Tracking
- AI Cost Monitoring

---

# Developer Tools

## Development

- Git
- GitHub
- ESLint
- Prettier
- Husky

---

## API Documentation

- Swagger / OpenAPI

---

## API Testing

- Postman
- Thunder Client

---

# Deferred Technologies

The following technologies are intentionally deferred.

They are **not part of the approved technology stack** and will only be introduced when customer demand, business growth, technical requirements, or operational evidence clearly justify the additional complexity.

This approach supports the company's **Depth before Breadth** strategy and evidence-driven engineering philosophy.

Before any deferred technology is adopted, it should answer the following questions:

- What business problem does it solve?
- Why can't the current technology stack solve it?
- What measurable value will it provide?
- Do the expected benefits outweigh the additional implementation and operational complexity?
- Can the engineering team effectively support and maintain it?

If these questions cannot be answered with validated evidence, the technology should remain deferred.

---

## Infrastructure

- Kubernetes

**Review Trigger**

Adopt when application scale, deployment complexity, or operational requirements exceed the capabilities of the current Docker-based infrastructure.

---

## Messaging & Event Streaming

- Kafka
- Advanced Event Streaming

**Review Trigger**

Adopt only when distributed event processing, high-throughput messaging, or service decoupling provides measurable business or operational value beyond the capabilities of the current platform.

---

## Artificial Intelligence

- Retrieval-Augmented Generation (RAG)
- Embeddings
- Fine-Tuned Models
- Multi-Agent Systems
- Vector Databases

**Review Trigger**

Adopt only when customer requirements demonstrate measurable improvements in productivity, decision-making, automation, or customer value.

---

## Mobile

- Native Mobile Applications

**Review Trigger**

Adopt when validated customer demand or product strategy demonstrates that native mobile applications provide greater value than responsive web applications.

---

## Analytics

- Advanced Data Warehouse

**Review Trigger**

Adopt when reporting, business intelligence, or analytical requirements exceed the capabilities of the operational database.

---

Deferred technologies will be reviewed as part of the company's architecture review process.

A technology may be promoted to the approved technology stack only when validated evidence demonstrates that its business and technical benefits outweigh its implementation and operational costs.

---

# Technology Decision Principles

Technology adoption should improve at least one of the following:

- Customer Value
- Engineering Productivity
- Platform Scalability
- Security
- Operational Reliability
- Maintainability
- Cost Efficiency

Technologies that do not create measurable value should not be adopted.

---

# Decision Summary

## Approved

- Full-stack TypeScript
- Next.js
- NestJS
- PostgreSQL
- Prisma ORM
- Redis
- Docker-Based Deployment
- Cloud-Native Strategy
- AI Provider Abstraction
- Multi-Payment Support
- Evidence-Driven Technology Adoption

---

## Open Questions

- When should Kubernetes replace Docker Compose?
- When will distributed event streaming become necessary?
- What AI provider mix offers the best long-term cost and performance?
- When should the platform transition to dedicated cloud infrastructure?

---

# Next Document

## 03-backend-architecture.md

This document defines how the approved technologies are organized into a scalable backend architecture, including service boundaries, modules, authentication flow, shared services, deployment strategy, and scalability approach.