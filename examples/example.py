import mockframe as mf

df = mf.MockFrame(
    {
        "name": mf.Types.Name,
        "address": mf.Types.Address,
        "age": mf.Types.Age,
        "email": mf.Types.Email,
    }
)


print(df.dtypes)
