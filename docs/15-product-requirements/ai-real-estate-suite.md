# EyesightWorks Technologies Operating Manual

**Document:** 15A of 21
**Title:** Product Requirements — AI Real Estate Suite
**Version:** 1.1
**Status:** Approved
**Owner:** EyesightWorks Technologies
**Last Updated:** 2026-09-21

---

# Product Overview

The AI Real Estate Suite is an intelligent software platform designed to help real estate businesses manage property information, create property listings, improve marketing content, respond to customer enquiries, and support property discovery.

The product combines practical real estate workflows with artificial intelligence capabilities.

The system is intended to help:

* Estate agencies
* Property managers
* Property developers
* Property owners
* Real estate marketing teams
* Property sales teams

The platform should reduce repetitive work, improve the quality and consistency of property information, accelerate customer communication, and support better property discovery.

The AI Real Estate Suite is part of the **AI Platform** of EyesightWorks Technologies.

The product should share reusable platform capabilities including:

* Authentication
* Authorization
* File management
* Notifications
* AI services
* Search
* Reporting
* Monitoring
* Audit logging
* Usage tracking

The product should begin with a focused MVP and expand only after customer evidence demonstrates measurable value.

---

# Product Vision

The vision of the AI Real Estate Suite is to help real estate businesses operate more efficiently by combining structured property management workflows with practical artificial intelligence.

The platform should make it easier for real estate professionals to:

* Create property listings
* Organize property information
* Generate marketing content
* Improve listing descriptions
* Manage property media
* Respond to enquiries
* Search and discover properties
* Maintain consistent property information
* Reduce repetitive administrative work
* Learn from customer activity

The long-term vision is to develop an intelligent real estate operating platform rather than simply an AI content-generation tool.

---

# Product Objective

The primary objective of the AI Real Estate Suite is to validate whether practical AI capabilities can create measurable value for real estate businesses.

The MVP should focus on:

* Structured property information
* Property listing management
* AI-assisted property description generation
* Editable AI-generated content
* Property media management
* Basic property search and discovery
* Customer enquiries
* Basic property workflow management
* Usage visibility
* Measurement of customer value

The MVP should not attempt to build every possible real estate feature.

Advanced capabilities such as:

* AI property recommendations
* Automated lead qualification
* Predictive property analytics
* Automated marketing campaigns
* AI agents
* Advanced valuation
* Automated customer conversations
* Voice assistants
* Large-scale property intelligence

should only be introduced after evidence demonstrates that they provide meaningful customer and business value.

---

# Target Users

## Real Estate Agents

Agents need to create property listings, market properties, communicate with prospective customers, and manage property information.

The platform should help agents reduce repetitive content work and respond to customers more efficiently.

---

## Property Managers

Property managers may manage multiple properties and need structured information, consistent records, and efficient communication.

Future product expansion may include property management workflows where validated demand exists.

---

## Property Developers

Developers may manage multiple developments and properties and require structured property information and marketing materials.

The platform may support development-level property organization as the product matures.

---

## Property Owners

Property owners may require simple tools for presenting properties and responding to prospective buyers or tenants.

The product should avoid unnecessary complexity for users managing a small number of properties.

---

## Real Estate Marketing Teams

Marketing teams may use the platform to create and improve:

* Property descriptions
* Marketing copy
* Listing summaries
* Promotional content
* Customer-facing property information

AI capabilities should remain assistive and editable rather than automatically publishing unverified claims.

---

# Customer Problems

Real estate businesses may experience several operational problems.

## Repetitive Listing Creation

Agents frequently create descriptions and marketing material for multiple properties.

This can consume significant time.

---

## Inconsistent Property Descriptions

Property information may be presented inconsistently across listings and marketing channels.

This can reduce clarity and create additional editing work.

---

## Slow Content Production

Real estate teams may need to prepare property descriptions quickly when new properties become available.

Manual content creation can slow the publishing process.

---

## Poor Property Information Organization

Property details may be stored across:

* Documents
* Spreadsheets
* Messaging applications
* Notes
* Websites
* Other systems

