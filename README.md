### Hexlet tests and linter status:
[![Actions Status](https://github.com/GregTMJ/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/GregTMJ/python-project-50/actions)
[![Python CI](https://github.com/GregTMJ/python-project-50/actions/workflows/gendiff-check.yml/badge.svg?branch=main)](https://github.com/Gregtmj/python-project-50/actions/workflows/gendiff-check.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/ef9e0ec11fccc91f442c/maintainability)](https://codeclimate.com/github/GregTMJ/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/ef9e0ec11fccc91f442c/test_coverage)](https://codeclimate.com/github/GregTMJ/python-project-50/test_coverage)

## Getting Started

#### Clone the current repository via command:
```git clone https://github.com/GregTMJ/python-project-50.git```

## Requirements
* python >= 3.7
* Poetry >= 1.14
* make >= 4

#### Check your pip version with the following command:
```python -m pip --version```

#### Make sure that pip is always up to date. If not, use the following:
```python -m pip install --upgrade pip```

#### Next install poetry on your OS. (the link is below)
[Poetry installation](https://python-poetry.org/docs/)
##### don't forget to init poetry packages with command ```poetry init```


## Makefile

#### Using the Makefile you can generate all the needed packages for you virtual environment
```make install``` to install poetry packages. \
```make build``` to build your packages inside your project. \
```make publish``` It will let us execute the publish command knowing exactly what is going into the build. \
```make package-install``` installs the built package from our OS, so we can start using simple shell commands.

#### test your application with the following command```gendiff -h```
##### also don't forget to check the tests inside the folder tests, check if everything works with the command: 
```poetry run pytest```
    
## Animated tests
#### Basic usage
[![asciicast](https://asciinema.org/a/525539.svg)](https://asciinema.org/a/525539)

#### Generating differences in stylish mode
[![asciicast](https://asciinema.org/a/525982.svg)](https://asciinema.org/a/525982)

#### Generating differences in plain mode
[![asciicast](https://asciinema.org/a/525983.svg)](https://asciinema.org/a/525983)

#### Generating differences in json mode
[![asciicast](https://asciinema.org/a/525984.svg)](https://asciinema.org/a/525984)