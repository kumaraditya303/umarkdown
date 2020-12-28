# -*- coding: utf-8 -*-
from typing import TextIO

try:
    import click
except ImportError:  # pragma:no cover
    print(
        """
            ===========================================
            || Ultra Markdown Command Line Interface ||
            ===========================================

             Ultra Markdown Cli dependencies not found.

        Make sure you have installed Ultra Markdown with cli.
            $ python -m pip install umarkdown[cli]
"""
    )
    exit(1)

from umarkdown import markdown


@click.command()
@click.argument(
    "file", required=True, type=click.File(mode="r", encoding="utf-8"), default="-"
)
@click.argument(
    "dest", required=True, type=click.File(mode="w", encoding="utf-8"), default="-"
)
@click.option(
    "--sourcepos",
    help="Include source position attribute.",
    is_flag=True,
    default=False,
    type=click.BOOL,
)
@click.option(
    "--hardbreaks",
    help="Treat newlines as hard line breaks.",
    is_flag=True,
    default=False,
    type=click.BOOL,
)
@click.option(
    "--nobreaks",
    help="Render soft line breaks as spaces.",
    is_flag=True,
    default=False,
    type=click.BOOL,
)
@click.option(
    "--unsafe",
    help="Render raw HTML and dangerous URLs.",
    is_flag=True,
    default=False,
    type=click.BOOL,
)
@click.option(
    "--smart",
    help="Use smart punctuation.",
    is_flag=True,
    default=False,
    type=click.BOOL,
)
@click.option(
    "--validate-utf8",
    help="Replace invalid UTF-8 sequences with U+FFFD.",
    is_flag=True,
    default=False,
    type=click.BOOL,
)
def main(
    file: TextIO,
    dest: TextIO,
    sourcepos: bool,
    hardbreaks: bool,
    nobreaks: bool,
    unsafe: bool,
    smart: bool,
    validate_utf8: bool,
):
    """
            \b
            ===========================================
            || Ultra Markdown Command Line Interface ||
            ===========================================
       Ultra Markdown is an ultrafast Markdown parser written in
          pure C with bindings for Python3.7+. It internally
    uses CMark, an ultrafast C library for parsing Markdown to HTML.

    """
    dest.write(
        markdown(
            text=file.read(),
            source_pos=sourcepos,
            hard_breaks=hardbreaks,
            no_breaks=nobreaks,
            unsafe=unsafe,
            smart=smart,
            validate_utf8=validate_utf8,
        )
    )
