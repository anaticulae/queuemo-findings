# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================
"""\
Different Documents             Different Findings          Images      Case
1                               5                           1           A

3                               5                           3           B

5                               0                           5           C

"""

import typing

import flask
import utila

import cached
import qview.api.findings
import qview.api.findings.renderer
import qview.api.findings.utils


@qview.api.findings.api_findings.route(
    '/findings/plots',
    methods=['GET'],
)
def plots():
    data = getdict(flask.request.args)
    documents, versions = data.get('documents', []), data.get('versions', [])
    findings = set(data.get('findings', []))
    plotinfo, grouped = select(documents, versions, findings)
    shortpath = [item['path'] for item in plotinfo]
    qview.api.findings.renderer.add_todo(
        shortpath,
        grouped,
        versions,
        findings,
    )
    dumped = flask.jsonify({'plots': plotinfo})
    return dumped


def select(
    documents: utila.Strings,
    versions: utila.Strings,
    findings: utila.Strings,
) -> typing.Tuple[list, dict]:
    # TODO: ADD FINDINGS
    root = cached.root()
    collected: cached.CachedResults = cached.load_root(
        root=root,
        document=documents,
        version=versions,
    )
    versions: str = version_raw(versions)
    grouped = qview.api.findings.utils.groupby_document(collected)
    result = []
    for docname, docs in grouped.items():
        path = f'{docname}_{versions}'
        # if item.config:
        #     path += f'_{item.config}'
        if findings:
            documents_findings = utila.flatten([item.findings for item in docs])
            selected_findings = [
                item for item in documents_findings if item.msgid in findings
            ]
            path += f'_{hashed(selected_findings)}'
        path = f'{path}.png'
        raw = {
            'document': docname,
            'version': versions,
            'path': path,
        }
        result.append(raw)
    return result, grouped


def version_raw(versions: list) -> str:
    versions: str = '_'.join(versions)
    versions = versions.replace('.', '_')
    return versions


def hashed(findings: cached.CachedFindings) -> str:
    merged = ''.join([item.msgid for item in findings])
    return hash(merged)


def getdict(collection) -> dict:
    """Convert hacky rpc request to usable dict data structure.

    Hint: May remove this HACK later.
    """
    result = {}
    for key in collection:
        result[key.replace('[]', '')] = collection.getlist(key)
    return result
