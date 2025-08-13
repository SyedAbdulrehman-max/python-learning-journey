#write a class train which has methods to book a ticket,get
#status(no of seats) and get fare information of train running
#under  railways.
from random import randint
class Train:
    def __init__(self , trainNO):
        self.trainNO = trainNO
        
    def book(self , fro, to):
        print(f"Ticket is booked in train no: {self.trainNO} From : {fro} To : {to} ")
    
    def getstatus(self):
        print(f"Train NO:{self.trainNO} Is ready!")
    
    def getfare(self  , fro , to):
        print(f"Ticket fare in train no : {self.trainNO} From: {fro} To:{to} is {randint(1,100)}")

t = Train(1239)
t.book("Lahore","Karachi")
t.getstatus()
t.getfare("Lahore "," Karachi")