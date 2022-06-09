## mockframe

---

[Struggles with mocking and pandas](https://hiremepls.vercel.app)

```py
import mockframe as mf

shape: Shape = {
    "name": mf.Types.Name,
    "age": mf.Types.Age,
    "date": mf.Types.Date,
    "home": mf.Types.Address,
}

print(MockFrame(shape, rows=10))# standard pandas DataFrame
```
