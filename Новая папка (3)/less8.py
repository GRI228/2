from tkinter import *
import requests
from bs4 import
from datetime import datetime

window = Tk()
window.title("Курс валют")
window.geometry("400x350+300+300")
window.resizable(width=False, height=False)

url = "http://www.cbr.ru/scripts/XML_daily.asp?"
today = datetime.today().strftime("%d/%m/%Y")
date = f"date_req={today}"
responce = requests.get(url+date)
xml = BeautifulSoup(responce.content, 'lxml')

def get_course(id):
    xml1 = xml.find("valute", {'id': id})
    return {"value": xml1.value.text, "nominal": xml1.nominal.text, "name": xml1.charcode.text}

img_logo = PhotoImage(file='logo.png')
logo = Label(window, image=img_logo)
logo.place(x=0, y=0)

lab = Label(window, text="Курс валют\n НАШ банк", fg="black", font="Arial 22")
lab.place(y=25, x=150)

course_info = Label(window, text=f"Курс валют на: {today.replace('/', '.')}", font="Arial 18")
course_info.place(y=150, x=90)

usd_dict = get_course("R01235")
usd_dict["value"] = float(usd_dict["value"].replace(',', '.'))
usd_dict["nominal"] = int(usd_dict["nominal"])
usd_course = Label(window, text=f"${round(usd_dict['value']/usd_dict['nominal'], 2)}", font="Arial 18")
usd_course.place(y=190, x=100)

usd_dict = get_course("R01375")
usd_dict["value"] = float(usd_dict["value"].replace(',', '.'))
usd_dict["nominal"] = int(usd_dict["nominal"])
usd_course = Label(window, text=f"¥{round(usd_dict['value']/usd_dict['nominal'], 2)}", font="Arial 18")
usd_course.place(y=240, x=100)
# file = open(r"/Users/klim/Desktop/Lesson6/Код/valutes.txt", 'a') # rwa
# file.write(f"{today}\n")
# for valute in ["R01235", "R01239", "R01375"]:
#     temp_dict = get_course(valute)
#     file.write(f"{round(float(temp_dict['value'].replace(',', '.')), 2)} рублей за {temp_dict['nominal']} за {temp_dict['name']}\n")
# file.close()

window.mainloop()