# {{ company_name }} Remote Communication Guidelines

## Introduction

Effective communication is the foundation of successful remote work. This document outlines how {{ company_name }} team members should communicate in a distributed environment to maintain productivity, clarity, and team cohesion.

## Communication Principles

Our remote communication is guided by these core principles:

* **Clarity**: Be specific and provide context in all communications
* **Documentation**: Document important information, decisions, and processes
* **Transparency**: Share information openly while respecting confidentiality requirements
* **Inclusivity**: Ensure all team members can participate regardless of location or time zone
* **Respect for time**: Be mindful of others' working hours and response expectations

## Communication Tools

{{ company_name }} uses the following tools for remote communication:

{% if communication_tools %}
{{ communication_tools }}
{% else %}
* **{{ chat_tool|default('Chat platform') }}**: For quick questions, informal discussions, and real-time collaboration
* **{{ email_system|default('Email') }}**: For formal communications, external correspondence, and non-urgent matters
* **{{ video_platform|default('Video conferencing') }}**: For meetings, interviews, and discussions that benefit from face-to-face interaction
* **{{ project_tool|default('Project management platform') }}**: For task tracking, project updates, and work coordination
* **{{ document_platform|default('Document collaboration') }}**: For collaborative creation and editing of documents
* **{{ knowledge_base|default('Knowledge base') }}**: For documentation, processes, and institutional knowledge
{% endif %}

## Communication Guidelines by Channel

### Chat Communications

* Use status indicators to show your availability
* Create topic-specific channels rather than having all discussions in general channels
* Use threads for detailed discussions to reduce channel noise
* Consider the urgency before tagging someone with @mentions
* {% if do_not_disturb|default(true) %}Respect "Do Not Disturb" status and after-hours boundaries{% endif %}

### Email Guidelines

* Use clear subject lines that indicate purpose and any action required
* Consider who truly needs to be included on emails (To vs. CC)
* Aim for clarity and brevity
* Include expected response times for action items

### Video Meetings

* Share agenda in advance when possible
* Test audio and video before important meetings
* Use video when possible to build connection, unless bandwidth issues occur
* Record important meetings for team members in different time zones (with appropriate notice)
* Always provide meeting notes or summaries for those unable to attend

### Documentation Best Practices

* Document decisions, processes, and important information in {{ knowledge_base|default('our knowledge base') }}
* Follow company templates and documentation standards
* Update documentation regularly to avoid outdated information
* Make documentation accessible to all relevant team members

## Asynchronous vs. Synchronous Communication

{{ company_name }} values efficient communication that respects everyone's time and focus.

### When to Use Asynchronous Communication

* Information sharing that doesn't require immediate feedback
* Updates that can be processed on the recipient's schedule
* Complex topics that benefit from thoughtful response
* Work spanning multiple time zones

### When to Use Synchronous Communication

* Urgent matters requiring immediate attention
* Sensitive discussions that benefit from real-time feedback
* Creative brainstorming and collaborative problem-solving
* Team building and social connections

## Response Time Expectations

{% if response_expectations %}
{{ response_expectations }}
{% else %}
* **Urgent messages**: Within {{ urgent_response_time|default('2-3 hours') }} during working hours
* **Standard messages**: Within {{ standard_response_time|default('24 hours') }}
* **Non-urgent requests**: Within {{ non_urgent_response_time|default('2-3 business days') }}

Team members should communicate proactively if they'll be unavailable or delayed in responding.
{% endif %}

## Time Zone Considerations

{% if global_team|default(true) %}
As a distributed team working across multiple time zones, we:

* Clearly communicate our working hours and availability
* Include time zones when scheduling meetings
* Rotate meeting times to share the burden of early/late meetings
* Record key meetings and provide detailed notes for those unable to attend
* Consider time zone differences when setting deadlines and response expectations
{% endif %}

## Language and Tone

* Be conscious that written communication lacks vocal tone and body language
* Use clear, concise language that minimizes potential misinterpretation
* Consider using emojis or emoticons to convey tone appropriately
* When tensions arise, switch to video or voice communication when possible
* Practice empathy and assume positive intent in all communications

Last Updated: {{ last_updated|default('January 1, 2024') }}
