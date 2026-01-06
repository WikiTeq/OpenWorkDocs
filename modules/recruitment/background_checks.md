# {{ company_name }} Background Check Policy

## Purpose

{{ company_name }} conducts background checks to verify information provided by candidates and to assess suitability for employment. Background checks help ensure workplace safety, protect company assets, and maintain trust with customers and partners.

{% if background_check_philosophy %}
{{ background_check_philosophy }}
{% else %}
We conduct background checks in compliance with applicable laws and regulations, treating all candidates fairly and consistently. Our process balances the need for workplace safety with respect for individual privacy and rights.
{% endif %}

## Legal Compliance

### Applicable Laws
Background checks are conducted in accordance with:
* Fair Credit Reporting Act (FCRA) - for US-based checks
* {% if eu_compliance|default(false) %}General Data Protection Regulation (GDPR) - for EU-based candidates{% endif %}
* {% if california_compliance|default(false) %}California Consumer Privacy Act (CCPA){% endif %}
* State and local laws governing employment verification and criminal background checks
* {% if international_compliance %}International privacy laws as applicable{% endif %}

### Consent Requirements
{% if consent_process %}
{{ consent_process }}
{% else %}
Candidates must provide written consent before background checks are initiated. Consent forms explain:
* What information will be checked
* How the information will be used
* Candidates' rights regarding the information
* How to dispute inaccurate information
{% endif %}

## Types of Background Checks

### Standard Checks (All Positions)
* Employment verification for previous {{ employment_history_years|default('2-3') }} years
* Education verification
* Professional license verification (when applicable)
* {% if reference_checks|default(true) %}Reference checks{% endif %}

### Position-Specific Checks

#### Customer-Facing Roles
* Criminal background check (severity and timeframe vary by role)
* {% if driving_record|default(false) %}Motor vehicle records{% endif %}
* {% if credit_check|default(false) %}Credit history{% endif %}

#### Financial Roles
* Criminal background check (including financial crimes)
* Credit history and financial stability assessment
* Regulatory license verification

#### Technical/Security Roles
* Criminal background check
* {% if security_clearance|default(false) %}Security clearance verification{% endif %}
* {% if export_control|default(false) %}Export control compliance{% endif %}

#### Healthcare Roles
* Criminal background check
* {% if healthcare_licensing|default(true) %}Professional licensing verification{% endif %}
* {% if drug_screening|default(false) %}Drug screening{% endif %}

### Additional Checks (As Needed)
{% if additional_checks %}
{{ additional_checks }}
{% else %}
* Professional certification verification
* Media and social media reviews
* {% if global_screening|default(false) %}International background checks{% endif %}
* {% if specialized_assessments %}Specialized assessments based on role requirements{% endif %}
{% endif %}

## Background Check Process

### Timing
Background checks are typically initiated:
* After verbal offer acceptance
* Before formal written offer
* After candidate consent is received

### Process Steps
1. **Candidate Consent**: Obtain written authorization
2. **Vendor Assignment**: Background check assigned to approved vendor
3. **Information Collection**: Vendor contacts references and conducts research
4. **Report Generation**: Findings compiled into report
5. **Review and Decision**: HR and hiring manager review results
6. **Candidate Notification**: Adverse action process if needed

### Timeline
{% if background_check_timeline %}
{{ background_check_timeline }}
{% else %}
Standard background checks are completed within {{ check_completion_time|default('3-5 business days') }}. Complex checks may take {{ extended_check_time|default('7-10 business days') }}.
{% endif %}

## Adverse Action Process

### FCRA Requirements (US)
If background check results may lead to adverse employment action:

1. **Pre-Adverse Action Notice**: Provide candidate with:
   * Copy of background check report
   * Summary of rights under FCRA
   * {{ adverse_action_days|default('5 business days') }} to dispute information

2. **Investigation**: Research candidate disputes
3. **Final Decision**: Make employment decision
4. **Adverse Action Notice**: If decision is negative, provide final notice

### Dispute Resolution
Candidates may dispute background check findings by:
* Contacting the background check vendor directly
* Providing additional information or context
* Requesting re-verification of disputed information

## Confidentiality and Privacy

### Information Handling
* Background check results are treated as confidential
* Access limited to authorized HR and hiring personnel
* Information used solely for employment decisions
* Records retained according to legal requirements

### Data Protection
{% if data_protection_measures %}
{{ data_protection_measures }}
{% else %}
* Use of SOC 2 compliant background check vendors
* Encryption of sensitive data
* Secure storage and transmission
* Regular security audits
{% endif %}

## Vendor Selection and Management

### Approved Vendors
{{ company_name }} uses pre-approved background check vendors who:
* Are licensed and insured
* Maintain high accuracy standards
* Comply with all applicable laws
* Provide comprehensive reporting

{% if vendor_list %}
**Approved Vendors**:
{{ vendor_list }}
{% endif %}

### Vendor Performance
We regularly evaluate vendor performance on:
* Accuracy and timeliness
* Customer service quality
* Compliance with legal requirements
* Cost-effectiveness

## Exceptions and Special Circumstances

### International Candidates
{% if international_process %}
{{ international_process }}
{% else %}
International background checks follow local laws and regulations. Process may vary by country and may include:
* Local criminal record checks
* Education verification through international agencies
* Reference checks with international contacts
{% endif %}

### Contingent Workers
Background checks for contractors and temporary workers follow the same standards as employees, adapted for the engagement type.

### Rehire Situations
Previous employees may have streamlined background check processes based on their employment history with {{ company_name }}.

## Questions and Concerns

### Candidate Questions
Candidates with questions about background checks should contact {% if background_check_contact %}{{ background_check_contact }}{% else %}Human Resources{% endif %}.

### Reporting Concerns
If you believe a background check was conducted improperly or contained errors, please contact {% if compliance_contact %}{{ compliance_contact }}{% else %}the Legal Department{% endif %}.

## Policy Updates

This background check policy is reviewed annually and updated to reflect changes in laws, technology, and best practices.

Last Updated: {{ last_updated|default('January 1, 2024') }}
