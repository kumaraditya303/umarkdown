# -*- coding: utf-8 -*-
import pytest
from click.testing import CliRunner

from umarkdown.cli import main


@pytest.fixture
def runner():
    yield CliRunner()


def test_cli(runner: CliRunner):
    with runner.isolated_filesystem():
        with open("hello.md", "w") as f:
            f.write("# Hello World")
        result = runner.invoke(main, ["hello.md"])
        assert "<h1>Hello World</h1>" in result.output
