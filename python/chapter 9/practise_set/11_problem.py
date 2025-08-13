#write a python program to remove to rename a file to any name 

with open("This is copy.txt","r") as f:
 contant= f.read()

with open("t.txt","w") as f:
    f.write(contant)