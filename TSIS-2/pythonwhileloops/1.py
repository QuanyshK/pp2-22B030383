#while loops
i = 1
while i < 6:
    print(i)
    i+=1
#with break
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i+=1
#continue
i = 0
while i<6:
    i+=1
    if i ==3:
        continue
    print(i)
#with else
i = 1
while i< 6:
    print(i)
    i+=1
else:
    print("i is not longer than 6")