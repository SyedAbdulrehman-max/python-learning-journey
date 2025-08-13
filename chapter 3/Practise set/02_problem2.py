'''Write a program to fill in a letter 
   template given below with name and date.
   letter= Dear <|name|>
           You are selected!
           <|Date|>
   '''


letter= '''Dear name
           You are selected!
           Date'''

print(letter.replace("name","Harry").replace("Date","24 sep 2026"))

# name = input("Enter Your Name:") 
# age = input("Enter your age:")
# print(f"Dear {name} you are selected for this job")
# print(f"Your age is {age}")


