# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pytest

import cached


@pytest.fixture
def example(testdir):
    # yapf:disable
    files = [
        cached.CachedResult(document='bachelor90', version='1.1.1', config='release'),
        cached.CachedResult(document='bachelor90', version='1.1.2', config='release'),
        cached.CachedResult(document='bachelor90', version='1.2.1', config='release'),
        cached.CachedResult(document='bachelor90', version='2.0.0', config='release'),
        cached.CachedResult(document='bachelor90', version='2.1.0', config='release'),
        cached.CachedResult(document='master110', version='1.1.1', config='prefix'),
        cached.CachedResult(document='master110', version='1.1.2', config='prefix'),
    ]
    # yapf:enable
    cached.dump_root(files, testdir.tmpdir)
    return testdir.tmpdir
