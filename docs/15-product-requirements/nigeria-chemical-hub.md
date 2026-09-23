# EyesightWorks Technologies Operating Manual

**Document:** 15B of 21

**Title:** Product Requirements — Nigeria Chemical Hub

**Version:** 1.1

**Status:** Approved

**Owner:** EyesightWorks Technologies

**Last Updated:** 2026-09-21

---

# Nigeria Chemical Hub

## 1. Product Overview

Nigeria Chemical Hub is an industry-focused digital marketplace designed to connect chemical buyers with suppliers, manufacturers, importers, distributors, laboratories, and other relevant businesses.

The platform will provide a structured environment where businesses can:

* Discover chemical products.
* Discover suppliers and manufacturers.
* Publish products and services.
* Create business profiles.
* Submit enquiries.
* Request quotations.
* Establish commercial relationships.
* Discover relevant business opportunities.

The product is intended to solve practical business discovery and sourcing problems rather than function as a general-purpose social network or directory.

Nigeria Chemical Hub will also provide a foundation for reusable marketplace capabilities that can later support the wider EyesightWorks Business Hub platform.

---

## 2. Product Vision

The vision of Nigeria Chemical Hub is to make it easier for businesses in Nigeria's chemical supply ecosystem to discover relevant products, suppliers, buyers, services, and commercial opportunities through a structured and trusted digital platform.

The product should progressively reduce the time and effort required to:

* Find relevant chemical products.
* Find suitable suppliers.
* Discover manufacturers and distributors.
* Understand basic product and supplier information.
* Contact potential suppliers.
* Submit enquiries.
* Request quotations.
* Discover relevant business services.
* Discover relevant commercial opportunities.

Future platform capabilities may extend into employment, broader business opportunities, and AI-assisted discovery and matching.

These capabilities should be introduced only when supported by customer evidence and measurable business value.

---

## 3. Product Objective

The primary objective of the MVP is to validate whether businesses have a meaningful need for a structured digital platform for chemical product and supplier discovery.

The MVP should therefore prioritize:

* Product discovery.
* Supplier discovery.
* Business discovery.
* Search.
* Filtering.
* Business profiles.
* Product listings.
* Enquiries.
* Quote requests.
* Basic verification.
* Measurable customer activity.

The MVP should remain focused on the core discovery and enquiry workflow.

Advanced automation, AI-assisted matching, payments, transaction management, employment capabilities, and broader marketplace features should be introduced only when customer evidence demonstrates that they provide meaningful value.

---

## 4. Target Users

The initial target users include:

### 4.1 Business Buyers

Organizations looking for chemical products, suppliers, manufacturers, distributors, laboratories, or related services.

### 4.2 Chemical Suppliers

Businesses that sell or distribute chemical products to other businesses.

### 4.3 Manufacturers

Companies that manufacture chemical products and want to reach potential buyers.

### 4.4 Importers and Distributors

Businesses involved in importing, distributing, or supplying chemical products.

### 4.5 Laboratories and Related Businesses

Organizations that provide relevant laboratory, testing, technical, or supporting services.

### 4.6 Business Operators

Organizations that may use the platform to discover suppliers, products, customers, services, and commercial opportunities.

---

## 5. Core User Problems

The product should focus on practical problems within the chemical business ecosystem, including:

* Difficulty discovering relevant suppliers.
* Difficulty discovering available chemical products.
* Limited visibility into supplier and product information.
* Difficulty identifying relevant businesses.
* Time spent searching through fragmented sources.
* Difficulty contacting suitable suppliers.
* Difficulty initiating quotation requests.
* Lack of structured business discovery.
* Limited visibility into relevant commercial opportunities.

The MVP should validate which of these problems are sufficiently important for users to repeatedly use the platform.

---

## 6. Core MVP Workflow

The initial product workflow should be:

**User → Register/Login → Business Profile → Create Product Listing → Search → View Product/Supplier → Enquiry → Supplier Response**

A simplified buyer workflow is:

**Discover → Search → Filter → View → Enquire → Request Quote**

A simplified supplier workflow is:

**Register → Create Business Profile → Add Product → Receive Enquiry → Respond**

This workflow represents the initial vertical slice of the product.

---

## 7. MVP Functional Requirements

### 7.1 User Accounts

The system should support:

* User registration.
* User login.
* Secure authentication.
* Basic account management.
* Appropriate user roles.

---

### 7.2 Business Profiles

Businesses should be able to create structured profiles containing appropriate information such as:

* Business name.
* Business description.
* Business category.
* Contact information.
* Location.
* Products or services.
* Verification status where applicable.

---

### 7.3 Product Listings

Authorized businesses should be able to create and manage product listings.

A product listing should support structured information such as:

