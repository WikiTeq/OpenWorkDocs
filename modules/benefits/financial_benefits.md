# {{ company_name }} Financial Benefits

## Retirement Plan

{% if retirement_plan|default(true) %}

{{ company_name }} offers a retirement plan to help employees save for their future financial security.

### Plan Type

Our retirement plan is a {{ retirement_plan_type|default('401(k)') }} administered by {{ retirement_provider|default('our retirement plan provider') }}.

### Contributions

* **Employee contributions**: You may contribute up to the IRS annual limit through convenient payroll deductions.
* **Company match**: {{ company_name }} matches {{ retirement_match_percent|default('100%') }} of your contributions up to {{ retirement_match_limit|default('6%') }} of your eligible compensation.

### Vesting

{% if retirement_immediate_vesting|default(false) %}
You are immediately 100% vested in all contributions, including the company match.
{% else %}
You are always 100% vested in your own contributions. Company matching contributions vest according to this schedule:
* {{ retirement_vesting_schedule|default('25% after 1 year, 50% after 2 years, 75% after 3 years, 100% after 4 years') }}
{% endif %}

### Eligibility

You become eligible to participate in the retirement plan after {{ retirement_eligibility_period|default('30 days of employment') }}.

{% if international_retirement|default(false) %}
### International Employees

For employees outside the {{ company_hq_country|default('United States') }}, {{ company_name }} offers equivalent retirement benefits through:
* {{ international_retirement_approach|default('A contribution to your local retirement system, matching what we provide to US employees') }}
{% endif %}

{% else %}
{{ company_name }} does not currently offer a retirement plan.
{% endif %}

## Additional Financial Benefits

{% if profit_sharing|default(false) %}
### Profit Sharing

{{ company_name }} shares {{ profit_sharing_percent|default('a portion') }} of company profits with eligible employees based on {{ profit_sharing_criteria|default('company performance and tenure') }}. Distributions typically occur {{ profit_sharing_timing|default('annually') }}.

Eligibility begins after {{ profit_sharing_eligibility|default('completing one full year of service') }}.
{% endif %}

{% if equity|default(false) %}
### Equity

{{ company_name }} offers {{ equity_type|default('equity opportunities') }} to eligible employees as part of our commitment to shared success. Our equity program includes:

* {{ equity_details|default('Details of our equity program are provided separately during the hiring process or when you become eligible') }}
{% endif %}

{% if bonuses|default(false) %}
### Performance Bonuses

{{ company_name }} may provide performance-based bonuses {{ bonus_frequency|default('annually') }} based on {{ bonus_criteria|default('individual and company performance') }}.
{% endif %}

{% if financial_wellness|default(false) %}
### Financial Wellness Program

{{ company_name }} offers resources to support your financial wellness, including:

* {{ financial_wellness_details|default('Access to financial planning resources and educational materials') }}
{% endif %}

{% if tuition|default(false) %}
### Tuition Assistance

{{ company_name }} provides tuition assistance of up to {{ tuition_amount|default('$5,000') }} per year for approved education programs related to your current position or career path within the company.

To be eligible, you must:
* {{ tuition_eligibility|default('Have completed at least one year of employment') }}
* {{ tuition_requirements|default('Maintain satisfactory job performance and receive prior approval for the educational program') }}
{% endif %}

{% if commuter|default(false) %}
### Commuter Benefits

{{ company_name }} offers pre-tax commuter benefits for eligible transportation expenses up to the IRS monthly limits.
{% endif %}

{% if flexible_spending|default(false) %}
### Flexible Spending Accounts

{{ company_name }} offers Flexible Spending Accounts (FSAs) that allow you to set aside pre-tax dollars for:

* **Healthcare FSA**: For eligible medical, dental, and vision expenses
* **Dependent Care FSA**: For eligible dependent care expenses

The annual contribution limits are set according to IRS guidelines.
{% endif %}
