validate:
	python src/validate_catalog.py

build: validate
	python src/build_README.py

verify: validate
	python src/build_README.py --check

check-urls:
	python src/validate_catalog.py --check-urls

check-resources:
	python src/validate_catalog.py --check-resources

supplement:
	python src/supplement_datasets.py

test:
	python -m unittest discover -s tests

lint:
	black --line-length 80 src
	flake8 src

add:
	python src/add_dataset.py
