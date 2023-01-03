# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
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
def test_qcon_run(cmd, mp):
    tests.qcon_.run(cmd, mp=mp)


def test_qcon_collect_home25(cached_example):
    cache = cached_example
    loaded = cached.load_root(cache)
    assert len(loaded) == 2


def test_cli_list(cached_example, mp, capsys):
    """\
    root: /tmp/dev/tmp/caelum_qcon_master/test_17_36_33/popen-gw8/test_cli_list0/cache

    order009                                 1.24.3    60
    home025                                  1.24.3    123
    """
    tests.qcon_.run(f'--list --root {cached_example}', mp=mp)
    stdout = utilatest.stdout(capsys).strip()
    assert len(stdout.splitlines()) == 4  # two files plus root: information
    assert all((len(line.split()) == 3 for line in stdout.splitlines()[2:]))


def test_cli_publish_invalid(testdir, mp, capsys):
    tests.qcon_.failure('--publish', mp=mp)
    stderr = utilatest.stderr(capsys).strip()
    assert 'could not dump any data' in stderr


@utilatest.requires(power.HOME025_PDF)
def test_cli_publish_single(testdir, mp, capsys):
    source = power.link(power.HOME025_PDF)
    tests.qcon_.run(
        f'-i {source} --publish --root {testdir.tmpdir}',
        mp=mp,
    )
    assert len(utila.file_list(testdir.tmpdir)) == 1
    stdout = utilatest.stdout(capsys)
    assert 'collect:' in stdout
    assert 'dump:' in stdout


@utilatest.requires(power.HOME025_PDF)
def test_cli_publish_overwriteversion(testdir, mp):
    version = '13.13.13'
    source = power.link(power.HOME025_PDF)
    cmd = (f'-i {source} --publish '
           f'--root {testdir.tmpdir} --overwrite_version {version}')
    tests.qcon_.run(cmd, mp=mp)
    loaded = cached.load_root(testdir.tmpdir)
    assert len(loaded) == 1
    assert loaded[0].version == version
