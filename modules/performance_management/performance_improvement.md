# {{ company_name }} Performance Improvement and Disciplinary Procedures

## Commitment to Fair Process

{{ company_name }} believes in giving employees every opportunity to succeed. Our performance improvement process is designed to be fair, supportive, and focused on helping employees meet expectations while maintaining accountability for performance standards.

{% if improvement_commitment %}
{{ improvement_commitment }}
{% else %}
We approach performance improvement as a collaborative process aimed at understanding root causes, providing necessary support, and achieving sustainable improvement. Our goal is always to help employees succeed in their roles.
{% endif %}

## Performance Expectations

### Clear Standards
All employees are expected to meet established performance standards including:

* **Job-Specific Requirements**: Core responsibilities and deliverables
* **Behavioral Standards**: Professional conduct and teamwork
* **Company Values**: Alignment with {{ company_name }} principles
* **Quality and Timeliness**: Meeting deadlines and quality expectations

### Performance Assessment
Performance is evaluated based on:
* **Results**: Achievement of goals and objectives
* **Behaviors**: Demonstration of required competencies
* **Impact**: Contribution to team and organizational success
* **Consistency**: Reliable performance over time

## Progressive Discipline Framework

{{ company_name }} follows a progressive approach to address performance issues:

### Step 1: Informal Coaching
**Purpose**: Address minor issues before they become significant problems
**Process**:
* Verbal discussion between employee and manager
* Clear identification of performance gap
* Specific improvement expectations and timeline
* Documentation of discussion and agreed actions
* Follow-up within {{ informal_followup|default('1-2 weeks') }}

### Step 2: Verbal Warning
**Purpose**: Formal documentation of performance issues
**Process**:
* Written documentation of performance concerns
* Specific examples and expectations
* Support resources and training offered
* Defined improvement period (typically {{ verbal_warning_period|default('30 days') }})
* Follow-up meeting to assess progress

### Step 3: Written Warning
**Purpose**: Escalation for continued performance issues
**Process**:
* Formal written warning document
* Detailed performance improvement plan
* Specific measurable goals and timelines
* Potential consequences for continued issues
* HR involvement and documentation
* Improvement period (typically {{ written_warning_period|default('60 days') }})

### Step 4: Final Warning/Suspension
**Purpose**: Last opportunity before termination
**Process**:
* Formal final warning with clear consequences
* Possible temporary suspension with or without pay
* Mandatory performance improvement plan
* Daily or weekly check-ins
* Decision point at end of improvement period

### Step 5: Termination
**Purpose**: Separation when improvement is not achieved
**Process**:
* Final decision based on documented performance history
* Separation meeting with HR present
* Final paycheck and benefits information
* Return of company property
* Exit interview and reference procedures

## Performance Improvement Plans (PIPs)

### PIP Structure
A formal Performance Improvement Plan includes:

#### Performance Issues
* Specific performance gaps and examples
* Impact on team, department, and company
* Historical context and previous discussions

#### Improvement Goals
* Specific, measurable objectives
* Clear timelines and milestones
* Observable behaviors and outcomes

#### Support and Resources
* Training and development opportunities
* Additional supervision and mentoring
* Tools, resources, or process changes needed

#### Monitoring and Check-ins
* Regular progress meetings ({{ pip_checkins|default('weekly') }})
* Progress tracking and documentation
* Adjustment of plan as needed

#### Consequences
* Clear statement of potential outcomes
* Timeline for improvement assessment
* Next steps if goals are not met

### PIP Timeline
{% if pip_timeline %}
{{ pip_timeline }}
{% else %}
* **Plan Duration**: Typically {{ pip_duration|default('60-90 days') }}
* **Initial Meeting**: Discussion and plan agreement
* **Progress Check-ins**: Regular status updates and support
* **Mid-Point Review**: Assessment of progress and plan adjustments
* **Final Review**: Determination of successful completion or next steps
{% endif %}

### PIP Success Criteria
A PIP is considered successful when:
* All improvement goals are met or exceeded
* Performance meets job expectations consistently
* Positive feedback from manager and stakeholders
* Sustainable behavior and performance changes

### PIP Extensions
In appropriate circumstances, PIPs may be extended:
* When significant progress is made but full success not achieved
* When external factors impact performance
* When additional time is needed for complex skill development

## Special Circumstances

### New Hire Probation
New employees are subject to probationary periods:
* **Initial Period**: {{ probationary_period|default('90 days') }} for most roles
* **Extended Probation**: Up to {{ extended_probation|default('6 months') }} for complex roles
* **Performance Reviews**: Regular check-ins at {{ probationary_reviews|default('30, 60, 90 days') }}

### Leadership Performance Issues
Performance issues for managers include additional considerations:
* **Team Impact**: Effect on team morale and performance
* **Leadership Standards**: Additional expectations for managers
* **Development Focus**: Emphasis on coaching and leadership skills

