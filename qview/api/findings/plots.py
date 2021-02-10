# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import collections
import json

import flask
import utila

import cached
import qview.api.findings
import qview.api.findings.renderer


@qview.api.findings.api_findings.route(
    '/findings/plots',
    methods=['GET'],
)
def plots():
    # TODO: WTF!!!
    data = json.loads(flask.request.args.get('data', ''))

    documents, versions = data['documents'], data['versions']
    findings = set(data['findings'])

    plot_info, grouped = select(documents, versions, findings)

    shortpath = [item['path'] for item in plot_info]
    qview.api.findings.renderer.add_todo(shortpath, grouped)

    dumped = flask.jsonify({'plots': plot_info})
    return dumped


def select(documents, versions: list, findings) -> dict:
    # TODO: ADD FINDINGS
    root = cached.root()
    collected: cached.CachedResults = cached.load_root(
        root=root,
        document=documents,
        version=versions,
    )
    versions: str = ''.join(versions)
    grouped = groupby_document(collected)
    result = []
    for document_name, docs in grouped.items():
        path = f'{document_name}_{versions}'
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
            'document': document_name,
            'version': versions,
            'path': path,
        }
        result.append(raw)
    return result, grouped


def groupby_document(documents) -> dict:
    collected = collections.defaultdict(list)
    for document in documents:
        collected[document.document].append(document)
    result = dict(collected)
    return result


def hashed(findings) -> str:
    merged = ''.join([item.msgid for item in findings])
    return hash(merged)
