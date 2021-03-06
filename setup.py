#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The setup script."""

# Imports
import io
from setuptools import setup, find_packages

# Readme file
with io.open('README.rst', encoding='utf-8') as readme_file:
    readme = readme_file.read()
# ChangeLog file
with io.open('HISTORY.rst', encoding='utf-8') as history_file:
    history = history_file.read()
# Requirements Variable
requirements: list = [
    # Package Requirements
    'pyyaml',
]
# Setup Requirements Variable
setup_requirements: list = [
    # Setup Requirements
]
# Test Requirements Variable
test_requirements: list = [
    # Test Requirements
]
setup(
    # Name of Package
    name='sshyc',

    # Version following SemVer Style
    version='1.0.2',

    # Description of the Package
    description='SSHYC short for SSH YAML Configuration is tool to make .ssh/config from YAML files.',

    # Description of the Package to show on PyPi (Longer Description)
    long_description=readme + '\n\n' + history,

    # The Project Main Page [For that project for now is just repository]
    url='https://github.com/paip-web/sshyc',

    # Author Details
    author='Patryk Adamczyk',
    author_email='patrykadamczyk@paipweb.com',

    # License
    license='MIT',

    # Classifiers of the Project
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        # 'Development Status :: 1 - Planning'
        # 'Development Status :: 2 - Pre-Alpha'
        # 'Development Status :: 3 - Alpha'
        # 'Development Status :: 4 - Beta'
        # 'Development Status :: 5 - Production/Stable'
        # 'Development Status :: 6 - Mature'
        # 'Development Status :: 7 - Inactive'
        'Development Status :: 5 - Production/Stable',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',

        # Topic
        'Topic :: Utilities',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: OS Independent',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: POSIX :: Linux',
        'Environment :: Console'
    ],

    # Keywords of your Project
    keywords='ssh tools ssh_config config yaml',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # Dependencies of the Project
    install_requires=requirements,
    tests_require=test_requirements,
    setup_requires=setup_requirements,

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'setup': ["wheel", "twine", "collective.checkdocs", "bumpversion"],
        # 'test': ['pylint', 'pytest', 'coverage'],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    # package_data={
    #    'sample': ['package_data.dat'],
    # },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'sshyc=sshyc:main',
        ],
    },
    # Python Required Version for the package
    python_requires='~=3.6',
)
