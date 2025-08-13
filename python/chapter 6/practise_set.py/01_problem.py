'''QNO1:
Write a program to find the greatest of four numbers entered by the user.
'''
n = int(input("Enter number"))
n2 = int(input("Enter number"))
n3 = int(input("Enter number"))
n4 = int(input("Enter number"))

if(n>n2 and n>n3 and n>n4):
    print("Greatest number is:",n)

if(n2>n and n2>n3 and n2>n4):
    print("Greatest number is:",n2)

if(n3>n2 and n3>n and n3>n4):
    print("Greatest number is:",n3)

if(n4>n2 and n4>n3 and n4>n):
    print("Greatest number is:",n4)

