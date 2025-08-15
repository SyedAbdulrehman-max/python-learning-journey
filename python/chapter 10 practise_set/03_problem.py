# create a class with a class attribute a; create an object
# from it and set "a" dierectly using object.a = o. does
# this change the class attribute
class Demo ():
    a = 4

o = Demo()
print(o.a) #print the class atrribute because the instance attrribute is not present

o.a = 6  #instance attribute is set

print(o.a) #print the instance attribute