import requests
import xml.etree.ElementTree as ET
from datetime import datetime
import contextlib

URL = "http://www.cbr.ru/scripts/XML_daily.asp?"
today = datetime.today().strftime("%d/%m/%Y")
url = f"{URL}?date_req={today}"
responce = requests.get(url)
xml = ET.fromstring(responce.content)

valid_codes = ['USD', 'EUR', 'GBP', 'JPY', 'CHF', 'CNY']

@contextlib.contextmanager
def get_course_info(currency_id):
    valute = xml.find(f"./Valute[CharCode='{currency_id}']")
    if valute:
        currency = float(valute.find('Value').text.replace(",", "."))
        yield f"(1 шт.) {valute.find('Name').text} стоит(ят) {currency:.4f} руб."
    else:
        yield f"Ошибка: валюта {currency_id} не найдена"

currency_id = input("Введите код валюты: ")
if currency_id not in valid_codes:
    print("Неверный код валюты")
else:
    with get_course_info(currency_id) as currency:
        print(currency)
