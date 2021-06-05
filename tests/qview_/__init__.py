# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import contextlib
import http
import json.decoder
import os
import threading

import qview.config


def decode(
    response,
    expected=None,
) -> dict:
    """Read binary data from response and convert them to str"""
    try:
        result = response.data.decode('utf8')
    except UnicodeDecodeError:
        # bytes response
        return response.data
    if expected is not None:
        assert response.status_code == expected
    with contextlib.suppress(json.decoder.JSONDecodeError):
        # json format
        return json.loads(result)
    # html format
    return result


def content(
    client,
    request: str,
    expected=http.HTTPStatus.OK,
    raw: bool = False,
):
    response = client.get(request, follow_redirects=True)
    assert response.status_code == expected, request + str(response)
    if raw:
        return response
    return decode(response)


def apicall(
    client,
    request: str,
    prefix=qview.config.API_PREFIX,
    expected=http.HTTPStatus.OK,
):
    cmd = prefix + request
    response = client.get(cmd)
    assert response.status_code == expected, request + str(response)
    return decode(response, expected=expected)


LOCK = threading.Lock()


@contextlib.contextmanager
def patch_todo(monkeypatch, testdir, root=None):
    testdir.mkdir('renderer')
    workdir = os.path.join(testdir.tmpdir, 'renderer')
    if root is None:
        testdir.mkdir('root')
        root = os.path.join(testdir.tmpdir, 'root')
    with LOCK:
        # TODO: INVESTIGATE HOW TO THIS BETTER
        with monkeypatch.context() as context:
            context.setenv('DEV_QVIEW_RENDERER_TMP', workdir)
            context.setenv('DEV_CACHED_ROOT', root)
            yield workdir
