class em:
    language = "py"
    salary = 100000
    

intro = em()
intro.language = "Javascript" #instance attributes take more prefence than assuming a value to the class from the previous
print( intro.language )


