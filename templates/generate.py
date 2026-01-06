#!/usr/bin/env python3
"""
OpenWorkDocs document generator
Compiles modular document templates based on company configuration
"""

import os
import sys
import yaml
import argparse
import logging
from pathlib import Path
import jinja2
from jinja2 import Environment, FileSystemLoader

def configure_logging(debug=False):
    """Configure logging based on verbosity level"""
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    return logging.getLogger("openworkdocs")

def load_config(config_path):
    """Load and validate the company configuration file"""
    logger = logging.getLogger("openworkdocs")
    try:
        logger.debug(f"Loading configuration from {config_path}")
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)

        # Basic validation
        if 'variables' not in config:
            logger.warning("No variables defined in config")

        if 'policies' not in config:
            raise ValueError("No policies defined in config")

        logger.debug(f"Config loaded successfully with {len(config.get('policies', {}))} policies")
        return config
    except Exception as e:
        logger.error(f"Error loading configuration: {e}")
        raise

def compile_document(policy_name, module_list, variables, modules_dir, output_dir):
    """Compile a single document from its constituent modules"""
    logger = logging.getLogger("openworkdocs")

    # Handle industry documents (single files, not modules)
    if policy_name.startswith('industries/'):
        industry_file = os.path.join(modules_dir, f"{policy_name}.md")
        if not os.path.exists(industry_file):
            logger.warning(f"Industry document {industry_file} not found, skipping")
            return

        # Set up Jinja environment
        env = Environment(loader=FileSystemLoader(modules_dir))

        try:
            template = env.get_template(f"{policy_name}.md")
            rendered_content = template.render(**variables)
        except jinja2.exceptions.TemplateSyntaxError as e:
            logger.error(f"Template syntax error in {policy_name}: Line {e.lineno}: {e.message}")
            return
        except Exception as e:
            logger.error(f"Error rendering {policy_name}: {e}")
            return

        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

        # Write the document (use the last part of the path as filename)
        doc_name = policy_name.split('/')[-1]
        output_path = os.path.join(output_dir, f"{doc_name}.md")
        with open(output_path, 'w') as f:
            f.write(rendered_content)

        logger.info(f"Generated {output_path}")
        return

    # Original logic for regular policy documents
    policy_dir = os.path.join(modules_dir, policy_name)

    # Check if policy directory exists
    if not os.path.exists(policy_dir):
        logger.warning(f"Policy directory {policy_dir} not found, skipping")
        return

    # Collect content from all modules
    combined_content = ""

    for module in module_list:
        module_path = os.path.join(policy_dir, f"{module}.md")

        if not os.path.exists(module_path):
            logger.warning(f"Module {module_path} not found, skipping")
            continue

        logger.debug(f"Loading module {module_path}")
        with open(module_path, 'r') as f:
            module_content = f.read()
            combined_content += module_content + "\n\n"

    # Set up Jinja environment
    logger.debug(f"Setting up Jinja environment for {policy_name}")
    env = Environment(loader=FileSystemLoader("."))

    try:
        template = env.from_string(combined_content)
        logger.debug(f"Template for {policy_name} compiled successfully")
    except jinja2.exceptions.TemplateSyntaxError as e:
        logger.error(f"Template syntax error in {policy_name}: Line {e.lineno}: {e.message}")
        return

    # Render the template with the company variables
    try:
        logger.debug(f"Rendering template for {policy_name}")
        rendered_content = template.render(**variables)
    except Exception as e:
        logger.error(f"Error rendering {policy_name}: {e}")
        return

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Write the compiled document
    output_path = os.path.join(output_dir, f"{policy_name}.md")
    with open(output_path, 'w') as f:
        f.write(rendered_content)

    logger.info(f"Generated {output_path}")

def main():
    parser = argparse.ArgumentParser(description='Generate company documents from templates')
    parser.add_argument('--config', required=True, help='Path to company configuration file')
    parser.add_argument('--output', default='output', help='Output directory for generated documents')
    parser.add_argument('--modules-dir', default='modules', help='Directory containing document modules')
    parser.add_argument('--debug', action='store_true', help='Enable debug logging')
    parser.add_argument('--validate-only', action='store_true', help='Validate templates without generating documents')
    args = parser.parse_args()

    # Configure logging
    logger = configure_logging(args.debug)

    # Validate modules if requested
    if args.validate_only:
        from validate_templates import validate_directory
        if validate_directory(args.modules_dir):
            logger.info("✓ All templates validated successfully")
            sys.exit(0)
        else:
            logger.error("✗ Validation failed")
            sys.exit(1)

    try:
        # Load configuration
        config = load_config(args.config)

        # Check for base commit
        base_commit = config.get('base_commit')
        if base_commit:
            logger.info(f"Using base commit: {base_commit}")
            # Here you would implement git operations to checkout the specified commit

        # Process each policy
        for policy_name, modules in config['policies'].items():
            logger.debug(f"Processing policy: {policy_name} with modules: {modules}")
            compile_document(policy_name, modules, config.get('variables', {}), args.modules_dir, args.output)

        # Process industry-specific documents
        industry = config.get('industry')
        if industry:
            industry_dir = os.path.join(args.modules_dir, 'industries', industry)
            if os.path.exists(industry_dir):
                logger.info(f"Processing industry documents for: {industry}")
                for filename in os.listdir(industry_dir):
                    if filename.endswith('.md'):
                        doc_name = filename[:-3]  # Remove .md extension
                        industry_path = f"industries/{industry}/{doc_name}"
                        logger.debug(f"Processing industry document: {industry_path}")
                        compile_document(industry_path, [], config.get('variables', {}), args.modules_dir, args.output)
            else:
                logger.warning(f"Industry directory {industry_dir} not found")

        logger.info(f"Document generation complete. Files written to {args.output}/")
    except Exception as e:
        logger.error(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
