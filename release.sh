#!/usr/bin/env sh

rm -rf dist build ramad.egg-info
python3 setup.py sdist bdist_wheel
twine  upload  dist/* --skip-existing -u slavaGanzin
sudo pip3 install --upgrade --ignore-installed ramda
