#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from sphinx.setup_command import BuildDoc

cmdclass = {"build_sphinx": BuildDoc}

name = "HackathonScraping-Tool"
version = "0.7"

setup(
    name=name,
    version=version,
    install_requires=["beautifulsoup4",
                      "selenium",
                      "pandas",
                      "sphinx",
                      "Jinja2",
                      "groundwork-sphinx-theme",
                      "chromedriver_binary<80"],
    packages=find_packages(),
    url="https://github.com/adjiap/hackathon-scraper-tool",
    license="MIT License",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Win32 (MS Windows)",
        "Framework :: Sphinx",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Topic :: Internet :: WWW/HTTP :: Browsers"
        "Topic :: Text Processing :: Markup :: HTML",
    ],
    author="Adji Arioputro",
    maintainer="Adji Arioputro",
    description="Script to crawl hackathon.com website",
    command_options={
        "build_sphinx": {
            "project": ("setup.py", name),
            "version": ("setup.py", version),
        }
    },
)
