#!/usr/bin/env python

import sys

import subprocess
from setuptools import setup
from distutils.command.build import build
from distutils.command.clean import clean


class Build(build):
    def run(self):
        if subprocess.call(["make"]) != 0:
            sys.exit(-1)


class Clean(clean):
    def run(self):
        if subprocess.call(["make", "clean"]) != 0:
            sys.exit(-1)


class FClean(clean):
    def run(self):
        if subprocess.call(["make", "fclean"]) != 0:
            sys.exit(-1)


class Rebuild(FClean, Build):
    def run(self):
        if subprocess.call(["make", "re"]) != 0:
            sys.exit(-1)

setup(
    name='motion detector optimization',
    packages=['opti_module'],
    cmdclass={
        'build': Build,
        'clean': Clean,
        'fclean': FClean,
        'rebuild': Rebuild
    }
)
