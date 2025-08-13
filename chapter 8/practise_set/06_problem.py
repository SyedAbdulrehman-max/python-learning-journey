#write a function which converts inches to cms.

n = int(input("Enter the Inches: "))

def converter(n):
    return n * 2.54

print(f"Your value is :",round(converter(n),2))

