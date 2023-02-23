import re
pat = r'a+b*'
s = input()
x = re.search(pat, s)
if x:
    print("yeeee buddy")
else:
    print("Mauricio, I cant... I cant move it move it")
#
import re
pat1 = r'a{1}b{2,3}'

b = input()
x = re.search(pat1, b)

if x:

    print("OMAEWA MOU SHINDEIRU")
else:
    print("NUNI?!")
#
import re 
pat = r'[a-z]+_[a-z]+'
s = input()
x = re.findall(pat, s)
print(x)
#
import re
pat = r'[A-Z]+[a-z]+'
s = input()
x = re.findall(pat, s)
print(x)
#
import re
pat = r'a+[a-z]+b'
s = input()
x = re.search(pat, s)
if x:
    print("AY YO")
else:
    print("Something in the way...")
#
import re
s = input()
x = re.sub("[ ,.]", ":", s)
print(x)
#
import re
s = input()
x = re.sub("_","",s)
print(x)
#
import re
s = input()
x = re.split(r'(?<!^)(?=[A-Z])', s)
print(x)
#
import re 
s = input()
pat = r'(?<=\w)(?=[A-Z])'
x = re.sub(pat, ' \1', s).strip()
print(x)
#
import re
s = input()
x = re.sub(r'(?<!^)(?=[A-Z])', '_', s)
print(x)
