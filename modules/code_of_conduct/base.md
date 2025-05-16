# {{ company_name }} Code of Conduct

## Our Commitment

At {{ company_name }}, we are committed to providing a respectful, inclusive, and professional environment for all employees, contractors, partners, and stakeholders. This Code of Conduct outlines our expectations for behavior, our procedures for addressing concerns, and our commitment to maintaining a workplace where everyone can thrive.

## Core Expectations

We expect all {{ company_name }} employees and contractors to:

* **Act with integrity** in all professional interactions and decisions
* **Communicate respectfully** with colleagues, clients, and partners
* **Embrace diversity** and the unique perspectives it brings to our organization
* **Collaborate openly** and share knowledge to strengthen our collective capabilities
* **Accept feedback graciously** and provide constructive feedback to others
* **Take responsibility** for your actions and their impact on others
* **Maintain confidentiality** of sensitive information

## Prohibited Conduct

{{ company_name }} strictly prohibits discrimination, harassment, and retaliation in any form. This includes, but is not limited to:

* Discrimination based on race, color, religion, gender, gender identity, sexual orientation, national origin, disability, age, or any other characteristic protected by applicable law
* Harassment, including unwelcome verbal, visual, or physical conduct
* Bullying, intimidation, or abusive language
* Retaliation against anyone who reports a concern or participates in an investigation

## Reporting Concerns

If you experience or witness behavior that violates this Code of Conduct, please report it through one of the following channels:

* Your direct manager
{% if hr_contact_email is defined %}
* Human Resources department at {{ hr_contact_email }}
{% endif %}
* {{ reporting_system|default('Our confidential reporting system') }}

All reports will be taken seriously and investigated promptly. {{ company_name }} will maintain confidentiality to the extent possible during any investigation.

## Consequences of Violations

Violations of this Code of Conduct may result in disciplinary action, up to and including termination of employment. The specific actions taken will depend on the nature, severity, and frequency of the violation.

## Commitment to Non-Retaliation

{{ company_name }} strictly prohibits retaliation against anyone who reports a potential violation of this Code of Conduct in good faith or participates in an investigation. Retaliation is itself a violation of this Code and will be subject to disciplinary action.

---

This Code of Conduct may be updated periodically. Employees are responsible for reviewing and adhering to the most current version.

Last updated: {{ last_updated|default('January 1, 2023') }}
