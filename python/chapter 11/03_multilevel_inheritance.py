class Employee:
    a= 1

class programer(Employee):
    b = 2

class manager(programer):
    c = 3

o = Employee

print(o.a)
print(o.b) #this is not present in employee

o  = programer

print(o.a)
print(o.b)

o  = manager
print(o.a , o.b , o.c)

