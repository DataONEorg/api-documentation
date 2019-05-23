import os

if os.environ.get("READTHEDOCS") == "True":
  from distutils.core import setup
else:
  from setuptools import setup

