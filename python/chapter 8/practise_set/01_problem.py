#write a program using functions to find greatest of three numbers.

a = int(input("Enter your 1st number: "))
b = int(input("Enter your 2nd number: "))
c = int(input("Enter your 3rd number: "))

def great(a, b, c): 
    if (a > b and a > c ):
        return a
    elif (b > a and b > c):
        return b
    elif (c > a and c > b) :
        return c

print ("The greater number is :",great(a,b,c))

