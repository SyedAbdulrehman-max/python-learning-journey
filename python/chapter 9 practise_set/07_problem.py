'''
write a program to find out the line number where python
is present from ques 6.
'''
with open ("log.txt") as f:
    lines = f.readline()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"The line is founded {lineno}")
        break
    lineno+=1
    
else:
     print(f"The python is not found!")