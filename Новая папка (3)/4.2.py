'''from tkinter import*
import random

class Knight:
    def _init_(self, h):
        self.x = 70
        self.y = h // 2
        self.v = 0
        self.photo = PhotoImage(file='knight.png')

    def up(self, event):
        self.v = 3

    def down(self, event):
        self.v = -3

    def stop(self, event):
        self.v = 0

    
window = Tk()

w = 600
h = 600

window.geometry(str(w)+'x'+str(h))
canvas = Canvas(window, width=h, height=h)
canvas.place(in_=window, x=0, y=0)
bg_photo = PhotoImage(file='bg_2.png')
canvas.create_image(300, 300, image=bg_photo)

knight = Knight(h)

def game():
    canvas.delete('all')
    canvas.create_image(300, 300, image=bg_photo)
    
    canvas.create_image(knight.x, knight.y, image='knight.photo')
    knight.y  += khight.v

    canvas.create_image(knight.x, knight.y, image='dragon.photo')
    dragon.x -= dragon.v

    a = ()


    
window.bind('<Key-Up>', knight.up)
window.bind('<Key-Down>', knight.down)
window.bind('<KeyRelease>', knight.stop)


window.mainloop()'''

from tkinter import*

class Image(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Прямоугольники и треугольники")
        self.pack
        c = Canvas(self)
        c.create_line(10, 10, 100, 100, 150, 50, 10, 10,fill="#1f1", width=2)
        #c.create_line(150, 10, 150, 100, 180, 200, 150, 10, fill="#2e2", width=2)
        #c.create_line(250, 110, 350, 150, 280, 200, 250, 110, fill="#2e2", width=2)

        c.create_rectangle(230, 10, 290, 60,outline="#f11", fill="#1f1", width=2)
        c.create_rectangle(20, 110, 90, 160,outline="#f11", fill="#1f1", width=2)
        c.pack(fill=BOTH, expand=True)

w = Tk()

f = Image()
w.geometry('400x250')


w.mainloop()
