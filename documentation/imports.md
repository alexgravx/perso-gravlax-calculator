## This document discusses ways to import Python packages.

### Experiment 1
--> The folder_name is DIFFERENT from the module_name in setup.py / pyproject.toml:

- The package should be installed with: `pip install <module_name>`
- The package should be imported with:  `from <folder_name> import <xxx>` or `import <folder_name>`

*Note*: `from <package_name> import <xxx>` does not work !
**The best practice is to name the module_name exactly as folder_name**, as written in the documentation: "The directory containing the Python files should match the project name. This simplifies the configuration and is more obvious to users who install the package."

Two examples: Pillow and scikit-learn:
 - We install Pillow with `pip install Pillow` and we import it with `from PIL import Image`
 - We install scikit-learn with `pip install scikit-learn` and we import it with `import sklearn`. See the
 github repository here: https://github.com/scikit-learn/scikit-learn

### Experiment 2: 
--> The` __init__.py` file is empty
`from gravlax_calculator import main` does not work, because
gravlax_calculator knows only what is inside `__init__.py`

You should get the function in the appropriate file under the package. This works:
```
from gravlax_calculator.calculator import main
main()
```

In the same way, `import gravlax_calculator` does not work, because
gravlax_calculator knows only what is inside `__init__.py`

You should get the function in the appropriate file under the package, like:
```
import gravlax_calculator.calculator as calc
calc.main()
```

### Experiment 3
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
- D'après la documentation: "Vous pouvez vous représenter les paquets comme des répertoires dans le système de fichiers et les modules comme des fichiers dans ces répertoires [...]. Comme les répertoires du système de fichiers, les paquets sont organisés de manière hiérarchique et les paquets peuvent eux-mêmes contenir des sous-paquets ou des modules."
- Lien de la documentation sur les imports: https://docs.python.org/fr/3.13/reference/import.html
