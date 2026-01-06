# {{ company_name }} Performance Review Process

## Overview

Performance reviews at {{ company_name }} provide structured opportunities for feedback, recognition, and development planning. Our review process emphasizes continuous dialogue, constructive feedback, and mutual growth between employees and managers.

{% if review_philosophy %}
{{ review_philosophy }}
{% else %}
We believe performance reviews should be developmental conversations focused on growth and achievement, not just evaluation. Reviews celebrate successes, identify development opportunities, and create action plans for future improvement.
{% endif %}

## Review Cycle and Timing

{% if review_cycle %}
{{ review_cycle }}
{% else %}
{{ company_name }} conducts performance reviews on a regular cycle:

* **Probationary Reviews**: {{ probationary_reviews|default('30, 60, and 90 days') }} for new hires
* **Annual Reviews**: Comprehensive performance discussions each year
* **Mid-Year Reviews**: Progress check-ins and adjustment discussions
* **Ad-Hoc Reviews**: As needed for promotions, role changes, or performance issues
{% endif %}

### Review Timeline
{% if review_timeline %}
{{ review_timeline }}
{% else %}
* **Self-Assessment Due**: {{ self_assessment_deadline|default('1 week before review') }}
* **Manager Review Completion**: {{ manager_review_deadline|default('1 week before meeting') }}
* **Review Meeting**: Scheduled within {{ meeting_window|default('2 weeks') }}
* **Calibration**: {{ calibration_window|default('1 week after individual reviews') }}
* **Final Approvals**: {{ approval_window|default('End of review cycle') }}
{% endif %}

## Review Preparation

### Employee Preparation
Employees should prepare for reviews by:

1. **Self-Assessment**: Complete self-evaluation form covering:
   * Accomplishments and key achievements
   * Challenges faced and lessons learned
   * Goal progress and metrics
   * Strengths and development areas
   * Career aspirations and growth plans

2. **Gather Evidence**: Collect specific examples and data:
   * Project outcomes and impact metrics
   * Feedback received from colleagues
   * Skills developed or certifications earned
   * {% if enable_360_feedback %}360-degree feedback from peers and stakeholders{% endif %}

3. **Reflect on Goals**: Review progress against quarterly/annual objectives

### Manager Preparation
Managers prepare comprehensive assessments including:

1. **Performance Data Review**: Analyze quantitative metrics and achievements
2. **Stakeholder Input**: Gather feedback from colleagues and cross-functional partners
3. **Goal Assessment**: Evaluate progress against established objectives
4. **Development Planning**: Identify growth opportunities and training needs
5. **Compensation Recommendations**: Prepare salary and bonus recommendations

## Review Meeting Structure

### Meeting Format
{% if review_format %}
{{ review_format }}
{% else %}
Performance review meetings typically last {{ meeting_duration|default('60 minutes') }} and follow this structure:

1. **Opening and Context Setting** (10 minutes)
   * Review meeting purpose and format
   * Discuss any changes since last review

2. **Self-Assessment Review** (15 minutes)
   * Employee shares accomplishments and self-assessment
   * Manager asks clarifying questions

3. **Manager Feedback** (20 minutes)
   * Review performance against goals and expectations
   * Discuss strengths, achievements, and areas for improvement
   * Provide specific examples and data

4. **Development Discussion** (10 minutes)
   * Career aspirations and growth opportunities
   * Training and development recommendations
   * Next steps and action items

5. **Goal Setting** (5 minutes)
   * Set or adjust goals for next period

6. **Closing** (5 minutes)
   * Summarize key points and action items
   * Confirm follow-up plans
{% endif %}

### Meeting Best Practices

#### For Employees
* Be prepared with specific examples
* Listen actively and ask questions
* Be open to constructive feedback
* Focus on future development and growth
* Take notes on key discussion points

#### For Managers
* Create a comfortable, confidential environment
* Balance positive feedback with constructive criticism
* Use specific examples and data to support feedback
* Focus on behaviors and outcomes, not personality
* End on a positive, forward-looking note

## Performance Rating System

{% if rating_system %}
{{ rating_system }}
{% else %}
{{ company_name }} uses a standardized rating system to ensure consistency:

* **5 - Exceptional**: Far exceeds expectations; role model performance
* **4 - Exceeds Expectations**: Consistently exceeds requirements; high impact
* **3 - Meets Expectations**: Fully meets job requirements; solid contributor
* **2 - Below Expectations**: Occasionally misses requirements; needs improvement
* **1 - Significantly Below**: Frequently misses requirements; substantial gaps
* **N/A - Too New**: Insufficient time in role for full assessment
{% endif %}

### Rating Calibration
{% if calibration_process %}
{{ calibration_process }}
{% else %}
To ensure fairness and consistency across the organization:
* Managers calibrate ratings within their teams
* Department leaders review ratings across teams
* HR provides guidance on rating distribution
* Executive leadership approves final rating distributions
{% endif %}

