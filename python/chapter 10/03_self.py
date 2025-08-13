class em:
    salary = 100000     #these are class attribute
    language = "py"

    def getinfo(self):
        print(f"This is my language {self.language} and this is my salary {self.language}")
    
    def greet(self):
        print("Good morning")
        print("Have a good day!")


intro = em()
intro.name  = "Rehman"  #This is instance attribute
print( intro.language , intro.name)

intro.getinfo()

intro.greet()