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


def decode(
        response,
        expected=None,
) -> dict:
    """Read binary data from response and convert them to str"""
    result = response.data.decode('utf8')
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
