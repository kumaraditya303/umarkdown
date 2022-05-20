#!/bin/env python
# -*- coding: utf-8 -*-
import shutil
import subprocess
from glob import glob
from pathlib import Path

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext as _build_ext


class build_ext(_build_ext):
    def get_tag(self):
        python, abi, plat = super().get_tag()

        if python.startswith("cp"):
            return "cp37", "abi3", plat

        return python, abi, plat

    def run(self):
        cmark_build = Path(__file__).parent / "third_party" / "cmark" / "build"
        if (cmark_build).exists():
            shutil.rmtree(cmark_build)
        cmark_build.mkdir(exist_ok=True)
        subprocess.check_call(["cmake", ".."], cwd=cmark_build)
        return super().run()


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
            sources=["./umarkdown/_internal.c", *glob("./third_party/cmark/src/*.c")],
            include_dirs=["./third_party/cmark/src/", "./third_party/cmark/build/src/"],
            define_macros=[("Py_LIMITED_API", "0x03060000")],
            py_limited_api=True,
        )
    ],
    cmdclass={"build_ext": build_ext},
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
        "cli": ["click==8.0.3"],
    },
)
