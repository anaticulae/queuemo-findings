# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import flask

import cached

findings_ = flask.Blueprint('findings', __name__)  # pylint:disable=invalid-name


@findings_.route('/findings')
def show_findings():
    documents = collect('document')
    versions = collect('version')
    rendered = flask.render_template(
        'findings/index.html',
        documents=documents,
        versions=versions,
    )
    return rendered


def collect(attribute: str):
    collected = set()
    files = cached.load_root(cached.root())
    for item in files:
        collected.add(getattr(item, attribute))
    result = sorted(list(collected))
    return result
