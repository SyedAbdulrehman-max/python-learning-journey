#write a program to print multiplication table of a given number using for loop.

table = int(input("Enter the table name: "))
for i in range(1,11):
    print(f"{table} X {i} = {table*i}")

print("Code is Ended!")