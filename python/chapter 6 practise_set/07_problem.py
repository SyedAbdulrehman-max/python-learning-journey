'''QNO7:
Write a program to find out wether a given post is talking about "Harry" or not.if in lowre and upper latter
'''
post = input("Enter your post::")

if ("Harry".lower() in post.lower()):
    print("This post talking about Harry")
else:
    print("This post is not talking about harry!!") 
