from dataclasses import dataclass


@dataclass
class RentData:
    rent_time: str | None = None
    color: str | None = None
    date_to_deliver: str = '10.12.2022'
    comment: str = 'Комментарий создан автотестом'
