#for loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
#through a string
for x in "banana":
    print(x)
#with break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
#with continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:

    if x == "banana":
       continue
    print(x)
#with range()
for x in range(2, 30, 3):
    print(x)
#
for x in range(2, 6):
  print(x)
#with else
for x in range(6):
    print(x)
else:
    print("finally.")
#nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
#
for x in [0, 1, 2]:
    pass