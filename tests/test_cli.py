# -*- coding: utf-8 -*-
from pathlib import Path

from click.testing import CliRunner

from umarkdown.cli import main


def test_cli_should_read_from_text_file(runner: CliRunner):
    with runner.isolated_filesystem():
        with open("hello.md", "w") as f:
            f.write("# Hello World")
        result = runner.invoke(main, ["hello.md"])
        assert result.exit_code == 0
        assert "<h1>Hello World</h1>" in result.output


def test_cli_should_read_from_text_file_and_write_to_file(runner: CliRunner):
    with runner.isolated_filesystem():
        with open("hello.md", "w") as f:
            f.write("# Hello World")
        result = runner.invoke(main, ["hello.md", "hello.html"])
        assert result.exit_code == 0
        assert "<h1>Hello World</h1>" in Path("hello.html").read_text()


def test_cli_with_source_pos(runner: CliRunner):
    with runner.isolated_filesystem():
        with open("hello.md", "w") as f:
            f.write("# Hello World")
        result = runner.invoke(main, ["hello.md", "--sourcepos"])
        assert result.exit_code == 0
        assert '<h1 data-sourcepos="1:1-1:13">Hello World</h1>' in result.output


def test_cli_with_hard_breaks(runner: CliRunner):

    with runner.isolated_filesystem():
        with open("hello.md", "w") as f:
            f.write("Hello,\nWorld!")
        result = runner.invoke(main, ["hello.md"])
        assert result.exit_code == 0
        assert "<p>Hello,\nWorld!</p>" in result.output

    with runner.isolated_filesystem():
        with open("hello.md", "w") as f:
            f.write("Hello,\nWorld!")
        result = runner.invoke(main, ["hello.md", "--hardbreaks"])
        assert result.exit_code == 0
        assert "<p>Hello,<br />\nWorld!</p>" in result.output


def test_cli_with_no_breaks(runner: CliRunner):

    with runner.isolated_filesystem():
        with open("hello.md", "w") as f:
            f.write("Hello,\nWorld!")
        result = runner.invoke(main, ["hello.md"])
        assert result.exit_code == 0
        assert "<p>Hello,\nWorld!</p>" in result.output
    with runner.isolated_filesystem():
        with open("hello.md", "w") as f:
            f.write("Hello,\nWorld!")
        result = runner.invoke(main, ["hello.md", "--nobreaks"])
        assert result.exit_code == 0
        assert "<p>Hello, World!</p>" in result.output


def test_cli_with_unsafe(runner: CliRunner):
    with runner.isolated_filesystem():
        with open("hello.md", "w") as f:
            f.write("<p>Hello World!</p>")
        result = runner.invoke(main, ["hello.md"])
        assert result.exit_code == 0
        assert "<!-- raw HTML omitted -->" in result.output

    with runner.isolated_filesystem():
        with open("hello.md", "w") as f:
            f.write("<p>Hello World!</p>")
        result = runner.invoke(main, ["hello.md", "--unsafe"])
        assert result.exit_code == 0
        assert "<p>Hello World!</p>" in result.output


def test_cli_with_smart(runner: CliRunner):
    with runner.isolated_filesystem():
        with open("hello.md", "w") as f:
            f.write("Hello---")
        result = runner.invoke(main, ["hello.md"])
        assert result.exit_code == 0
        assert "<p>Hello---</p>" in result.output

    with runner.isolated_filesystem():
        with open("hello.md", "w") as f:
            f.write("Hello---")
        result = runner.invoke(main, ["hello.md", "--smart"])
        assert result.exit_code == 0
        assert "<p>Hello—</p>" in result.output
