
from __future__ import absolute_import

import os
from glob import glob

from setuptools import find_packages, setup


def read(fname):
    """
    Args:
        fname:
    """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


# Declare minimal set for installation
required_packages = [
    "boto3>=1.20.21,<2.0",
    "pandas",
]

setup(
    name="aws_feature_store",
    version="0.0.17",
    description="Simplified SageMaker Feature Store",
    long_description_content_type="text/markdown",
    long_description=read('README.md'),
    packages=find_packages(),
    py_modules=[os.path.splitext(os.path.basename(path))[0] for path in glob("aws_feature_store/*.py")],
    include_package_data=True,
    author="Ihor Bilyk",
    url="https://github.com/bilykigor/aws_feature_store",
    license="Apache License 2.0",
    keywords="Simplified SageMaker Feature Store",
    python_requires=">= 3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    install_requires=required_packages
)
