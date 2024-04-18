import json

def load_shopping_list(filename):
    """
    Load a shopping list from a file.

    Args:
        filename (str): The name of the file to load the shopping list from.

    Returns:
        list: The loaded shopping list as a list of items.

    Raises:
        FileNotFoundError: If the specified file does not exist.
    """
    try:
        with open(filename, 'r') as file:
            shopping_list = json.load(file)
    except FileNotFoundError:
        print("File containing Shopping List not found. However, you can contine..")
        shopping_list = []
    return shopping_list

def save_shopping_list(shopping_list):
    """
    This function saves a shopping list.

    Parameters:
    shopping_list (list): The shopping list to be saved.

    Returns:
    None
    """
    with open("shopping_list.txt", "w") as file:
        json.dump(shopping_list, file)

def display_shopping_list(shopping_list):
    """
    Display the items in the shopping list.

    Args:
        shopping_list (list): A list of items in the shopping list.

    Returns:
        None
    """

    print("Your Shopping List currently is as under :\n------------------------------------------")
    for i in range(len(shopping_list)):
        print(i+1, "--", "\t", shopping_list[i]["item"], "--", shopping_list[i]["description"])


def add_item(shopping_list):
    """
    This function adds an item to the shopping list.

    Parameters:
    shopping_list (list): The list to which the item will be added.

    Returns:
    None
    """
    
    # take input from user for item name
    item = input("Enter item name: ")
    
    # take input from user for item description
    description = input("Enter item description: ")
    
    # append the new item to the shopping list
    shopping_list.append({'item': item, 'description':description})

    # add this item and description to file also
    save_shopping_list(shopping_list)
    
def update_item(shopping_list):
    """
    Update an item in the shopping list.

    Args:
        shopping_list (list): The list of items in the shopping list.

    Returns:
        None
    """
    update_item_sr = int(input("Enter the serial number of the item you want to update: "))
    try:
        pass
        updated_item = input("Enter updated item name: ")
    
        updated_description = input("Enter updated item description: ")
     
        shopping_list[update_item_sr-1] = {'item': updated_item, 'description':updated_description}
    except:
        print("Kindly enter the valid serial number of item you want to update. You can review shopping list by pressing 1. ")
    finally:
        save_shopping_list(shopping_list)

def delete_item(shopping_list):
    """
    Deletes an item from the shopping list.

    Args:
        shopping_list (list): The list from which the item will be deleted.

    Returns:
        None
    """
    to_be_deleted_item_sr = int(input("Enter the serial number of the item you want to delete: "))

    try:
        del shopping_list[to_be_deleted_item_sr-1] 
    except Exception as e:
        print("Kindly enter valid serial number of item you want to delete. ")
        print("Extra Error log are as follows: ")
        print(e)
        print("-" * 40)
    finally:
        save_shopping_list(shopping_list)


def main():
    filename = "shopping_list.txt"
    shopping_list = load_shopping_list(filename)
    
    while True:
        print("\n1. Display Shopping List")
        print("2. Add Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            display_shopping_list(shopping_list)
        elif choice == '2':
            add_item(shopping_list)
        elif choice == '3':
            update_item(shopping_list)
        elif choice == '4':
            delete_item(shopping_list)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again with valid choice. ")

if __name__ == "__main__":
    main()