#write a program using function to convert celsius to fahrenheit

n = int(input("Enter a number: "))

def converter(n):
    return 5*(n-32)/9

print(f"This is your celsius {n} in fahrenheit ",round(converter(n),2))

