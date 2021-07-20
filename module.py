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

def delete_existing_item(List):
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

def edit_existing_item(List):
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

def show_current_list(List):
    """ This function takes a list as an input, then allows the user to view all the entries 
    in the current inputted list."""
    print("Inside your current list: \n ")
    for item in List:
        print(item)
    

def create_new_item(List):
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

def show_existing_orders(List):
    """This function takes in a list and confirms if it's empty, and returns none. If the list isn't empty, it prints out
    an enumerated listing of the items, then returns the list.
    """
    if len(List) == 0:
        print("Your orders list is currently empty.")
        return None
    else:
        print("The current orders list is:")
        for placement, order in enumerate(List):
            print(placement, order)
    return List

def create_new_order(couriers, new_orders):
    """The purpose of this function is to take two lists, and append a dictionary of an order 
    (name, number, address, courier, status of order) into the second list, then return the second list."""
    try:
        customers_name = input("Please enter a name for the order: ").title()
        customers_address = input("Please enter an address for delivery: ").upper()
        customers_contact = input("Please enter a valid U.K number for us to contact you: +44 ")
        
        if customers_name == "" or customers_address == "" or customers_contact == "": # Checks for empty strings in contact details
            raise ValueError
        elif customers_contact.isdigit() == False or len(customers_contact) != 11: # checks to confirm if number entered is valid phone length and is all digits
            raise ValueError
               
    except ValueError:
        print("Some details necessary for your order are missing, please try again.")   
    except Exception as e:
        print(f"Error: {e}. Please try again.")
    else:
        for identification, courier in enumerate(couriers):
            print(identification, courier)
                   
        print("\n")   
        courier_selection = input("Enter the identification number of the courier you wish to select: ")
        try: 
            courier_identification = int(courier_selection)
            if courier_identification > len(couriers) - 1: # Checks for valid index range in list
                raise IndexError
            elif courier_identification < 0: # Also checks for valid index range in list
                raise IndexError
                    
        except IndexError:
            print("Sorry, that number isn't a valid choice for a courier. Please try again.")
        except Exception as e:
            print(f"Error: {e}. Try again.")

        else:
            new_orders.append({"Customers' Name": customers_name, "Customers' Address": customers_address,\
                "Customers' Phone Number": customers_contact, "Courier": courier_identification,\
                    "Status": "Preparing"})
            print("Your order has been placed.")
                
            return new_orders

def update_order_status(orders, orders_status):
    """The purpose of this function allows the user to update the status of their order. 
    It takes in two lists and returns the updated version of the second list."""
        
    if len(orders) == 0:
        print("This list called {orders} is currently empty. Please use 'Option 2' in 'Orders Menu' to create an order.")
            
    elif len(orders_status) == 0:
        print("This list called {orders_status} is currently empty. Please use a list with values inside.")
            
    else:
        print("Your current orders are:")
        for location, order in enumerate(orders):
            print(location, order)
        print("\n")
        order_index_value = input("Which order would you like to edit? Please enter a number listed above: ")
        
        print("Your options for status change are:")
        for space, order in enumerate(orders_status):
            print(space, order)
        print("\n")
        orders_status_index = input("Please enter the number of the status you'd like to set: ")
            
        try:
            if int(orders_status_index) > len(orders_status) - 1 or int(orders_status_index) < 0:
                print("Your order's status is out of range.")
                raise IndexError
            
            elif int(order_index_value) > len(orders) - 1 or int(order_index_value) < 0:
                print("Your orders' index value is out of range.")
                raise IndexError
            
            else:
                orders[int(order_index_value)]["Status"] = orders_status[int(orders_status_index)]
        except IndexError:
            print("Error: Index is out of range.")
        except Exception as e:
            print(f"Error: {e}. Please try again.")
        else:
            print("Your orders' status has been updated. Here is your new order:")
            print(orders[int(order_index_value)])
            return orders    
    
def update_existing_order(orders):
    """The purpose of this function is to allow the user to make updates to existing orders.
    """
    if len(orders) == 0:
        print("The {orders} is currently empty. Please use 'Option 2' in 'Orders Menu' to create an order.")
                
    else:
        for placement, order in enumerate(orders):
            print(placement, order)
        print("\n")
            
        selected_order = input("Which order would you like to update? Please enter a number: ")
        print("\n")
    
        try:
            if int(selected_order) > len(orders) - 1 or  int(selected_order) < 0:
                raise IndexError
            else:
                updated_orders = orders[int(selected_order)]
                    
        except IndexError:
            print("Error: Index error. Please try again.")
        except Exception as e:
            print(f"Error: {e}, Please try again.")
                
        else:
            # Bug: Can change values in phone number + Status to anything
            for key, value in updated_orders.items():
                print(f"Curerent Key: {key}, Current Value: {value}")
                print("\n")
                value_change = input("What would you like the new this new value to be?: ").title()
                if value_change == "":
                    print("\n")
                    print("You haven't inputted anything to change the value")
                else:
                    orders[int(selected_order)][key] = value_change
            return orders

def delete_existing_order(orders_list):
    """The purpose of this function allows the user to in put a function, then delete an entire order 
    from the list of orders. It returns the updated list of orders."""
    
    if len(orders_list) == 0:
        print("This {orders_list} is currently empty, please use 'Option 2' in 'Orders Menu' to create an order.")
            
    else:
        for placement, order in enumerate(orders_list):
            print(placement, order)
                
        print("\n")    

        remove_item = input("Enter the number of the order you'd like to delete: ")
            
        try:
            if int(remove_item) < 0 or int(remove_item) > len(orders_list) - 1:
                raise IndexError
            else:
                del orders_list[int(remove_item)]
                    
        except IndexError:
            print("Error: Index value error")
        except Exception as e:
            print(f"Error: {e}, please try again.")
                
        else:
            print("You've successfully removed the order.")
            print("\n")
            return orders_list