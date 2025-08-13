a = 90 #global word
def fun():
    global a #we chage the global veriable
    a = 3   #its a local 
    print(a)

fun()
print(a)