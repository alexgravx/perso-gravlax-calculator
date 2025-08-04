# This document discusses ways to import Python packages.

## Module name and directory name

--> The folder_name is DIFFERENT from the module_name in setup.py / pyproject.toml:

- The package should be installed with: `pip install <module_name>`
- The package should be imported with:  `from <folder_name> import <xxx>` or `import <folder_name>`

*Note*: `from <package_name> import <xxx>` does not work !
**The best practice is to name the module_name exactly as folder_name**, as written in the documentation: "The directory containing the Python files should match the project name. This simplifies the configuration and is more obvious to users who install the package."

Two examples: Pillow and scikit-learn:
 - We install Pillow with `pip install Pillow` and we import it with `from PIL import Image`
 - We install scikit-learn with `pip install scikit-learn` and we import it with `import sklearn`. See the
 github repository here: https://github.com/scikit-learn/scikit-learn

 ## Import syntax

--> `import <package>` vs `from <package> import <module>`:
- With `import x` you can refer to thing in x like `x.y`. This form let you rename the import with the keyword `as`.
- With `from x import y` you can refer to things in x directly like `y`. This form *imports the names directly into the local namespace*, but can also create conflicts, and cannot use `reload()`

*Note*: This is a common misconception: these syntaxes both always import the whole module. There is also no performance difference between the two approaches. See for example this detailed SO answer: http://softwareengineering.stackexchange.com/questions/187403/import-module-vs-from-module-import-function

## The `__init__.py` file

The `__init__.py` file is used inside a Python package. But it is not necessary since Python 3.3+ !!
`__init__.py` initialize the package by running some code the first time the package is imported.

It allows you for example to:
- simplify the imports of different components, dependencies or functions into the namespace with `from .file import function`
- adjust certain features such as `from package import *` with `__all__`attribute

*Note*: anything defined in the init file, even a variable, can be directly imported when you import the package.

### If the file is empty

--> The` __init__.py` file is empty

`from gravlax_calculator import main` does not work, because
main was not imported in the namespace via `__init__.py`
You should get the function in the appropriate file under the package. This works:
```
from gravlax_calculator.calculator import main
main()
```

In the same way, `import gravlax_calculator` does not work.
You should get the function in the appropriate file under the package. This works:
```
import gravlax_calculator.calculator as calc
calc.main()
```

*Note*: since Python 3.3, you don't need to use an empty `__init__.py` file to create a package.
You can create what is called a "namespace package". However, an empty init file is still recommended and will create a "regular package". See SO post here: https://stackoverflow.com/questions/37139786/is-init-py-not-required-for-packages-in-python-3-3

### If the file contains imports

--> The `__init__.py` file contains `from .calculator import main`

This works:
```
from gravlax_calculator import main
main()
```
and this works too:
```
import gravlax_calculator as calc
calc.main()
```

## Relative imports, absolute imports and errors

*Warning*: depending on where you run the code, the import is gonna work differently.
Here is an example with the following filestructure:

```
.
├── main.py
└── gravlax_calculator
    ├── __init__.py
    └── calculator.py
```

The main file contains:
```
from gravlax_calculator import main
main()
```

The init file can contain different types of import:

1) Absolute import: `from calculator import main`

Running from the main file raise an *error* because calculator is not 
accessible from the root of the filestructure described above.

*Note*: to avoid an error, we should use relative import or add the PYTHONPATH variable

2) Relative import: `from .calculator import main`

The relative import means we are looking for the module in the current package.
We can now run the main file without *errors*. **This is the best option for init file.**

`.` means actual module and `..` means parent module. Thus, we can import another
submodule from a subpackage with `from ..parent.supackage import submodule`

*Notes*: 
- Warning: relative import work only in regular package (with init file) !!!
- We cannot run directly the init file because it doesn't see any other init file, 
so doesn't know it is in a regular package: "no known parent package".
We should use absolute import or use `if __name__ == "__main__"`.

## PYTHONPATH variable

The variable PYTHONPATH is an environment variable which you can set to add additional directories where python will look for modules and packages. This variable is not set by default and not needed for Python to work because it it already knows where to find its standard libraries through **system path** (sys.path).

You can look to system path with the following code:
```
import sys
for i in sys.path:
    print(i)
```

The PYTHONPATH variable is useful if you want to use absolute imports and you are in a subpackage, 
to extend the points where Python will look for packages. Here is an example:
```
.
└── MyProject
    ├── App
    │   └── app.py   
    └── Package
        └── module.py
```

If we want to import module in `app.py`, we can either:
- Use relative import with `from ..myproject.package import module`, but this needs to have init files.
- Use absolute import with `from package import module` (no need to use init files).
Add the PYTHONPATH with:
    - `export PYTHONPATH='.'` in MyProject;
    - `export PYTHONPATH='/Users/.../MyProject'` from anywhere;

You can then look the updated sys.path

## Basic import without `__init__.py`

Python can import files and functions without the need to use `__init__.py`,
through what is called "namespace packages". Let's suppose we have the following tree:

```
.
├── main.py
├── functionnality.py
└── package
    ├── subpackage
    │   └── fourth.py          
    ├── second.py
    └── third.py
```

In `main.py`, we can do:
```
from functionnality import *
from functionnality import function
from package import second
from package.second import *
from package.second import function
```
But we cannot do:
```
from package import *
```
To do this, we would need to create a regular package 
and add a `__init__.py` file in the package folder.

Example of `__init__.py` file:
```
__all__ = ["second", "third"] --> to specify which modules / files to import with *
from .second import function
from .third import another_function
```

*Note*: there is no need to pip install a package to import it if you have the source code alongside. It is however recommended to install and import it properly. We can make an editable import with `pip install -e`

## Documentation

Link of the documentation about imports: https://docs.python.org/fr/3.13/reference/import.html
