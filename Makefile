PROJECT_NAME:=base_ontology
EXECUTER:=uv run

all: format lint 
clean:
	rm -rf .mypy_cache .pytest_cache .coverage htmlcov

format:
	$(EXECUTER) ruff format .

lint:
	$(EXECUTER) ruff check . --fix
	$(EXECUTER) mypy .

