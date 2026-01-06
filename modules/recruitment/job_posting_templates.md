# {{ company_name }} Job Posting Templates

## Standard Job Posting Structure

All {{ company_name }} job postings follow a consistent structure to ensure clarity, compliance, and appeal to qualified candidates.

### Required Elements

#### Job Title and Summary
```
[Job Title]

{{ company_name }} is seeking a talented [Job Title] to join our [Department/Team]. In this role, you will [brief 2-3 sentence description of primary responsibilities and impact].
```

#### About {{ company_name }}
{% if company_description %}
{{ company_description }}
{% else %}
{{ company_name }} is [brief company description focusing on mission, values, and unique aspects]. We are committed to [key company commitments like innovation, diversity, customer success, etc.].
{% endif %}

#### Key Responsibilities
* [Primary responsibility 1]
* [Primary responsibility 2]
* [Primary responsibility 3]
* [Additional responsibilities as needed]

#### Required Qualifications
* [Education/certification requirements]
* [Years of experience requirements]
* [Technical skills required]
* [Soft skills required]
* [Other mandatory qualifications]

#### Preferred Qualifications
* [Nice-to-have skills or experience]
* [Advanced qualifications]
* [Specialized knowledge]

#### What We Offer
{% if benefits_highlights %}
{{ benefits_highlights }}
{% else %}
* Competitive compensation and benefits package
* {% if remote_work|default(false) %}Flexible remote work options{% endif %}
* {% if professional_development|default(true) %}Professional development and growth opportunities{% endif %}
* {% if equity|default(false) %}Equity participation{% endif %}
* Collaborative and inclusive work environment
{% endif %}

#### How to Apply
{% if application_instructions %}
{{ application_instructions }}
{% else %}
Please submit your resume, cover letter, and any relevant work samples through our careers portal at [careers website]. Applications will be reviewed on a rolling basis.
{% endif %}

## Position-Specific Templates

### Technical Roles Template
```
We're looking for a [Senior/Staff/Principal] [Role] to design, build, and maintain [systems/products/features] that serve [user base/problem solved].

You will:
- Lead [specific technical responsibilities]
- Collaborate with [cross-functional teams]
- Mentor junior team members
- Contribute to [architectural/technical decisions]

Requirements:
- [X] years of experience in [relevant technology/domain]
- Proficiency in [required technologies]
- Experience with [relevant methodologies/tools]
- Strong problem-solving and communication skills
```

### Leadership Roles Template
```
{{ company_name }} is seeking an experienced [Director/VP/Head of] [Department] to lead our [team/department] and drive [key objectives].

In this role, you will:
- Provide strategic direction for [department/function]
- Manage and develop a team of [team size]
- Collaborate with executive leadership on [key initiatives]
- Drive [specific outcomes/metrics]

Ideal candidates have:
- [X+] years of leadership experience
- Proven track record in [relevant domain]
- Experience scaling [teams/processes/systems]
- Strategic thinking and execution skills
```

### Entry-Level Roles Template
```
We're excited to welcome talented graduates and early-career professionals to {{ company_name }} through our [program name or general entry-level roles].

As a [Role] at {{ company_name }}, you'll:
- [Primary learning and contribution activities]
- Work closely with experienced mentors
- Contribute to real projects from day one
- Participate in our comprehensive training program

We're looking for:
- [Degree/major requirements or equivalent experience]
- [Key skills or demonstrated abilities]
- Passion for [company mission/domain]
- Eagerness to learn and grow
```

## Diversity and Inclusion Language

All job postings include inclusive language to attract diverse candidates:

### Geographic Diversity
"{{ company_name }} supports remote work arrangements for eligible positions. We welcome applicants from diverse geographic locations."

### Inclusive Language Examples
* Use "they/them" pronouns where appropriate
* Avoid gender-coded language (e.g., "rockstar" instead of gender-specific terms)
* Include statements about work-life balance and flexibility
* Highlight diversity, equity, and inclusion commitments

## Compliance Requirements

### Equal Employment Opportunity Statement
"{{ company_name }} is an equal opportunity employer. We celebrate diversity and are committed to creating an inclusive environment for all employees."

{% if additional_compliance_statements %}
{{ additional_compliance_statements }}
{% endif %}

### Pay Transparency
{% if pay_transparency|default(false) %}
"When applicable, {{ company_name }} includes salary ranges in job postings to promote transparency and fairness in compensation."
{% endif %}

## Template Customization Guidelines

### Industry-Specific Adaptations
* **Technology**: Emphasize innovation, collaboration, and technical challenges
* **Finance**: Highlight regulatory compliance, risk management, and analytical skills
* **Healthcare**: Focus on patient impact, regulatory knowledge, and care quality
* **Education**: Stress learning outcomes, student success, and pedagogical expertise

### Company Size Considerations
* **Startup**: Emphasize growth opportunities, autonomy, and impact
* **Mid-size**: Highlight work-life balance, career development, and stability
* **Enterprise**: Focus on scale, resources, and comprehensive benefits

## Quality Assurance Checklist

Before publishing job postings, ensure they include:
- [ ] Accurate job title and level
- [ ] Clear responsibilities and expectations
- [ ] Required and preferred qualifications
- [ ] Compensation information (when required by law)
- [ ] Benefits highlights
- [ ] Equal opportunity statement
- [ ] Application instructions
- [ ] Contact information for questions

Last Updated: {{ last_updated|default('January 1, 2024') }}
