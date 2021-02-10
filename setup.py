# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in library_system/__init__.py
from library_system import __version__ as version

setup(
	name='library_system',
	version=version,
	description='Alloaction and assign books to students',
	author='Elijah',
	author_email='elaahmuigai@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
