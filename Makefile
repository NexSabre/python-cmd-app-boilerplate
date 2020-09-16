clean:
	rm -rf src/dist/ src/build src/python_cmd_app_boilerplate

build: clean
	python setup.py sdist bdist_wheel