## Feedback Delivery

### Constructive Feedback Guidelines
* **Be Specific**: Use concrete examples rather than generalizations
* **Focus on Impact**: Explain how behaviors affect outcomes
* **Balance Positive and Negative**: Acknowledge strengths alongside areas for improvement
* **Make it Actionable**: Provide clear steps for improvement
* **Be Timely**: Address issues when they occur, not just during reviews

### Receiving Feedback
* **Listen Actively**: Pay attention without interrupting
* **Seek Clarification**: Ask questions to understand the feedback
* **Express Appreciation**: Thank the person for their input
* **Take Notes**: Document key points for future reference
* **Follow Up**: Discuss progress in subsequent meetings

## Performance Improvement Plans

When performance issues are identified, {{ company_name }} follows a structured improvement process:

### Verbal Discussion
Initial concerns are addressed through informal coaching conversations.

### Written Improvement Plan
For sustained issues, a formal Performance Improvement Plan (PIP) includes:
* Specific performance expectations and standards
* Measurable improvement goals with timelines
* Support resources and training opportunities
* Regular check-in schedule
* Consequences for continued performance issues

### PIP Timeline
{% if pip_timeline %}
{{ pip_timeline }}
{% else %}
* **Plan Duration**: Typically {{ pip_duration|default('60-90 days') }}
* **Check-in Frequency**: {{ pip_checkins|default('Weekly or bi-weekly') }} progress meetings
* **Final Assessment**: Performance evaluation at plan conclusion
* **Next Steps**: Successful completion, extension, or separation
{% endif %}

## Documentation and Records

### Review Documentation
All performance reviews are documented including:
* Self-assessment and manager evaluation
* Performance ratings and detailed feedback
* Development plans and action items
* Agreed-upon goals and timelines
* Follow-up meeting schedules

### Record Retention
{% if retention_policy %}
{{ retention_policy }}
{% else %}
Performance records are retained in accordance with legal requirements and company policy. Records are typically kept for {{ retention_period|default('7 years') }}.
{% endif %}

## Appeals and Dispute Resolution

{% if appeals_process %}
{{ appeals_process }}
{% else %}
Employees who disagree with their performance review may appeal by:

1. **Informal Resolution**: Discuss concerns with manager within {{ informal_appeal_window|default('5 business days') }}
2. **Formal Appeal**: Submit written appeal to HR within {{ formal_appeal_window|default('10 business days') }}
3. **Review Process**: HR investigation and potential review committee
4. **Final Decision**: HR or executive leadership determination
{% endif %}

## Development Planning

### Individual Development Plans
Based on review discussions, employees and managers create development plans covering:
* **Skill Development**: Training courses, certifications, workshops
* **Career Growth**: Job rotations, stretch assignments, mentoring
* **Leadership Development**: Management training, executive coaching
* **Education Support**: Tuition reimbursement, conference attendance

### Resources Available
{% if development_resources %}
{{ development_resources }}
{% else %}
{{ company_name }} provides:
* Annual learning and development budget
* Access to online learning platforms
* Leadership development programs
* {% if mentorship_program %}Mentorship and coaching opportunities{% endif %}
* {% if tuition_assistance %}Tuition assistance programs{% endif %}
{% endif %}

## Compensation and Career Decisions

### Salary Adjustments
Performance reviews inform compensation decisions:
* **Merit Increases**: Based on performance rating and market positioning
* **Promotion Eligibility**: Strong performance required for advancement
* **Bonus Determination**: Individual performance component of bonus calculations

### Career Planning
Reviews include career development discussions:
* **Promotion Timelines**: Expected timeframes for advancement
* **Skill Requirements**: Competencies needed for next-level roles
* **Development Opportunities**: Internal job opportunities and transitions

## Continuous Feedback Culture

### Between Formal Reviews
{{ company_name }} encourages ongoing feedback through:
* **Weekly Check-ins**: Regular one-on-one meetings
* **Real-time Feedback**: Immediate recognition and constructive input
* **Peer Feedback**: Cross-team and colleague input
* **360-Degree Reviews**: Comprehensive stakeholder feedback

### Feedback Tools
{% if feedback_tools %}
{{ feedback_tools }}
{% else %}
* Performance management software
* Anonymous feedback platforms
* Recognition and appreciation tools
* Regular pulse surveys
{% endif %}

## Questions and Support

For questions about the performance review process, please contact {% if performance_contact %}{{ performance_contact }}{% else %}Human Resources{% endif %}.

{% if review_resources %}
**Additional Resources**:
{{ review_resources }}
{% endif %}

Last Updated: {{ last_updated|default('January 1, 2024') }}
