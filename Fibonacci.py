# def fib():
#     a, b = 1, 1
#     while True:
#         yield a
#         a, b = b, a + b
#
#
# for index, x in enumerate(fib()):
#     if index == 10:
#         break
#     print("%s" % x)
#

class MyClass:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

# p1 = MyClass('Biology', '1 semestr')
# print(p1.name)
# print(p1.duration)

    def __str__(self):
        return f'{self.name}({self.duration})'

p1 = MyClass('Biology', '1 semestr')
print(p1)