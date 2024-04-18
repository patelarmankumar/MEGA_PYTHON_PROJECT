import sqlite3


def load_shopping_list(db_name):
    """
    This function loads a shopping list from a SQLite database.
    Parameters:
    db_name (str): The name of the SQLite database.

    Returns:
    shopping_list (list): A list of tuples representing the shopping list. Each tuple corresponds to a row in the database.

    """
    
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        # Execute a query to select all rows from the shopping_list table
        cursor.execute("SELECT * FROM shopping_list")

        # Fetch all rows from the cursor and append them to the shopping_list
        shopping_list = cursor.fetchall()
            
    except sqlite3.Error as error:
        # Print any error that occurs while connecting to the database
        print("Error occurred while connecting to the database:", error)

    finally:
        # Close the connection to the database
        if conn:
            conn.close()

        # Return the shopping list
        return shopping_list


def write_to_db(shopping_list):
    """
    Helper function to write current state of shopping list to db
    """

    try:
        
        conn = sqlite3.connect(db_name)
        cursor = conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS shopping_list
                 (item text, description text)''')
        
        cursor.execute("DELETE FROM shopping_list")

        for item, description in shopping_list:
            cursor.execute("INSERT INTO shopping_list (item, description) VALUES (?, ?)",(item,description))
        
        conn.commit()
        conn.close()

    except sqlite3.Error as error:
        # Print any error that occurs while connecting to the database
        print("Error occurred while connecting to the database:", error)

    finally:
        print("Item added to Shopping List successfully.....")

        

def display_shopping_list(shopping_list):
    """
    This function is intended to display a shopping list.
    
    Parameters:
    shopping_list (list): A list of items to be purchased.
    
    Returns:
    None
    """
    print("Your Shopping List is as under: ")
    print("*" * 50)
    for i in shopping_list:
        print(shopping_list.index(i)+1, ".", i[0],"-----",i[1])
    print("*" * 50)


def add_item(shopping_list):
    """
    This function is intended to add an item to a shopping list.

    Parameters:
    shopping_list (list): The shopping list to which the item will be added.

    Returns:
    None: This function does not return anything. It modifies the shopping list in place.
    """
     # take input from user for item name
    item = input("Enter item name: ")
    
    # take input from user for item description
    description = input("Enter item description: ")
    
    # append the new item to the shopping list
    shopping_list.append((item, description))

    # writing this change into db
    write_to_db(shopping_list)


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
     
        shopping_list[update_item_sr-1] = (updated_item, updated_description)  
    except:
        print("Kindly enter the valid serial number of item you want to update. You can review shopping list by pressing 1. ")
    finally:
        write_to_db(shopping_list)

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
        write_to_db(shopping_list)

def main():
    """
    This is the main function that runs an infinite loop.
    The loop will continue to run until it's manually stopped.
    """
    global db_name
    db_name = "shopping_list.db"

    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)

    # Now you can use `conn` to interact with the database
    cursor = conn.cursor()

    # Create a table    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS shopping_list (
            id INTEGER PRIMARY KEY,
            item TEXT NOT NULL,
            description TEXT NOT NULL
        )
    """)
    conn.close()

    shopping_list = load_shopping_list(db_name)
    if not shopping_list:  # Check if list is empty after loading
        shopping_list = []
    
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
            write_to_db(shopping_list)
        elif choice == '3':
            update_item(shopping_list)
            write_to_db(shopping_list)
        elif choice == '4':
            delete_item(shopping_list)
            write_to_db(shopping_list)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again with valid choice. ")

    


if __name__ == "__main__" :
    main()