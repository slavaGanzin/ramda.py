from setuptools import setup
from setuptools.command.build_py import build_py
from subprocess import call
from os import path


class BuildCommand(build_py):
    def run(self):
        build_py.run(self)


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ramda",
    version="0.7.5",
    description="Python clone of ramda.js (ramdajs.com)",
    url="http://github.com/slavaGanzin/ramda.py",
    author="Slava Ganzin",
    author_email="slava.ganzin@gmail.com",
    packages=["ramda", "ramda.private", "ramda.private.curry_spec"],
    install_requires=["toolz"],
    tests_require=["nose2", "coverage", "mock", "six"],
    cmdclass={"build_py": BuildCommand},
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False,
)
