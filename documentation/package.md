## Reminder: library vs package vs module in Python

The terminology may be mixed up in everyday language, 
but the exact correct terminology is:
- module: a python file with some functionnalities: classes, functions, methods, etc;
- package: a directory containing a `__init__.py` file and 1+ modules;
- library: a directory containing a `__init__.py` file, multiple modules AND packages: 1+ packages and 0+ modules; 

When you import something with pip, it is either a package or a library, and
most of the time a package. A library can be seen as a super-package containing other packages.

The order to remember is: **library > package > sub-package > module**

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

*Note*: `import <package>` vs `from <package> import <module>`.
- With `import x` you can refer to thing in x like `x.y`. This form let you rename the import with the keyword `as`.
- With `from x import y` you can refer to things in x directly like `y`. This form *imports the names directly into the local namespace*, but can also create conflicts, and cannot use `reload()`

*Note*: This is a common misconception: these syntaxes both always import the whole module. There is also no performance difference between the two approaches. See for example this detailed SO answer: http://softwareengineering.stackexchange.com/questions/187403/import-module-vs-from-module-import-function