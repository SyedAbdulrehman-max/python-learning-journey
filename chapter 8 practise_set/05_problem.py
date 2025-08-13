#write a function to print first n lines of the following pattern:
#  ***
#  **
#  * 

n = int(input("Enter a number: "))

def star(n):
    if (n<=0):
        return
    print("*"*n)
    star(n-1)
   
star(n)