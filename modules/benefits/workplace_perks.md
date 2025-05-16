# {{ company_name }} Workplace Perks

## Remote Work Support

{% if remote_work|default(true) %}

{{ company_name }} is committed to supporting a productive remote work environment for our team members.

### Home Office Setup

{% if home_office_stipend|default(true) %}
{{ company_name }} provides a one-time stipend of {{ home_office_amount|default('$500') }} to help set up your home workspace when you join the company.

Eligible items include:
* Desk and ergonomic chair
* Monitor, keyboard, and other computer peripherals
* Lighting and other workspace accessories
{% endif %}

{% if technology_refresh|default(true) %}
### Technology Refresh Program

{{ company_name }} provides new computers to employees every {{ tech_refresh_cycle|default('3 years') }}. You'll receive a {{ computer_type|default('laptop') }} appropriate for your role, configured with necessary software.
{% endif %}

{% if internet_stipend|default(false) %}
### Internet Stipend

{{ company_name }} provides a monthly stipend of {{ internet_amount|default('$50') }} to offset the cost of reliable high-speed internet service.
{% endif %}

{% if coworking_allowance|default(false) %}
### Coworking Space Allowance

If you prefer to work outside your home, {{ company_name }} will reimburse up to {{ coworking_amount|default('$200') }} per month for coworking space membership.
{% endif %}

{% else %}
{{ company_name }} provides appropriate work equipment based on job requirements. Please speak with your manager about your specific needs.
{% endif %}

## Professional Development

{% if professional_development|default(true) %}

{{ company_name }} supports your continued growth and development.

### Learning and Education

* Annual professional development budget of {{ development_budget|default('$1,000') }} per employee
* Access to {{ learning_platform|default('online learning platforms and courses') }}
* Support for attending relevant conferences and workshops

### Certification Support

{{ company_name }} covers the cost of relevant professional certifications and continuing education required for your role.

{% if mentorship_program|default(false) %}
### Mentorship Program

{{ company_name }} offers a structured mentorship program to help employees develop skills and advance their careers within the organization.
{% endif %}

{% else %}
{{ company_name }} supports professional development on a case-by-case basis. Please discuss opportunities with your manager.
{% endif %}

## Wellness Benefits

{% if wellness_benefits|default(true) %}

{{ company_name }} values your physical and mental wellbeing.

{% if wellness_stipend|default(false) %}
### Wellness Stipend

Employees receive a monthly wellness stipend of {{ wellness_amount|default('$50') }} to use toward activities that support your physical and mental health, such as:
* Gym memberships
* Fitness apps
* Meditation subscriptions
* Other wellness services
{% endif %}

{% if mental_health|default(true) %}
### Mental Health Resources

{{ company_name }} provides access to mental health support through {{ mental_health_provider|default('our Employee Assistance Program (EAP)') }}, which includes:
* Confidential counseling sessions
* 24/7 crisis support
* Work-life resource referrals
{% endif %}

{% if wellness_programs|default(false) %}
### Wellness Programs

{{ company_name }} offers periodic wellness challenges, workshops, and resources to support your wellbeing.
{% endif %}

{% else %}
{{ company_name }} encourages employees to prioritize their wellbeing and supports reasonable accommodations for health needs.
{% endif %}

## Additional Perks

{% if company_swag|default(true) %}
### Company Swag

New team members receive a welcome package with {{ company_name }} branded items. Additional company swag is distributed periodically.
{% endif %}

{% if company_events|default(true) %}
### Company Events

{{ company_name }} hosts {{ company_events_frequency|default('regular') }} virtual events and {{ retreat_frequency|default('annual') }} in-person gatherings to build team connections.
{% endif %}

{% if recognition_program|default(false) %}
### Recognition Program

{{ company_name }} celebrates employee achievements through our {{ recognition_program_name|default('recognition program') }}, which includes peer nominations and rewards for outstanding contributions.
{% endif %}

{% if referral_bonus|default(false) %}
### Referral Bonus

Refer qualified candidates who are hired and successfully complete their {{ referral_period|default('90-day') }} probation period to receive a {{ referral_amount|default('$1,000') }} bonus.
{% endif %}

{% if discount_program|default(false) %}
### Employee Discount Program

{{ company_name }} offers employees access to discounts on various products and services through our {{ discount_program_name|default('corporate discount program') }}.
{% endif %}

{% if additional_custom_perks %}
### Additional Perks

{{ additional_custom_perks }}
{% endif %}
