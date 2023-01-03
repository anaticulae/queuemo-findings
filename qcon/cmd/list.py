# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import cached


def run(root: str):
    utila.log()
    files = cached.load_root(root)
    for item in files:
        line = '{:<40} {:<10}{:<10}'.format(  # pylint:disable=C0209
            item.document,
            item.version,
            len(item.findings),
        )
        utila.log(line)
    return utila.SUCCESS
