#!/usr/bin/env python3
"""
Test suite for OpenWorkDocs document generator
"""

import os
import sys
import unittest
import tempfile
import shutil
from pathlib import Path
import yaml

# Add the project root to the path so we can import the generate module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from templates.generate import load_config, compile_document

class TestConfigLoader(unittest.TestCase):
    """Test the configuration loading functionality"""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_valid_config(self):
        """Test loading a valid configuration file"""
        config_path = os.path.join(self.temp_dir, 'valid_config.yaml')
        with open(config_path, 'w') as f:
            f.write("""
variables:
  company_name: Test Company
policies:
  test_policy:
    - base
""")

        config = load_config(config_path)
        self.assertEqual(config['variables']['company_name'], 'Test Company')
        self.assertIn('test_policy', config['policies'])

    def test_missing_policies(self):
        """Test loading a config with missing policies section"""
        config_path = os.path.join(self.temp_dir, 'invalid_config.yaml')
        with open(config_path, 'w') as f:
            f.write("""
variables:
  company_name: Test Company
""")

        with self.assertRaises(ValueError):
            load_config(config_path)

class TestDocumentCompilation(unittest.TestCase):
    """Test document compilation from modules"""

    def setUp(self):
        self.temp_dir = tempfile.mkdtemp()
        self.modules_dir = os.path.join(self.temp_dir, 'modules')
        self.output_dir = os.path.join(self.temp_dir, 'output')

        # Create test module structure
        os.makedirs(os.path.join(self.modules_dir, 'test_policy'))

        # Create a base module with template variables
        with open(os.path.join(self.modules_dir, 'test_policy', 'base.md'), 'w') as f:
            f.write("# {{ company_name }} Test Policy\n\nThis is a test.")

        # Create an additional module
        with open(os.path.join(self.modules_dir, 'test_policy', 'addon.md'), 'w') as f:
            f.write("\n## Additional Section\n\n{% if feature_enabled %}Feature is enabled.{% else %}Feature is disabled.{% endif %}")

    def tearDown(self):
        shutil.rmtree(self.temp_dir)

    def test_basic_compilation(self):
        """Test basic document compilation"""
        variables = {
            'company_name': 'Test Company'
        }

        compile_document('test_policy', ['base'], variables, self.modules_dir, self.output_dir)

        output_path = os.path.join(self.output_dir, 'test_policy.md')
        self.assertTrue(os.path.exists(output_path))

        with open(output_path, 'r') as f:
            content = f.read()

        self.assertIn('# Test Company Test Policy', content)

    def test_multiple_modules(self):
        """Test compilation of multiple modules into one document"""
        variables = {
            'company_name': 'Test Company',
            'feature_enabled': True
        }

        compile_document('test_policy', ['base', 'addon'], variables, self.modules_dir, self.output_dir)

        output_path = os.path.join(self.output_dir, 'test_policy.md')
        with open(output_path, 'r') as f:
            content = f.read()

        self.assertIn('# Test Company Test Policy', content)
        self.assertIn('## Additional Section', content)
        self.assertIn('Feature is enabled', content)

    def test_conditional_content(self):
        """Test conditional content based on variables"""
        variables = {
            'company_name': 'Test Company',
            'feature_enabled': False
        }

        compile_document('test_policy', ['base', 'addon'], variables, self.modules_dir, self.output_dir)

        output_path = os.path.join(self.output_dir, 'test_policy.md')
        with open(output_path, 'r') as f:
            content = f.read()

        self.assertIn('Feature is disabled', content)

class TestEndToEnd(unittest.TestCase):
    """End-to-end test using fixture files"""

    def setUp(self):
        # Create paths for test fixtures and output
        self.fixtures_dir = os.path.join(os.path.dirname(__file__), 'fixtures')
        self.output_dir = os.path.join(self.fixtures_dir, 'output')

        # Create output directory if it doesn't exist
        os.makedirs(self.output_dir, exist_ok=True)

    def test_sample_config(self):
        """Test using the sample config and real modules"""
        # Skip if fixtures directory doesn't exist
        if not os.path.exists(os.path.join(self.fixtures_dir, 'sample_config.yaml')):
            self.skipTest("Test fixtures not found")

        # This would call the actual generate script
        # Using subprocess to run it as a separate process
        import subprocess
        result = subprocess.run([
            sys.executable,
            os.path.join(os.path.dirname(os.path.dirname(__file__)), 'templates', 'generate.py'),
            '--config', os.path.join(self.fixtures_dir, 'sample_config.yaml'),
            '--output', self.output_dir
        ], capture_output=True, text=True)

        # Check if process was successful
        self.assertEqual(result.returncode, 0, f"Process failed with output: {result.stderr}")

        # Check if expected files were created
        self.assertTrue(os.path.exists(os.path.join(self.output_dir, 'code_of_conduct.md')))

if __name__ == '__main__':
    unittest.main()
