# {{ company_name }} Time Off Benefits

## Paid Time Off (PTO)

{% if pto_policy|default(true) %}

{{ company_name }} provides paid time off to allow employees to rest, recharge, and attend to personal matters.

### PTO Allowance

Full-time employees receive {{ pto_days|default('15') }} days of paid time off per calendar year. {% if pto_accrual|default(true) %}PTO accrues at the rate of {{ pto_accrual_rate|default('1.25 days') }} per month.{% endif %}

{% if pto_prorated_first_year|default(true) %}
Your PTO allowance is prorated based on your start date during your first year at {{ company_name }}.
{% endif %}

### Rollover Policy

{% if pto_rollover|default(true) %}
Unused PTO days roll over from year to year, up to a maximum balance of {{ pto_rollover_cap|default('25') }} days.
{% else %}
Unused PTO does not roll over from year to year. You are encouraged to use your full PTO allowance each year.
{% endif %}

### Requesting Time Off

To request time off, {{ pto_request_process|default('please notify your manager with reasonable advance notice and ensure your responsibilities are covered during your absence.') }}

### PTO Upon Termination

{% if pto_payout|default(true) %}
If you leave {{ company_name }}, you will be paid for any unused, accrued PTO.
{% else %}
Unused PTO is not paid out upon termination of employment.
{% endif %}

{% else %}
{{ company_name }} does not currently offer a formal PTO policy. Please discuss time off needs with your manager.
{% endif %}

## Holidays

{% if paid_holidays|default(true) %}

{{ company_name }} observes the following {{ holiday_count|default('10') }} paid holidays each year:

{% if holiday_list %}
{{ holiday_list }}
{% else %}
* New Year's Day
* Martin Luther King Jr. Day
* Memorial Day
* Independence Day
* Labor Day
* Thanksgiving Day
* Day after Thanksgiving
* Christmas Eve
* Christmas Day
* New Year's Eve
{% endif %}

{% if floating_holidays|default(false) %}
In addition to these fixed holidays, employees receive {{ floating_holiday_count|default('2') }} floating holidays to use at their discretion each year.
{% endif %}

{% if holiday_substitution|default(true) %}
When a holiday falls on a weekend, it will typically be observed on the nearest weekday.
{% endif %}

{% else %}
{{ company_name }} does not currently offer paid holidays. Please discuss holiday time off with your manager.
{% endif %}

## Family and Medical Leave

{% if family_leave|default(true) %}

{{ company_name }} provides family and medical leave in accordance with applicable laws and to support employees during important life events.

### Parental Leave

{% if parental_leave|default(true) %}
* **Primary caregiver**: {{ primary_caregiver_leave|default('12 weeks') }} of paid leave at {{ primary_caregiver_pay|default('100%') }} of regular pay
* **Secondary caregiver**: {{ secondary_caregiver_leave|default('4 weeks') }} of paid leave at {{ secondary_caregiver_pay|default('100%') }} of regular pay

This leave must be taken within {{ parental_leave_window|default('12 months') }} of the birth, adoption, or foster placement of a child.
{% endif %}

### Medical Leave

{% if medical_leave|default(true) %}
Employees may take up to {{ medical_leave_duration|default('12 weeks') }} of leave for their own serious health condition, with {{ medical_leave_pay|default('short-term disability benefits') }} available during this time.
{% endif %}

### Family Care Leave

{% if family_care_leave|default(true) %}
Employees may take up to {{ family_care_leave_duration|default('12 weeks') }} of leave to care for a family member with a serious health condition. {{ family_care_leave_pay|default('This leave may be partially paid depending on circumstances and applicable laws.') }}
{% endif %}

### Eligibility

Employees become eligible for family and medical leave after {{ family_leave_eligibility|default('12 months of employment') }}.

{% else %}
{{ company_name }} provides family and medical leave in accordance with applicable laws. {% if hr_contact_name is defined %}Please contact {{ hr_contact_name }} for specific information.{% else %}Please speak with your manager for specific information.{% endif %}
{% endif %}

## Additional Time Off

{% if additional_leave_types|default(true) %}

### Bereavement Leave

{{ company_name }} provides {{ bereavement_days_immediate|default('5') }} days of paid leave following the death of an immediate family member and {{ bereavement_days_extended|default('3') }} days for extended family.

### Jury Duty

Employees called for jury duty will receive {{ jury_duty_pay|default('full pay') }} for up to {{ jury_duty_days|default('10') }} days while serving.

{% if voting_time|default(true) %}
### Voting Time

{{ company_name }} encourages civic participation and provides {{ voting_time_hours|default('up to 2 hours') }} of paid time off to vote when polls are not open outside working hours.
{% endif %}

{% if sabbatical|default(false) %}
### Sabbatical Leave

After {{ sabbatical_eligibility|default('every 5 years') }} of continuous employment, eligible employees may take a {{ sabbatical_duration|default('4-week') }} paid sabbatical to recharge and pursue personal enrichment.
{% endif %}

{% if volunteer_time|default(false) %}
### Volunteer Time Off

{{ company_name }} offers {{ volunteer_days|default('2') }} paid days per year for employees to volunteer with qualified organizations.
{% endif %}

{% endif %}
