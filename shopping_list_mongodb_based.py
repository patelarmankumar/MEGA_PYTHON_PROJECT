from pymongo import MongoClient

from dotenv import load_dotenv
import os

def load_shopping_list(collection):
    """
    Load the shopping list from a MongoDB collection.

    Parameters:
    collection (pymongo.collection.Collection): The MongoDB collection to load the shopping list from.

    Returns:
    list: The shopping list retrieved from the collection.
    """
    try:
        shopping_list = list(collection.find())
        return shopping_list
    except:
        return []

def write_to_db(shopping_list):
    """
    Write the shopping list data to the database.

    Args:
    shopping_list (list): A list of items to be inserted into the database.

    Returns:
    None
    """
    try:
        if shopping_list:
            collection.delete_many({})  # Clear existing data only if there's new data to insert
            collection.insert_many(shopping_list)
    except Exception as e:
        print("Error occurred while writing to the database:", e)

def display_shopping_list(shopping_list):
    """
    Display the items in the shopping list with their descriptions.

    Parameters:
    shopping_list (list): A list of dictionaries where each dictionary represents an item with its description.

    Returns:
    None
    """

    print("Your Shopping List is as under: ")
    print("*" * 50)
    for i in shopping_list:
        print(shopping_list.index(i)+1, ".", i['item'],"-----",i['description'])
    print("*" * 50)

def add_item(shopping_list):

    """
    Function to add a new item to the shopping list.

    Parameters:
    shopping_list (list): The current shopping list to which the new item will be added.

    Returns:
    None
    """

    # take input from user for item name
    item = input("Enter item name: ")
    
    # take input from user for item description
    description = input("Enter item description: ")
    
    # append the new item to the shopping list
    shopping_list.append({'item':item, 'description':description})

    write_to_db(shopping_list)

def update_item(shopping_list):
    """
    Function to update an item in the shopping list.

    Parameters:
    shopping_list (list): List of dictionaries representing items in the shopping list.

    Returns:
    None
    """

    update_item_sr = int(input("Enter the serial number of the item you want to update: "))
    try:
        
        updated_item = input("Enter updated item name: ")
    
        updated_description = input("Enter updated item description: ")
     
        shopping_list[update_item_sr-1] = ({'item':updated_item, 'description':updated_description}) 
    except:
        print("Kindly enter the valid serial number of item you want to update. You can review shopping list by pressing 1. ")
    finally:
        write_to_db(shopping_list)

def delete_item(shopping_list):

    """
    Function to delete an item from the shopping list.

    Parameters:
    shopping_list (list): The list containing the shopping items.

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
        write_to_db(shopping_list)


def main():
    """
    Main function to interact with the shopping list application.
    """
    load_dotenv()  # This will automatically load the .env file and parse the DB_URI
    mongo_db_uri = os.getenv('DB_URI')
    # Now you can use mongo_db_uri to connect to your MongoDB database

    connection_string = mongo_db_uri

    # Connect to the MongoDB Atlas cluster
    client = MongoClient(connection_string)

    # Access database 
    db = client.shopping_list_db

    # Access collection 
    global collection
    collection = db.shopping_list_collection

    shopping_list = load_shopping_list(collection)
    
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