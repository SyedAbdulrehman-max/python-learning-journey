#solve the problem of 01_problem using while loop

table = int(input("Enter the table name: "))
i=1
while (i<11):
    print(f"{table} X {i} = {table*i}")
    i+=1
