.PHONY: help lint test

SRC=./src
TEST_PATH=./tests

.DEFAULT: help
help:
	@echo "make lint"
	@echo "       run pylint and mypy"
	@echo "make test"
	@echo "       run tests"

lint:
	pylint ${SRC}

test:
	py.test --verbose --color=yes $(TEST_PATH)