class em:
    salary = 100000     #these are class attribute
    language = "py"
    def __init__(self , name , salary , language): #this is dunder method which calls atumatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am gone creat a new world which is better and fair ].")
    def getinfo(self):
        print(f"This is my language {self.language} and this is my salary {self.language}")
    
    def greet(self):
        print("Good morning")
        print("Have a good day!")


intro = em("Harry" , 20000, "javascript")
# intro.name  = "Rehman"  #This is instance attribute

print( intro.name , intro.language , intro.salary)

