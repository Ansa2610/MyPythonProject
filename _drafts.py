# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return '({0}, {1})'.format(self.x, self.y)
#
# p1 = Point(2, 3)
# p2 = Point(4, 5)
# print(p1)

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

dog1 = Dog('Barney', 12)
dog2 = Dog('Mustik', 3)
print(dog1 > dog2)

