'''
write a program to find out whether a file is identical &
matches the content of another file.
'''
with open("this.txt","r") as f:
    word1  = f.read()

with open("this_is_copy.txt","r") as f:
    word2 = f.read()

if (word1 == word2):
    print("The contant is identical")
else:
    print("The contant is not identical")