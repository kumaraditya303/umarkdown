# -*- coding: utf-8 -*-
import pytest

from umarkdown import markdown


def test_umarkdown_with_text():
    with pytest.raises(TypeError):
        markdown()
    assert "<h1>Hello World</h1>\n" == markdown(text="# Hello World")


def test_umarkdown_with_source_pos():
    assert '<h1 data-sourcepos="1:1-1:13">Hello World</h1>\n' == markdown(
        "# Hello World", source_pos=True
    )


def test_umarkdown_with_hard_breaks():
    assert "<p>Hello,\nWorld!</p>\n" == markdown("Hello,\nWorld!")
    assert "<p>Hello,<br />\nWorld!</p>\n" == markdown(
        "Hello,\nWorld!", hard_breaks=True
    )


def test_umarkdown_with_no_breaks():
    assert "<p>Hello,\nWorld!</p>\n" == markdown("Hello,\nWorld!")
    assert "<p>Hello, World!</p>\n" == markdown("Hello,\nWorld!", no_breaks=True)


def test_umarkdown_with_unsafe():
    assert "<!-- raw HTML omitted -->\n" == markdown("<p>Hello World!</p>")
    assert "<p>Hello World!</p>\n" == markdown("<p>Hello World!</p>", unsafe=True)


def test_umarkdown_with_smart():
    assert "<p>Hello---</p>\n" == markdown("Hello---")
    assert "<p>Hello—</p>\n" == markdown("Hello---", smart=True)
