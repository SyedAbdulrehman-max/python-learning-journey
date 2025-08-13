class em:
    salary = 100000     #these are class attribute
    language = "py"

intro = em()
intro.name  = "Rehman"  #This is instance attribute
print( intro.language , intro.name)

intro = em()
intro.pro  = "Develpore"
print(intro.language , intro.pro)

#here name is instance attribute and salary and language are class
# attributes as they directly belonge to the class

