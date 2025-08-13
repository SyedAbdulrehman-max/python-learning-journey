'''
write a program to find out whether a file is identical &
matches the content of another file.
'''
with open("this.txt","r") as f:
    word1 = f.read()

with open("This is copy.txt","r") as f:
    word2 = f.read()

if (word1 == word2):
    print('''Yes a file is identical & matches the content of another file. ''')
else:
    print('''No, a file is identical & matches the content of another file.''')
