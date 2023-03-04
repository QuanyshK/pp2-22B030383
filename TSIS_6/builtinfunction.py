from functools import reduce
a = input()
calc = [int(i) for i in a.split()]
b = reduce(lambda x, y: x * y, calc)
print(b)
#
a = str(input())
print("upper:", sum( i.isupper() for i in a), "lower:", sum(i.islower() for i in a))
#
a = str(input())
b = reversed(a)
if list(a) == list(b):
    print("Palindrome")
else:
    print("Not palindrome")
# 
import time
import math
a = int(input())
msec = int(input())
time.sleep(msec/1000)
print("Square root of", a, "after", msec, "miliseconds is", a**0.5)
#
a2 = (0, True)
print( all(a2))
