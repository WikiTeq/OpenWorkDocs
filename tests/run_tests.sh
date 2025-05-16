#!/bin/bash
# Helper script to run all tests and validations

# Run template validation
echo "Validating templates..."
python templates/validate_templates.py || exit 1

# Run unit tests
echo "Running unit tests..."
pytest -xvs tests/ || exit 1

# Run test generation
echo "Testing document generation..."
python templates/generate.py --config tests/fixtures/sample_config.yaml --output tests/fixtures/output --debug || exit 1

echo "All tests passed!"
