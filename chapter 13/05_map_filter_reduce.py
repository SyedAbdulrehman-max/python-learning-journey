from functools import reduce

l= [1,2,3,4,5]

square  = lambda x:x*x
sqlist = map(square, l)
print(list(sqlist))

#FIlter ex
def even(n):
    if (n%2 == 0):
        return True
    return False

onlyeven = filter(even, l)
print(list(onlyeven))

#Reduce Ex
def sum (a ,b):
    return a+b

print(reduce(sum,l))
