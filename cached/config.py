# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os
import sys

import configo
import utila


def root() -> str:
    try:
        path = configo.env('DEV_CACHED_ROOT')
    except KeyError:
        utila.error('require global env `DEV_CACHED_ROOT`')
        sys.exit(utila.FAILURE)
    os.makedirs(path, exist_ok=True)
    return path
