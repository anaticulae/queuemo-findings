# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import qview.api.findings.renderer
from tests.cached_ import FILES


def test_versions():
    versions = qview.api.findings.renderer.versions(FILES)

    expected = ['1.1.1', '1.1.2', '1.2.1', '2.0.0', '2.1.0']
    assert versions == expected
