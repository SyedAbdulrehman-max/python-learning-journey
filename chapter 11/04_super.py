class Employee:
    def __init__(self):
        print("Constructor of emp")
    a= 1

class programer(Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of programer")
    b = 2

class manager(programer):
    def __init__(self):
        super().__init__
        print("Constructor of manager")
    c = 3

# o = Employee

# print(o.a)
# print(o.b) #this is not present in employee

o  = programer()


print(o.a)
print(o.b)

# o  = manager
# print(o.a , o.b , o.c)

