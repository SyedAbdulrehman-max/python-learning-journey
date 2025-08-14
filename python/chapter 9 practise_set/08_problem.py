'''
write a program to make a copy of a text file "this.txt"
'''
with open("this.txt","r") as f:
    word = f.read()

with open ("this_is_copy.txt","w") as f:
    f.write(word)