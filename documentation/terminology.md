# Terminology reminder: library vs package vs module in Python

The terminology may be mixed up in everyday language, 
but the exact correct terminology is:
- module: a python file with some functionnalities: classes, functions, methods, etc;
- package: a directory containing modules;
- library: a directory containing multiple packages and possibly modules;

As written in the documentation: "You can think of packages as the directories on a file system and modules as files within directories. It’s important to keep in mind that all packages are modules, but not all modules are packages. Or put another way, packages are just a special kind of module that contains a __path__ attribute."

*Notes*: 
- Packages and libraries used to contain a `__init__.py` file, 
but it's not necessary anymore in recent versions of Python (3.3+). It is
however recommended to use an empty init file to create a "regular package".
- When you import something with pip, it is either a package or a library, and
most of the time a package. A library can be seen as a super-package containing other packages.
- The order to remember is: **library > package > sub-package > module**

## A concrete example:

Here is a concrete example:
```
.
├── main.py                     --> script
└── MyLib                       --> library
    ├── __init__.py
    ├── Package1                --> package
    │   ├── __init__.py
    │   ├── module1.py          --> module
    │   └── module2.py          
    ├── Package2
    │   ├── __init__.py
    │   └── module3.py
    ├── Package3
    │   ├── __init__.py
    │   └── module4.py
    └── some_module.py
```

Examples: 
- matplotlib is a library
- numpy is a library

## Imports in python script

The imports work as follow:
```
import MyLib                                --> import library
from MyLib import Package1                  --> import package
from MyLib.Package1 import module1          --> import module
from MyLib.Package1.module1 import main     --> import function
```

*Note*: for more informations, see immports.md