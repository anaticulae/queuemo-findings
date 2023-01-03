# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import os
import pickle  # nosec

import semver
import utila

import cached


def dumps(document: cached.CachedResult) -> bytes:
    dumped = pickle.dumps(document)
    return dumped


def loads(raw: bytes) -> cached.CachedResult:
    try:
        document = pickle.loads(raw)  # nosec
    except pickle.UnpicklingError:
        return None
    return document


def dump_result(
    document: cached.CachedResult,
    root: str,
    overwrite: bool = True,
) -> str:
    if document.version is None:
        utila.error(f'could not dump {document.document}, '
                    'require --overwrite_version parameter')
        return None

    named = name(version=document.version, config=document.config)
    parent = os.path.join(root, document.document)
    path = os.path.join(parent, named)
    os.makedirs(parent, exist_ok=True)  # create parent
    utila.debug(f'write: {path}')
    dumped = cached.dumps(document)
    writer = utila.file_create_binary
    if overwrite:
        writer = utila.file_replace_binary
    writer(path, dumped)
    return path


def load_result(
    document: str = None,
    version: str = None,
    config: str = None,
    root: str = None,
) -> cached.CachedResult:
    named = name(version=version, config=config)
    path = os.path.join(root, document, named)
    assert os.path.exists(path), str(path)
    loaded = utila.file_read_binary(path)
    document = loads(loaded)
    if document is None:
        utila.error(f'could not load document: {document} {version} {config}')
    return document


def dump_root(
    documents: cached.CachedResults,
    root: str,
    overwrite: bool = True,
):
    assert os.path.exists(root), str(root)
    if isinstance(documents, cached.CachedResult):
        documents = [documents]
    for document in documents:
        dump_result(document, root, overwrite=overwrite)


def load_root(
    root: str,
    document: str = None,
    version: str = None,
    config: str = None,
) -> cached.CachedResults:
    result = []
    for item in collect_root(root, document, version, config):
        path = os.path.join(root, item)
        raw = utila.file_read_binary(path)
        loaded = loads(raw)
        if loaded is None:
            utila.error(f'could not load document: {path}')
            continue
        result.append(loaded)
    return result


def collect_root(
    root: str,
    document: str = None,
    version: str = None,
    config: str = None,
) -> 'paths':
    collected = []
    if isinstance(document, str):
        document = [document]
    if isinstance(version, list):  # pylint:disable=W0160
        version = [version_raw(item) for item in version]
    else:
        version = [version_raw(version)] if version else None
    if isinstance(config, str):
        config = [config]
    for item in utila.file_list(root):
        raw = str(item)
        if skip(document, raw):
            continue
        if skip(version, raw):
            continue
        if skip(config, raw):
            continue
        collected.append(item)
    return collected


def skip(items: list, raw: str) -> bool:
    if not items:
        return False
    if any((item in raw for item in items)):
        return False
    return True


def version_raw(raw: str):
    """\
    >>> version_raw('v3.2.5')
    '03_02_05'
    """
    # remove version prefix
    raw = raw[1:] if raw[0] == 'v' else raw
    parsed = semver.parse(raw)
    major = str(parsed['major']).zfill(2)
    minor = str(parsed['minor']).zfill(2)
    patch = str(parsed['patch']).zfill(2)
    result = f'{major}_{minor}_{patch}'
    return result


def name(version: str, config: str = 'default'):
    """\
    >>> name('v3.2.5')
    '03_02_05_default'
    """
    version = version_raw(version)
    return f'{version}_{config}'
