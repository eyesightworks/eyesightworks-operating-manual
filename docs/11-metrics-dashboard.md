# EyesightWorks Technologies Operating Manual

**Document:** 11 of 17

**Title:** Metrics Dashboard

**Version:** 1.0

**Status:** Draft

**Owner:** EyesightWorks Technologies

**Last Updated:** 2026-09-20

---

# Revision History

| Version | Date       | Changes                             |
| ------- | ---------- | ----------------------------------- |
| 1.0     | 2026-09-20 | Initial Metrics Dashboard Framework |

---

# Metrics Dashboard

## Executive Summary

This document defines how EyesightWorks Technologies measures, monitors, reviews, and communicates business, product, customer, revenue, engineering, and operational performance.

The Metrics Dashboard converts company activity into measurable evidence.

The purpose of the dashboard is not simply to display numbers.

The dashboard should help the company understand:

* What is happening
* Why it may be happening
* Whether objectives are being achieved
* Where problems are emerging
* Which decisions may be required
* Whether investments are producing expected outcomes

The company follows the principle:

**Measure → Understand → Decide → Improve**

Metrics should support the company's operating philosophy:

**Business → Product → Architecture → Engineering**

---

# Scope of This Document

This document defines:

* Metrics principles
* Business metrics
* Customer metrics
* Product metrics
* Revenue metrics
* Engineering metrics
* Operational metrics
* Metric ownership
* Measurement frequency
* Dashboard structure
* Metric review
* Trend analysis
* Action tracking
* Cross-document relationships

This document does not define:

* Product specifications
* Technical architecture
* Detailed financial accounting
* Marketing campaign execution
* Customer support procedures
* Development standards

Those subjects are documented separately within the Operating Manual.

---

# Metrics Philosophy

Metrics exist to improve decision quality.

A metric should answer a meaningful business, product, customer, engineering, or operational question.

The company should avoid measuring numbers simply because they are easy to collect.

The company follows the principle:

**Measure What Matters.**

A metric should have a clear relationship to:

* A company objective
* A customer outcome
* A product outcome
* A business outcome
* An operational requirement
* A decision

---

# Metrics Principles

## Business Outcomes Before Activity

The company should prioritize outcome metrics over activity metrics.

For example:

**Activity:**

* Number of features released

**Outcome:**

* Number of customers successfully using the feature

Activity measurements may be useful, but they should not be confused with business success.

---

## Measurement Before Assumptions

Important decisions should use measurable evidence whenever practical.

Metrics should help the company identify whether assumptions are supported by actual results.

---

## Consistent Definitions

Each metric should have a clear definition.

The company should document:

* Metric name
* Definition
* Formula
* Data source
* Owner
* Frequency
* Target where applicable

Different teams should not use different definitions for the same metric without documentation.

---

## Trends Before Isolated Numbers

A single number rarely provides sufficient context.

The company should examine:

* Historical values
* Changes over time
* Comparisons with targets
* Segment differences
* Significant events affecting results

Trends should be interpreted together with customer and business evidence.

---

## Actionable Metrics

A metric is more valuable when its movement can lead to a decision or action.

Metrics should therefore be connected to:

* Investigation
* Experimentation
* Product changes
* Operational improvements
* Business decisions

---

# Metrics Categories

The company should organize metrics into the following major categories:

```text
Business
   ↓
Customer
   ↓
Product
   ↓
Revenue
   ↓
Engineering
   ↓
Operations
```

Different products may use additional categories where necessary.

---

# Business Metrics

Business metrics measure the overall performance and progress of the company.

Examples include:

* Number of active business customers
* New customers
* Customer growth
* Customer retention
* Customer acquisition
* Business opportunities generated
* Qualified leads
* Partnerships
* Market expansion
* Business conversion

Business metrics should reflect actual company objectives.

---

# Customer Metrics

Customer metrics measure customer acquisition, engagement, satisfaction, retention, and outcomes.

Examples include:

* New customer registrations
* Active customers
* Returning customers
* Customer activation
* Customer retention
* Customer churn
* Customer enquiries
* Customer response rate
* Customer satisfaction
* Support requests
* Customer problem resolution

Customer metrics should be interpreted alongside customer feedback.

---

# Product Metrics

Product metrics measure how customers interact with and benefit from the product.

Examples include:

* Active users
* Feature adoption
* Workflow completion
* Search activity
* Product views
* Applications
* Enquiries
* Transactions
* Conversion rates
* User retention
* Session activity
* Feature usage

Product metrics should focus on meaningful customer behavior rather than vanity metrics.

---

# Revenue Metrics

Revenue metrics measure financial performance generated by products and services.

Examples include:

* Revenue
* Monthly recurring revenue where applicable
* Average revenue per customer
* Number of paying customers
* Payment success rate
* Transaction volume
* Subscription conversions
* Customer lifetime value where measurable
* Refunds
* Failed payments

