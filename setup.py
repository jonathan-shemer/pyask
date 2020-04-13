#!/usr/bin/env python

from os.path import exists

from setuptools import setup

setup(name='pyask',
      version='0.2.2',
      description='A set of pure utility methods for python.',
      url='https://github.com/jonathan-shemer/pyask',
      license='MIT',
      author='Jonathan Shemer',
      keywords='pure utility methods for python',
      packages=['pyask'],
      long_description=(open('README.md').read() if exists('README.md') else ''),
      long_description_content_type='text/markdown',
      python_requires=">=3.7",
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Programming Language :: Python :: Implementation :: CPython",
          "Programming Language :: Python :: Implementation :: PyPy"])
