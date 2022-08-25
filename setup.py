# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in dossier/__init__.py
from dossier import __version__ as version

setup(
	name='dossier',
	version=version,
	description='dossier moto',
	author='nassim',
	author_email='sebbaghnassim@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
