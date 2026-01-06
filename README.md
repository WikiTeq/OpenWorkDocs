# OpenWorkDocs

OpenWorkDocs is an open-source document generation system for creating customizable company documents including policies, standard operating procedures (SOPs), and guidelines from modular templates.

## Overview

This repository provides a framework to generate company documents using:

- Modular document components that can be assembled based on your needs
- Configuration-based customization without requiring code modifications
- Jinja2 templating for dynamic content based on company variables
- Comprehensive testing to ensure document integrity

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/OpenWorkDocs.git
cd OpenWorkDocs
```

2. Create a virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Quick Start

1. Create your company configuration file (or modify the example):
```bash
cp templates/company_config.yaml my_company_config.yaml
```

2. Edit `my_company_config.yaml` with your company details and preferred modules

3. Generate your documents:
```bash
python templates/generate.py --config my_company_config.yaml --output my_docs
```

4. Find your generated documents in the `my_docs` directory

### Command Line Options

```
python templates/generate.py --help
```

Available options:
- `--config`: Path to company configuration file (required)
- `--output`: Directory to write generated documents (default: 'output')
- `--modules-dir`: Directory containing document modules (default: 'modules')
- `--debug`: Enable debug logging
- `--validate-only`: Validate templates without generating documents

## Configuration

The configuration file controls which documents are generated and what variables are used in templates:

```yaml
# Company variables for template substitution
variables:
  company_name: "Acme Tech"
  hr_contact_email: "hr@acme-tech.com"
  last_updated: "February 15, 2024"
  remote_work: true
  open_source_participation: true

# Policies to generate and their constituent modules
policies:
  code_of_conduct:
    - base
    - tech_company
    - us_specific

  benefits:
    - base
    - health_insurance
    - financial_benefits
```

### Available Modules

Each policy type has multiple modules that can be included:

- **code_of_conduct**: base, tech_company, us_specific
- **benefits**: base, health_insurance, financial_benefits, time_off, workplace_perks
- **dress_code**: base, software_developer, customer_support, sales_staff, design_team, marketing_team, product_management, executive_leadership, human_resources, it_operations
- **remote_work**: base, communication, home_office, security, work_life_balance
- **recruitment**: base, job_posting_templates, interview_process, background_checks, offer_letters
- **performance_management**: base, goal_setting, performance_reviews, development_plans, performance_improvement

## Template Validation

To validate templates without generating documents:

```bash
python templates/validate_templates.py
```

or

```bash
python templates/generate.py --validate-only
```

## Testing

Run the test suite:

```bash
./tests/run_tests.sh
```

Or run specific test components:

```bash
make validate  # Validate template syntax
make test      # Run unit tests
make coverage  # Generate test coverage report
```

## Project Structure

```
OpenWorkDocs/
├── modules/               # Document module templates
│   ├── benefits/          # Benefits policy modules
│   ├── code_of_conduct/   # Code of conduct modules
│   ├── dress_code/        # Dress code modules
│   └── remote_work/       # Remote work policy modules
├── templates/             # Generation and utility scripts
├── tests/                 # Test files and fixtures
└── my_docs/               # Generated documents (default output)
```

## Contributing

Contributions are welcome! To contribute:

1. Ensure your templates validate with the validation tool
2. Run the test suite to ensure everything works
3. Follow Jinja2 best practices for template creation

## License

This project is licensed under [INSERT LICENSE] - see the LICENSE file for details.

## Acknowledgments

- Built with [Jinja2](https://jinja.palletsprojects.com/) templating engine
- Inspired by the need for customizable, reusable company documentation
