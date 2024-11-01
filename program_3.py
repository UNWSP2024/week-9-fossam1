#Samuel Foss
#program 3 Average Numbers
#11/1/24

# Program #3: Average Numbers
# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# (please use the provided numbers.txt)
# Write a program that reads all of the numbers stored in the file and calculates their total.

# The program should handle the following exceptions:

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file
# are converted to a number.
def sum_numbers_from_file():
    ######################
    total = 0
    lines = 0
    try:
        with open ("numbers.txt", "r") as file:
            for line in file:
                try:
                    num = int(line.strip())
                    total += num
                    lines += 1
                except valueerror:
                    print("A Value Error Has Occured")
        average = total / lines
        print(f"Here is the sum of the numbers in your file: {total}")
        print(f"Here is the average of the numbers in your file: {average:.2f}")
    except IOerror:
        print("A IO Error Has Occured")

    ######################
    print('In the sum_numbers_from_file function')

# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()

#output
#Here is the sum of the numbers in your file: 871
#Here is the average of the numbers in your file: 174.20
#In the sum_numbers_from_file function

#Process finished with exit code 0
#32
#55
#98
#466
#220
