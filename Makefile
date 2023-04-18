install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	sudo apt-get update && sudo apt-get install libgl1 -y

format:
	black *.py

test:
	python -m pytest -vv test/test-*.py

lint:
	pylint --disable=R,C *.py

all: install test format lint