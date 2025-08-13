'''write a program to mine a log file and find out whether it
contains 'python' '''

with open("log.txt","r") as f:
    word = f.read()

if("python" in word):
    print("Yes, python is founded ")
else:
    print("No, python is no found")