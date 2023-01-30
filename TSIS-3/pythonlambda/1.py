x = lambda a : a +10
print(x(5))
#2
x = lambda a, b : a * b
print(x(5, 6))
#3
def func(n):
    return lambda a : a * n
doubler = func(2)
print(doubler(11))
#4
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))