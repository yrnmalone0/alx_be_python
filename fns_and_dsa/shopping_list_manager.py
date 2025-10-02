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
            add_item = input("Add an item: ")
            shopping_list.append(add_item)
            print(f"Item added successfully: {shopping_list}")
            pass
        elif choice == '2':
            # Prompt for and remove an item
            remove_item = input("Remove an item: ")
            if remove_item in shopping_list:
                shopping_list.remove(remove_item)
                print(f"Item removed successfully: {shopping_list}")
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