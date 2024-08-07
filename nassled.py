class Human:
    head = True
    _legs = True
    _arms = True

    def say_hello(selfs):
        print('Hello')


    def about(self):
        print(self.head)
        print(self._arms)
        print(self._legs)

class Student(Human):
    
#    head = False
#     def about(self):
#         print('I am a student')
    pass
class Teacher(Human):
    pass

human = Human()
human.about()
student = Student()
student.about()
print(dir(human))
print(dir(student))
#  print(student.head)