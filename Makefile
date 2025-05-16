.PHONY: test lint validate generate clean

test:
	pytest -xvs tests/

lint:
	flake8 templates/ tests/

validate:
	python templates/validate_templates.py

generate:
	python templates/generate.py --config my_company_config.yaml --output my_docs

test-generate:
	python templates/generate.py --config tests/fixtures/sample_config.yaml --output tests/fixtures/output

clean:
	rm -rf my_docs/ tests/fixtures/output/ __pycache__/ .pytest_cache/ .coverage htmlcov/

coverage:
	pytest --cov=templates tests/ --cov-report=html
	@echo "Open htmlcov/index.html in your browser to view the coverage report"
