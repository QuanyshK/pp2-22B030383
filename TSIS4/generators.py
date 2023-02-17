def gen_square(n):
	for i in range(n):
		yield i**2
a = int(input())
square = gen_square(a)
for squ in square:
	print(squ)
#
def even(n):
    for i in range(n+1):
	    if i%2==0:
		    yield i
a = int(input())
x = even(a)
for h in x:
	print(h, end = ', ')
#
def even(n):
    for i in range(n+1):
	    if i%3==0 and i%4==0:
		    yield i
a = int(input())
x = even(a)
for h in x:
	print(h)
#
def squares(a, b):
	for i in range(a, b):
		yield i**2
c = int(input())
d = int(input())
s = squares(c, d)
for squa in s:
	print(squa)
#
def cdown(n):
	while n>=0:
		yield n
		n -= 1 
a = int(input())
x = cdown(a)
for v in x:
	print(v)