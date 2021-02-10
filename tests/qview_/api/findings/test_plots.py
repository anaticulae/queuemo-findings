# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import tests.conftest
import tests.qview_


def test_plots_get_empty(client, testdir, monkeypatch):
    with tests.qview_.patch_todo(monkeypatch, testdir):
        content = tests.qview_.apicall(client, 'findings/plots')
    assert not content['plots']


def test_plots_get_root(client, testdir, monkeypatch):
    with tests.qview_.patch_todo(monkeypatch, testdir, tests.conftest.CACHED):
        content = tests.qview_.apicall(client, 'findings/plots')
    assert len(content['plots']) == 2
    assert len(utila.file_list('renderer')) == 2


def test_plots_get_homework25(client, testdir, monkeypatch):
    with tests.qview_.patch_todo(monkeypatch, testdir, tests.conftest.CACHED):
        # TODO: SIMPLIFY!
        content = tests.qview_.apicall(
            client,
            'findings/plots?documents%5B%5D=homework25',
        )
    assert len(content['plots']) == 1
    assert len(utila.file_list('renderer')) == 1


def test_plots_get_homework25_error1220_error1221(client, testdir, monkeypatch):
    # TODO: SIMPLIFY!
    cmd = ('findings/plots?documents%5B%5D=homework25&'
           'findings%5B%5D=E1220&findings%5B%5D=E1221')
    with tests.qview_.patch_todo(monkeypatch, testdir, tests.conftest.CACHED):
        content = tests.qview_.apicall(client, cmd)
    assert len(content['plots']) == 1
    assert len(utila.file_list('renderer')) == 1
