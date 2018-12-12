#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

from setuptools import setup
from setuptools.command.install import install

VERSION = "1.0.4"

def readme():
    """print long description"""
    with open('README.md') as f:
        return f.read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != VERSION:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, VERSION
            )
            sys.exit(info)

setup(
    name='teleinfo',
    version=VERSION,
    url='http://github.com/demikl/python-teleinfo',
    author='Mickael Le Baillif',
    author_email='mickael.le.baillif@gmail.com',
    license='MIT',
    description='EDF Teleinfo frame acquisition',
    long_description=readme(),
    packages=['teleinfo'],
    install_requires=['pyserial'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Topic :: Home Automation",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    entry_points= {
        'console_scripts': [
            'teleinfo_json=teleinfo.utils:frame_to_json'
        ]
    },
    cmdclass={
        'verify': VerifyVersionCommand,
    }
)
