# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import painter
import utila

import qview.view.findings
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
    cmd = 'findings/plots?documents=homework25&findings=E1220&findings=E1221'
    with tests.qview_.patch_todo(monkeypatch, testdir, tests.conftest.CACHED):
        content = tests.qview_.apicall(client, cmd)
    assert len(content['plots']) == 1
    rendered = utila.file_list('renderer', absolute=True)
    assert len(rendered) == 1
    painter.show_figure(rendered[0])


def test_plots_selective_findings(client, testdir, monkeypatch):
    cmd = 'findings/plots?documents=homework25&findings=E1220&findings=W4001'
    with tests.qview_.patch_todo(monkeypatch, testdir, tests.conftest.CACHED):
        content = tests.qview_.apicall(client, cmd)
    assert len(content['plots']) == 1
    rendered = utila.file_list('renderer', absolute=True)
    assert len(rendered) == 1
    painter.show_figure(rendered[0])


def test_plots_all(client, testdir, monkeypatch):
    """Select all possible parameter and for two resources."""
    documents = 'documents%5B%5D=homework25&documents%5B%5D=order009'
    versions = [f'versions%5B%5D={item}' for item in tests.conftest.VERSIONS]
    versions = '&'.join(versions)
    findings = qview.view.findings.findings(tests.conftest.CACHED)
    findings = 'findings%5B%5D=' + '&findings%5B%5D='.join(findings)
    call = f'findings/plots?{documents}&{versions}&{findings}'
    with tests.qview_.patch_todo(monkeypatch, testdir, tests.conftest.CACHED):
        content = tests.qview_.apicall(client, call)
        plots = content['plots']
        home25, order009 = plots[0]['path'], plots[1]['path']
        home25 = tests.qview_.apicall(client, f'/plots/{home25}', prefix='')
        order009 = tests.qview_.apicall(client, f'/plots/{order009}', prefix='')
    # plots contain content
    assert len(home25) == 41867
    assert len(order009) == 41679
