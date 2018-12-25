import os
import sys

import spectre

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION = spectre.__version__

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name="django-spectre",
    version=VERSION,
    description="""Spectre support for Django project""",
    long_description=readme,
    author="jiaxin",
    author_email="edison7500@gmail.com",
    packages=["bootstrap3"],
    include_package_data=True,
    license="MIT LICENSE",
    zip_safe=False,
    keywords="django-spectre",
)