* Product name.
* Product category.
* Description.
* Supplier/business.
* Availability information where appropriate.
* Location.
* Contact/enquiry capability.
* Relevant supporting information.

Product information should be presented clearly and should avoid unsupported or misleading claims.

---

### 7.4 Search

Users should be able to search for relevant:

* Products.
* Suppliers.
* Manufacturers.
* Businesses.

Search should be designed around practical discovery rather than general content browsing.

---

### 7.5 Filtering

Where useful, users should be able to narrow search results using relevant attributes such as:

* Product category.
* Supplier type.
* Location.
* Availability.
* Business type.

Filters should be introduced according to actual customer needs rather than adding unnecessary complexity.

---

### 7.6 Enquiries

Users should be able to submit enquiries to businesses or suppliers.

An enquiry should provide enough information for the receiving business to understand the customer's request and respond appropriately.

---

### 7.7 Quote Requests

The MVP should provide a basic mechanism for users to request quotations where appropriate.

The first implementation does not need to become a full transaction or procurement system.

The objective is to validate whether quote requests generate meaningful business interactions.

---

### 7.8 Basic Verification

The platform should provide basic controls for improving trust in business and product information.

Verification may include appropriate business information checks and administrative review.

The exact verification process should evolve based on customer evidence, operational capacity, and applicable requirements.

---

### 7.9 Moderation

The platform should provide basic moderation capabilities for:

* Business listings.
* Product listings.
* Inappropriate content.
* Suspicious activity.
* Incorrect or misleading information.

---

## 8. Trust and Safety Requirements

Because the platform deals with chemical-related products and business information, trust and safety are important product requirements.

The platform should:

* Encourage accurate product information.
* Avoid unsupported product claims.
* Provide appropriate business verification mechanisms.
* Maintain auditable administrative actions where practical.
* Apply appropriate controls to sensitive or regulated information.
* Consider applicable legal, regulatory, health, safety, and environmental requirements.
* Provide appropriate moderation and reporting mechanisms.

The platform should not present the marketplace as a substitute for professional, regulatory, or safety guidance.

Where a product or activity requires additional controls, the platform should apply those controls before enabling the relevant workflow.

---

## 9. AI and Automation

AI should not be treated as the primary reason for building Nigeria Chemical Hub.

AI capabilities may be introduced where they demonstrate measurable value, including:

* Improved search.
* Product discovery.
* Supplier discovery.
* Query understanding.
* Product or business categorization.
* Recommendation.
* AI-assisted matching.
* Business information assistance.

AI-generated information must be treated as assistive rather than automatically authoritative.

The company should measure whether AI improves a real customer outcome before expanding AI functionality.

---

## 10. Business Model and Commercial Validation

The initial product should be designed to support future commercial models without requiring the MVP to implement every possible revenue mechanism.

Potential commercial models may include:

* Supplier subscriptions.
* Featured listings.
* Premium business profiles.
* Qualified lead/enquiry services.
* Business promotion.
* Transaction-related services where appropriate.
* Enterprise services.

Commercial decisions should be based on customer validation and measurable demand.

The first objective is to establish whether users will consistently use the platform and whether meaningful business enquiries can be generated.

---

## 11. Success Measures

The product should measure evidence of real customer value.

Initial success measures include:

* Number of active suppliers.
* Number of active buyers.
* Number of quality product listings.
* Number of searches.
* Number of product/business views.
* Number of qualified enquiries.
* Number of quotation requests.
* Supplier response activity.
* Repeat user activity.
* Time required to discover relevant products or suppliers.
* Customer feedback.
* Evidence of commercial outcomes.

The most important early signal is not total registration volume but whether the platform generates meaningful discovery and business interactions.

---

## 12. Risks

Key risks include:

### Trust Risk

Users may not trust product or supplier information.

### Regulatory Risk

Chemical-related products and activities may involve applicable legal, regulatory, health, safety, or environmental requirements.

### Listing Quality Risk

Poor or incomplete listings may reduce the usefulness of the marketplace.

### Verification Risk

Insufficient supplier verification may reduce customer confidence.

### Fraud Risk

The platform may attract misleading listings, fraudulent businesses, or inappropriate activity.

### Marketplace Liquidity Risk

The platform may fail to attract enough buyers and suppliers to create useful marketplace activity.

### Operational Risk

Moderation, verification, customer support, and business onboarding may require more operational effort than expected.

### AI Risk

AI-generated recommendations or information may be incorrect or unsuitable.

### Data Risk

Business and product information must be handled appropriately and securely.

### Adoption Risk

Businesses may prefer existing channels and fail to adopt a new platform.

---

## 13. Dependencies

The product depends on the following EyesightWorks Technologies documents and capabilities:

