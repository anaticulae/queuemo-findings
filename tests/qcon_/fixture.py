# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import power
import pytest

import cached
import tests.qcon_


@pytest.fixture
def cached_example(testdir, mp):
    cache = os.path.join(testdir.tmpdir, 'cache')
    os.makedirs(cache)

    home25 = power.link(power.HOME025_PDF)
    order09 = power.link(power.ORDER009_PDF)
    cmd = f'-i {home25} -i {order09} --publish --root {cache}'
    tests.qcon_.run(cmd, mp=mp)

    loaded = cached.load_root(cache)
    assert len(loaded) == 2
    return cache
