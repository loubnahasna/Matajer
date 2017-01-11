# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from pip.req import parse_requirements
import re, ast

# get version from __version__ variable in matajer/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('matajer/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

requirements = parse_requirements("requirements.txt", session="")

setup(
	name='matajer',
	version=version,

	description='orders and products',
	author='loubna',
	author_email='loubna.hasna@exa.com.sa',

)
