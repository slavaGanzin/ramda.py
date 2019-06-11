from setuptools import setup
from setuptools.command.build_py import build_py
from subprocess import call


class PasteurizeBuildCommand(build_py):
    def run(self):
        call(["pip", "install", "future"])
        call(["pasteurize", "./ramda"])
        build_py.run(self)


setup(
    name='ramda',
    version='0.5.1',
    description='Python clone of ramda.js (ramdajs.com)',
    url='http://github.com/slavaGanzin/ramda.py',
    author='Slava Ganzin',
    author_email='slava.ganzin@gmail.com',
    packages=[
        'ramda',
        'ramda.private',
        'ramda.private.curry_spec',
    ],
    install_requires=['future'],
    tests_require=['nose', 'coverage', 'mock'],
    cmdclass={
        'build_py': PasteurizeBuildCommand
    },
    zip_safe=False
)
