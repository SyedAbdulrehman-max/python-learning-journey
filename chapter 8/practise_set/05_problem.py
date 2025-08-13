#write a function to print first n lines of the following pattern:
#  ***
#  **
#  * 
n = 3
def star(n):
    if(n <= 0):
        return 
    print("*" * n)
    star(n-1)


star(n)