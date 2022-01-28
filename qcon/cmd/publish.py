# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utila

import cached


def run(inputpaths: utila.Strings, root: str, overwrite_version: str = None):
    documents = []
    for inputpath in inputpaths:
        utila.log(f'collect: {inputpath}')
        try:
            document = cached.collect(inputpath)
            if overwrite_version:
                utila.debug(f'overwrite collected version: {overwrite_version}')
                document.version = overwrite_version
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
