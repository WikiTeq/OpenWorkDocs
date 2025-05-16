## Tech-Specific Workplace Expectations

### Open Collaboration Culture

As a technology company, {{ company_name }} values open collaboration and the free exchange of ideas. We expect team members to:

* **Share knowledge freely** while respecting intellectual property rights
* **Document decisions and processes** to maintain institutional knowledge
* **Contribute constructively** to technical discussions and code reviews
* **Practice responsible disclosure** when identifying security vulnerabilities
* **Balance innovation with stability** when suggesting changes to systems

### Digital Communication Guidelines

Our work environment includes significant digital communication. When communicating through digital channels, we expect:

* **Thoughtful messaging**: Consider the appropriate platform for your message (chat vs. email vs. issue tracker)
* **Clear context**: Provide sufficient background information when asking questions or requesting assistance
* **Respectful discourse**: Especially in technical debates, focus on ideas rather than individuals
* **Appropriate response times**: Respect boundaries while maintaining reasonable responsiveness
* **Inclusive language**: Use terminology that is accessible to team members of various backgrounds and experience levels

### Open Source Engagement

{% if open_source_participation|default(true) %}
When participating in open source communities or representing {{ company_name }} in technical forums:

* Follow the respective community's guidelines and codes of conduct
* Clearly distinguish between personal opinions and company positions
* Respect open source licenses and contribution agreements
* Obtain appropriate approvals before contributing company code to open projects
* Represent {{ company_name }} professionally in all public technical discussions
{% endif %}

### Technology Ethics

{{ company_name }} is committed to the ethical development and use of technology:

* Consider the societal impact and potential unintended consequences of our products
* Design systems with privacy, security, and accessibility as core principles
* Raise concerns about potentially harmful applications of our technology
* Refuse to participate in projects that may cause harm or violate our values
* Advocate for responsible data practices and algorithmic fairness

### Remote/Distributed Work Expectations

{% if remote_work|default(true) %}
As a company that embraces remote work, we have additional expectations:

* Maintain appropriate work availability during your designated hours
* Communicate your status and availability clearly to team members
* Create boundaries between work and personal life to prevent burnout
* Participate actively in virtual meetings and discussions
* Proactively build relationships with colleagues despite physical distance
{% endif %}
