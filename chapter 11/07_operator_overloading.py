class Number:
    def __init__(self , n):
        self.n  = n
    
    def _add_(self,num):
        return self.n + num.n

n = Number(1)
m = Number(2)

print(n + m)