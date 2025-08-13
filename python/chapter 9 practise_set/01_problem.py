#write a program to read the text from a given file'poems.txt' 
# and find out whether it contains the word 'twinkle'

with open("problem_1.txt") as word :
    contant = word.read() # Read once and store in a variable

    if "twinkle" in contant:
        print("twinkle is found!")