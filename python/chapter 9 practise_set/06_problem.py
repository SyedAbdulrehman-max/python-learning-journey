'''write a program to mine a log file and find out whether it
contains 'python' 
'''
import random
lan = ["python", "java", "c++","react"]
r = random.choice(lan)
print(r)
with open("log.txt","w") as f:
    f.write(r)

with open("log.txt","r") as f:
    read = f.read()

if("python" in read):
    print("python is founded")
else:
    print("python is not founded")