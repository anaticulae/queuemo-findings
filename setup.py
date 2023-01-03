#!/usr/bin/env python
# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

PACKAGES = [
    'cached',
    'qcon',
    'qcon.cmd',
    'qview',
    'qview.api',
    'qview.api.findings',
    'qview.view',
]
ENTRY_POINTS = dict(console_scripts=[
    'qcon = qcon.cli:main',
    'qview = qview.cli:main',
])

if __name__ == "__main__":
    utila.install(
        __file__,
        include_package_data=True,
    )
