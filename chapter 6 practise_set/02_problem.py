'''QNO2:
write a program to find out whether a student has passed or failed if it requires a total
of 40% and at least 33% in each subject to pass.Assume 3 subjects and take marks as an input
from the user.
'''
s1 = int(input("Enter your marks: "))
s2 = int(input("Enter your marks: "))
s3 = int(input("Enter your marks: "))

total_percentage=(100*(s1+s2+s3)/300)

if (total_percentage >= 40 and s1 >=30 and s2 >=30 and s3>=30):
    print("you are passed!",total_percentage,"%")
else:
    print("you are faild!",total_percentage,"%")