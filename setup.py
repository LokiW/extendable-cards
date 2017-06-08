#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='extendable-cards',
      version='1.0',
      description='Playing card representation program',
      author='Loki White',
      author_email='loki.w.white@gmail.com',
      url='https://github.com/LokiW/extendable-cards',
      packages=find_packages(),
      setup_requires=["pytest-runner"],
      tests_requires=["pytest"]
    )

