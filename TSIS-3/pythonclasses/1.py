#1
class Class:
    x = 5
#2
p1 = Class()
print(p1.x)
#3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)
#5
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)
print(p1)
#6
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
p1 = Person("John", 36)
print(p1)
#7
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def func(self):
        print("Hello mni " + self.name)
p1 = Person("John", 36)
p1.func()
#8
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age
  def myfunc(abc):
    print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()
#9 modify
p1.age = 40
#10 delete
del p1
#11
class Person:
  pass



