# Utilize Python lists to create a simple shopping list manager that allows users to add items, view the current list, and remove items.

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:  # continuously display a menu to user until they choose to exit
        display_menu() # calling display_menu function
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"{item} added successfully!")
            pass
        elif choice == '2':
            # Prompt for and remove an item
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed successfully!")
            else:
                print("Item cannot be found")
            pass
        elif choice == '3':
            # Display the shopping list
            if shopping_list:
                print("Your current shopping list: ")
                for item in shopping_list:
                    print(f'- {item}')
            else:
                print("Shopping list is empty!!")
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()