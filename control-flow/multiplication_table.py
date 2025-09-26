## This script will ask the user to enter a number, then use a for loop to print the multiplication table for that number from 1 to 10.

# Ask the user to input a number for which they want to see the multiplication table
number = int(input("Enter a number to see its multiplication table: "))

# Use a for loop to iterate through the numbers 1 to 10.
for i in range(1,11):

    #For each iteration, calculate the product of the user’s number and the iterator
    product_of_number = number * i
    print(f'{number} * {i} = {product_of_number}')