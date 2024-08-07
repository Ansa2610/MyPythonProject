# number = input()
# cherry = 2.5
# cost = 38
# fin = int(number) - int(cherry * cost)
# print(fin)

# cost = int(input())
# weight = int(input())
# customer = int(input())
# money = int(customer) - int(cost * weight)
# print(money)


# name = input()
# cost = int(input())
# weight = int(input())
# customer = int(input())
# print('Чек')
# print(f'{name} - {weight}кг - {cost}руб/кг')
# print(f'Итого: {cost*weight}руб')
# print(f'Внесено: {customer}руб')
# print(f'Сдача: {customer-cost*weight}руб')

# x = int(input())
# print(x * 'Купи слона!\n')

# x = int(input())
# y = input()
# print(x * (f'Я больше никогда не буду писать "{y}"!\n'))

# n = int(input())
# m = int(input())
# x = int(n * m / 2)
# print(x)

# color = input()
# match color:
#     case 'красный' | 'жёлтый':
#         print('Стоп.')
#     case 'зелёный':
#         print('Можно ехать.')
#     case _:
#         print('Некорректное значение.')

# a = 1234
# b = a //1000 % 10
# print(b)

# a = input()
# print(a)
# print(a)
# print(a)

# a = int(input())
# b = int(input())
# c = a + b // 1000 % 10
# print(c)

# print(5 * 5)
# print(5 **5)
# print(5 / 5)
# print(5 // 5)
# print(5 % 5)

# k = int(input("Введите количество чисел: "))
# n = int(input("Введите конец без вклюения диапазона: "))
# for i in range(k, n):
#     print(i)

# list = (1, 2,3, 4, 5)
# for i in list:
#     print(i)

# for letter in 'table':
#     if letter == 'r':
#         break
#     print(letter)

# name = input("Как Вас зовут? ")
# x = input("Как дела? ")
# print("Здравствуйте, ", name)
# if "хорошо" in x:
#     print("Я за вас рада!")
# else:
#     print("Всё наладится!")

# name = input("Как Вас зовут? \n")
# print(f'Здравствуйте, {name}!')
# x = input("Как дела? \n")
# if "хорошо" in x:
#     print("Я за вас рада!")
# else:
#     print("Всё наладится!")
#
# from dis import dis
#
#
# def some_func():
#     a = 'I am from modul 2'
#     print('I am from modul 2')
#     return a

class Person:
    def __init__(self, name, age, car, status):
        self.name = name
        self.age = age
        self.car = car
        self.status = status
#
# tom = Person('Tom', 22, 'Toyota', 'Single')
# ann =Person('Ann', 25, 'Mercedes', 'Married')
# print(tom.name, tom.age, tom.car, tom.status)
# print(ann.name, ann.age, ann.car, ann.status)
#
# tom.age = 35
# print(tom.name, tom.age, tom.car, tom.status)

# class Person:
#     def say_hello(self):
#         print('Hello, I am happy')
#
# tom = Person()
# ann = Person()
# tom.say_hello()
# ann.say_hello()

# class Person:
#
#     def __init__(self, name, age):
#         self.name = name  # имя человека
#         self.age = age  # возраст человека
#
#     def display_info(self):
#         print(f"Name: {self.name}  Age: {self.age}")
#
#
# tom = Person("Tom", 22)
# tom.display_info()  # Name: Tom  Age: 22
# ann = Person('Anna', 23)
# ann.display_info()

for char in 'Python':
    print(char)
