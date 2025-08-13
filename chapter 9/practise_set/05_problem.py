#Repeat program 4 for a list of such words to be censored.


words  = ["donkey", "is" , "gillani", "syed"]

with open("donkey.txt","r") as f:
    contant = f.read()

for word in words:
    contant = contant.replace(word ,"#"*len(word) )

with open("donkey.txt","w") as f:
    f.write(contant)