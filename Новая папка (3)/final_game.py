from tkinter import *
import random

window = Tk()

w = 600
h = 600
window.resizable(width=False, height=False)

window.geometry(str(w) + 'x' + str(h))

# Холст для отрисовки игрового поля
canvas = Canvas(window, width=w, height=h)
canvas.place(in_=window, x=0, y=0)


# Фон для игры
bg_photo = PhotoImage(file='bg_2.png')

# Персонаж
class Knight:
    def __init__(self):
        self.x = 70
        self.y = h // 2
        self.v = 0
        self.v_x = 0
        self.photo = PhotoImage(file='knight.png')
# Движение
    def up(self, event):
        self.v = -3

    def down(self, event):
        self.v = 3

    def right(self, event):
        self.v_x = 3

    def left(self, event):
        self.v_x = -3

    def stop(self, event):
        self.v = 0
        self.v_x = 0

    # Дракон
class Dragon:
    def __init__(self):
        self.x = 750
        self.y = random.randint(100, 500)
        self.v = random.randint(1,3)
        self.photo = PhotoImage(file='dragon.png')

knight = Knight()

dragons = []
for i in range(3):
    dragons.append(Dragon())

def game():
    canvas.delete('all')
    canvas.create_image(300,300, image=bg_photo)
    canvas.create_image(knight.x,knight.y,image=knight.photo)
    knight.y += knight.v
    knight.x += knight.v_x

    if knight.y < 0:
        knight.y = 0
    if knight.y > h - 50:
        knight.y = h - 50
    if knight.x > 600:
        knight.x = 600
    if knight.x < 5:
        knight.x = 5


    current_dragon = 0
    dragon_to_kill = -1

    for dragon in dragons:
        dragon.x -= dragon.v
        canvas.create_image(dragon.x,dragon.y,image=dragon.photo)
        # Проверка столкновений
        if ((dragon.x-knight.x)**2) + ((dragon.y - knight.y)**2) <= (96)**2:
            dragon_to_kill = current_dragon

        current_dragon += 1

        if dragon.x <= 0:
            canvas.delete('all')
            canvas.create_text(w//2, h//2, text="You lose!", font="Verdana 42", fill='red')
            break


    if dragon_to_kill >= 0:
        del dragons[dragon_to_kill]

    # Условие выигрыша
    if len(dragons) == 0:
        canvas.delete('all')
        canvas.create_text(w//2, h//2, text="You win!", font="Verdana 42", fill='red')
    else:
        window.after(5, game)


game()

window.bind('<w>', knight.up)
window.bind('<s>', knight.down)
window.bind('<KeyRelease>', knight.stop)
window.bind('<d>', knight.right)
window.bind('<a>', knight.left)

window.mainloop()