Revenue metrics should be based on reliable financial data.

Accounting records remain the authoritative source for formal financial reporting.

---

# Engineering Metrics

Engineering metrics measure software development effectiveness and system quality.

Examples include:

* Deployment frequency
* Release frequency
* Build success rate
* Test success rate
* Defect rate
* Production incidents
* Mean time to recovery
* Lead time for changes
* API performance
* Error rate
* Failed deployments

Engineering metrics should improve engineering decisions rather than encourage unhealthy activity.

The company should avoid optimizing engineering teams for metric performance at the expense of product quality or customer outcomes.

---

# Operational Metrics

Operational metrics measure the reliability and health of company systems.

Examples include:

* System availability
* API uptime
* Response time
* Error rate
* Infrastructure incidents
* Database health
* Backup status
* Recovery performance
* Security incidents
* Monitoring alerts

Operational metrics should help identify problems before they create significant customer impact.

---

# Metric Definition Standard

Every important metric should have a documented definition.

The standard metric record is:

| Field       | Description                                                      |
| ----------- | ---------------------------------------------------------------- |
| Metric ID   | Unique identifier                                                |
| Metric Name | Name of the metric                                               |
| Category    | Business, Customer, Product, Revenue, Engineering, or Operations |
| Definition  | What the metric measures                                         |
| Formula     | Calculation method where applicable                              |
| Data Source | System or source providing the data                              |
| Owner       | Person responsible for the metric                                |
| Frequency   | How often the metric is reviewed                                 |
| Target      | Expected value where applicable                                  |
| Threshold   | Level requiring investigation where applicable                   |
| Action      | Expected response when significant change occurs                 |

---

# Metric Ownership

Every critical metric should have an owner.

The metric owner is responsible for:

* Maintaining the metric definition
* Verifying data quality
* Reviewing performance
* Identifying significant changes
* Reporting issues
* Initiating investigation where required

Metric ownership prevents important measurements from becoming unmanaged.

---

# Measurement Frequency

Different metrics require different review frequencies.

Typical frequencies include:

| Frequency | Typical Use                                  |
| --------- | -------------------------------------------- |
| Real-Time | Critical operational health                  |
| Daily     | Product activity and system monitoring       |
| Weekly    | Customer activity and operational trends     |
| Monthly   | Business, revenue, and product performance   |
| Quarterly | Strategic performance and company objectives |

The appropriate frequency should depend on the metric's importance and volatility.

---

# Dashboard Structure

The primary dashboard should organize information into meaningful sections.

```text
EyesightWorks Metrics Dashboard
│
├── Business
├── Customers
├── Product
├── Revenue
├── Engineering
└── Operations
```

The dashboard should highlight:

* Current performance
* Historical trends
* Targets
* Important changes
* Risks
* Required actions

---

# Dashboard Status

Important metrics may use status indicators to simplify review.

Approved status categories are:

* Healthy
* Watch
* Action Required
* Critical

These statuses should be based on documented thresholds where practical.

They should not replace detailed analysis.

---

# Metric Thresholds

Where appropriate, important metrics should have defined thresholds.

For example:

```text
Target
   ↓
Healthy
   ↓
Watch
   ↓
Action Required
   ↓
Critical
```

Thresholds should be based on:

* Historical performance
* Business objectives
* Customer impact
* Operational requirements
* Product expectations

Thresholds should be reviewed when business conditions change.

---

# Trend Analysis

The company should review meaningful trends rather than only current values.

Trend analysis should consider:

* Direction
* Rate of change
* Duration
* Magnitude
* Customer segment
* Product area
* Business impact

A significant change should trigger investigation when necessary.

---

# Metric Review Process

Metric review should follow a structured process:

```text
Collect

↓

Validate

↓

Measure

↓

Compare

↓

Interpret

↓

Identify Change

↓

Decide

↓

Act

↓

Measure Again
```

The purpose is to turn metrics into action rather than passive reporting.

---

# Metrics and Customer Feedback

Metrics should be evaluated together with customer feedback.

For example:

```text
Metric Change
     +
Customer Feedback
     ↓
Evidence
     ↓
Analysis
     ↓
Decision
```

A metric may indicate that a problem exists, while customer feedback may help explain why it exists.

Neither should automatically be treated as complete evidence by itself.

---

# Metrics and Decision Log

Significant metric changes may trigger formal decisions.

Examples include:

* Major customer growth
* Significant revenue changes
* Major product adoption changes
* Repeated production failures
* Major security incidents
* Significant customer churn

Where a metric results in a significant company decision, the appropriate Decision ID should be recorded.

---

# Metrics and Customer Feedback Status

Customer feedback lifecycle states may provide useful supporting metrics.

Examples include:

* New feedback count
* Reviewing feedback count
* Validated feedback count
* Addressed feedback count
* Archived feedback count

