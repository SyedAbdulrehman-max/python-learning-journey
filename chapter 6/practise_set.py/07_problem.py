'''QNO7:
Write a program to find out wether a given post is talking about "Harry" or not.
'''
post = input("Enter the post: ")

if("Harry".lower() in post.lower()):
    print("This post talking about harry")
else:
    print("This post not talking aboout harry")