This can make information difficult to manage consistently.

---

## Customer Enquiry Management

Prospective buyers or tenants may ask questions about properties.

Without structured workflows, enquiries may be difficult to track and respond to consistently.

---

## Property Discovery

Customers may struggle to find relevant properties when property information is poorly structured or search capabilities are limited.

---

## Repetitive Administrative Work

Real estate professionals may spend time performing repetitive activities that could potentially be assisted by software and AI.

The product should identify these activities and validate whether automation produces measurable value.

---

# Value Proposition

The AI Real Estate Suite aims to provide real estate businesses with practical tools that reduce repetitive work and improve property information management.

The core value proposition is:

> **Help real estate businesses create better property information, work faster, respond more efficiently, and improve property discovery using practical software and AI.**

The product should prioritize measurable outcomes rather than AI functionality for its own sake.

Potential measurable outcomes include:

* Reduced time required to create listings
* Faster customer response
* Improved listing quality
* Increased listing completion
* Increased property discovery
* Increased customer enquiries
* Increased repeat usage
* Reduced repetitive administrative work

---

# Core Product Workflow

The initial workflow should be simple.

```text
Register
   ↓
Login
   ↓
Create Real Estate Business Profile
   ↓
Add Property
   ↓
Enter Structured Property Information
   ↓
Upload Property Media
   ↓
Generate AI-Assisted Description
   ↓
Review and Edit
   ↓
Publish Property Listing
   ↓
Customer Searches Properties
   ↓
Views Property
   ↓
Makes Enquiry
   ↓
Business Receives Enquiry
   ↓
Business Responds
   ↓
Measure Activity
```

This workflow represents the initial MVP vertical slice.

---

# MVP Functional Requirements

## 1. User Accounts

The system should support:

* User registration
* Secure login
* User account management
* Appropriate authentication
* Role-based access where required

---

## 2. Business Profile

Authorized users should be able to create and manage a real estate business profile.

The profile may include:

* Business name
* Business description
* Contact information
* Location
* Business type
* Relevant business information

The profile should provide the foundation for managing properties and receiving enquiries.

---

## 3. Property Management

Authorized users should be able to:

* Create properties
* Edit properties
* View properties
* Update property information
* Set property status
* Remove or deactivate listings where appropriate

Property information should be structured rather than stored only as unstructured text.

---

## 4. Property Information

A property should support relevant structured information such as:

* Property title
* Property type
* Price
* Location
* Description
* Availability/status
* Property attributes
* Business/agent information
* Property media

The system should avoid requiring unnecessary fields during the initial MVP.

---

## 5. Property Media

Authorized users should be able to upload appropriate property media.

The system should support:

* Image upload
* Image management
* Association of media with properties
* Appropriate file validation
* Secure file handling

Media capabilities should remain focused on the needs of property listings.

---

## 6. AI-Assisted Description Generation

The platform should allow a user to generate an AI-assisted property description from structured property information.

The workflow should be:

```text
Property Information
        ↓
AI Generation
        ↓
Generated Description
        ↓
User Review
        ↓
User Edit
        ↓
Publish
```

AI output should remain editable and should not automatically be treated as verified factual information.

The system should be designed to minimize unsupported property claims.

---

## 7. Property Search

Customers should be able to search available properties.

Search should support relevant property information and should prioritize useful discovery over unnecessary complexity.

---

## 8. Property Filtering

Where supported by validated customer needs, users should be able to filter properties using relevant attributes such as:

* Property type
* Location
* Price
* Availability
* Other validated property characteristics

Filters should be introduced based on actual customer requirements.

---

## 9. Property Discovery

Customers should be able to:

* Browse properties
* View property details
* View property media
* Review relevant property information
* Identify the responsible business or agent
* Submit enquiries

---

## 10. Customer Enquiries

Customers should be able to submit enquiries about properties.

Businesses should be able to:

* Receive enquiries
* View enquiries
* Track enquiry status where appropriate
* Respond to enquiries

The initial MVP should focus on establishing the enquiry workflow rather than building a complex customer relationship management system.

---

## 11. Usage Visibility

