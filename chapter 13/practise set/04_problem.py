#write a program to filter a list of number which are divisible by 5.

def divisible5(n):
    if(n%5 ==0):
        return True
    return False

a = [1, 2, 323,324,324,234,23124, 55,23]
f = list(filter(divisible5, a))
print(f)