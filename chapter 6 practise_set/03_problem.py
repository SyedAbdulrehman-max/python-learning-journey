'''QNO3:
A spam comment is defined as a text containg following keywords:
"Make a lot of money""buy now""subscribe this""click this". write a 
program to detect these spams
'''
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

massage = input("Enter the paragrah:  ")

if (p1 in massage) or (p2 in massage) or (p3 in massage) or (p4 in massage):
    print("spam words detected ")