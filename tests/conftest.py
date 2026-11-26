# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2023 by Helmut Konrad Schewe. All rights reserved.
# This file is property of Helmut Konrad Schewe. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import functools
import os

import configos
import hoverpower
import pytest
import utilo
from utilotest import mp  # pylint:disable=W0611
from utilotest import td  # pylint:disable=W0611

import qcon
import qview.config
from tests.cached_ import example  # pylint:disable=W0611

pytest_plugins = ['pytester', 'xdist']  # pylint: disable=invalid-name

os.environ['DEV_CACHED_ROOT'] = utilo.join('~', '.tmp/qcon/dev_cached')


def pytest_configure():
    tmpdir = utilo.tmpdir(qcon.ROOT)
    shared = utilo.join(tmpdir, 'shared')
    configos.export(
        shared,
        utilo.join(shared, 'todo'),
        utilo.join(shared, 'ready'),
    )
    # TODO: MOVE AFTER UPGRADING CONFIGS
    os.environ['SHARED_TMP'] = utilo.join(shared, 'tmp')
    configos.makedirs()


PACKAGE = qcon.PROCESS
hoverpower.setup(qcon.ROOT)

RESOURCES = [
    hoverpower.HOME025_PDF,
    hoverpower.ORDER009_PDF,
]

CACHED = os.path.join(hoverpower.generated(), 'dev_cached_root')
VERSIONS = ['10.1.0', '10.1.1', '10.1.2', '10.2.0']

qview.config.SYNC = True


def cached() -> bool:
    if not utilo.exists(CACHED):
        return False
    return len(utilo.file_list(CACHED)) > 0


require_cached = pytest.mark.skipif(not cached(), reason='require CACHED')


@pytest.mark.usefixtures('session')
def pytest_sessionstart():
    hoverpower.run()


def extract(files):
    os.makedirs(CACHED, exist_ok=True)
    # TODO: MOVE TO QUEUEMO?
    todo = [functools.partial(runme, source) for source in files]
    utilo.fork(
        *todo,
        worker=len(todo),
    )


def runme(source: str):
    outpath = hoverpower.link(source)
    cmd = f'queuemo_single -i {source} -o {outpath} --create'
    utilo.run(cmd, verbose=True)
    cmd = f'qcon -i {outpath} --root {CACHED} --publish'
    utilo.run(cmd, verbose=True)
    for version in VERSIONS:
        cmd = (f'qcon -i {outpath} --root {CACHED} --publish '
               f'--overwrite_version={version}')
        utilo.run(cmd, verbose=True)
