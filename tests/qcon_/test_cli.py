# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import power
import pytest
import utila
import utilatest

import cached
import tests.qcon_


@pytest.mark.parametrize('cmd', [
    '--help',
])
@pytest.mark.usefixtures('testdir')
def test_qcon_run(cmd, monkeypatch):
    tests.qcon_.run(cmd, monkeypatch=monkeypatch)


def test_qcon_collect_home25(cached_example):
    cache = cached_example
    loaded = cached.load_root(cache)
    assert len(loaded) == 2


def test_cli_list(cached_example, monkeypatch, capsys):
    tests.qcon_.run(f'--list --root {cached_example}', monkeypatch=monkeypatch)

    stdout = utilatest.stdout(capsys).strip()
    assert len(stdout.splitlines()) == 2
    assert all((len(line.split()) == 3 for line in stdout.splitlines()))


def test_cli_publish_invalid(testdir, monkeypatch, capsys):
    tests.qcon_.failure(f'--publish', monkeypatch=monkeypatch)
    stderr = utilatest.stderr(capsys).strip()
    assert 'could not dump any data' in stderr


def test_cli_publish_single(testdir, monkeypatch, capsys):
    source = power.link(power.HOME025_PDF)
    tests.qcon_.run(
        f'-i {source} --publish --root {testdir.tmpdir}',
        monkeypatch=monkeypatch,
    )
    assert len(utila.file_list(testdir.tmpdir)) == 1
    stdout = utilatest.stdout(capsys)
    assert 'collect:' in stdout
    assert 'dump:' in stdout
