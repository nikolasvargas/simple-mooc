#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from setuptools import find_packages, setup

CURRENT_PYTHON_VERSION = sys.version_info[:2]
REQUIRED_PYTHON_VERSION = (3, 5)

if CURRENT_PYTHON_VERSION < REQUIRED_PYTHON_VERSION:
    sys.stderr.write("""
==========================
Unsupported Python version
==========================

This version of Django requires Python {}.{}, but you're trying to install it on Python {}.{}
""".format(*(REQUIRED_PYTHON_VERSION + CURRENT_PYTHON_VERSION)))
    sys.exit(1)


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name='Simple MOOC',
    version='0.1dev',
    python_requires='>={}.{}'.format(*REQUIRED_PYTHON_VERSION),
    author="Níkolas Vargas",
    author_email='vargasnikolass@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['Django', 'flake8', 'Pillow'],
    long_description=read('README.md')
)
