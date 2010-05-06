#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = '0.3'

#import ez_setup
#ez_setup.use_setuptools()

from setuptools import setup

setup(
  name = "pit",
  version = __version__,
  py_modules = ['pit'],
  author='Yoshiori SHOJI',
  author_email='yoshiori@gmail.com',
  description='pit: account management tool',
  install_requires = ['pyYAML'],
)
