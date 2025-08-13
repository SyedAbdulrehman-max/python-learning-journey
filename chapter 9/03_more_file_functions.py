f = open("03_file.txt")

#print the all lines one by one

# line1 = f.readline()
# print(line1,type(line1))

# line2 = f.readline()
# print(line2,type(line2))

# line3 = f.readline()
# print(line3,type(line3))

# line4 = f.readline()
# print(line4,type(line4))

'''
printing all lines by using loop line by line 
'''
lines = f.readline()

# while(lines != ""):
#     print(lines)
#     lines = f.readline()
if (lines != [100]):
    print(lines)
    lines = f.readline()
    



f.close()