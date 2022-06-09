__version__ = "0.1.0"

"""
import mockframe as mf

shape: Shape = {
    "name": mf.Types.Name,
    "age": mf.Types.Age,
    "date": mf.Types.Date,
    "home": mf.Types.Address,
}

print(MockFrame(shape, rows=10))# standard pandas DataFrame
"""

from mockframe.core import MockFrame as MockFrame
from mockframe.provider import Types as Types
