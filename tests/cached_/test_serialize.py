# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import cached


def test_dump_and_load_document():
    data = cached.CachedResult()
    dumped = cached.dumps(data)

    loaded = cached.loads(dumped)
    assert loaded == data


def test_load_root(example):
    loaded = cached.load_root(example)
    assert len(loaded) == 7


def test_load_root_filter(example):
    loaded = cached.load_root(example, document='bachelor90')
    assert len(loaded) == 5

    loaded = cached.load_root(example, document='bachelor90', version='1.1.1')
    assert len(loaded) == 1

    loaded = cached.load_root(example, version='1.1.1')
    assert len(loaded) == 2
