# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import cached


def run(root: str):
    utila.log()
    files = cached.load_root(root)
    for item in files:
        line = '{:<40} {:<10}{:<10}'.format(
            item.document,
            item.version,
            len(item.findings),
        )
        utila.log(line)
    return utila.SUCCESS
