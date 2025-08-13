f = open("file.txt")
print(f.read())
f.close()

#The same code can be written using 'with' statemant like this:

with open("file.txt") as f:
    print(f.read())

# you dont need to close the file this will do automatic