#with for
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
#loop through the ind
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])
#with while
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
#
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
