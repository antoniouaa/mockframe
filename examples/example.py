import mockframe as mf

df = mf.MockFrame(
    {
        "name": mf.Types.Name,
        "address": mf.Types.Address,
        "age": mf.Types.Age,
    }
)
print(df.dtypes)

import pandas as pd

assert isinstance(df, pd.DataFrame)
assert df.shape == (100, 3)
assert df["name"].dtype == "string"
assert df["address"].dtype == "string"
assert df["age"].dtype == "Int64"
