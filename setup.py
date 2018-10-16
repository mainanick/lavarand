#!/usr/bin/env python

import os
import sys

from codecs import open

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

# 'setup.py publish' shortcut.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    if os.name == 'nt':
        os.system('python -m twine upload dist/*')
    else:
        os.system('twine upload dist/*')
    sys.exit()

packages = ['lavarand']

requires = ['requests']

api = {}
with open(os.path.join(here, 'lavarand', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), api)

setup(
    name=api['__title__'],
    version=api['__version__'],
    description=api['__description__'],
    author=api['__author__'],
    author_email=api['__email__'],
    url=api['__url__'],
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'lavarand': 'lavarand'},
    include_package_data=True,
    install_requires=requires,
    license=api['__license__'],
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ),
)