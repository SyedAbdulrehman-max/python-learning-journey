'''QNO3:
Can a Python set contain both 18 (an integer) and '18' (a string) as separate values?
'''
s = set()
s.add(18)

s.add("18") #output is {'18', 18}

#its means we can do 