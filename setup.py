#!/usr/bin/env python

from distutils.core import setup
from glob import glob
from setuptools import find_packages

setup(name='Factorial',
	version='1.0',
	author='Ethan Hansen',
	packages=find_packages('src'),
	package_dir={'': 'src'},
	py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
	)