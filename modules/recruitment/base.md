# {{ company_name }} Recruitment and Hiring Policy

## Introduction

{{ company_name }} is committed to attracting, recruiting, and hiring the best talent to support our mission and goals. This recruitment policy outlines our commitment to fair, transparent, and effective hiring practices that promote diversity, inclusion, and equal opportunity for all applicants.

{% if diversity_statement %}
{{ diversity_statement }}
{% else %}
We believe that a diverse workforce drives innovation and better business outcomes. We are committed to creating an inclusive recruitment process that welcomes applicants from all backgrounds and experiences.
{% endif %}

## Equal Employment Opportunity

{{ company_name }} provides equal employment opportunity to all applicants and employees without regard to race, color, religion, sex, national origin, age, disability, veteran status, sexual orientation, gender identity, or any other characteristic protected by applicable law.

{% if affirmative_action|default(false) %}
As an affirmative action employer, {{ company_name }} actively seeks to increase the representation of underrepresented groups in our workforce.
{% endif %}

## Job Posting and Advertising

### Internal Job Postings
{% if internal_posting_required|default(true) %}
All open positions are posted internally first for a minimum of {{ internal_posting_days|default('5 business days') }} to provide current employees with the opportunity to apply for advancement opportunities within the company.
{% endif %}

### External Advertising
{{ company_name }} advertises open positions through various channels to reach qualified candidates:

{% if job_boards %}
{{ job_boards }}
{% else %}
* Professional networking sites (LinkedIn, industry-specific platforms)
* {{ company_name }} careers page
* Professional associations and conferences
* {% if university_partnerships|default(false) %}University career centers and partnerships{% endif %}
* {% if employee_referrals|default(true) %}Employee referral program{% endif %}
{% endif %}

## Application Process

### How to Apply
{% if application_method %}
{{ application_method }}
{% else %}
Applicants can apply for positions through our online application system accessible via our careers page. We accept applications via email only in exceptional circumstances.
{% endif %}

### Application Requirements
All applications should include:
* Current resume/CV
* Cover letter (when requested)
* References (provided upon request)
* {% if portfolio_required|default(false) %}Portfolio or work samples (for creative/design roles){% endif %}
* {% if assessment_required|default(false) %}Pre-employment assessment results{% endif %}

## Screening and Selection Process

### Initial Screening
{% if screening_process %}
{{ screening_process }}
{% else %}
The recruitment team conducts initial screening of applications to identify qualified candidates who meet the minimum requirements for the position. This includes:
* Review of qualifications and experience
* Assessment of cultural fit
* Verification of eligibility to work
{% endif %}

### Interviews
{{ company_name }} conducts structured interviews designed to assess candidates' skills, experience, and fit for the role and organization.

{% if interview_stages %}
{{ interview_stages }}
{% else %}
* **Phone/Video Screening**: Initial conversation with a recruiter or hiring manager
* **Technical Assessment**: Skills evaluation for technical or specialized roles
* **Panel Interview**: Meeting with multiple team members and stakeholders
* **Final Interview**: Discussion with senior leadership or executive team
{% endif %}

### Reference and Background Checks
{% if background_checks_required|default(true) %}
{{ company_name }} conducts reference and background checks for final candidates as permitted by law. These may include:
* Employment verification
* Criminal background checks (where legally permitted)
* Education verification
* Credit checks (for financial roles only)
* Drug screening (for safety-sensitive positions)
{% endif %}

{% if reference_policy %}
{{ reference_policy }}
{% else %}
We contact professional references provided by candidates to gain insights into their work performance and professional conduct.
{% endif %}

## Offer Process

### Employment Offers
{% if offer_process %}
{{ offer_process }}
{% else %}
Successful candidates receive formal employment offers that include:
* Job title and description
* Compensation details (salary, bonuses, benefits)
* Start date and work location
* Reporting structure
* Benefits enrollment information
{% endif %}

### Offer Acceptance
Candidates typically have {{ offer_deadline|default('5 business days') }} to accept or decline offers. Extensions may be granted for exceptional circumstances.

### Contingencies
{% if offer_contingencies %}
{{ offer_contingencies }}
{% else %}
Employment offers may be contingent upon:
* Successful completion of background checks
* Verification of eligibility to work in the designated location
* Satisfactory reference checks
* {% if drug_screening|default(false) %}Negative drug screening results{% endif %}
{% endif %}

## New Hire Onboarding

### Pre-Start Activities
{% if pre_start_activities %}
{{ pre_start_activities }}
{% else %}
New hires complete pre-employment paperwork and onboarding activities before their start date, including:
* Benefits enrollment
* Tax form completion
* {% if background_check_completion|default(true) %}Background check completion{% endif %}
* Technology and equipment setup
* {% if welcome_package|default(true) %}Welcome package and orientation materials{% endif %}
{% endif %}

## Recruitment Timeline

{% if recruitment_timeline %}
{{ recruitment_timeline }}
{% else %}
We strive to maintain efficient recruitment processes:
* Job posting to first interviews: {{ posting_to_interview|default('1-2 weeks') }}
* Interview process completion: {{ interview_completion|default('2-4 weeks') }}
* Offer to start date: {{ offer_to_start|default('1-2 weeks') }}
{% endif %}

## Confidentiality and Non-Disclosure

All applicants and candidates are required to maintain confidentiality regarding proprietary information shared during the recruitment process.

## Questions and Contact Information

{% if recruitment_contact_name or recruitment_contact_email %}
For questions about our recruitment process or to check on application status, please contact {% if recruitment_contact_name %}{{ recruitment_contact_name }}{% else %}the Recruitment Team{% endif %}{% if recruitment_contact_email %} at {{ recruitment_contact_email }}{% endif %}{% if recruitment_contact_phone %} or call {{ recruitment_contact_phone }}{% endif %}.
{% else %}
For questions about our recruitment process, please contact your hiring manager or the Human Resources department.
{% endif %}

{% if careers_website %}
Visit our careers page at [{{ careers_website_name|default('Careers') }}]({{ careers_website }}) for current openings and application information.
{% endif %}

## Policy Updates

This recruitment policy is reviewed periodically and may be updated to reflect changes in best practices, legal requirements, or company needs.

Last Updated: {{ last_updated|default('January 1, 2024') }}
