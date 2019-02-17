# Img2sh

Img2sh is a tool to show images directly on terminal.
For color images 256 xterm color support is required. This script basically resize the image with antialliasing and quantized its colors to xterm color pallette.


### Demo

```
img2sh demo.jpeg
```

Result:

![](https://user-images.githubusercontent.com/13440502/52919655-aa89d400-3315-11e9-8c4a-7a7e057b8fa4.png)


```
usage: img2sh [-h] [-w WIDTH] Image

Show images directly on terminal.

positional arguments:
  Image

optional arguments:
  -h, --help            show this help message and exit
  -w WIDTH, --width WIDTH
                        image width
```

### Installing

It can be easily install using pip.

```
pip install img2sh --user
```

Installing from source:

```
git clone https://github.com/mozanunal/img2sh
cd img2sh
pip install -r requirements.txt
python setup.py install
```


### Development

#### Setup development environment

Pipenv is using for environment management. 

```
pipenv install --dev
```

Following command should be executed to create interactive shell in this pipenv.
```
pipenv shell
```

#### Development

In this repo issue based development is active. For any problems or new enhancements please open a issue.

Autopep8 is using for formatting.
Pylint is using for linting.

#### Deployment

The following 2 commands are required to deploy over pypi.
```
python setup.py sdist bdist_wheel
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```

### Licence

MIT

### Acknowledges
This package is developed using:
- [Pillow](https://pillow.readthedocs.io/en/stable/installation.html)
- [colored](https://gitlab.com/dslackw/colored)


### Contributors
- [mozanunal](https://github.com/mozanunal)
