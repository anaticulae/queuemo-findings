# =============================================================================
# C O P Y R I G H T
# -----------------------------------------------------------------------------
# Copyright (c) 2021 by Helmut Konrad Fahrendholz. All rights reserved.
# This file is property of Helmut Konrad Fahrendholz. Any unauthorized copy,
# use or distribution is an offensive act against international law and may
# be prosecuted under federal law. Its content is company confidential.
# =============================================================================

import dataclasses
import typing


@dataclasses.dataclass
class CachedFinding:
    msgid: str = None
    page: int = None


CachedFindings = typing.List[CachedFinding]


@dataclasses.dataclass
class CachedResult:
    document: str = None
    version: str = None
    config: str = None
    findings: CachedFindings = dataclasses.field(default_factory=list)

    def __len__(self):
        return len(self.findings)

    def __getitem__(self, index):
        return self.findings[index]  # pylint:disable=E1136


CachedResults = typing.List[CachedResult]