* **Document 02 — Business Architecture**
* **Document 03 — Backend Architecture**
* **Document 03A — Technology Architecture**
* **Document 05 — Database Architecture**
* **Document 06 — API Architecture**
* **Document 07 — Product Roadmap**
* **Document 08 — Decision Log**
* **Document 09 — Customer Feedback**
* **Document 11 — Metrics Dashboard**
* **Document 12 — Business Value Framework**
* **Document 14 — Development Standards**
* **Document 17 — Risk Register**
* **Document 18 — Governance**
* **Document 19 — Security**
* **Document 20 — Business Continuity**
* **Document 21 — Monitoring**

The product should not bypass these governance and engineering controls.

---

## 14. MVP Boundaries

The following capabilities are **not required for the first MVP** unless validation demonstrates a clear need:

* Full payment processing.
* Complex transaction management.
* Logistics management.
* Advanced AI matching.
* Automated procurement.
* Employment marketplace.
* Full job marketplace.
* Complex recommendation engines.
* Large-scale messaging infrastructure.
* Multi-industry expansion.
* Advanced analytics.

These capabilities may remain future opportunities within the broader EyesightWorks Business Hub strategy.

---

## 15. Expansion Path

If the Chemical Hub MVP demonstrates meaningful customer demand, the platform may progressively expand into:

### Phase 2 — Business Opportunities

* Broader business discovery.
* Services.
* More advanced enquiries.
* Supplier/customer matching.
* Improved business profiles.

### Phase 3 — Jobs and Employment

* Job postings.
* Job seeker profiles.
* Job search.
* Applications.
* Employer/job seeker discovery.

### Phase 4 — AI-Assisted Discovery

* Semantic search.
* Intelligent recommendations.
* Supplier matching.
* Buyer matching.
* Opportunity matching.

### Phase 5 — Broader Business Hub

Reusable marketplace capabilities can be extended to other industries while preserving the principle of validating each new vertical before significant expansion.

Expansion should be driven by evidence rather than by technical possibility alone.

---

## 16. Product Validation Questions

Before significant investment in the platform, EyesightWorks Technologies should validate:

1. Do chemical businesses actively experience the discovery problem?
2. How do businesses currently find suppliers and products?
3. What makes a supplier trustworthy?
4. What information do buyers need before contacting a supplier?
5. Are businesses willing to create and maintain listings?
6. Are suppliers willing to respond to enquiries?
7. Do enquiries lead to meaningful commercial conversations?
8. Which marketplace features create measurable value?
9. What would businesses pay for?
10. What operational and regulatory requirements must be addressed before expansion?

The answers should be captured through Document 09 — Customer Feedback and relevant decisions should be recorded in Document 08 — Decision Log.

---

## 17. Product Quality Standard

Nigeria Chemical Hub should be considered successful at the MVP stage when it demonstrates evidence that:

* Businesses can discover relevant products and suppliers.
* Suppliers can publish useful business/product information.
* Buyers can submit meaningful enquiries.
* Suppliers can respond to enquiries.
* The platform generates measurable customer activity.
* Trust and moderation controls are workable.
* Customers report meaningful improvement over their existing discovery process.
* The company has evidence to justify further investment.

The goal is not to build the largest marketplace immediately.

The goal is to prove a valuable business workflow that can be expanded responsibly.

---

## 18. Relationship to the Wider EyesightWorks Business Hub

Nigeria Chemical Hub is both a focused industry product and a potential foundation for reusable marketplace infrastructure.

The long-term platform model may support:

**Businesses → Products/Services → Buyers → Opportunities → Jobs → Job Seekers → Search → Matching → Enquiries/Applications**

However, the Chemical Hub MVP should remain focused on:

**Businesses → Products → Buyers → Search → Discovery → Enquiry**

The broader Business Hub should emerge through validated expansion rather than being forced into the first MVP.

This preserves the company's **depth before breadth** strategy.

---

## 19. Product Decision Rule

Every significant feature should be evaluated using the EyesightWorks Technologies operating filter:

> **Does this increase our chances of getting paying customers?**

If a feature does not solve a validated customer problem, improve a measurable business outcome, reduce meaningful operational risk, or support a validated commercial opportunity, it should not automatically be included in the MVP.

---

## 20. Next Steps

The approved product requirement should now be used to guide:

1. Customer validation.
2. MVP scope confirmation.
3. Business architecture.
4. Technical architecture.
5. Database design.
6. API design.
7. UI/UX design.
8. Development.
9. Testing.
10. Launch readiness.
11. Customer measurement.
12. Iteration based on evidence.

The next implementation decision should be made from the validated MVP scope rather than from additional documentation expansion.

---

## 21. Operating Principle

**Trust → Discover → Connect → Enquire → Learn → Improve**

The product should begin with a focused business problem, validate customer demand, build the minimum useful marketplace workflow, measure real customer activity, and expand only when evidence supports further investment.
