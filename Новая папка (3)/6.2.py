import requests
from bs4 import BeautifulSoup
import datetime

url = 'http://www.cbr.ru/scripts/XML_daily.asp?'
today = datetime.datetime.today()
today = today.strftime('%d/%m/%Y')
date = f'date_req={today}'
responce = requests.get(url+date)
xml = BeautifulSoup(responce.content, 'lxml')

def get_course(id):
    return xml.find('valute', {'id': id}).value.text

print(get_course('R01235'), 'рублей за 1 доллар')
print(get_course('R01239'), 'рублей за 1 евро')
print(get_course('R01375'), 'рублей за 10 юаней')
print(get_course('R01035'), 'рублей за 1 фунт')
print(get_course('R01090B'), 'рублей за 1 белорусский рубль')


'''from tkinter import*

window = Tk()
window.geometry = ('700x500')
window.title = ('ABC')'''

'''from tkinter import*

class Image(Frame):
    def __init__(self):
        # Инициализирую предка этого класса
        Frame.__init__(self)
        # Устанавливаю заголовок окна
        self.master.title("Прямоугольники и треугольники")
        # Размещаю на всё окно рамку
        self.pack(fill=BOTH, expand=True)

        # Создаю объект для рисования (Canvas) по рамке (self)
        c = Canvas(self)
        # Создаю 3 треугольника. Толщина линии - 2 пикселя
        c.create_line(10, 10, 100, 100, 150, 50, 10, 10,
                      fill="#1f1", width=2)
        c.create_line(150, 10, 150, 100, 180, 200, 150, 10,
                      fill="#2e2", width=2)
        c.create_line(250, 110, 350, 150, 280, 200, 250, 110,
                      fill="#2e2", width=2)

        # Рисую 2 прямоугольника.
        c.create_rectangle(230, 10, 290, 60,
                           outline="#f11", fill="#1f1", width=2)
        c.create_rectangle(20, 110, 90, 160,
                           outline="#f11", fill="#1f1", width=2)
        # Размещаю нарисованное на всё окно
        c.pack(fill=BOTH, expand=True)

    # Создаю главное окно


w = Tk()
# Создаю изображение, которое описано выше
f = Image()

# Устанавливаю размер основного окна
w.geometry("400x250")
# Запускаю главный цикл обработки событий
w.mainloop()'''


