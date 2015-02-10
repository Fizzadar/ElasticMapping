#!/usr/bin/env python
# ElasticMapping
# File: setup.py
# Desc: needed

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    version='1.0',
    name='ElasticMapping',
    description='A simple mappings builder for Elasticsearch',
    author='Nick Barrett',
    author_email='pointlessrambler@gmail.com',
    url='http://github.com/Fizzadar/ElasticMapping',
    package_dir={
        'ElasticMapping': 'elasticmapping'
    },
    packages=[
        'elasticmapping'
    ]
)
