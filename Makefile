

install:
	pip3 install --user -e . --no-deps

test:
	python3 -m unittest -v --failfast cocomoco/tests/tests.py

lint:
	pylint3 --disable=too-many-instance-attributes cocomoco/cocomoco.py

setup:
	python3 setup.py sdist
	python3 setup.py bdist_wheel --universal

upload: setup
	twine upload dist/*

bootstrap:
	python3 -m pip install --user --upgrade setuptools wheel twine

really-clean:
	git clean -fdx
