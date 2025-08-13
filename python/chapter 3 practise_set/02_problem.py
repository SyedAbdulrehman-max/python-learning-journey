'''Write a program to fill in a letter 
   template given below with name and date.
   letter= Dear <|name|>
           You are selected!
           <|Date|>
   '''


letter= '''Dear name
           You are selected!
           Date'''

print(letter.replace("name","Harry").replace("Date", "23 march 2025"))