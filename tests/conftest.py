# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import functools

import power
import pytest
import utila

import qcon
from tests.cached_ import example  # pylint:disable=W0611

pytest_plugins = ['pytester', 'xdist']  # pylint: disable=invalid-name

PACKAGE = qcon.PROCESS
power.setup(qcon.ROOT)

RESOURCES = [
    power.ORDER009_PDF,
    power.HOME025_PDF,
]


@pytest.mark.usefixtures('session')
def pytest_sessionstart():
    power.run()


def extract(files):
    # TODO: MOVE TO QUEUEMO?
    todo = []
    for source in files:

        def runme(source=source):
            outpath = power.link(source)
            cmd = f'queuemo_single -i {source} -o {outpath} --create'
            utila.log(cmd)
            utila.run(cmd)

        todo.append(functools.partial(runme, source))
    utila.fork(*todo, worker=4)
