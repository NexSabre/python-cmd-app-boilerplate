# Python CMD Application Boilerplate
This is boilerplate for python application which should work in thru the command line.

## How to build 
To build application as the [wheel package](https://pythonwheels.com/) you need a `wheel` package. 

### Prerequisite
You can install it thru PiP:
`pip install setuptools wheel`

### Building a wheel
Type a command:
`python setup.py sdist bdist_wheel`

### Installation of the build package
To install a build package, type: 
`pip install dist/python-cmd-app-boilerplate-0.1-py3-none-any.whl`

In the `dist` directory upper command create `.tar.gz` and `.whl` files.
