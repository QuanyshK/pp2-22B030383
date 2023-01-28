#tuples
tuple = ("apple", "banana", "cherry")
print(tuple)
#tuple2
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#tuple can be of any data  type
thistuple = (("apple", "banana", "cherry"))
print(thistuple)
#index
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#negative index
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
#range od index
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#range of negga index
histuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#with if
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

