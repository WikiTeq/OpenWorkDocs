# {{ company_name }} Remote Work Security Guidelines

## Introduction

Remote work introduces unique security challenges. This document outlines security requirements and best practices for safeguarding {{ company_name }}'s data, systems, and information when working remotely.

## General Security Principles

All remote workers must follow these security principles:

* Apply the same security standards remotely as you would in an office environment
* Assume personal responsibility for protecting company assets and information
* Report security incidents immediately
* Stay informed about evolving security threats and protocols

## Device Security

### Company-Provided Devices

{% if company_devices|default(true) %}
When using company-provided equipment:

* Do not allow others to use your company-issued devices
* Keep operating systems and software updated with required security patches
* Do not install unauthorized software without IT approval
* Enable automatic screen locks after {{ screen_lock_time|default('5') }} minutes of inactivity
* Use company-provided antivirus and security software
{% endif %}

### Personal Devices (BYOD)

{% if byod_allowed|default(true) %}
If using personal devices for work (BYOD):

* Ensure devices meet minimum security requirements specified by IT
* Install required security software provided by {{ company_name }}
* Keep personal devices updated with the latest security patches
* Use separate user accounts for work and personal activities when possible
* Understand that {{ company_name }} may require certain management tools on personal devices used for work
{% else %}
{{ company_name }} does not permit the use of personal devices for company work.
{% endif %}

## Network Security

### Internet Connection

* Use secure, password-protected Wi-Fi networks
* Avoid using public Wi-Fi for sensitive work; use a company-provided VPN when working from public locations
* Consider using a dedicated network or VLAN for work devices when possible
* Ensure your home router has a strong password and firmware updates applied

### VPN Usage

{% if vpn_required|default(true) %}
* Always connect to the company VPN when accessing company resources
* Follow proper VPN connection and disconnection procedures
* Report VPN connection issues immediately to IT
{% endif %}

## Data Protection

### Confidential Information

* Be mindful of screen privacy in public or shared spaces
* Use privacy screens when working in public areas
* Log out of sensitive systems when stepping away from your device
* Dispose of printed confidential materials by shredding
* Do not download sensitive data to local devices unless absolutely necessary and authorized

### File Storage and Sharing

* Store work files only in approved company repositories ({{ approved_storage|default('company cloud storage') }})
* Do not use unauthorized cloud storage or file-sharing services
* Encrypt sensitive files when appropriate
* Limit sharing permissions to only those who require access

## Password and Authentication Security

* Use strong, unique passwords for all work accounts
* Enable multi-factor authentication (MFA) for all supported systems
* Do not share passwords or authentication credentials
* Use the company-approved password manager for secure credential storage
* Lock devices when not in use

## Physical Security

* Secure devices when not in use, even at home
* Do not leave company devices unattended in vehicles or public places
* Report lost or stolen devices immediately to {{ security_contact|default('IT and your manager') }}
* Consider the physical security of papers and documents containing company information
* Be aware of your surroundings when discussing sensitive information

## Meeting and Communication Security

* Verify participants before discussing sensitive information in virtual meetings
* Do not record meetings unless necessary and authorized
* Be careful about screen sharing and what may be inadvertently displayed
* Use waiting rooms or passwords for sensitive virtual meetings
* Verify email recipients before sending sensitive information

## Incident Reporting

If you experience a security incident or suspect a security breach:

1. Contact {{ security_incident_contact|default('the IT Security team') }} immediately at {{ security_email|default('security@company.com') }}
2. Document what happened and any actions taken
3. Follow instructions provided by the security team
4. Do not attempt to investigate or remediate serious security incidents on your own

## Compliance and Auditing

* Remote devices may be subject to security auditing and monitoring
* Compliance with these guidelines is mandatory for all remote workers
* Failure to follow security guidelines may result in revocation of remote work privileges or other disciplinary action

## Training and Awareness

{{ company_name }} provides regular security training for remote workers. All remote employees must:

* Complete required security awareness training
* Stay informed about updated security policies and procedures
* Participate in security drills and testing as required

Last Updated: {{ last_updated|default('January 1, 2024') }}
