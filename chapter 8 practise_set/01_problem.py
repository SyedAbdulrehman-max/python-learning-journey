#write a program using functions to find greatest of three numbers.

a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))

def greater():
    if a>b and a>c:
        print(f"The greater number is {a}")
    elif b>a and b>c:
     print(f"The greater number is {b}")
    elif c>a and c>b:
       print(f"The greater number is {c}")
    
greater()