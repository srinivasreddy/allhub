# flake8: NOQA

from setuptools import *

requires = open("requirements.txt").read().splitlines()

setup(
    name="allhub",
    version="0.0.3",
    packages=find_packages(exclude=["tests"]),
    description="Clone all projects from Github to your local directory.",
    include_package_data=True,
    keywords="scripts utilities github",
    author="Srinivas Reddy Thatiparthy",
    author_email="srinivas.thatiparthy@gmail.com",
    license="PSF",
    install_requires=requires,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.6.0",
    project_urls={"Source": "https://github.com/srinivasreddy/allhub"},
)
