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
