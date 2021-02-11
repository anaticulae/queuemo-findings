# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import os
import threading

import painter
import semver
import utila

import cached
import qview.config


def render(
        documents: cached.CachedResults,
        versions=None,
        legend: str = None,
        findings: set = None,
) -> bytes:
    """\
    # Title: Draw title if selective findings are used. If no selective
             findings are used, the title is rendered in finding legend.
    """
    title = documents[0].document if documents and findings else ''
    if not legend and documents:
        legend = documents[0].document
    versions, counted = data(documents, versions=versions, findings=findings)
    legend = list(findings) if findings else [legend]
    versions = [f'v{item}' for item in versions]
    ymax_ = ymax(documents) * 1.1
    painted = painter.plot_render(
        counted,
        labels=versions,
        legends=legend,
        width=11.16,
        ylim=(0, ymax_),
        title=title,
    )
    result = painter.png(painted)
    return result


def add_todo(paths, documents, versions, findings=None):
    workdir = qview.config.renderer_workdir()
    todo = []
    for path, document in zip(paths, documents.values()):
        rendered = os.path.join(workdir, path)
        if os.path.exists(os.path.join(workdir, path)):
            continue
        utila.file_create_binary(rendered)
        # render asynchronously
        todo.append([rendered, document, versions, findings])
    if not todo:
        return
    if qview.config.sync():
        render_todo(todo)
        return
    run = threading.Thread(target=render_todo, args=(todo,))
    run.start()


def render_todo(todo):
    for path, documents, versions, findings in todo:
        rendered = render(documents, versions=versions, findings=findings)
        utila.file_replace_binary(path, rendered)


def data(
        documents: cached.CachedResults,
        versions=None,
        findings: set = None,
) -> list:
    if not versions:
        versions = versions_(documents)
    collected = collections.defaultdict(int if not findings else list)
    for document in documents:
        collected[document.version] = count_findings(document, findings)
    counted = [collected[item] for item in versions]
    return versions, counted


def versions_(documents: cached.CachedResults) -> list:
    collected = set()
    for document in documents:
        parsed = semver.parse_version_info(document.version)
        collected.add(parsed)
    result = sorted(list(collected))
    result = [str(item) for item in result]
    return result


def ymax(documents) -> int:
    maxfinding = max([len(item.findings) for item in documents], default=5)
    maxfinding = max(maxfinding, 5)
    return maxfinding


def count_findings(document, findings):
    collected = document.findings
    if not findings:
        return len(collected)
    document_findings = [finding.msgid for finding in document]
    collected = [document_findings.count(finding) for finding in findings]
    return collected
