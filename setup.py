#!/usr/bin/env python3

from setuptools import *

setup(
    name="allhub",
    version="0.0.1",
    packages=find_packages(exclude=["tests"]),
    description="Clone all projects from Github to your local directory.",
    include_package_data=True,
    keywords="scripts utilities github",
    author="Srinivas Reddy Thatiparthy",
    author_email="srinivas.thatiparthy@gmail.com",
    license="PSF",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.6.0",
)
