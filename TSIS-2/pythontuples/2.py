#change
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#add

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#remove
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
#unpacking a tuple
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
#using asterisk
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#loops in tuples same of lists
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1
#or
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#we can join two tuples and multiply
tuple = ("a", "v", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple + tuple2
print(tuple3)
#and
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)