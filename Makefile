install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	sudo apt-get update && sudo apt-get install libgl1 -y

format:
	black *.py
	black test/*.py

lint:
	pylint --disable=R,C *.py
	pylint --disable=R,C test/*.py

check:
	pytest test/test-sample.py
	pytest test/test-cluster.py


all: install format lint check