class Employee:
    company = "ITC"
    name = "Farhan"
    salary = 1000
    def show(self):
        print(f"This name of the employe is {self.name} and the salary is {self.salary}")
    

class coder():
   language = "py"
   def printlanguage(self):
      print(f"this is my language {self.language}")

class programmer(Employee):
    company  = "ITC FUNCTION"   
    def showlanguage(self):
     print(f"The name of this language is {self.company}")

a = Employee()
b = programmer()

a.show()
b.showlanguage()

a