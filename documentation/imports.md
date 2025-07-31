## This document discusses ways to import Python packages.

### Module name and directory name

--> The folder_name is DIFFERENT from the module_name in setup.py / pyproject.toml:

- The package should be installed with: `pip install <module_name>`
- The package should be imported with:  `from <folder_name> import <xxx>` or `import <folder_name>`

*Note*: `from <package_name> import <xxx>` does not work !
**The best practice is to name the module_name exactly as folder_name**, as written in the documentation: "The directory containing the Python files should match the project name. This simplifies the configuration and is more obvious to users who install the package."

Two examples: Pillow and scikit-learn:
 - We install Pillow with `pip install Pillow` and we import it with `from PIL import Image`
 - We install scikit-learn with `pip install scikit-learn` and we import it with `import sklearn`. See the
 github repository here: https://github.com/scikit-learn/scikit-learn

### What is `__init__.py` file ?

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

*Notes*:
- According to the documentation: "Vous pouvez vous représenter les paquets comme des répertoires dans le système de fichiers et les modules comme des fichiers dans ces répertoires [...]. Comme les répertoires du système de fichiers, les paquets sont organisés de manière hiérarchique et les paquets peuvent eux-mêmes contenir des sous-paquets ou des modules."
- Link of the documentation about imports: https://docs.python.org/fr/3.13/reference/import.html

### Basic import: what you can do without `__init__.py`

Python can import files and function without the need to use `__init__.py`.
Let's suppose we have the following tree:

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
To do this, we would need to create a package and add a `__init__.py` file in the package folder.

Example of `__init__.py` file:
```
__all__ = ["second", "third"] --> to specify which modules / files to import with *
from .second import function
from .third import another_function
```
