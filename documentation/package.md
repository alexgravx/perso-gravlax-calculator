# Python packages

There are some confusions in the terminology. To understand the differences
between module, package and library, see terminology.md 

About how to import a Python package, see imports.md

## Regular vs namespace packages

Python 3.3+ supports Implicit Namespace Packages that allows it to create a package without an `__init__.py` file. This is called a namespace package in contrast to a regular package which does have an `__init__.py` file (empty or not empty).

However, creating a namespace package should ONLY be done if there is a need for it. For most use cases and developers out there, this doesn't apply so you should stick with EMPTY `__init__.py` files regardless.

### Namespace package usecase

To demonstrate the difference between the two types of python packages, lets look at the following example:
```
google_pubsub/              <- Package 1
    google/                 <- Namespace package (there is no __init__.py)
        cloud/              <- Namespace package (there is no __init__.py)
            pubsub/         <- Regular package (with __init__.py)
                __init__.py <- Required to make the package a regular package
                foo.py

google_storage/             <- Package 2
    google/                 <- Namespace package (there is no __init__.py)
        cloud/              <- Namespace package (there is no __init__.py)
            storage/        <- Regular package (with __init__.py)
                __init__.py <- Required to make the package a regular package
                bar.py
```

Only skip `__init__.py` files if you want to create namespace packages. Only create namespace packages if you have different libraries that reside in different locations and you want them each to contribute a subpackage to the parent package, i.e. the namespace package.

Keep on adding empty `__init__.py` to your directories because 99% of the time you just want to create regular packages. Also, Python tools out there such as mypy and pytest require empty `__init__.py` files to interpret the code structure accordingly. This can lead to weird errors if not done with care.

See SO post: https://stackoverflow.com/questions/37139786/is-init-py-not-required-for-packages-in-python-3-3

## Building a regular package

### With setup.py (legacy)

```
from setuptools import setup, find_packages

setup(
    name="gravlax_calculator",                        ---> name of the package
    version="1.0",
    packages=find_packages(),                         ---> find subfolders with __init__.py
    entry_points={                                    ---> creation of a CLI
        "console_scripts": [
            "gravlax-calc = calculator:main"
        ]
    }
)
```

OR

```
setup(
    name="gravlax_calculator",                        ---> name of the package
    version="1.0",
    py_modules=["calculator"]                         ---> name of the python file at same level of setup.py 
)
```

Then launch:
- `python3 setup.py bdist_wheel` to build the package
- `pip install ./dist/*.whl` to install the package

### With pyproject.toml

```
[project]
name = "gravlax_calculator"
version = "1.1"

[build-system]
requires = ["setuptools >= 77.0.3"]
build-backend = "setuptools.build_meta"
```

Then launch:
- `python3 -m build` to build the package
- `pip install ./dist/*.whl` to install the package

## Uploading a package

Create an account on pypi. 
You can then upload a package on PyPi with theses commands:
```
python3 -m pip install --upgrade twine
python3 -m twine upload dist/*
```

## Documentation

More informations here: https://packaging.python.org/en/latest/tutorials/packaging-projects/