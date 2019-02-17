# Img2sh

Img2sh is a tool to show images directly on terminal

### Installing

```
pip install img2sh --user
```

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
```

### Development

#### Setup development environment

Pipenv is using for environment management. 

```
pipenv install --dev
```

```
pipenv shell
```

#### Development

#### Deployment

```
python setup.py sdist bdist_wheel
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```


### Licence

### Acknowledges
This package is developed using:
- [Pillow](https://pillow.readthedocs.io/en/stable/installation.html)
- [colored](https://gitlab.com/dslackw/colored)


### Contributors
- [mozanunal](https://github.com/mozanunal)
