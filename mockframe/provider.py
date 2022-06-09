import datetime
from typing import Callable
from dataclasses import dataclass

from faker import Faker
from faker.providers import python as faker_python, person, date_time


fake = Faker()
fake.add_provider(faker_python)
fake.add_provider(person)
fake.add_provider(date_time)


@dataclass
class Types:
    Name: str = fake.name
    Address: str = fake.address
    Date: datetime.datetime = fake.date_object
    Age: Callable = staticmethod(lambda: fake.unique.random_int(min=1, max=110))
