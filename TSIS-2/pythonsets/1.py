#set
set2 = {"apple", "banana", "cherry"}
print(set2)
# set unordered and unchangebled and quplicates not allowed
set2 = {"apple", "banana", "cherry", "apple"}
print(set2)
#same situation with data types, length
#constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
#access items
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
#add
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
#add sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
#add any iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
#remove elements
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
#
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
#

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()
print(x)
print(thisset)
#
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
#
x = {"apple", "banana", "cherry"}
del x
print(x)
#for loop
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)
#join two sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) #or set3.update(set name)
print(set3)
#keep only duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
#
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)