#create a class "programer" for storing information of few
# programer working at microsoft


class programer():
    company ="Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary =  salary
        self.pin    = pin

e = programer("Harry" , 10000 , 219238)
print(f"Name :{e.name}  salary : {e.salary} pin : {e.pin} Company: {e.company}")
r = programer("Rohan" , 10000 , 219238)
print(f"Name :{r.name}  salary : {r.salary} pin : {r.pin} Company: {r.company}")
