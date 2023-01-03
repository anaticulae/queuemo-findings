# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import power
import utilatest

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


def test_dump_load_result(testdir):
    data = cached.CachedResult(
        document='helm',
        version='1.1.1',
        config='easy',
    )
    cached.dump_result(data, root=testdir.tmpdir)
    loaded = cached.load_result(
        document='helm',
        version='1.1.1',
        config='easy',
        root=testdir.tmpdir,
    )
    assert loaded == data


@utilatest.requires(power.HOME025_PDF)
def test_collect_and_dump(testdir):
    source = power.link(power.HOME025_PDF)
    document = cached.collect(source)
    cached.dump_root(document, testdir.tmpdir)
    loaded = cached.load_result(
        document=document.document,
        version=document.version,
        config=document.config,
        root=testdir.tmpdir,
    )
    assert loaded == document
