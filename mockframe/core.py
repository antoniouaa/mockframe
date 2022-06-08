from typing import Optional, Dict

import pandas
import faker
from faker.providers import python as faker_python

Shape = Dict[str, type]


@pandas.api.extensions.register_dataframe_accessor("mock")
class MockFrameAccessor:
    def __init__(self, frame: pandas.DataFrame) -> None:
        self._obj = frame
        self._fake = faker.Faker()
        self._fake.add_provider(faker_python)

    def __call__(self, shape: Shape, rows: int) -> pandas.DataFrame:
        self._shape = shape
        values = {}
        for column, type_ in self._shape.items():
            values[column] = self._fake.pylist(rows, False, type_)

        return pandas.DataFrame(data=values)


def MockFrame(shape: Shape, rows: Optional[int] = 100) -> pandas.DataFrame:
    return pandas.DataFrame().mock(shape, rows)