These measurements can help the company understand how efficiently customer evidence is being processed.

---

# Metrics and Launches

Launch metrics should be defined before a significant product launch.

Examples include:

* New registrations
* Activation
* Usage
* Conversion
* Revenue
* Customer retention
* Errors
* Performance
* Support requests

Document 10 provides the launch readiness framework.

Document 11 provides the measurement framework after launch.

---

# Product Performance Review

After launch, the company should review whether the product is achieving the intended outcomes.

The review should compare:

* Expected outcome
* Actual outcome
* Customer behavior
* Business results
* Technical performance
* Customer feedback

Where results differ materially from expectations, the company should investigate the cause.

---

# Metric Data Quality

Metrics are only useful when the underlying data is reliable.

The company should monitor:

* Missing data
* Duplicate data
* Incorrect values
* Broken tracking
* Inconsistent definitions
* Data-source failures
* Delayed reporting

Important decisions should not rely on data known to be unreliable without explicitly documenting the limitation.

---

# Dashboard Governance

The Metrics Dashboard should remain focused and useful.

The company should:

* Remove metrics that no longer provide value
* Add metrics when new business needs emerge
* Review metric definitions
* Maintain ownership
* Preserve historical data
* Avoid unnecessary dashboard complexity

The dashboard should evolve with the company.

---

# Metrics Review Meeting

Where applicable, periodic metrics reviews should examine:

* Major positive changes
* Major negative changes
* New risks
* Customer trends
* Revenue trends
* Product performance
* Engineering performance
* Operational health
* Required decisions

Every review should focus on what the measurements mean for the company.

---

# Metrics Records

Important metric definitions should be maintained in a consistent format.

A metric record should include:

| Field            | Description                                  |
| ---------------- | -------------------------------------------- |
| Metric ID        | Unique metric identifier                     |
| Metric Name      | Name of the metric                           |
| Category         | Metric category                              |
| Definition       | Definition                                   |
| Formula          | Calculation                                  |
| Data Source      | Source of measurement                        |
| Owner            | Responsible person                           |
| Review Frequency | Review schedule                              |
| Target           | Target value                                 |
| Threshold        | Investigation threshold                      |
| Current Status   | Healthy, Watch, Action Required, or Critical |
| Related Decision | Decision ID where applicable                 |

---

# Review Triggers

A formal metrics review should occur when:

* A critical metric changes significantly
* A target is repeatedly missed
* Customer behavior changes materially
* Revenue changes significantly
* Product adoption changes significantly
* Operational reliability deteriorates
* Security events occur
* Major business assumptions change

Metrics should trigger investigation rather than automatic conclusions.

---

# Measurement Lifecycle

Metrics should follow a continuous lifecycle:

```text
Define
   ↓
Collect
   ↓
Validate
   ↓
Measure
   ↓
Review
   ↓
Interpret
   ↓
Act
   ↓
Improve
```

The company should continuously improve the quality and usefulness of its measurements.

---

# Relationship With Other Operating Manual Documents

## Decision Log

Document 08 provides decision governance when important metrics lead to significant business decisions.

---

## Customer Feedback

Document 09 provides qualitative and behavioral evidence that complements quantitative metrics.

---

## Launch Checklist

Document 10 defines launch readiness and identifies metrics that should be monitored after launch.

---

## Product Roadmap

Metrics provide evidence for evaluating whether roadmap investments are achieving expected results.

---

## Engineering Documents

Engineering metrics help evaluate development quality, reliability, and operational performance.

---

# Decision Summary

## Approved

* Metrics Dashboard as the central measurement framework
* Business metrics
* Customer metrics
* Product metrics
* Revenue metrics
* Engineering metrics
* Operational metrics
* Metric ownership
* Metric definitions
* Measurement frequency
* Dashboard status categories
* Threshold-based monitoring
* Trend analysis
* Metrics connected to customer feedback
* Metrics connected to the Decision Log
* Launch metrics
* Continuous measurement lifecycle

---

## Open Questions

* Which metrics should appear on the company-wide dashboard?
* Which metrics require real-time monitoring?
* Who owns each critical metric?
* What targets should be established for each product?
* Which thresholds should trigger formal investigation?
* How often should dashboard definitions be reviewed?
* Which metrics should be visible to the entire company?

---

# Operating Principle

The Metrics Dashboard exists to convert company activity and customer behavior into actionable evidence.

The company should follow:

**Measure → Understand → Decide → Act → Learn**

Metrics should support better decisions, not become a substitute for judgment.

---

# Next Document

## 12-technical-architecture.md

This document defines the technical architecture principles and structure used by EyesightWorks Technologies to transform approved business and product requirements into scalable technical systems.

It will define:

* Architecture principles
* System boundaries
* Application architecture
* Service architecture
* Data architecture
* API architecture
* Infrastructure architecture
* Security architecture
* Scalability considerations
* Technical decision governance
