from hashlib import new
import os

files = os.listdir()

name = input("Enter File Initial Name: ")

for file in files:
    if(file.endswith('.py')):
        pass
    else:
        old_name = os.path.basename(file)
        new_name = name+" "+old_name
        print(new_name)
        os.rename(old_name,new_name)
        print(old_name)