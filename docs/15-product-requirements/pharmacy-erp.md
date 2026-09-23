# EyesightWorks Technologies Operating Manual

**Document:** 15C of 21

**Title:** Product Requirements — Pharmacy ERP

**Version:** 1.1

**Status:** Approved

**Owner:** EyesightWorks Technologies

**Last Updated:** 2026-09-21

---

# Pharmacy ERP

## 1. Product Overview

Pharmacy ERP is a cloud-based business management system designed to help pharmacies manage their day-to-day operations through a structured digital platform.

The product is intended to provide pharmacies with practical tools for managing products, inventory, sales, purchasing, customers, suppliers, and operational information.

The system should reduce manual administrative work, improve visibility into pharmacy operations, and provide reliable business information for decision-making.

The product should prioritize practical business value rather than unnecessary complexity.

---

## 2. Product Vision

The vision of Pharmacy ERP is to provide an affordable and practical business management platform that helps pharmacies operate more efficiently.

The system should progressively reduce the time and effort required to:

* Manage pharmacy products.
* Monitor inventory.
* Record sales.
* Manage suppliers.
* Track purchases.
* Manage customers.
* Monitor stock levels.
* Review business activity.
* Make operational decisions.

The product should provide a foundation that can later support additional pharmacy management capabilities when customer evidence demonstrates meaningful demand.

---

## 3. Product Objective

The primary objective of the MVP is to validate whether pharmacies will consistently use a centralized digital system to manage important day-to-day business operations.

The MVP should prioritize:

* Product management.
* Inventory management.
* Sales recording.
* Purchase recording.
* Supplier management.
* Customer management.
* Basic reporting.
* User accounts and roles.
* Measurable operational activity.

The MVP should remain focused on the core pharmacy management workflow.

Advanced automation, AI, complex accounting, advanced analytics, integrations, and other capabilities should only be introduced when customer evidence demonstrates meaningful value.

---

## 4. Target Users

The initial target users include:

### 4.1 Pharmacy Owners

Owners who need visibility into business operations, inventory, sales, purchases, and overall performance.

### 4.2 Pharmacists

Pharmacy professionals who manage products, sales, inventory, and other operational activities.

### 4.3 Pharmacy Staff

Authorized employees who perform day-to-day activities such as recording sales, receiving stock, and managing products.

### 4.4 Managers

Users responsible for supervising pharmacy operations and reviewing business information.

### 4.5 Administrators

Authorized users responsible for system configuration, user management, permissions, and operational oversight.

---

## 5. Core User Problems

The product should focus on practical pharmacy business problems, including:

* Difficulty maintaining accurate inventory records.
* Manual recording of sales and purchases.
* Difficulty identifying low-stock products.
* Limited visibility into business activity.
* Difficulty managing large numbers of products.
* Difficulty tracking suppliers and purchases.
* Time spent maintaining separate records.
* Difficulty generating useful operational reports.
* Limited visibility into staff activities.

The MVP should validate which of these problems are sufficiently important for pharmacies to repeatedly use the platform.

---

## 6. Core MVP Workflow

The initial product workflow should be:

**Register/Login → Pharmacy Setup → Add Products → Manage Inventory → Record Purchase → Record Sale → Monitor Stock → Review Reports**

A simplified sales workflow is:

**Search Product → Check Availability → Record Sale → Update Inventory → Generate Sale Record**

A simplified purchasing workflow is:

**Select Supplier → Record Purchase → Receive Stock → Update Inventory → Store Purchase Record**

This workflow represents the initial vertical slice of the product.

---

## 7. MVP Functional Requirements

### 7.1 User Accounts

The system should support:

* User registration.
* Secure login.
* User account management.
* Role-based access.
* Appropriate session/authentication controls.

---

### 7.2 Pharmacy Setup

An authorized user should be able to establish the pharmacy's basic business profile.

The setup should support appropriate information such as:

* Pharmacy name.
* Business contact information.
* Location.
* Basic operational information.
* Authorized users.

The setup process should remain simple enough for a pharmacy to complete without unnecessary configuration.

---

### 7.3 Product Management

Authorized users should be able to:

* Add products.
* Edit products.
* View products.
* Search products.
* Categorize products.
* Manage product information.
* Identify active and inactive products where appropriate.

Product information should be structured so that it can support inventory and sales workflows.

---

### 7.4 Inventory Management

The system should provide basic inventory visibility.

Core capabilities should include:

* Recording stock received.
* Recording stock changes.
* Viewing current stock.
* Identifying low-stock products.
* Updating inventory after purchases.
* Updating inventory after sales.
* Maintaining inventory records.

Inventory should remain connected to the relevant product and transaction records.

---

### 7.5 Sales Management

