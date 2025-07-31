## Experiment 1 ##
# If the folder name is DIFFERENT from the module name in setup.py:
# The package should be installed with: `pip install <module_name>`
# The package should be imported with:  `from <folder_name> import <xxx>` or `import <folder_name>`
# Note: `from <package_name> import <xxx>` does not work
# The best practice is to name the module_name exactly as folder_name

## Experiment 2 ##
# The __init__.py file is empty
# `from gravlax_calculator import main` does not work
# gravlax_calculator knows only what is inside __init__.py

# You should get the function in the appropriate file under the package
# This works
from gravlax_calculator.calculator import main
main()

## Experiment 3 ##
# The __init__.py file is empty
# `import gravlax_calculator` does not work
# gravlax_calculator knows only what is inside __init__.py

# You should get the function in the appropriate file under the package
# This works
import gravlax_calculator.calculator as calc
calc.main()

## Experiment 4 ##
# The __init__.py file contains `from .calculator import main`

# This works
from gravlax_calculator import main
main()

## Experiment 5 ##
# The __init__.py file contains `from .calculator import main`

# This works
import gravlax_calculator as calc
calc.main()



