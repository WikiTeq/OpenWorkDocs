# {{ company_name }} Health Insurance Benefits

## Medical Insurance

{% if medical_insurance|default(true) %}

{{ company_name }} offers medical insurance through {{ medical_provider|default('our selected insurance carrier') }}. Our goal is to provide comprehensive healthcare coverage that supports your wellbeing and gives you peace of mind.

### Plan Options

{{ company_name }} offers {{ medical_plan_count|default('a comprehensive') }} medical plan option(s):

{% if medical_plan_details %}
{{ medical_plan_details }}
{% else %}
* {{ medical_plan_type|default('PPO (Preferred Provider Organization)') }} plan with in-network and out-of-network coverage
* Coverage for preventive care, office visits, hospitalization, prescription drugs, and emergency services
* Access to a broad network of healthcare providers
{% endif %}

### Cost Sharing

* **Company contribution**: {{ medical_company_contribution|default('75%') }} of the premium
* **Employee contribution**: {{ medical_employee_contribution|default('25%') }} of the premium through {{ medical_payment_method|default('payroll deductions') }}

{% if medical_rate_table|default(true) %}
#### Premium Rates

| Coverage Level | Employee Cost ({{ medical_cost_frequency|default('Per Pay Period') }}) |
|----------------|------------------------------------------|
| Employee Only | {{ medical_employee_only_cost|default('$XX.XX') }} |
| Employee + Spouse/Partner | {{ medical_employee_spouse_cost|default('$XX.XX') }} |
| Employee + Child(ren) | {{ medical_employee_children_cost|default('$XX.XX') }} |
| Family | {{ medical_family_cost|default('$XX.XX') }} |
{% endif %}

### Eligibility

You become eligible for medical insurance coverage {{ medical_eligibility_period|default('on your first day of employment') }}. Coverage extends to:

* You
* Your spouse or domestic partner
* Your dependent children up to age {{ dependent_age_limit|default('26') }}

### Enrollment

You can enroll in medical coverage:
* When first eligible as a new employee
* During annual open enrollment (typically {{ open_enrollment_period|default('in November') }})
* Within {{ qualifying_event_window|default('30 days') }} of a qualifying life event (such as marriage, birth of a child, or loss of other coverage)

{% else %}
{{ company_name }} does not currently offer medical insurance. {% if hr_contact_name is defined %}Please contact {{ hr_contact_name }} for information about healthcare options.{% else %}Please speak with your manager for information about healthcare options.{% endif %}
{% endif %}

## Dental Insurance

{% if dental_insurance|default(true) %}

{{ company_name }} provides dental insurance through {{ dental_provider|default('our dental insurance carrier') }} to help you maintain good dental health.

### Coverage

* **Preventive services**: {{ dental_preventive_coverage|default('100%') }} coverage for routine exams, cleanings, and x-rays
* **Basic services**: {{ dental_basic_coverage|default('80%') }} coverage for fillings, extractions, and root canals
* **Major services**: {{ dental_major_coverage|default('50%') }} coverage for crowns, bridges, and dentures
* **Annual maximum benefit**: {{ dental_annual_maximum|default('$1,500') }} per person
* **Deductible**: {{ dental_deductible|default('$50 individual / $150 family') }}

### Cost

* **Company contribution**: {{ dental_company_contribution|default('100%') }} of the premium
* **Employee contribution**: {{ dental_employee_contribution|default('0%') }} of the premium

### Eligibility and Enrollment

Dental coverage eligibility and enrollment periods match those of our medical insurance program.

{% else %}
{{ company_name }} does not currently offer dental insurance.
{% endif %}

## Vision Insurance

{% if vision_insurance|default(true) %}

{{ company_name }} offers vision insurance through {{ vision_provider|default('our vision insurance carrier') }} to help cover the cost of eye exams and vision correction.

### Coverage

* **Eye exams**: Covered once every {{ vision_exam_frequency|default('12 months') }}
* **Eyeglass frames**: {{ vision_frames_allowance|default('$150') }} allowance every {{ vision_frames_frequency|default('24 months') }}
* **Eyeglass lenses**: Covered once every {{ vision_lenses_frequency|default('12 months') }}
* **Contact lenses**: {{ vision_contacts_allowance|default('$150') }} allowance every {{ vision_contacts_frequency|default('12 months') }}
* **Additional discounts** on lens options and laser vision correction

### Cost

* **Company contribution**: {{ vision_company_contribution|default('100%') }} of the premium
* **Employee contribution**: {{ vision_employee_contribution|default('0%') }} of the premium

### Eligibility and Enrollment

Vision coverage eligibility and enrollment periods match those of our medical insurance program.

{% else %}
{{ company_name }} does not currently offer vision insurance.
{% endif %}

## International Employee Healthcare

{% if international_employees|default(false) %}

For employees outside the {{ company_hq_country|default('United States') }}, {{ company_name }} provides healthcare support through:

{% if international_healthcare_approach %}
{{ international_healthcare_approach }}
{% else %}
* Reimbursement for private health insurance (up to {{ international_reimbursement_cap|default('the equivalent cost of US employee coverage') }})
* Support for navigating local healthcare systems
* Ensuring equivalent access to quality healthcare regardless of location
{% endif %}

{% if hr_contact_name is defined %}
Please contact {{ hr_contact_name }} for specific details related to your location.
{% else %}
Please speak with your manager for specific details related to your location.
{% endif %}
{% endif %}
