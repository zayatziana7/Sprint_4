from dataclasses import dataclass

all_accordions = []


@dataclass
class ImportantQuestionAccordion:
    number: int
    question: str
    answer: str

    def __post_init__(self):
        all_accordions.append(self)


how_much_accordion = ImportantQuestionAccordion(
    number=0,
    question='Сколько это стоит? И как оплатить?',
    answer='Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
)
want_few_accordion = ImportantQuestionAccordion(
    number=1,
    question='Хочу сразу несколько самокатов! Так можно?',
    answer='Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто'
           ' сделать несколько заказов — один за другим.'
)
how_to_calculate_rent_time_accordion = ImportantQuestionAccordion(
    number=2,
    question='Как рассчитывается время аренды?',
    answer='Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды'
           ' начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30,'
           ' суточная аренда закончится 9 мая в 20:30.'
)
today_order_accordion = ImportantQuestionAccordion(
    number=3,
    question='Можно ли заказать самокат прямо на сегодня?',
    answer='Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
)
update_order_accordion = ImportantQuestionAccordion(
    number=4,
    question='Можно ли продлить заказ или вернуть самокат раньше?',
    answer='Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
)
recharger_accordion = ImportantQuestionAccordion(
    number=5,
    question='Вы привозите зарядку вместе с самокатом?',
    answer='Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без'
           ' передышек и во сне. Зарядка не понадобится.'
)
cancel_order_accordion = ImportantQuestionAccordion(
    number=6,
    question='Можно ли отменить заказ?',
    answer='Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
)
mcad_accordion = ImportantQuestionAccordion(
    number=7,
    question='Я жизу за МКАДом, привезёте?',
    answer='Да, обязательно. Всем самокатов! И Москве, и Московской области.'
)
