# {{ company_name }} Remote Work Policy

## Introduction

{{ company_name }} supports remote work as an effective way to accomplish our business goals while providing flexibility to our team members. This policy outlines our approach to remote work, expectations, and resources available to ensure success in a distributed environment.

{% if remote_first|default(false) %}
As a remote-first organization, {{ company_name }} designs all processes, communications, and workflows to function optimally in a distributed environment.
{% elif hybrid|default(false) %}
{{ company_name }} operates on a hybrid model, combining remote work with in-person collaboration at our office locations.
{% else %}
{{ company_name }} allows remote work options for eligible roles and employees.
{% endif %}

## Scope and Eligibility

{% if eligibility_statement %}
{{ eligibility_statement }}
{% else %}
Remote work eligibility is based on job function, business needs, and individual performance. Not all positions are suited for remote work due to operational requirements. Each department determines remote work eligibility for its roles {% if hr_department_name is defined %}in consultation with {{ hr_department_name }}{% else %}based on team and business needs{% endif %}.
{% endif %}

## Remote Work Models

{% if remote_work_models %}
{{ remote_work_models }}
{% else %}
{{ company_name }} offers the following remote work arrangements:

* **Fully Remote**: Employees work remotely 100% of the time from an approved location.
* **Hybrid Remote**: Employees split time between remote work and in-office work according to team schedules and requirements.
* **Occasional Remote Work**: Primarily office-based employees who occasionally work remotely.

{% if location_restrictions|default(true) %}
Remote work locations must comply with {{ company_name }}'s geographic restrictions based on tax, legal, and business considerations.
{% endif %}
{% endif %}

## Core Hours and Availability

{% if core_hours_statement %}
{{ core_hours_statement }}
{% else %}
While we value flexibility, we also need to ensure effective collaboration across teams. Remote employees are expected to:

* Be available during core business hours of {{ core_hours|default('10:00 AM to 3:00 PM') }} in their assigned time zone, unless otherwise agreed upon
* Communicate their working hours and availability status through designated channels
* Respond to messages within reasonable timeframes during their working hours
* Notify their team of any significant deviations from their regular schedule
{% endif %}

## Equipment and Home Office Setup

{{ company_name }} is committed to ensuring employees have the tools and equipment needed to work effectively.

{% if equipment_provided|default(true) %}
The company provides standard equipment including:
* {{ primary_equipment|default('Computer/laptop appropriate for your role') }}
* {{ secondary_equipment|default('Necessary accessories and peripherals') }}

For detailed information about equipment and home office support, please refer to our [Home Office Setup Guidelines](home_office.md).
{% endif %}

## Communication Expectations

Effective communication is essential for remote work success. Team members are expected to:

* Maintain regular communication with managers and team members
* Be responsive during working hours
* Utilize appropriate communication tools for different types of interactions
* Document important decisions and information for asynchronous reference

For detailed information, please refer to our [Remote Communication Guidelines](communication.md).

## Performance Management

Remote work does not change performance expectations. Leaders and employees should:

* Clearly define objectives, deliverables, and timelines
* Hold regular check-ins to discuss progress and challenges
* Provide timely feedback
* Focus on results rather than activity or hours worked

## Security and Confidentiality

Remote employees must adhere to all company security policies and take special precautions to ensure the security of company data and information when working outside of company facilities. For detailed security requirements, please refer to our [Remote Work Security Guidelines](security.md).

## Support for Remote Workers

{{ company_name }} offers various resources to support remote workers:

* Virtual collaboration tools and technology
* Remote-specific training and development
* {% if wellness_support|default(true) %}Wellness resources and support for work-life balance{% endif %}
* {% if remote_engagement|default(true) %}Virtual team building and engagement activities{% endif %}

## Questions and Support

For questions about the remote work policy or for assistance with remote work arrangements, please contact {% if hr_department_name is defined %}{{ remote_work_contact|default('your manager or ' + hr_department_name) }}{% else %}{{ remote_work_contact|default('your manager') }}{% endif %}.

Last Updated: {{ last_updated|default('January 1, 2024') }}
