#write a class "calculator" capable of finding square, cube and 
# square root of a number

n = int(input("Enter your number for square: "))

class calculator():
    def __init__(self ,n):
        self.n = n
    
    def square(self):
        print(f"The square of {self.n} is {self.n**2}")
    
    def cube(self):
        print(f"The cube of {self.n} is {self.n**3}")
    
    def squareroot(self):
        print(f"The squareroot of {self.n} is {self.n**1/2}")

a = calculator(n)
a.square()
a.cube()
a.squareroot()

        