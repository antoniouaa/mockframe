from typing import TypeVar

import pandas

from mockframe.provider import fake

T = TypeVar("T")
Shape = dict[str, T]


def MockFrame(shape: Shape, rows: int = 100) -> pandas.DataFrame:
    data = {heading: mock_column(col, rows) for heading, col in shape.items()}

    df = pandas.DataFrame(data)
    return df.convert_dtypes()


def mock_column(t: T, length: int) -> tuple[list[T], T]:
    if length <= 0:
        return []

    try:
        col = list(fake.pylist(length, False, [t]))
    except AttributeError:
        col = [t() for _ in range(length)]

    return list(col)
