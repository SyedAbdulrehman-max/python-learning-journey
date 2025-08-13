'''QNO4:
what will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add("20") #length of s after these operation?

'''
s = set()
s.add(20)
s.add(20.0)
s.add("20") #length of s after these operation?
print(len(s)) #output is 2 because 20 and 20.0 are equal python check it on numrical values