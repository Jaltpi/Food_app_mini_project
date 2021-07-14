def main_menu():
    """ The purpose of this function is to give the user the option to access the products menu, couriers menu, or exit the application."""
    main_menu_options = """
    Welcome to the main menu, the options are:
    0) Exit App
    1) Proceed to Products Menu
    2) Proceed to Couriers' Menu
    3) Proceed to Orders' Menu
    """
    print(main_menu_options)
    

def products_menu():
    """The purpose of this function enables the user choose from the options to return to main menu, 
    view products list, add new products, delete products, and edit existing products."""
    
    product_menu_options = """
    Welcome to the products menu, your options are:
    0) Return to main menu
    1) Show current products list
    2) Add a new item to the products list
    3) Edit an existing item from the products list
    4) Delete an item from the products list
    """
    print(product_menu_options)
    
def couriers_menu():
    """The purpose of this function enables the user choose from the options to return to main menu, 
    view couriers' list, add new couriers, delete couriers, and edit existing couriers."""
    
    couriers_menu_options = """
    Welcome to the couriers menu, your options are:
    0) Return to main menu
    1) Show current couriers list
    2) Add a new person to the couriers list
    3) Edit an existing person from the couriers list
    4) Delete a person from the couriers list
    """
    print(couriers_menu_options)

def deletion_item(List):
    """
    This function takes a list as an input, then allows the user to delete an object from the list. Afterwards
    the function returns the updated list.
    """
    for index, value in enumerate(List):
        print(index, value)
    
    delete_item = input("Input the identification number of the element you wish to delete: ")

    try: List.pop(int(delete_item))
    except Exception as e:
        print(f"Error: {e}. Please try again.")
    else:
        print(f"The updated list is: \n {List}")
    return List

def edit_item(List):
    """
    This function takes a list as an input, then allows the user to edit an item from the list, 
    and returns the updated list.
    """
    for index, value in enumerate(List):
        print(index, value)
    index_value = input("Which element would you like to update? Input a number listed above: ")
    updated_item = input("What would you like to re-name this element?: ").title()
            
    try: List[int(index_value)] = updated_item
    except Exception as e:
        print(f"Error: {e}. Please try again.")
    else:
        print(f"The updated list is: \n {List}")
    return List

def current_list(List):
    """ This function takes a list as an input, then allows the user to view all the entries 
    in the current inputted list."""
    print("Inside your current list: \n ")
    for item in List:
        print(item)
    

def create_new(List):
    """
    This function takes a list as an input, then
    allows the user to add a new entry into the list, and returns the updated list.
    """
    new_entry = input("Please type in a name you'd like to add: ").title()
    List.append(new_entry)   
    print(f"The updated list is now:\n {List}")
    return List

def orders_menu():
    """
    The purpose of this function enables the user choose from the options to return to main menu, 
    view orders list, add an order to orders list, update an existing order, update an existing order status,
    and delete an existing order.
    """
    order_menu_options = """
    Welcome to the Order Menu, the options are:
    0) Return to main menu
    1) Show current orders
    2) Place an order
    3) Update an existing order's status
    4) Update an existing order
    5) Delete an order
    """
    print(order_menu_options)