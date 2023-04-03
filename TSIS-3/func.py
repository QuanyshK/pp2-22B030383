def fun(n):
    print(n * 28.3495231)
a = float(input())
fun(a)
#
def far(n):
    print((5/9)*(n-32))
a = int(input())
far(a)
#
def solve(h, l):
    for i in range(0, h):
        if (h-i)*4 + i*2 == l:
            print(i)
            print(h-i)
            break
h = int(input())
l = int(input())
solve(h, l)
#
def filter_prime(n):
    a = [int(n) for n in n.split()]
    for i in a:
        if int(i)%2 == 1:
            print(i, end=' ')
            
b = input()
print(filter_prime(b))
#
from itertools import permutations
def perm(strg):
    for i in list(permutations(strg)):
        print(i)
a = input().split()
perm(a)
#
def revers(s):
    res = s[::-1]
    print(res)
a = input().split()
revers(a)

#
def has3(n):
    if "3 3" in n:
        return True
    else:
        return False
a = input().split()
print(has3(a))
#
def spygame(n):
    for i in range(0, len(n)):
        if n[i] == 0:
            for x in range(i+1, len(n)):
                if n[x] == 0:
                    for y in range(x+1, len(n)):
                        if n[y] == 7:
                            print("True")
                else:
                    print("False")
a = input().split()
spygame(a)
#
import math
def vol(n):
    print((4/3)*3.14*n*n)
a = float(input())
vol(a)
#
def notset(n):
    ns2 = []
    for i in n:
        if i not in ns2:
            ns2.append(i)
    print(ns2, end = ' ')
a = input().split()
notset(a)
#
def pal(n):
    res = n[::-1]
    if n == res:
        return True
    else:
        return False
a= input()
pal(a)
#
def histo(n):
    for i in n:
        print("*"*int(i))
a = input().split()
histo(a)
#
import random
def game(a, rand, user, cnt):
    if a == rand:
        print("Good job,", user+"!", "You guessed my number in", cnt, "guesses!")
    elif a < rand:
        print("Your guess is too low.")
    else:
        print("Your guess is too more.")
user = input("Hello! What is your name?")
rand = random.randint(1, 12)
a = cnt = 0
print("Well,", user+",", "I am thinking of a number between 1 and 20.")
while a != rand:
    a = int(input("Take a guess."))
    cnt+=1
    game(a, rand, user, cnt)

