from setuptools import setup, find_packages

setup(
    name="gravlax_calculator",
    version="1.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "gravlax-calc = gravlax_calculator:main"
        ]
    }
)