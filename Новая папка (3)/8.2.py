from tkinter import*
import requests
from bs4 import BeautifulSoup
from datetime import datetime

window = Tk()
window.title('Мое приложение')
window.geometry('500x500+200+200')

url = "http://www.cbr.ru/scripts/XML_daily.asp?"
today = datetime.today().strftime("%d/%m/%Y")
date = f"date_req={today}"
responce = requests.get(url+date)
xml = BeautifulSoup(responce.content, 'lxml')

def get_course(id):
    xml1 = xml.find("valute", {'id': id})
    return {"value": xml1.value.text, "nominal": xml1.nominal.text, "name": xml1.charcode.text}

img_logo = PhotoImage(file='bg_2.png')
logo = Label

file = open(r"/Users/klim/Desktop/Lesson6/Код/valutes.txt", 'a') # rwa
file.write(f"{today}\n")
for valute in ["R01235", "R01239", "R01375"]:
    temp_dict = get_course(valute)
    file.write(f"{round(float(temp_dict['value'].replace(',', '.')), 2)} рублей за {temp_dict['nominal']} за {temp_dict['name']}\n")
file.close()

count = 0

def change_label():
    global count
    count += 1
    lab['text']= count

lab = Label(window, text='Текст', bg='#f2a268', fg='#00000', font='16')
lab.place(x=100, y=100)

btn = Button(text='НАЖМИ МЕНЯ', background='#f2a268', fg='#00000', font='16', command=change_label)
btn.place(x=200, y=200)
window.mainloop()