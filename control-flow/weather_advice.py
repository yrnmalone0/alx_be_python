# This script will ask the user about the current weather conditions and provide clothing recommendations based on the input. This task aims to demonstrate the use of if, elif, and else statements to make decisions in a program.

# Prompt user for weather input
user_prompt = input("What's the weather like today? (sunny/rainy/cold): ")

# Provide clothing recommendations
if user_prompt == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif user_prompt == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif user_prompt == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
    