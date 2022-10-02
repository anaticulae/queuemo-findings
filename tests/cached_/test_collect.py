# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import power
import utilatest

import cached


@utilatest.requires(power.HOME025_PDF)
def test_collect():
    source = power.link(power.HOME025_PDF)
    collected = cached.collect(source)
    assert collected
    assert len(collected) >= 50  # NOT VALIDATED
    assert collected.version
    assert collected.document
