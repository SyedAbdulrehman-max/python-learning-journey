# write a program to input name, marks and phone
# number of a student and format it using the format function like below:
# "the name of the student is harry, his marks are 72 and phone number is 99999888"

name = input("enter name:")
marks = int(input("enter marks:"))
phone = int(input("enter phone"))

s = "The name of the student is {0}, his marks is {1} and his phone is {2}".format(name,marks,phone)
print(s)