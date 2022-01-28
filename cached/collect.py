# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import iamraw
import link
import protocol
import utila

import cached


def collect(path: str) -> 'cached.CachedResult':
    findings = os.path.join(path, 'result', '__optimized__')
    if not utila.exists(findings):
        raise ValueError(f'could not find {findings}')
    pagefindings: iamraw.PageFindings = protocol.load_grouped(findings)
    collected = []
    for page in pagefindings:
        for finding in page.content:
            item = cached.CachedFinding(
                page=page.page,
                msgid=finding.solution.msgid,
            )
            collected.append(item)
    document, version, config = document_version_config(path)
    result = cached.CachedResult(
        findings=collected,
        config=config,
        document=document,
        version=version,
    )
    return result


def document_version_config(path: str) -> tuple:
    job = link.load_job(os.path.join(path, link.JOB_FILE_NAME))
    document = simplify_filename(job.title)
    if os.path.exists(path):
        loaded = link.load_debug(path)
    else:
        utila.error(f'could not load config: {path}')
        loaded = {}
    version = loaded.get('queuemo', None)
    config = loaded.get('config', cached.CONFIG_DEFAULT)
    return document, version, config


def simplify_filename(name):
    name = name.replace('.pdf', '')
    # beautify document name
    name = name.replace('-', '_')
    name = name.replace(' ', '_')
    name = name.lower()
    return name
