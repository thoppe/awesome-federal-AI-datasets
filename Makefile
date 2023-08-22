build:
	python src/build_README.py

lint:
	black --line-length 80 src
	flake8 src
