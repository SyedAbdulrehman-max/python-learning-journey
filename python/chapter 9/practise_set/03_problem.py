'''write a program to generate multiplication tables from 2 to 20
 and write it to the different files. Place these files in a folder
for a 13-year old'''


def generatetable(n):
    table = ""
    for i in range(1, 11):                                # This function makes a multiplication table for any number we give it
        table += f"{n}X{i}={n*i}\n"                       # Write down: number X count = answer (like 5X3=15)
    with open(f"tables/table_{n}.txt","w") as f:          # Open a new file to save our table (like opening a notebook)
        f.write(table)                                    # Write the whole table into the file     
for i in range(2, 21):                                    # Do this for numbers 2, 3, 4, 5, ... up to 20
    generatetable(i)                                      # Make a multiplication table for each number