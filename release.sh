#!/usr/bin/env sh

rm -rf dist build ramad.egg-info
python3 setup.py sdist bdist_wheel
python3 -m twine  upload  dist/* --skip-existing -u slavaGanzin

