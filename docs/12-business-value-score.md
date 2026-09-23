# EyesightWorks Technologies Operating Manual

**Document:** 12 of 17

**Title:** Business Value Score

**Version:** 1.0

**Status:** Draft

**Owner:** EyesightWorks Technologies

**Last Updated:** 2026-09-20

---

# Revision History

| Version | Date       | Changes                                |
| ------- | ---------- | -------------------------------------- |
| 1.0     | 2026-09-20 | Initial Business Value Score Framework |

---

# Business Value Score

## Executive Summary

This document defines how EyesightWorks Technologies evaluates business opportunities, product opportunities, customer problems, and potential investments using a structured Business Value Score.

The purpose of the Business Value Score is to improve decision quality by evaluating opportunities against consistent business criteria rather than relying only on intuition, enthusiasm, technical interest, or isolated customer requests.

The Business Value Score supports the company's operating philosophy:

**Business → Product → Architecture → Engineering**

Business value should be understood before significant product or engineering investment is approved.

The framework helps the company determine:

* Which opportunities deserve further investigation
* Which opportunities should receive investment
* Which opportunities should be validated first
* Which opportunities should be deferred
* Which opportunities should be rejected

The Business Value Score is a decision-support tool and does not automatically determine the final decision.

---

# Scope of This Document

This document defines:

* Business value evaluation principles
* Opportunity evaluation criteria
* Business Value Score calculation
* Evidence requirements
* Opportunity validation
* Investment evaluation
* Risk considerations
* Review requirements
* Business Value records
* Cross-document relationships

This document does not define:

* Detailed product specifications
* Technical architecture
* Engineering implementation
* Project schedules
* Marketing campaign execution
* Financial accounting procedures

Those subjects are documented separately within the Operating Manual.

---

# Business Value Philosophy

The company should invest resources in opportunities that can create meaningful customer, business, or strategic value.

Business value should be evaluated before significant resources are committed.

The company follows the principle:

**Value Before Investment.**

An opportunity should not receive significant investment simply because:

* It is technically interesting
* A single person requested it
* It appears popular
* A competitor has implemented something similar
* It is easy to build
* It uses a new technology

The opportunity should demonstrate a reasonable connection between:

**Customer Need → Evidence → Business Value → Investment**

---

# Business Value Principles

## Customer Value Before Feature Value

A feature should not be considered valuable simply because it exists.

The company should evaluate whether the opportunity creates a meaningful improvement for customers.

Customer value may include:

* Solving an important problem
* Saving time
* Reducing cost
* Increasing revenue
* Improving reliability
* Improving accessibility
* Improving customer experience
* Reducing operational difficulty

---

## Evidence Before Investment

Significant investments should be supported by available evidence.

Evidence may include:

* Customer feedback
* Customer interviews
* Product analytics
* Revenue data
* Market research
* Sales evidence
* Usage patterns
* Competitive research
* Customer willingness to take action

The quality of the evidence should influence the confidence assigned to the opportunity.

---

## Business Value Before Technical Complexity

Technical complexity does not automatically create business value.

Engineering effort should be justified by the customer or business outcome the work is expected to produce.

A technically sophisticated solution with limited customer value should not automatically receive higher priority than a simpler solution that solves an important customer problem.

---

## Strategic Alignment

An opportunity should support the company's current strategic direction.

Strategic alignment should consider:

* Company objectives
* Target customers
* Product direction
* Revenue strategy
* Long-term platform direction
* Existing capabilities

Opportunities that do not align with company direction should require stronger evidence before receiving significant investment.

---

## Risk Awareness

Business value should be considered together with risk.

Risks may include:

* Market risk
* Customer adoption risk
* Revenue risk
* Operational risk
* Technical risk
* Security risk
* Legal or regulatory risk
* Dependency risk

A high-value opportunity may still require staged investment when uncertainty or risk is high.

---

# Business Value Score Framework

The initial Business Value Score uses a 100-point evaluation model.

| Evaluation Criterion |  Weight |
| -------------------- | ------: |
| Customer Value       |      20 |
| Revenue Potential    |      20 |
| Strategic Alignment  |      15 |
| Market Opportunity   |      15 |
| Evidence Strength    |      10 |
| Feasibility          |      10 |
| Time to Value        |      10 |
| **Total**            | **100** |

Each criterion is evaluated using a score from **0 to 5**.

The weighted result is then used to produce the final Business Value Score.

The scoring model may be reviewed and adjusted as the company gains more operating experience.

---

# Evaluation Criteria

## Customer Value

Customer Value measures how strongly the opportunity addresses a meaningful customer need.

Consider:

* Problem severity
* Number of affected customers
* Frequency of the problem
* Customer willingness to adopt
* Expected customer outcome

A problem with strong evidence of meaningful customer impact should receive a higher score.

---

## Revenue Potential

Revenue Potential evaluates the opportunity's ability to contribute to company revenue.

Consider:

