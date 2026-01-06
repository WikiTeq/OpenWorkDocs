# {{ company_name }} Performance Management Policy

## Overview

{{ company_name }} is committed to fostering a culture of continuous improvement, growth, and excellence. Our performance management process is designed to align individual contributions with company goals, provide clear feedback, and support professional development.

{% if performance_philosophy %}
{{ performance_philosophy }}
{% else %}
Performance management at {{ company_name }} is not just about evaluation—it's about enabling every team member to achieve their best work, grow their skills, and contribute meaningfully to our mission.
{% endif %}

## Performance Management Framework

Our approach to performance management includes:

* **Goal Setting**: Establishing clear, measurable objectives aligned with company priorities
* **Regular Feedback**: Ongoing coaching and development conversations
* **Formal Reviews**: Structured performance evaluations and career discussions
* **Development Planning**: Creating paths for skill growth and career advancement
* **Recognition**: Celebrating achievements and contributions

{% if performance_cycle %}
{{ performance_cycle }}
{% else %}
Our performance cycle typically follows an annual calendar with quarterly check-ins, mid-year reviews, and annual performance discussions.
{% endif %}

## Performance Expectations

### Core Competencies
{% if core_competencies %}
{{ core_competencies }}
{% else %}
All {{ company_name }} employees are expected to demonstrate excellence in:

* **Results Delivery**: Consistently achieving goals and delivering high-quality work
* **Collaboration**: Working effectively with team members and cross-functional partners
* **Innovation**: Contributing creative solutions and continuous improvement
* **Communication**: Clearly articulating ideas and actively listening
* **Leadership**: Taking initiative and supporting team success
{% endif %}

### Role-Specific Expectations
Individual performance expectations are tailored to each role and level, considering:
* Job responsibilities and scope
* Required skills and experience
* Team and departmental goals
* Company objectives

## Performance Rating System

{% if rating_system %}
{{ rating_system }}
{% else %}
{{ company_name }} uses a performance rating system to provide clear feedback:

* **Exceeds Expectations**: Consistently exceeds role requirements and demonstrates exceptional performance
* **Meets Expectations**: Successfully fulfills all job requirements and responsibilities
* **Below Expectations**: Does not fully meet job requirements and needs improvement
* **Not Applicable**: New hire still in probationary period
{% endif %}

{% if rating_definitions %}
{{ rating_definitions }}
{% endif %}

## Performance Review Process

### Self-Assessment
Employees prepare a self-assessment covering:
* Accomplishments and achievements
* Challenges faced and lessons learned
* Goal progress and metrics
* Development areas and growth plans
* Feedback for managers and the organization

### Manager Assessment
Managers provide comprehensive feedback including:
* Performance against goals and objectives
* Demonstration of core competencies
* Development progress and skill growth
* Areas of strength and improvement opportunities
* Career development recommendations

### Calibration and Review
{% if calibration_process %}
{{ calibration_process }}
{% else %}
Performance ratings are calibrated across teams to ensure fairness and consistency. Final ratings are reviewed and approved by department leadership.
{% endif %}

## Compensation and Rewards

Performance directly influences compensation decisions:

* **Base Salary Adjustments**: Based on performance rating, market positioning, and internal equity
* **Bonus Eligibility**: Tied to individual and company performance achievement
* **Promotion Opportunities**: Strong performance is required for advancement
* {% if equity_program %}**Equity Grants**: Performance may influence equity compensation{% endif %}

## Performance Improvement Plans

When performance issues arise, {{ company_name }} follows a structured improvement process:

### Informal Coaching
Initial performance concerns are addressed through:
* Regular feedback conversations
* Additional training and resources
* Clear action plans with timelines

### Formal Performance Improvement Plan (PIP)
For sustained performance issues:
* Written performance improvement plan
* Specific, measurable improvement goals
* Regular check-in meetings
* Defined timeline (typically 30-90 days)
* Support resources and training opportunities

### Disciplinary Actions
If performance does not improve:
* Verbal warning with documentation
* Written warning
* Suspension with or without pay
* Termination of employment

## Development and Growth

{{ company_name }} is committed to employee development:

### Learning and Development
* Access to training programs and courses
* Conference and certification reimbursement
* {% if mentorship_program %}Mentorship and coaching programs{% endif %}
* {% if tuition_assistance %}Tuition assistance for degree programs{% endif %}

### Career Planning
* Career path discussions during performance reviews
* Internal job posting preferences
* {% if internal_mobility %}Internal mobility opportunities{% endif %}
* Succession planning for leadership roles

## Performance Documentation

All performance-related discussions and decisions are documented:

* Performance reviews and feedback
* Goal setting and progress tracking
* Development plans and training records
* Disciplinary actions and improvement plans
* Compensation and promotion decisions

Documentation is maintained in accordance with applicable laws and company retention policies.

## Appeals Process

{% if appeals_process %}
{{ appeals_process }}
{% else %}
Employees who disagree with their performance rating or review outcome may appeal the decision by:

1. Discussing concerns with their manager within {{ appeal_timeline|default('5 business days') }}
2. Escalating to HR if unresolved
3. Requesting review by department leadership or HR committee
4. Final appeal to executive leadership if necessary
{% endif %}

## Questions and Support

For questions about the performance management process, please contact {% if hr_contact_name %}{{ hr_contact_name }}{% else %}Human Resources{% endif %}{% if hr_contact_email %} at {{ hr_contact_email }}{% endif %}{% if hr_contact_phone %} or call {{ hr_contact_phone }}{% endif %}.

{% if performance_resources %}
**Additional Resources**:
{{ performance_resources }}
{% endif %}

Last Updated: {{ last_updated|default('January 1, 2024') }}
