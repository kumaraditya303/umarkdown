#!/bin/env python
# -*- coding: utf-8 -*-
from glob import glob
from pathlib import Path

from setuptools import Extension, setup

setup(
    name="umarkdown",
    author="Kumar Aditya",
    author_email="",
    url="https://umarkdown.netlify.app/",
    description="Python wrapper of Markdown using CMark.",
    keywords=["Markdown", "CMark"],
    long_description=Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    license="BSD License",
    packages=["umarkdown"],
    include_package_data=True,
    zip_safe=False,
    entry_points={"console_scripts": ["umarkdown=umarkdown.cli:main"]},
    ext_modules=[
        Extension(
            "umarkdown._internal",
            sources=[*glob("./umarkdown/*.c"), *glob("./lib/*.c")],
            include_dirs=["./umarkdown", "./lib"],
            extra_compile_args=["-D_GNU_SOURCE"],
            extra_link_args=["-lm"],
        )
    ],
    classifiers=[
        "Programming Language :: C",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: Site Management",
        "Topic :: Software Development :: Documentation",
        "Topic :: Text Processing :: Filters",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Text Processing :: Markup :: Markdown",
        "License :: OSI Approved :: BSD License",
    ],
    use_scm_version=True,
    python_requires=">=3.7",
    extras_require={
        "cli": ["click==7.1.2"],
    },
    setup_requires=["setuptools_scm", "wheel"],
)
