# Ultra Markdown ⚡

<img width="800" alt="Ultra Markdown" src="https://user-images.githubusercontent.com/59607654/103167048-d3524d00-484d-11eb-96ca-70608a7529fc.png">

<p align="center">Ultra Markdown, an ultra fast (high performance) Markdown parser written in pure C with bindings for Python 3.7+. </p>

<p align="center" >
 <img src="https://img.shields.io/pypi/v/umarkdown?logo=pypi&style=flat-square"/>
 <img src="https://pepy.tech/badge/umarkdown" />
 <img src="https://img.shields.io/codecov/c/github/kumaraditya303/umarkdown?logo=codecov&style=flat-square" />
<img src="https://api.netlify.com/api/v1/badges/2dad1b5d-eddc-4bff-8c6a-5bc00fd11acd/deploy-status" />
</p>

---

**Source** : [https://github.com/kumaraditya303/umarkdown](https://github.com/kumaraditya303/umarkdown)

** Docs** : [https://umarkdown.netlify.app/](https://umarkdown.netlify.app/)

---

_Ultra Markdown, an ultra fast (high performance) Markdown parser compliant with the markdown [spec](https://spec.commonmark.org/) written in pure C with bindings for Python 3.7+. Unlike others, **Ultra Markdown** is written using Python's C API and uses [CMark](https://github.com/commonmark/cmark), an ultra fast Markdown parser written in C._

---

## Features 🚀

- **Fast** - Very high performance, One of the fastest Markdown Parser available for Python.
- **Intuitive** - Great IDE support as it ships with stubs out of the box.
- **Standards** - Based on CMark C library which is fully compliant with the markdown [spec](https://github.com/commonmark/cmark).
- **Command Line Interface** - Ships with a Cli based on [click](https://github.com/pallets/click) for Cli usage.
- **Support** - Fully supported on Windows, Linux, MacOS.

---

## Installation ✔

- Install Ultra Markdown with pip:

```bash
$ python -m pip install umarkdown
```

- Install Ultra Markdown with cli with pip:

```bash
$ python -m pip install umarkdown[cli]
```

---

## Installation from source ✔

> ### Prerequisites

- Compiler: gcc or clang on Linux and MacOS, MSVC for Windows.
- Python: 3.7 or greater

> ### Installation Process

- Clone the repository:

```bash
$ git clone https://github.com/kumaraditya303/umarkdown
```

- Install requirements with pip:

```bash
$ pip install -r requirements.txt
```

- Build extensions and install:

```bash
$ pip install -e .[cli]
```

---

## Usage 🚀

Can be used as a drop in replacement for most Markdown parsers.

```python
>>> from umarkdown import markdown
>>> print(markdown("# Hello World!"))
<h1>Hello World!</h1>
```

---

## License 📜

This project is licensed under BSD 3-Clause License.
