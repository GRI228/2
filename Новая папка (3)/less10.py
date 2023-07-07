# Модификаторы доступа
# public - можно читать, можно записывать
# private __ - нельзя читать и записывать
# protected 

"""
class Human:

    def __init__(self, name, sex, age, height, weight):
        self.__name = name
        self.__sex = sex
        self.age = age
        self.height = height
        self.weight = weight

    def set_name(self, name):
        self.__name = name

    def get_sex(self):
        return self.__sex

human1 = Human("Klim", "Male", 19, 175, 62)
human1.__sex = "Helicopter"
print(human1.get_sex())
"""

import random

class Tank:
    def __init__(self, model, armor, health, min_damage, max_damage):
        self.model = model
        self.armor = armor
        self.damage = random.randint(min_damage, max_damage)
        self.health = health

    def print_info(self):
        print(f"{self.model} имеет лобовую броню {self.armor}мм при {self.health} ед. здоровья и может нанести {self.damage} урона")

    def shot(self, enemy):
        if enemy.health <= 0:
            print(f"Экипаж танка {enemy.model} уничтожен")
        else:
            print(f"{self. model} сделал выстрел в {enemy.model}")
            enemy.health_down(self.damage)

    def health_down(self, damage):
        self.health -= damage
        self.print_info()

class SuperTank(Tank):
    def __init__(self, model, armor, health, min_damage, max_damage):
        super().__init__(model, armor, health, min_damage, max_damage)
        self.force_armor = True

    def health_down(self, damage):
        super().health_down(damage / 2)

tank1 = Tank("T-34", 90, 100, 20, 30)
tank2 = Tank("Tiger", 120, 100, 50, 120)
tank3 = SuperTank("CoolTank", 200, 100, 50, 70)
tank1.shot(tank2)
tank1.shot(tank3)