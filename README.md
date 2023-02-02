## mockframe

---

[Struggles with mocking and pandas](https://www.hiremepls.dev/blog/struggles_with_mocking_and_pandas)

```py
import mockframe as mf

shape: Shape = {
    "name": mf.Types.Name,
    "age": mf.Types.Age,
    "date": mf.Types.Date,
    "home": mf.Types.Address,
}

print(MockFrame(shape, rows=10)) # standard pandas DataFrame
```
