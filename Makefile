build:
	python src/supplement_datasets.py
	python src/build_README.py
	make lint

lint:
	black --line-length 80 src
	flake8 src

add:
	python src/add_dataset.py
