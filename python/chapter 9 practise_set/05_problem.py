#Repeat program 4 for a list of such words to be censored.

list = ["Syed","gillani","ali","Hamza"]

with open ("list.txt","r") as f:
    contant  = f.read()

for lists in list:
 contant = contant.replace(lists,"#"*len(lists))

with open("list.txt", "w") as f:
    f.write(contant)