* Customer willingness to pay
* Revenue model
* Pricing opportunity
* Number of potential paying customers
* Recurring revenue potential
* Expansion opportunities

Revenue potential should be supported by evidence whenever possible.

---

## Strategic Alignment

Strategic Alignment measures how closely the opportunity supports company direction.

Consider:

* Company strategy
* Target market
* Current product direction
* Existing capabilities
* Long-term platform objectives

---

## Market Opportunity

Market Opportunity evaluates the size, demand, and accessibility of the potential market.

Consider:

* Number of potential customers
* Evidence of demand
* Market growth
* Competitive environment
* Accessibility of the target market

The company should avoid relying only on theoretical market size.

Actual ability to reach customers should also be considered.

---

## Evidence Strength

Evidence Strength measures how confident the company should be in the information supporting the opportunity.

Evidence may include:

* Multiple customer interviews
* Repeated customer requests
* Customer behavior
* Product usage data
* Sales results
* Market research
* Customer willingness to pay
* Successful validation experiments

A single unsupported opinion should receive limited evidence strength.

---

## Feasibility

Feasibility evaluates whether the company can reasonably execute the opportunity.

Consider:

* Engineering effort
* Required skills
* Infrastructure requirements
* Dependencies
* Operational requirements
* Integration complexity
* Available resources

---

## Time to Value

Time to Value measures how quickly the opportunity can begin producing meaningful customer or business value.

Consider:

* Development time
* Customer onboarding time
* Time to first use
* Time to measurable outcome
* Time to revenue

Opportunities that can be validated or delivered incrementally may reduce uncertainty faster.

---

# Business Value Scoring Process

Business value evaluation should follow a structured process.

```text
Opportunity

↓

Customer Problem

↓

Evidence Collection

↓

Business Analysis

↓

Score Evaluation

↓

Review

↓

Decision

↓

Investment

↓

Measurement
```

The purpose of the process is to reduce uncertainty before committing significant resources.

---

# Scoring Guidelines

Each criterion should be scored from 0 to 5.

| Score | General Meaning                           |
| ----: | ----------------------------------------- |
|     0 | No meaningful value or evidence           |
|     1 | Very limited value or weak evidence       |
|     2 | Low value or limited evidence             |
|     3 | Moderate value or reasonable evidence     |
|     4 | Strong value or strong evidence           |
|     5 | Exceptional value or very strong evidence |

Scores should be supported by documented reasoning.

A score should not be selected simply to make an opportunity appear attractive.

---

# Business Value Score Calculation

The weighted score for each criterion is calculated using:

```text
Criterion Score ÷ 5 × Criterion Weight
```

For example, if Customer Value receives a score of 4:

```text
4 ÷ 5 × 20 = 16 points
```

The final Business Value Score is the sum of all weighted criteria.

Example:

| Criterion           | Score |  Weight | Weighted Result |
| ------------------- | ----: | ------: | --------------: |
| Customer Value      |     4 |      20 |              16 |
| Revenue Potential   |     3 |      20 |              12 |
| Strategic Alignment |     5 |      15 |              15 |
| Market Opportunity  |     3 |      15 |               9 |
| Evidence Strength   |     4 |      10 |               8 |
| Feasibility         |     4 |      10 |               8 |
| Time to Value       |     3 |      10 |               6 |
| **Total**           |       | **100** |          **74** |

The example demonstrates the calculation method only. It does not represent an approved company opportunity.

---

# Business Value Score Interpretation

The initial interpretation framework is:

| Score Range | Interpretation          | Recommended Action                     |
| ----------: | ----------------------- | -------------------------------------- |
|      80–100 | Very strong opportunity | Consider priority investment           |
|       65–79 | Strong opportunity      | Validate and consider investment       |
|       50–64 | Moderate opportunity    | Gather more evidence                   |
|       30–49 | Weak opportunity        | Defer or investigate carefully         |
|        0–29 | Very weak opportunity   | Do not prioritize without new evidence |

The score should be treated as decision support rather than an automatic approval mechanism.

A lower score should not permanently eliminate an opportunity when new evidence can materially change the evaluation.

---

# Evidence Requirements

A Business Value Score should identify the evidence supporting the evaluation.

The evaluation record should include:

* Opportunity description
* Customer problem
* Target customer
* Evidence collected
* Revenue assumptions
* Strategic rationale
* Estimated effort
* Major risks
* Score by criterion
* Final Business Value Score
* Decision
* Decision owner
* Related Decision ID where applicable

Important assumptions should be explicitly identified.

---

# Opportunity Validation

High-value opportunities with weak evidence should not automatically receive immediate large-scale investment.

The company may use controlled validation activities such as:

* Customer interviews
* Prototype testing
* Landing page experiments
* Product demonstrations
* Pilot programs
* Pre-orders
* Paid trials
* Manual service delivery
* Market tests

Validation should increase evidence quality before larger investment.

---

# Investment Decision Framework

The Business Value Score may result in one of several outcomes:

