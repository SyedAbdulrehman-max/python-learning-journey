# write a program to display a/b where a and b are integers.
# if b=0, display infinite by handling the 'zerodivisionerror'.

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    print(a/b)
except ZeroDivisionError as e:
    print("Infinite")