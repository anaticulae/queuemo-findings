# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os
import sys

import configos
import utilo


def root() -> str:
    try:
        path = configos.env(
            'DEV_CACHED_ROOT',
            default='~/.tmp/qcon/dev_cached',
        )
    except KeyError:
        # TODO: REMOVE LATER OR CHANGE?
        utilo.error('require global env `DEV_CACHED_ROOT`')
        sys.exit(utilo.FAILURE)
    os.makedirs(path, exist_ok=True)
    return path
