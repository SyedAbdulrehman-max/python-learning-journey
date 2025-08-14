#write a python program to remove to rename a file to any name 
with open ("this.txt","r") as f:
    contant = f.read()

with open ("change the name","w") as f:
    f.write(contant)