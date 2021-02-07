# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import pickle  # nosec

import cached


def dumps(document: cached.CachedResult) -> bytes:
    dumped = pickle.dumps(document)
    return dumped


def loads(raw: bytes) -> cached.CachedResult:
    document = pickle.loads(raw)  # nosec
    return document
