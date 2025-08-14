'''
A file contains a word "Donkey" multiple times.
you need to write a program which replace this word with
#### by updating the same file.

'''


with open("donkey.txt","r") as f:
    contant=f.read()

contantview = contant.replace("donkey","###")

with open ("donkey.txt","w") as f:
    f.write(contantview)
