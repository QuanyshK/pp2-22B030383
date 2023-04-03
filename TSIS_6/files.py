import os

path = input()
print("Directories:")
for dir_name in os.listdir(path):
    if os.path.isdir(os.path.join(path, dir_name)):
        print(dir_name)
print("\nFiles:")
for file_name in os.listdir(path):
    if os.path.isfile(os.path.join(path, file_name)):
        print(file_name)
print("\nAll Directories and Files:")
for name in os.listdir(path):
    full_path = os.path.join(path, name)
    if os.path.isdir(full_path):
        print("[D] " + name)
    elif os.path.isfile(full_path):
        print("[F] " + name)
#
import os 
path = input()
print("Exists the path:", os.access(path, os.F_OK))
print("Access to read:", os.access(path, os.R_OK))
print("Access to write:", os.access(path, os.W_OK))
print("Check if path can be executed:", os.access(path, os.X_OK))
#
import os
path = input()
if os.path.exists(path):
   print("File exists")
   print(os.path.dirname(path))
   print(open(path, "r").read())
else: print("File doesn't exist")
#
import os
path = input()
x = open(path, "r")
lines = len(x.readlines())
print(lines)
#
lst = input().split()
open("line.txt", "x")
f = open("line.txt", "a")
f.write(str(lst))
f.close()
#
for i in range(ord('Z') - ord('A')+1):
    txt = "{}.txt"
    open(txt.format(chr(65+i)), "x")
#
import os
path = input()
f = open(path, "rt")
c = open("Copy.txt", "w")
c.write(f.read())
c.close
import os
path = input()
if os.path.exists(path) and os.access(path, os.X_OK):
   os.remove(path)
else: print("File doesn't exist")








