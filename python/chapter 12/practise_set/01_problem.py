# Write a program to opem three files 1.txt,2.txt and 3.txt if any these files are not
# present, a massage without exiting the program must be printed prompting the same

try:
    with open("1.file.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)


try:    
    with open("2.file.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)


try:    
    with open("3.file.txt","r") as f:
        print(f.read())
except Exception as e:
    print(e)

print("Have a good day!")


