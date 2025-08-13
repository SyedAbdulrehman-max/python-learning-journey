#add a static method in problem 2 to greet the user with hello


n = int(input("Enter your number for square: "))
class calculator():
    def __init__(self , n):
        self.n = n

    def square(self):
        print(f"The square of {n} is {self.n*self.n}")

    def cube(self):
        print(f"The cube of {n} is {self.n*self.n*self.n}")
    
    def sr(self):
        print(f"The Square Root of {n} is {self.n**1/2}")
    
    @staticmethod
    def hello():
        print("Hello There!")
a = calculator (n)

a.hello()
a.square()
a.cube()
a.sr()