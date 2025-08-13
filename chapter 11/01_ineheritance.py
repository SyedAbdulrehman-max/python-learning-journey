class Employee:
    company = "ITC"
    def show(self):
        print(f"This name of the employe is {self.name} and the salary is {self.salary}")

# class programmer:
#     company  = "ITC FUNCTION"
#     def show(self):
#         print(f"This name of the employe is {self.name} and the salary is {self.salary}")
    
#     def showlanguage(self):
#         print(f"The name of this language is {self.language}")

class programmer(Employee):
    company  = "ITC FUNCTION"   
    def showlanguage(self):
     print(f"The name of this language is {self.language}")


a = Employee()
b = programmer()

print(a.company, b.company,)