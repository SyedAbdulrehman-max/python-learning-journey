#write a program using function to convert celsius to fahrenheit

f = int(input("Enter temparture: "))

def converter(f):
    return 5*(f-32)/9

print(f"Your temprataur {f} in celsius is", round(converter(f),2) )




