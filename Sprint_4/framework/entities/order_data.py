from dataclasses import dataclass

from framework.entities.rent_data import RentData


@dataclass
class OrderData:
    name: str
    surname: str
    address: str
    metro_station: str
    rent_data: RentData
    phone_number: str = '89111111111'


default_order = OrderData(
    name='Петя',
    surname='Петров',
    address='Адрес для автотестов',
    metro_station='Бульвар Рокоссовского',
    rent_data=RentData()
)
