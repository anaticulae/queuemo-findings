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

findings = lambda number: [cached.CachedFinding(msgid='E01010')] * number  # pylint:disable=C0103

# yapf:disable
FILES = [
    cached.CachedResult(document='bachelor90', version='1.1.1', config='release', findings=findings(15)),
    cached.CachedResult(document='bachelor90', version='1.1.2', config='release', findings=findings(30)),
    cached.CachedResult(document='bachelor90', version='1.2.1', config='release', findings=findings(90)),
    cached.CachedResult(document='bachelor90', version='2.0.0', config='release', findings=findings(10)),
    cached.CachedResult(document='bachelor90', version='2.1.0', config='release', findings=findings(5)),
    cached.CachedResult(document='master110', version='1.1.1', config='prefix'),
    cached.CachedResult(document='master110', version='1.1.2', config='prefix'),
]
# yapf:enable


@pytest.fixture
def example(testdir):
    cached.dump_root(FILES, testdir.tmpdir)
    return testdir.tmpdir
