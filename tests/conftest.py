# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021-2022 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import functools
import os

import power
import pytest
import utila

import qcon
import qview.config
from tests.cached_ import example  # pylint:disable=W0611

pytest_plugins = ['pytester', 'xdist']  # pylint: disable=invalid-name

PACKAGE = qcon.PROCESS
power.setup(qcon.ROOT)

RESOURCES = [
    power.ORDER009_PDF,
    power.HOME025_PDF,
]

CACHED = os.path.join(power.generated(), 'dev_cached_root')
VERSIONS = ['10.1.0', '10.1.1', '10.1.2', '10.2.0']

qview.config.SYNC = True


@pytest.mark.usefixtures('session')
def pytest_sessionstart():
    power.run()


def extract(files):
    os.makedirs(CACHED, exist_ok=True)
    # TODO: MOVE TO QUEUEMO?
    todo = []
    for source in files:
        todo.append(functools.partial(runme, source))
    utila.fork(*todo, worker=4)


def runme(source: str):
    outpath = power.link(source)
    cmd = f'queuemo_single -i {source} -o {outpath} --create'
    utila.run(cmd, verbose=True)
    cmd = f'qcon -i {outpath} --root {CACHED} --publish'
    utila.run(cmd, verbose=True)
    for version in VERSIONS:
        cmd = (f'qcon -i {outpath} --root {CACHED} --publish '
               f'--overwrite_version={version}')
        utila.run(cmd, verbose=True)
