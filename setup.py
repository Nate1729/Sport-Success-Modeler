"""Setup file.
"""

from setuptools import setup, find_packages

# Read contents of README.md file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    README = f.read()

with open('sport_sucess_modeler/core/VERSION') as version_file:
    version = version_file.read().strip()
assert isinstance(version, str)

install_requirements = ['numpy', 'pandas', 'matplotlib', 'requests', 'bs4']

setup(name='sport_success_modeler',
      version=version,
      description='Used to develop models to predict sports team success.',
      long_description=README,
      license='',
      author='Nate Ferreira',
      author_email='nferreira1729@gmail.com',
      download_url='https://github.com/Nate1729/sport_sucess_modeler',
      install_requires=install_requirements,
      packages=find_packages(),
      )
