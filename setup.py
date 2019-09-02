#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Roberto Preste
from setuptools import setup, find_packages

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = ["Click>=7.0", "pandas>=0.23.4", "requests>=2.20.1",
                "aiohttp>=3.4.4", "vcfpy==0.12.1", "sqlalchemy>=1.2.16",
                "apybiomart==0.3.5", "scikit-allel==1.2.1"]

setup_requirements = ["pytest-runner", ]

test_requirements = ["pytest", ]

setup(  # pragma: no cover
    author="Roberto Preste",
    author_email="robertopreste@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    description="Variant annotator for MToolBox.",
    entry_points={
        "console_scripts": [
            "mtoolnote=mtoolnote.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    long_description_content_type="text/x-rst",
    include_package_data=True,
    keywords="mtoolnote",
    name="mtoolnote",
    packages=find_packages(include=["mtoolnote"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/mitoNGS/mtoolnote",
    version='0.1.0',
    zip_safe=False,
)
