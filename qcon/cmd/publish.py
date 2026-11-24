# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import utilo

import cached


def run(inputpaths: utilo.Strings, root: str, overwrite_version: str = None):
    documents = []
    for inputpath in inputpaths:
        utilo.log(f'collect: {inputpath}')
        try:
            document = cached.collect(inputpath)
            if overwrite_version:
                utilo.debug(f'overwrite collected version: {overwrite_version}')
                document.version = overwrite_version
        except ValueError:
            utilo.error(f'not a valid document folder: {inputpath}')
            continue
        documents.append(document)
    if documents:
        utilo.log(f'dump: {root}')
        cached.dump_root(documents, root=root)
        return utilo.SUCCESS
    utilo.error('could not dump any data')
    return utilo.FAILURE
