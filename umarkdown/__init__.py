# -*- coding: utf-8 -*-
"""

Ultra Markdown
--------------

Ultra Markdown is an ultrafast Markdown parser written in
pure C with bindings for Python3.7+. It internally uses CMark,
an ultrafast C library for parsing Markdown to HTML.
Unlike others, Ultra Markdown is written using Python's C API
which makes it ultrafast for parsing Markdown.

Project Made and Maintained by Kumar Aditya.

License: BSD (see LICENSE.md for details).
"""

from ._internal import CMARK_VERSION, markdown

__all__ = ["markdown", "CMARK_VERSION"]
