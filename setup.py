from setuptools import setup, find_packages

setup(
    name="gravlax_calculator",
    version="1.0",
    py_modules=["calculator"],
    entry_points={
        "console_scripts": [
            "gravlax-calc = calculator:main"
        ]
    }
)