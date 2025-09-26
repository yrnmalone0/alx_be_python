## This script will prompt the user to enter a positive integer, then use nested loops to print a square pattern of that size made of asterisks (*).


# Ask the user to input a positive integer that represents the size of the pattern
size = int(input("Enter the size of the pattern: "))

row = 0

# Using a while loop to iterate through each row of the pattern.
while row < size:

    # use a for loop to print asterisks (*) side by side without advancing to a new line
    for i in range(size):
        print("*", end="")
    print()
    row += 1