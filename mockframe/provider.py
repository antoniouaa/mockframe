import decimal
import datetime
from typing import Callable
from dataclasses import dataclass

from faker import Faker
from faker.providers import python as faker_python, person, date_time, geo, internet

PROVIDERS = [faker_python, person, date_time, geo, internet]

fake = Faker()
for provider in PROVIDERS:
    fake.add_provider(provider)


@dataclass
class Types:
    Name: str = fake.name
    Address: str = fake.address
    Date: datetime.datetime = fake.date_object
    Age: Callable = staticmethod(lambda: fake.random.randint(1, 110))
    Latitude: decimal.Decimal = fake.latitude
    Longitude: decimal.Decimal = fake.longitude
    Email: str = fake.ascii_email
