#Samuel Foss
#Program 1 Item Counter
#11/1/24

# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.

def count_file_lines():
    ######################
    with open("names.txt", "r") as file:
        line = file.readlines()
        print(f"There are {len(line)} lines in the file")
    ######################
    print('In the count_file_lines function')



# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()

#Output
#There are 31 lines in the file
#In the count_file_lines function

#Process finished with exit code 0
