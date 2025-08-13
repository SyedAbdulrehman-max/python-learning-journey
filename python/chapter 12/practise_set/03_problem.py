# write a list comprehension to print a list which contains the multiplication
# table of a user entered number

n = int(input("Enter a number: "))

table=[n*i for i in range(1,11)]


print(table)


# n = int(input("Enter a number:"))

# for i in range(1,11):
#     print(f"{n}x{i} = {n*i}")