Authorized users should be able to record sales.

The sales workflow should:

1. Identify the product.
2. Confirm availability.
3. Record the quantity.
4. Record the sale.
5. Update inventory.
6. Preserve the sale record.

The first MVP does not need to become a full accounting or financial-management system.

---

### 7.6 Purchase Management

Authorized users should be able to record purchases from suppliers.

The workflow should support:

* Selecting a supplier.
* Selecting products.
* Recording quantities.
* Recording purchase information.
* Receiving stock.
* Updating inventory.
* Preserving the purchase record.

---

### 7.7 Supplier Management

The system should support basic supplier records, including appropriate information such as:

* Supplier name.
* Contact information.
* Products supplied.
* Purchase history where appropriate.

The MVP should focus on useful operational supplier information rather than building a separate supplier marketplace.

---

### 7.8 Customer Management

The system should support basic customer records where required by the validated pharmacy workflow.

Customer functionality should remain appropriately scoped and should only collect information necessary for the supported business workflow.

---

### 7.9 Reporting

The MVP should provide basic operational reporting.

Initial reporting may include:

* Sales activity.
* Purchase activity.
* Inventory status.
* Low-stock products.
* Product activity.
* Basic business activity.

Reports should help pharmacy operators make practical operational decisions.

---

### 7.10 User Roles and Permissions

The system should provide role-based access appropriate to pharmacy operations.

Different users should only have access to functions necessary for their responsibilities.

Examples may include:

* Owner.
* Pharmacist.
* Manager.
* Staff.
* Administrator.

Permissions should be designed around actual operational responsibilities rather than unnecessary complexity.

---

## 8. Data and Record Requirements

The system should maintain reliable records for important operational activities.

Core records should include:

* Users.
* Pharmacy/business information.
* Products.
* Inventory.
* Suppliers.
* Customers where required.
* Sales.
* Purchases.
* Relevant user activity.

Important business records should not be silently overwritten when historical information is required for operational visibility or reporting.

---

## 9. Security and Access Control

Because Pharmacy ERP manages business and operational information, security is a core product requirement.

The system should:

* Use authenticated access.
* Apply role-based permissions.
* Protect sensitive credentials and secrets.
* Restrict administrative functionality.
* Maintain appropriate audit information.
* Protect business records from unauthorized access.
* Apply appropriate backup and recovery procedures.
* Follow the requirements defined in Document 19 — Security.

Security decisions should be implemented according to the actual risks of the product and not treated as an optional later feature.

---

## 10. Privacy and Data Handling

The system should collect and store only information required for the supported pharmacy workflows.

Where customer or other sensitive information is handled, the product should:

* Apply appropriate access controls.
* Minimize unnecessary data collection.
* Protect stored information.
* Provide appropriate retention and deletion controls.
* Follow applicable requirements.
* Follow the security principles established by Document 19.

The MVP should avoid collecting sensitive information that is not required for its validated business workflow.

---

## 11. AI and Automation

AI is not a requirement for the first Pharmacy ERP MVP.

AI or automation may later be introduced where it demonstrates measurable value, including:

* Inventory insights.
* Demand analysis.
* Business reporting assistance.
* Product categorization.
* Operational recommendations.
* Automated administrative assistance.

AI capabilities should not be added simply because they are technically possible.

The product should first prove that the core pharmacy workflow provides real customer value.

---

## 12. Business Model and Commercial Validation

The product should be designed to support future commercial models.

Potential commercial models may include:

* Monthly subscription.
* Annual subscription.
* Tiered plans.
* Premium features.
* Multi-branch plans.
* Enterprise pharmacy plans.
* Optional implementation or support services.

The initial objective is not to implement every pricing model.

The objective is to validate whether pharmacies will use the system consistently and whether the product provides sufficient operational value to support a sustainable commercial model.

---

## 13. Success Measures

The product should measure evidence of real operational value.

Initial success measures include:

* Number of active pharmacies.
* Number of active users.
* Daily or weekly operational activity.
* Number of products managed.
* Number of sales recorded.
* Number of purchases recorded.
* Inventory activity.
* Inventory accuracy.
* Report usage.
* Reduction in manual record keeping.
* Time required to complete common workflows.
* User retention.
* Customer feedback.
* Evidence of willingness to pay.

The most important early signal is whether pharmacies repeatedly use the system as part of their normal operations.

---

## 14. Risks

### Data Quality Risk

Incorrect product, inventory, sales, or purchase information may reduce system reliability.

### Security Risk

Unauthorized access could expose sensitive business information.

### Workflow Risk

A system that is too complicated may reduce adoption.

### Adoption Risk

Pharmacies may continue using existing manual processes or alternative systems.

