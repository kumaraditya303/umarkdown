# -*- coding: utf-8 -*-
import os
import shutil
import tempfile

import pytest
from click.testing import CliRunner


@pytest.fixture
def runner():
    yield CliRunner()


@pytest.fixture(autouse=True)
def isolate_filesystem():
    cwd = os.getcwd()
    t = tempfile.mkdtemp()
    os.chdir(t)
    try:
        yield t
    finally:
        os.chdir(cwd)
        try:
            shutil.rmtree(t)
        except (OSError, IOError):
            pass
