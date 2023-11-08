.PHONE: init run scan

init:
	@echo "Installin Python Poetry and Python dependencies inside a virtual environment"
	curl -sSL https://install.python-poetry.org | python3 -
	poetry env use $(shell which python3.10) && \
	poetry install

run:
	@echo "Running LLM chain"
	poetry run python src/run.py

scan:
	@echo "Running Giskard scan"
	poetry run python src/scan.py	