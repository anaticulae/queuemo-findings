# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
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
    document = pickle.loads(raw)  # nosec
    return document


def dump_result(document: cached.CachedResult, root: str) -> str:
    named = name(version=document.version, config=document.config)
    parent = os.path.join(root, document.document)
    path = os.path.join(parent, named)
    os.makedirs(parent, exist_ok=True)  # create parent
    utila.debug(f'write: {path}')
    dumped = cached.dumps(document)
    utila.file_create_binary(path, dumped)
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
    return document


def dump_root(documents: cached.CachedResults, root: str):
    assert os.path.exists(root), str(root)
    if isinstance(documents, cached.CachedResult):
        documents = [documents]
    for document in documents:
        dump_result(document, root)


def load_root(
        root: str,
        document: str = None,
        version: str = None,
        config: str = None,
) -> cached.CachedResults:
    result = []
    for item in collect_root(root, document, version, config):
        item = os.path.join(root, item)
        raw = utila.file_read_binary(item)
        loaded = loads(raw)
        result.append(loaded)
    return result


def collect_root(
        root: str,
        document: str = None,
        version: str = None,
        config: str = None,
) -> 'paths':
    collected = []
    version = version_raw(version) if version else None
    for item in utila.file_list(root):
        raw = str(item)
        if document and document not in raw:
            continue
        if version and version not in raw:
            continue
        if config and config not in raw:
            continue
        collected.append(item)
    return collected


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
