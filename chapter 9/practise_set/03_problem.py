'''write a program to generate multiplication tables from 2 to 20
 and write it to the different files. Place these files in a folder
for a 13-year old'''

# This function makes a multiplication table for any number we give it
def generatetable(n):
    # Start with an empty piece of paper (empty string)
    table = ""
    # Count from 1 to 10
    for i in range(1, 11):
        # Write down: number X count = answer (like 5X3=15)
        table += f"{n}X{i}={n*i}\n"
    # Open a new file to save our table (like opening a notebook)
    with open(f"tables/table_{n}.txt","w") as f:
        # Write the whole table into the file
        f.write(table) 

# Do this for numbers 2, 3, 4, 5, ... up to 20
for i in range(2, 21):
    # Make a multiplication table for each number
    generatetable(i)