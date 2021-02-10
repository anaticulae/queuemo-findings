# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os

import flask

import cached
import qview.config

findings_ = flask.Blueprint('findings', __name__)  # pylint:disable=invalid-name


@findings_.route('/findings')
def show_findings():
    documents = collect('document')
    versions = collect('version')
    findings_collected = findings()
    rendered = flask.render_template(
        'findings/index.html',
        documents=documents,
        versions=versions,
        findings=findings_collected,
    )
    return rendered


@findings_.route('/plots/<string:image>')
def view_plot(image: str = None):
    workdir = qview.config.renderer_workdir()

    image = os.path.join(workdir, image)
    if not os.path.exists(image):
        return b''

    # Hint: contextmanager does not work here
    response = flask.send_file(open(image, mode='rb'), mimetype='image')
    return response


def collect(attribute: str):
    collected = set()
    files = cached.load_root(cached.root())
    for item in files:
        collected.add(getattr(item, attribute))
    result = sorted(list(collected))
    return result


def findings():
    collected = set()
    files = cached.load_root(cached.root())
    for item in files:
        collected.update({finding.msgid for finding in item.findings})
    result = sorted(list(collected))
    return result
