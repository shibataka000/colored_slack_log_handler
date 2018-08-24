"""
distutils/setuptools install script.
"""

import os
from setuptools import setup, find_packages


def find_install_requires():
    """
    Find install_requires from requirements.txt
    """
    path = os.path.join(os.path.dirname(__file__), "requirements.txt")
    return [x.strip() for x in open(path) if not x.startswith("#")]


setup(
    name="colored_slack_log_handler",
    version="0.0.6",
    description="Python color-coding Slack log handler",
    author="shibataka000",
    url="https://github.com/shibataka000/colored_slack_log_handler",
    packages=find_packages(),
    install_requires=find_install_requires(),
    license="MIT",
    classifiers=[]
)
