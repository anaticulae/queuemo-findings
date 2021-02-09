# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import json

import flask

import cached
import qview.api.findings


@qview.api.findings.api_findings.route(
    '/findings/plots',
    methods=['GET'],
)
def plots():
    # TODO: WTF!!!
    data = json.loads(flask.request.args.get('data', ''))

    documents, versions = data['documents'], data['versions']
    findings = set(data['findings'])

    path, collected = select(documents, versions, findings)

    dumped = flask.jsonify({'plots': path})
    return dumped


def select(documents, versions, findings) -> dict:
    # TODO: ADD FINDINGS
    root = cached.root()
    collected = cached.load_root(
        root=root,
        document=documents,
        version=versions,
    )
    result = []
    for item in collected:
        path = f'{item.document}_{item.version}'
        if item.config:
            path += f'_{item.config}'
        if findings:
            selected_findings = [
                item for item in item.findings if item.msgid in findings
            ]
            path += f'_{hashed(selected_findings)}'
        path = f'{path}.png'
        raw = {
            'document': item.document,
            'version': item.version,
            'path': path,
        }
        result.append(raw)
    return result, collected


def hashed(findings) -> str:
    merged = ''.join([item.msgid for item in findings])
    return hash(merged)