The system should provide basic visibility into product usage.

Relevant metrics may include:

* Properties created
* Listings published
* AI descriptions generated
* Property views
* Searches
* Enquiries
* User activity

This information should support product validation and business decision-making.

---

# AI Requirements

AI is a core component of this product, but it must remain connected to measurable customer value.

The initial AI capability should focus primarily on property-description assistance.

AI should:

* Use structured property information as input.
* Generate editable content.
* Avoid inventing unsupported property facts.
* Allow users to review output before publication.
* Track appropriate usage information.
* Support cost monitoring.
* Allow future replacement of the underlying AI provider where practical.

AI-generated content should be treated as assistance rather than an authoritative source of property facts.

---

# Trust and Content Quality

The platform should reduce the risk of inaccurate property information.

The product should:

* Encourage structured property data.
* Require user review of AI-generated descriptions.
* Avoid automatically publishing unverified AI output.
* Preserve user control over final content.
* Provide appropriate moderation capabilities.
* Support correction of inaccurate information.

The system should not represent AI-generated claims as independently verified facts.

---

# Security and Access Control

The product should apply appropriate security controls.

The system should:

* Authenticate users.
* Authorize protected operations.
* Protect secrets and credentials.
* Restrict administrative operations.
* Protect uploaded files.
* Protect business and property information.
* Maintain appropriate audit information.
* Follow Document 19 — Security.

Security requirements should be implemented according to the actual risks of the product.

---

# Privacy and Data Handling

The product should collect only information required for the supported workflows.

The system should:

* Minimize unnecessary data collection.
* Apply appropriate access controls.
* Protect stored information.
* Handle uploaded media securely.
* Apply appropriate retention and deletion practices.
* Follow applicable privacy requirements.

AI processing should also consider the information being sent to external AI providers and should minimize unnecessary sensitive data.

---

# Business Model and Commercial Validation

Potential commercial models may include:

* Subscription plans
* AI usage plans
* Premium business accounts
* Featured property listings
* Property marketing services
* Enterprise plans
* Optional implementation or support services

The first MVP does not need to implement every commercial model.

The immediate objective is to determine whether the product provides sufficient value for real estate businesses to use it repeatedly and whether there is evidence of willingness to pay.

---

# Success Measures

The product should measure real customer outcomes.

Initial success measures include:

* Number of active businesses
* Number of active users
* Number of properties created
* Number of properties published
* Number of AI descriptions generated
* AI description acceptance/edit rate
* Time saved creating property descriptions
* Number of property views
* Number of searches
* Number of enquiries
* Enquiry response activity
* Repeat usage
* Customer feedback
* Evidence of willingness to pay

The most important early signal is whether AI and the surrounding workflow produce measurable improvement over the customer's previous process.

---

# Risks

## AI Accuracy Risk

AI-generated descriptions may contain unsupported or incorrect information.

## AI Cost Risk

Frequent AI usage may create costs that are not sustainable under the chosen commercial model.

## Adoption Risk

Real estate businesses may continue using existing tools instead of adopting the platform.

## Data Quality Risk

Poor property information may reduce the quality of listings and AI output.

## Privacy Risk

Property, business, customer, or other information may require appropriate protection.

## Security Risk

Unauthorized access could expose business, customer, or property information.

## Content Risk

Users may publish misleading or inaccurate property information.

## Operational Risk

Managing enquiries, moderation, support, and uploaded media may require additional operational capacity.

## Provider Dependency Risk

Dependence on an external AI provider could affect cost, availability, or product behavior.

The architecture should therefore avoid unnecessary lock-in where practical.

---

# MVP Boundaries

The first MVP should remain focused on:

* User accounts
* Business profiles
* Property management
* Structured property information
* Property media
* AI-assisted description generation
* Search
* Property discovery
* Customer enquiries
* Basic usage measurement

The following capabilities are not required for the first MVP unless customer validation demonstrates a clear need:

* Advanced AI agents
* Predictive analytics
* Automated valuation
* Voice assistants
* Automated marketing campaigns
* Advanced lead qualification
* Complex CRM
* Complex property management
* Financial/accounting systems
* Large-scale property intelligence
* Advanced recommendation engines

