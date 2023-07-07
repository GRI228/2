# class Singleton(object):
#     def __new__(cls):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(Singleton, cls).__new__(cls)
#         return cls.instance

# s = Singleton()
# print("Object created", s, id(s))
# s1 = Singleton()
# print("Object created", s1, id(s1))

from datetime import datetime

def timedelta(func):
    def wrapper(val):
        start = datetime.now()
        res = func(val)
        end = datetime.now()
        print(f"time: {end-start}")
        return res
    return wrapper

@timedelta
def get_list_1(val):
    return [i for i in range(val + 1) if i % 2 == 0]

@timedelta
def get_list_2(val):
    new_list = []
    for i in range(val+1):
        if i % 2 == 0:
            new_list.append(i)
    return new_list

val = 1000000

a = get_list_1(val)
b = get_list_2(val)