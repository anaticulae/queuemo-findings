# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import tests.conftest
import tests.qview_


def test_findings(client):
    findings = tests.qview_.content(client, '/findings')
    assert '<h1>Findings</h1>' in findings


@tests.conftest.require_cached
def test_view_plots_home025(client, testdir, mp):
    with tests.qview_.patch_todo(mp, testdir, tests.conftest.CACHED):
        # TODO: SIMPLIFY!
        content = tests.qview_.apicall(
            client,
            'findings/plots?documents%5B%5D=home025',
        )
        assert len(content['plots']) == 1
        selected_plot = content['plots'][0]['path']
        images = tests.qview_.content(
            client,
            f'/plots/{selected_plot}',
            raw=True,
        )
    images = images.data
    assert len(images) > 200
