#create a class "programer" for storing information of few
# programer working at microsoft

class programer():
    company = "Microsoft"
    def __init__(self ,name ,salary , ex):
        self.name = name
        self.salary = salary
        self.ex = ex
    
e = programer("Ali" , 50000 ,"5 years" )
print(f"Name : {e.name} salary : {e.salary} Ex : {e.ex}")
r = programer("Hamza",10000,"10years")
print(f"Name : {r.name} salary : {r.salary} EX : {e.ex}")
        

