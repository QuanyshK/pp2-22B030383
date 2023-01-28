#append elements
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#insert
thislist = ["apple", "banana", "orange"]
thislist.insert(1, "orange")
print(thislist)
#extend
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#add any iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)