These may remain future opportunities.

---

# Expansion Path

If the MVP demonstrates meaningful customer demand, the product may expand progressively.

## Phase 2 — Improved Property Operations

Potential capabilities include:

* Advanced property workflows
* Better enquiry management
* Improved search
* Saved properties
* Improved media management
* Additional reporting

---

## Phase 3 — AI-Assisted Discovery

Potential capabilities include:

* Semantic property search
* AI-assisted recommendations
* Intelligent property matching
* Natural-language property discovery

---

## Phase 4 — Customer and Lead Intelligence

Potential capabilities include:

* Lead qualification assistance
* Customer activity analysis
* Follow-up assistance
* Enquiry prioritization

---

## Phase 5 — Intelligent Real Estate Platform

Potential capabilities may include:

* Advanced property intelligence
* Predictive analytics
* Automated marketing assistance
* Broader property management workflows
* Additional real estate business operations

Expansion should be driven by customer evidence and measurable business value.

---

# Product Validation Questions

Before significant investment in advanced capabilities, EyesightWorks Technologies should validate:

1. Do real estate businesses experience the identified problems?
2. How are property listings currently created?
3. How much time is spent creating property descriptions?
4. Do businesses find AI-generated descriptions useful?
5. How much editing is normally required?
6. Do businesses want structured property management?
7. Do customers use the search and discovery workflow?
8. Do property listings generate meaningful enquiries?
9. Does the product improve response time?
10. Will businesses use the platform repeatedly?
11. Are businesses willing to pay for the product?
12. Which additional features would provide the greatest validated value?

Customer evidence should be captured through Document 09 — Customer Feedback.

Important decisions should be recorded through Document 08 — Decision Log.

---

# Product Quality Standard

The AI Real Estate Suite should be considered successful at the MVP stage when it demonstrates evidence that:

* Real estate businesses can create and manage properties.
* Users can generate useful AI-assisted descriptions.
* Users can review and edit AI output.
* Properties can be discovered through search.
* Customers can view property information.
* Customers can submit enquiries.
* Businesses can receive and respond to enquiries.
* Usage can be measured.
* Users report meaningful value.
* There is evidence supporting continued investment.

The goal is not to build a complete real estate operating platform immediately.

The goal is to prove that a focused combination of real estate workflow and practical AI creates measurable customer value.

---

# Relationship to the EyesightWorks Product Strategy

The AI Real Estate Suite represents a focused AI-enabled vertical product within the wider EyesightWorks Technologies strategy.

The product provides an opportunity to develop reusable capabilities for:

* Authentication
* Organizations
* Property management
* File management
* AI services
* Search
* Enquiries
* Notifications
* Usage tracking
* Reporting
* Monitoring

These capabilities may later support other EyesightWorks products.

However, the AI Real Estate Suite should remain focused on validated real estate problems rather than becoming a generic AI platform during the MVP stage.

This follows the company's **depth before breadth** principle.

---

# Product Decision Rule

Every significant feature should be evaluated using the EyesightWorks Technologies operating filter:

> **Does this increase our chances of getting paying customers?**

Features should be prioritized when they:

* Solve a validated customer problem.
* Improve a measurable customer outcome.
* Reduce meaningful operational work.
* Improve customer retention.
* Support a validated commercial opportunity.

Technical novelty alone is not sufficient justification for adding a feature to the MVP.

---

# Next Steps

The approved product requirement should guide:

1. Customer validation.
2. MVP scope confirmation.
3. Business architecture.
4. Technical architecture.
5. Database design.
6. API design.
7. UI/UX design.
8. AI integration design.
9. Development.
10. Testing.
11. Launch readiness.
12. Customer measurement.
13. Iteration based on evidence.

The product should move from requirement to implementation only after the MVP scope has been sufficiently validated and the required architecture has been defined.

---

# Operating Principle

**Structured Property Data → Practical AI → User Review → Better Listings → Better Discovery → Enquiries → Measure → Improve**
