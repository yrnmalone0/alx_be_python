# This script will define functions to convert temperatures between Celsius and Fahrenheit, demonstrating the use of global variables to store conversion factors that are accessible within functions.

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9



# The formula to convert a temperature(F) in Fahrenheit to Celsius(C) is:
# C = (F − 32) * 5/9

# To convert a temperature from Celsius(°C) to Fahrenheit(°F), we use the formula:
# F = (C * 9/5) + 32


def convert_to_celsius(fahrenheit):
    calc_celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return calc_celsius


def convert_to_fahrenheit(celsius):
    calc_fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return calc_fahrenheit


temperature = float(input("Enter the temperature to convert: "))
temperature_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if temperature_type == "F":
    print(f"{temperature}°F is {convert_to_celsius(temperature)}°C")

elif temperature_type == "C":
    print(f"{temperature}°C is {convert_to_fahrenheit(temperature)}°F")

else:
    print("Invalid temperature. Please enter a numeric value.")