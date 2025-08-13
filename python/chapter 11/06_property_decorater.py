class employee:
    a  = 1

    @classmethod
    def show (cls):
        print(f"The class arrtibute is {cls.a}")
    
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]



e = employee()

e.a = 3
e.name = "harry"
print(e.fname)
e.show()