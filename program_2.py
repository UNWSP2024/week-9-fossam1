#Samuel Foss
#Program 2 Random Number File Writer
#11/1/24

# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500.
# The application should let the user specify how many random numbers the file will hold
# (up to 1000).

import random

def writerandomnumbers():
    numberamount = int(input("Enter the amount of numbers you want to create: "))
    if numberamount > 1000 : numberamount = 1000
    if numberamount < 1 : numberamount = 1

    with open("numbers.txt", "w") as file:
        for i in range(numberamount):
            rnumber = random.randint(1,500)
            file.write(f"{rnumber}\n")

    print(f"{numberamount} random numbers have been placed inside of your file")

writerandomnumbers()

#output
#Enter the amount of numbers you want to create: 5
#5 random numbers have been placed inside of your file

#Process finished with exit code 0
#32
#55
#98
#466
#220