* Invest
* Validate
* Modify
* Defer
* Reject

The decision should consider both the score and the supporting evidence.

A high score with weak evidence may require validation before major investment.

A moderate score with strong evidence may justify a limited experiment.

The company should favor staged investment when uncertainty is high.

---

# Investment Stages

Where appropriate, opportunities should move through staged investment.

```text
Idea

↓

Initial Evidence

↓

Small Validation

↓

Business Value Evaluation

↓

Limited Investment

↓

Measured Results

↓

Scale Investment
```

This approach reduces the risk of committing significant resources before an opportunity has been adequately validated.

---

# Business Value and Customer Feedback

Customer feedback from Document 09 should be considered when evaluating customer value and evidence strength.

The relationship is:

```text
Customer Feedback
       ↓
Evidence
       ↓
Business Value Evaluation
       ↓
Investment Decision
```

Customer feedback should inform the evaluation but should not automatically determine the score.

---

# Business Value and Metrics

Metrics from Document 11 should be used to measure whether an investment produces its expected results after implementation or launch.

The relationship is:

```text
Business Value Evaluation
       ↓
Investment
       ↓
Launch
       ↓
Metrics
       ↓
Results
       ↓
Review
```

Actual results should be compared with the original assumptions.

---

# Business Value Review

Business Value Scores should be reviewed when significant new information becomes available.

Review triggers may include:

* Significant customer feedback
* Major market changes
* Revenue changes
* New competitive information
* Major technical discoveries
* Changes in company strategy
* Significant changes in implementation cost

A previous score should not be treated as permanent when the underlying evidence changes.

---

# Business Value Records

Each significant Business Value evaluation should be documented.

A Business Value record should include:

| Field            | Description                                |
| ---------------- | ------------------------------------------ |
| Opportunity ID   | Unique identifier                          |
| Opportunity Name | Clear opportunity title                    |
| Date             | Date of evaluation                         |
| Owner            | Person responsible for evaluation          |
| Customer Problem | Problem being addressed                    |
| Target Customer  | Intended customer segment                  |
| Evidence         | Supporting evidence                        |
| Score            | Final Business Value Score                 |
| Decision         | Invest, Validate, Modify, Defer, or Reject |
| Risks            | Major known risks                          |
| Assumptions      | Important assumptions                      |
| Related Feedback | Linked customer feedback records           |
| Related Decision | Linked Decision ID                         |

The record should preserve both the score and the reasoning behind it.

---

# Governance

Business Value evaluations should be performed consistently for significant opportunities.

The company should ensure:

* Scoring criteria remain documented
* Evidence is preserved
* Assumptions are visible
* Scores are reviewable
* Decisions have clear owners
* Significant decisions are connected to the Decision Log

The Business Value Score should improve decision transparency without creating unnecessary administrative work for small decisions.

---

# Relationship With Other Operating Manual Documents

## Decision Log

Document 08 records significant decisions resulting from business value evaluations.

Significant investment decisions should reference the appropriate Decision ID.

---

## Customer Feedback

Document 09 provides customer evidence used to evaluate:

* Customer problems
* Customer value
* Evidence strength
* Opportunities
* Validation results

---

## Launch Checklist

Document 10 provides launch readiness requirements after an opportunity has been approved for implementation and launch.

---

## Metrics Dashboard

Document 11 provides the measurement framework used to evaluate results after investment and launch.

---

## Product Roadmap

Business Value Scores may provide evidence for product prioritization and roadmap decisions.

An opportunity may influence roadmap priority when supported by sufficient evidence and strategic alignment.

---

## Architecture and Engineering Documents

Business Value evaluation should occur before significant architectural or engineering investment.

Technical decisions should support opportunities that provide sufficient customer and business value.

---

# Decision Summary

## Approved

* Business Value Score as a structured evaluation framework
* Evidence-based opportunity evaluation
* Customer value as a primary criterion
* Revenue potential evaluation
* Strategic alignment evaluation
* Market opportunity evaluation
* Evidence strength evaluation
* Feasibility evaluation
* Time-to-value evaluation
* Weighted 100-point scoring model
* Staged investment
* Opportunity validation
* Periodic score review
* Connection to Customer Feedback
* Connection to Decision Log
* Connection to Launch Checklist
* Connection to Metrics Dashboard

---

## Open Questions

* Which opportunity types require a formal Business Value Score?
* What minimum score should trigger a formal investment review?
* Who approves high-value investments?
* How often should the scoring weights be reviewed?
* Which business metrics should measure investment outcomes?
* When should an opportunity be rescored?
* What level of evidence is required before a major investment?

---

# Operating Principle

The Business Value Score exists to help EyesightWorks Technologies invest resources where evidence indicates meaningful customer and business value.

The company should follow:

**Evidence → Value → Decision → Investment → Measurement → Learning**

Business value should be demonstrated through customer outcomes, business results, and measurable evidence rather than assumptions alone.

---

# Next Document

## 13-technical-architecture.md

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
