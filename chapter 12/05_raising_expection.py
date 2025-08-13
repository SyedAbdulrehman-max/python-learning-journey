a = int(input("Enter a number"))
b = int(input("Enter a number"))
print(f"The division a/b is {a/b}")

if(b==0):
    raise ZeroDivisionError ("hey our program not divide number by zero")
else:
    print(f"The division a/b is {a/b}")