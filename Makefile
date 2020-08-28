# From: https://github.com/levlaz/circleci.py/blob/master/Makefile

.PHONY: help clean dev package test

help:
	@echo "This project assumes that an active Python virtualenv is present."
	@echo "The following make targets are available:"
	@echo "	 dev 	install all deps for dev env"
	@echo "	 test	run all tests with coverage"

clean:
	rm -rf dist/*

dev:
	pip install --upgrade pip
        pip install coverage
	pip install codecov
	pip install pylint
	pip install twine
	pip install -e .

package:
	python setup.py sdist
	python setup.py bdist_wheel

test:
	coverage run -m unittest discover
