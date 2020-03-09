# flake8: NOQA

from setuptools import *

setup(
    name="allhub",
    version="0.0.7",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    description="Interact with Github REST API v3",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="scripts utilities github REST API V3",
    author="Srinivas Reddy Thatiparthy",
    author_email="srinivas.thatiparthy@gmail.com",
    license="PSF",
    install_requires=["requests==2.22.0"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.5",
    project_urls={"Source": "https://github.com/srinivasreddy/allhub"},
)