### Operational Risk

Poorly designed inventory or sales workflows could create incorrect business records.

### Continuity Risk

System downtime or data loss could disrupt pharmacy operations.

### Integration Risk

Future integrations with payment, accounting, supplier, or other systems may introduce additional technical dependencies.

### Regulatory Risk

Pharmacy operations may involve applicable legal, regulatory, privacy, and professional requirements.

### Commercial Risk

Pharmacies may not be willing to pay enough for the product to support sustainable operations.

---

## 15. MVP Boundaries

The first MVP should remain focused on the core operational workflow.

The following capabilities are not required for the first MVP unless customer validation demonstrates a clear need:

* Advanced accounting.
* Payroll.
* Complex financial management.
* Full procurement automation.
* Advanced AI.
* Advanced business intelligence.
* Complex payment integrations.
* Automated supplier ordering.
* Multi-country support.
* Large-scale third-party integrations.
* Complex healthcare integrations.

These may remain future opportunities.

The MVP should prioritize reliable operational records and a simple user experience.

---

## 16. Expansion Path

If the MVP demonstrates meaningful customer demand, the product may progressively expand.

### Phase 2 — Advanced Pharmacy Operations

Potential capabilities include:

* More advanced inventory controls.
* Expiry management.
* Batch management.
* More detailed reporting.
* Improved purchasing workflows.
* Multi-user operational controls.

### Phase 3 — Multi-Branch Operations

Potential capabilities include:

* Multiple pharmacy branches.
* Centralized management.
* Branch-level inventory.
* Branch reporting.
* Central administration.

### Phase 4 — Integrations

Potential integrations may include:

* Payment services.
* Accounting systems.
* Supplier systems.
* Other validated business tools.

### Phase 5 — AI-Assisted Operations

Potential capabilities may include:

* Inventory insights.
* Demand forecasting.
* Operational recommendations.
* Business intelligence assistance.
* Automated reporting assistance.

Expansion should be driven by customer evidence and business value.

---

## 17. Product Validation Questions

Before significant investment in advanced capabilities, EyesightWorks Technologies should validate:

1. Do pharmacies experience the identified operational problems?
2. What tools or processes do pharmacies currently use?
3. Which workflows consume the most time?
4. Which inventory problems are most costly or disruptive?
5. What information do pharmacy owners need to make decisions?
6. Which users will operate the system daily?
7. What permissions are required for different staff roles?
8. Which reports are genuinely useful?
9. Will pharmacies consistently use the system?
10. Are pharmacies willing to pay for the product?
11. Which features would justify continued investment?
12. What regulatory and operational requirements must be addressed?

Customer evidence should be captured through Document 09 — Customer Feedback.

Important product decisions should be recorded through Document 08 — Decision Log.

---

## 18. Product Quality Standard

Pharmacy ERP should be considered successful at the MVP stage when it demonstrates evidence that:

* Pharmacies can set up and use the system.
* Users can manage products.
* Inventory can be updated reliably.
* Purchases can be recorded.
* Sales can be recorded.
* Inventory reflects relevant business activity.
* Authorized users can access the functions appropriate to their roles.
* Basic reports provide useful operational information.
* Pharmacies repeatedly use the system.
* Users report meaningful improvement over their previous process.
* There is evidence supporting continued investment.

The goal is not to build a complete enterprise pharmacy system immediately.

The goal is to prove a reliable, useful, and commercially viable pharmacy workflow.

---

## 19. Relationship to the EyesightWorks Product Strategy

Pharmacy ERP represents a focused vertical product within the wider EyesightWorks Technologies strategy.

The product provides an opportunity to develop reusable capabilities for:

* User management.
* Organizations.
* Products.
* Inventory.
* Transactions.
* Roles and permissions.
* Reporting.
* Business operations.

These capabilities may later support other business-management products.

However, the Pharmacy ERP MVP should remain focused on pharmacy operations rather than becoming a generic ERP platform.

This follows the company's **depth before breadth** principle.

---

## 20. Product Decision Rule

Every significant feature should be evaluated using the EyesightWorks Technologies operating filter:

> **Does this increase our chances of getting paying customers?**

Features should be prioritized when they:

* Solve a validated customer problem.
* Improve a measurable operational outcome.
* Reduce meaningful business risk.
* Improve customer retention.
* Support a validated commercial opportunity.

Technical interest alone is not sufficient justification for adding a feature to the MVP.

---

## 21. Next Steps

The approved product requirement should guide:

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

The product should move from requirement to implementation only after the MVP scope has been sufficiently validated and the required architecture has been defined.

---

## 22. Operating Principle

**Reliable Data → Controlled Access → Efficient Workflow → Measurable Operations → Learn → Improve**
