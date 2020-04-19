# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README') as f:
    readme = f.read()

setup(
    name='limit_handling',
    version='0.0.1',
    description='Backend API responsible for plan based limit handling',
    long_description=readme,
    author='Mate Kapeter',
    url='',
    packages=find_packages(exclude=('tests', 'docs'))
)