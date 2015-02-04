#!/bin/sh

VERSION=`python setup.py version`

echo "# Releasing ElasticMapping v$VERSION..."

echo "# Doing git..."
git tag -a v$VERSION -m v$VERSION
git push --tags

echo "# Doing pypi..."
python sdist upload

echo "# Released!"