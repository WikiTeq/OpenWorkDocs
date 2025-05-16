#!/usr/bin/env python3
"""
OpenWorkDocs template validator
Checks for Jinja2 syntax errors in module templates
"""

import os
import sys
import argparse
from pathlib import Path
import jinja2
from jinja2 import Environment, FileSystemLoader

def validate_template(file_path):
    """Validate a single template file for Jinja2 syntax errors"""
    try:
        with open(file_path, 'r') as f:
            template_content = f.read()

        # Try to parse the template
        env = Environment(loader=FileSystemLoader("."))
        env.from_string(template_content)
        return True
    except jinja2.exceptions.TemplateSyntaxError as e:
        print(f"Syntax error in {file_path}:")
        print(f"  Line {e.lineno}: {e.message}")
        return False
    except Exception as e:
        print(f"Error validating {file_path}: {e}")
        return False

def validate_directory(directory):
    """Validate all markdown files in a directory and subdirectories"""
    success = True
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                if not validate_template(file_path):
                    success = False
    return success

def main():
    parser = argparse.ArgumentParser(description='Validate Jinja2 templates in Markdown files')
    parser.add_argument('--modules-dir', default='modules', help='Directory containing document modules')
    args = parser.parse_args()

    if not os.path.exists(args.modules_dir):
        print(f"Error: Directory {args.modules_dir} not found")
        sys.exit(1)

    print(f"Validating templates in {args.modules_dir}...")
    if validate_directory(args.modules_dir):
        print("✓ All templates validated successfully")
        sys.exit(0)
    else:
        print("✗ Validation failed. Please fix the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
