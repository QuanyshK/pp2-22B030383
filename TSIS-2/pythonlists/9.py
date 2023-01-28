#copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#or
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#join lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#second way
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
#third way
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
