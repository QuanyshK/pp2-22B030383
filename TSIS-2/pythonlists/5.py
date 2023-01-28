#remove spec item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#same but with index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#pop() can removes last item if you dont have specify ind
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#same but with del
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#clear the list
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)