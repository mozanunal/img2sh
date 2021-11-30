# Img2sh

Img2sh is a tool to show images directly on terminal.
For color images 256 xterm color support is required. This script basically resize the image with antialliasing and quantized its colors to xterm color pallette.


### Demo

Testing the package is super easy. Install and run.

```
pip install img2sh --user
img2sh demo.jpeg
```

Result:
 
![](https://user-images.githubusercontent.com/13440502/52919655-aa89d400-3315-11e9-8c4a-7a7e057b8fa4.png) 

<!--![](https://user-images.githubusercontent.com/13440502/59116723-e0020e00-8954-11e9-8d3a-e482ec543368.png)-->

### Demo with interactive mode

```
img2sh demo.jpeg -w 80 -i

q: quit z: zoom+ x: zoom- c: reset 
arrow keys for navigation 
cmd: q
```

![](https://user-images.githubusercontent.com/13440502/59120360-e34dc780-895d-11e9-8b2a-1d7ea5b25fe4.gif)



For detailed usage arguments:

```
$ python img2sh/cli.py --help

usage: cli.py [-h] [-w WIDTH] [-i] Image

Show images directly on terminal.

positional arguments:
  Image                 the directory of the image which will be opened

optional arguments:
  -h, --help            show this help message and exit
  -w WIDTH, --width WIDTH
                        image width on the terminal
  -i, --interactive     open image in interactive mode
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

Conda is using for environment management. 

```
conda create -n img2sh python=3.8
```

Following command should be executed to create interactive shell in this conda environment.
```
conda activate img2sh
```

#### Development

In this repo issue based development is active. For any problems or new enhancements please open a issue.

Autopep8 is used for formatting.
Pylint is used for linting.

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
