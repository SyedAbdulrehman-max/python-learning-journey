#write a function to print multiplication table of a given number 

n = int(input("Enter the table number:"))

def table(n):
    for item in range(1,11):
      print(f"{n} X {item} = ", item*n)


table(n)