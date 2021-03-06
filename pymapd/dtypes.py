"""
https://www.python.org/dev/peps/pep-0249/#type-objects
"""
import datetime
import time
from typing import Any, List

from mapd import MapD


T = MapD.TDatumType


class DataType:

    def __init__(self, matches):
        # type: (List[Any]) -> None
        self._matches = set(matches)

    def __eq__(self, other):
        # type: (Any) -> bool
        return other in self._matches

    def __ne__(self, other):
        # type: (Any) -> bool
        return not (self == other)

    def __hash__(self):
        # type: () -> int
        return hash(tuple(self._matches))


Binary = memoryview
Date = datetime.date
Time = datetime.time
Timestamp = datetime.datetime

BINARY = DataType([])
STRING = DataType([T.STR, T.POINT, T.LINESTRING, T.POLYGON,
                   T.MULTIPOLYGON, T.GEOMETRY, T.GEOGRAPHY])
NUMBER = DataType([T.SMALLINT, T.INT, T.BIGINT, T.FLOAT, T.DECIMAL, T.DOUBLE,
                   T.BOOL, T.TINYINT])
DATETIME = DataType([T.DATE, T.TIME, T.TIMESTAMP])
ROWID = DataType([])


def DateFromTicks(ticks):
    # type: (int) -> Date
    return Date(*time.localtime(ticks)[:3])


def TimeFromTicks(ticks):
    # type: (int) -> Time
    return Time(*time.localtime(ticks)[3:6])


def TimestampFromTicks(ticks):
    # type: (int) -> Timestamp
    return Timestamp(*time.localtime(ticks)[:6])
