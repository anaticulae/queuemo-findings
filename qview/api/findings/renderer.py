# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections

import semver

import cached


def render(documents: cached.CachedResults, findings: set = None) -> bytes:
    pass


def data(documents: cached.CachedResults, findings: set = None) -> list:
    collected = collections.defaultdict(0)
    for document in documents:
        collected[document.version] = len(document.findings)


def versions(documents: cached.CachedResults) -> list:
    collected = set()
    for document in documents:
        parsed = semver.parse_version_info(document.version)
        collected.add(parsed)
    result = sorted(list(collected))
    result = [str(item) for item in result]
    return result
