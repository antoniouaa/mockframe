from decimal import Decimal
import re
import datetime

import numpy
import pytest

from mockframe import MockFrame, Types


@pytest.fixture
def shape():
    return {
        "date": Types.Date,
        "name": Types.Name,
        "address": Types.Address,
        "age": Types.Age,
        "email": Types.Email,
        "lat": Types.Latitude,
        "lon": Types.Longitude,
    }


def test_is_dataframe(shape):
    df = MockFrame(shape)

    assert df.__class__.__name__ == "DataFrame"
    assert df.shape == (100, len(shape))


def test_cols_are_of_type(shape):
    types = {
        "date": datetime.date,
        "name": str,
        "address": str,
        "age": numpy.int64,
        "email": str,
        "lat": Decimal,
        "lon": Decimal,
    }

    df = MockFrame(shape)
    for label, t in types.items():
        print(df[label].to_list())
        assert all(isinstance(val, t) for val in df[label].to_list())


def test_name_has_at_least_one_space(shape):
    df = MockFrame(shape)
    df["name_test"] = df["name"].str.count(" ")

    assert (df["name_test"] >= 1).all()


def test_age_within_limits(shape):
    df = MockFrame(shape)

    assert (df["age"] < 110).all()
    assert (df["age"] >= 1).all()


def test_email_passes_regex(shape):
    df = MockFrame(shape)

    pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")
    for email in df["email"].to_list():
        assert pattern.match(email)
