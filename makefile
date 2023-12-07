default:
	@cat makefile

env:
	python3 -m venv env
	. env/bin/activate; pip install -r requirements.txt

#run the file in the bin folder
run:
	@. env/bin/activate; python3 bin/clockdeco_param.py

.PHONY: tests

tests:
	. env/bin/activate; pytest -vv tests


.PHONY: lint

lint:
	pylint bin/perceptron.py
