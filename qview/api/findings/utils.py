# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections

import cached


def different_documents(documents: cached.CachedResults) -> int:
    doccount = len({item.document for item in documents})
    return doccount


def groupby_document(documents: cached.CachedResults) -> dict:
    collected = collections.defaultdict(list)
    for document in documents:
        if not document:
            continue
        collected[document.document].append(document)
    result = dict(collected)
    return result


def groupby_findings(documents: cached.CachedResults, findings: set) -> dict:
    # Doccount > 1 Findings > 0
    doccount = different_documents(documents)
    if doccount <= 1 and not findings:
        # negative case
        return None
    result = {}
    for finding in findings:
        result[finding] = documents[:]
    return result
