#==============================================================================
# C O P Y R I G H T
#------------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
#==============================================================================

import utila

import cached
import qcon
import qcon.cmd.list
import qcon.cmd.publish

CMD = [
    utila.Command(
        longcut='publish',
        message='collect results and merge to database',
    ),
    utila.Command(
        longcut='list',
        message='list results in data base',
    ),
    utila.Parameter(
        longcut='root',
        message=f'cache directory to write dumps(default:{cached.root()})',
    ),
    utila.Parameter(
        longcut='overwrite_version',
        message='overwrite or define queuemo version of collected file',
    ),
]


@utila.saveme
def main():
    parser = utila.create_parser(
        todo=CMD,
        version=qcon.__version__,
        config=utila.ParserConfiguration(
            outputparameter=False,
            inputparameter=True,
            cacheflag=False,
            pages=False,
            waitingflag=False,
        ),
    )
    args = utila.parse(parser)
    inputpath, _ = utila.sources(args)  # pylint:disable=W0612,W0632

    root = args.get('root', None)
    if not root:
        root = cached.root()
    overwrite_version = args.get('overwrite_version', None)
    if args.get('publish'):
        returncode = qcon.cmd.publish.run(
            inputpath,
            root,
            overwrite_version=overwrite_version,
        )
        if returncode:
            return returncode
    if args.get('list'):
        returncode = qcon.cmd.list.run(root)
        if returncode:
            return returncode
    return utila.SUCCESS
