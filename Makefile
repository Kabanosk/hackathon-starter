.PHONY: lint black isort pylint

lint: black isort pylint

black:
	@echo "LINTING WITH BLACK"
	@poetry run black .

isort:
	@echo "LINTING WITH ISORT"
	@poetry run isort .

pylint:
	@echo "LINTING WITH PYLINT"
	@poetry run pylint --recursive y .
