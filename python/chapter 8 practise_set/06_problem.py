#write a function which converts inches to cms.

n = int(input("Enter a inches: "))

def i_to_c(n):
   return n * 2.54

print(f"The inches {n} into cms is {round(i_to_c(n),1)}")