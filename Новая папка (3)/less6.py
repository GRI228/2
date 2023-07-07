import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "http://www.cbr.ru/scripts/XML_daily.asp?"
today = datetime.today().strftime("%d/%m/%Y")
date = f"date_req={today}"
responce = requests.get(url+date)
xml = BeautifulSoup(responce.content, 'lxml')

def get_course(id):
    xml1 = xml.find("valute", {'id': id})
    return {"value": xml1.value.text, "nominal": xml1.nominal.text, "name": xml1.charcode.text}

str_to_num = {
    "1": "один",
    "2": "два",
}

file = open(r"/Users/klim/Desktop/Lesson6/Код/valutes.txt", 'a') # rwa
file.write(f"{today}\n")
for valute in ["R01235", "R01239", "R01375"]:
    temp_dict = get_course(valute)
    file.write(f"{round(float(temp_dict['value'].replace(',', '.')), 2)} рублей за {temp_dict['nominal']} за {temp_dict['name']}\n")
file.close()

# 123451