n = int(input("Enter the number: "))

def factorial(n):
    if( n==1 or n==0):
        return 1
    return n*factorial(n-1)
print(f"The facetorial number of {n} is ",factorial(n),end=" ")

if (factorial(n) <= 20):
    print("Program Working!", )
else:
    print("Program encrypted!") 

