#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)
#syntax => newlist = [x for in fruits if x != "apple"]
newlist = [x for x in fruits if x != "apple"]
#iterable
newlist = [x for x in range(10) if x < 5]
#expression
newlist = [x.upper() for x in fruits]
newlist = ['hello' for x in fruits]
newlist = [x if x != "banana" else "orange" for x in fruits]
