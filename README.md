# Ultra Markdown ⚡

![](https://img.shields.io/pypi/v/umarkdown?logo=pypi&style=flat-square)
[![Downloads](https://pepy.tech/badge/umarkdown)](https://pepy.tech/project/umarkdown)
![](https://img.shields.io/codecov/c/github/kumaraditya303/umarkdown?logo=codecov&style=flat-square)[![Netlify Status](https://api.netlify.com/api/v1/badges/2dad1b5d-eddc-4bff-8c6a-5bc00fd11acd/deploy-status)](https://app.netlify.com/sites/umarkdown/deploys)

<img width="800" alt="Ultra Markdown" src="https://user-images.githubusercontent.com/59607654/103167048-d3524d00-484d-11eb-96ca-70608a7529fc.png">

Ultra Markdown, an ultra fast (high performance) Markdown parser compliant with the markdown [spec](https://spec.commonmark.org/) written in pure C with bindings for Python 3.7+. Unlike others, **Ultra Markdown** is written using Python's C API and uses [CMark](https://github.com/commonmark/cmark), an ultra fast Markdown parser written in C.

---

**Source** : [https://github.com/kumaraditya303/umarkdown](https://github.com/kumaraditya303/umarkdown)

**Docs** : [https://umarkdown.netlify.app/](https://umarkdown.netlify.app/)

---

## Features 🚀

- Fast - Very high performance, One of the fastest Markdown Parser available for Python.
- Intuitive - Great IDE support as it ships with stubs out of the box.
- Standards - Based on CMark C library which is fully compliant with the markdown [spec](https://github.com/commonmark/cmark).
- Command Line Interface - Ships with a Cli based on [click](https://github.com/pallets/click) for Cli usage.
- Support - Fully supported on Windows, Linux, MacOS.

---

## Installation ✔

Install with pip:

```bash
$ python -m pip install umarkdown
# Or Install with cli
$ python -m pip install umarkdown[cli]
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

## Benchmarks

![](https://raw.githubusercontent.com/kumaraditya303/umarkdown/master/docs/images/benchmarks.svg)

- Higher score is better.

---
