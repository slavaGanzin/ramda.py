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
    version='0.2.1',
    description='A Python package for curried functional programming',
    url='http://github.com/slavaGanzin/pyramda',
    author='Slava Ganzin',
    author_email='slava.ganzin@gmail.com',
    packages=[
        'ramda',
    ],
    install_requires=['future'],
    tests_require=['nose', 'coverage', 'mock'],
    cmdclass={
        'build_py': PasteurizeBuildCommand
    },
    zip_safe=False
)
