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
    packages=["spectre"],
    include_package_data=True,
    license="MIT LICENSE",
    zip_safe=False,
    keywords="django-spectre",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
    ],
)
