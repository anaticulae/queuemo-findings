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


def run(inputpaths: utila.Strings, root: str):
    documents = []
    for inputpath in inputpaths:
        utila.log(f'collect: {inputpath}')
        try:
            document = cached.collect(inputpath)
        except ValueError:
            utila.error(f'not a valid document folder: {inputpath}')
            continue
        documents.append(document)
    if documents:
        utila.log(f'dump: {root}')
        cached.dump_root(documents, root=root)
        return utila.SUCCESS
    utila.error('could not dump any data')
    return utila.FAILURE