### Policy Violations
Separate from performance issues, policy violations follow specific procedures:
* **Minor Violations**: Verbal counseling and training
* **Serious Violations**: Formal disciplinary action up to termination
* **Legal Compliance**: Adherence to employment laws and regulations

## Support During Improvement

### Resources Provided
{{ company_name }} provides comprehensive support during performance improvement:

#### Training and Development
* **Skills Training**: Specific training for performance gaps
* **Mentoring**: Assignment of experienced mentors
* **Job Shadowing**: Observation of high-performing colleagues

#### Managerial Support
* **Regular Feedback**: Frequent check-ins and coaching
* **Resource Allocation**: Additional tools and support needed
* **Process Guidance**: Clear expectations and success criteria

#### HR Support
* **Process Guidance**: Ensuring fair and consistent application
* **Documentation**: Proper record-keeping and communication
* **Additional Resources**: Access to employee assistance programs

### Employee Responsibilities
During improvement periods, employees are expected to:
* **Active Participation**: Engage fully in improvement activities
* **Open Communication**: Discuss challenges and seek help when needed
* **Progress Tracking**: Monitor and report on improvement progress
* **Professional Conduct**: Maintain positive attitude and team relationships

## Documentation and Records

### Performance Records
All performance improvement actions are documented:
* **Discussion Notes**: Records of all conversations and meetings
* **Performance Data**: Metrics and examples supporting concerns
* **Improvement Plans**: Detailed PIPs and progress tracking
* **Outcome Documentation**: Final results and decisions

### Record Retention
{% if retention_policy %}
{{ retention_policy }}
{% else %}
Performance improvement records are retained for {{ retention_period|default('7 years') }} in accordance with legal requirements and company policy.
{% endif %}

### Employee Access
Employees have the right to review their performance records and may request copies for their files.

## Appeals and Dispute Resolution

### Internal Appeals
{% if appeals_process %}
{{ appeals_process }}
{% else %}
Employees may appeal performance improvement decisions by:

1. **Informal Resolution**: Discussion with manager within {{ informal_appeal_window|default('3 business days') }}
2. **HR Review**: Submission of appeal to HR within {{ hr_appeal_window|default('5 business days') }}
3. **Management Review**: Escalation to department leadership if unresolved
4. **Final Decision**: HR determination with executive input if needed
{% endif %}

### External Options
For legal concerns or disputes:
* **Government Agencies**: Contact relevant labor departments
* **Legal Counsel**: Consultation with employment attorney
* **Mediation Services**: Third-party mediation when appropriate

## Confidentiality and Communication

### Confidentiality Requirements
Performance improvement discussions are confidential and limited to:
* Employee and direct manager
* HR representatives as appropriate
* Senior leadership for escalation purposes

### Communication Guidelines
* **Clear and Respectful**: All communications maintain professional tone
* **Fact-Based**: Discussions focus on observable behaviors and outcomes
* **Solution-Oriented**: Emphasis on improvement and support
* **Documented**: All significant discussions are recorded

## Prevention and Early Intervention

### Proactive Measures
{{ company_name }} emphasizes prevention through:
* **Clear Expectations**: Well-defined job requirements and standards
* **Regular Feedback**: Ongoing performance discussions
* **Development Focus**: Continuous skill-building and growth
* **Support Systems**: Resources for work challenges and personal issues

### Early Warning Signs
Managers should address potential issues early:
* **Communication Gaps**: Lack of progress updates or responsiveness
* **Quality Issues**: Declining work quality or missed deadlines
* **Behavioral Changes**: Attitude or engagement shifts
* **Peer Feedback**: Concerns raised by colleagues or team members

## Employee Assistance

### Support Resources
During performance improvement, employees have access to:
* **Employee Assistance Program**: Counseling and support services
* **Work-Life Resources**: Help with personal or work-life challenges
* **Career Counseling**: Guidance on career transition if needed
* **Legal Consultation**: Advice on employment rights and options

### Wellness Considerations
Performance issues may sometimes stem from:
* **Health Concerns**: Medical or mental health issues
* **Personal Challenges**: Family or life circumstances
* **Work Environment**: Team dynamics or role fit issues
* **Skill Gaps**: Lack of training or experience

## Questions and Support

For questions about performance improvement procedures, please contact {% if hr_contact_name %}{{ hr_contact_name }}{% else %}Human Resources{% endif %}{% if hr_contact_email %} at {{ hr_contact_email }}{% endif %}{% if hr_contact_phone %} or call {{ hr_contact_phone }}{% endif %}.

{% if support_resources %}
**Additional Support Resources**:
{{ support_resources }}
{% endif %}

Last Updated: {{ last_updated|default('January 1, 2024') }}
