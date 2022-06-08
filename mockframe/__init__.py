__version__ = "0.1.0"

"""
import mockframe as mf

shape = {
    "name": mf.Name,
    "address": mf.Address,
    "age": mf.Age,
    "text": mf.Text,
    "phone": mf.PhoneNumber,
}

mocked = mf.MockFrame(shape) # standard pandas DataFrame
"""

from mockframe.core import MockFrame as MockFrame
