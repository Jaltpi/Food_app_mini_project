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


def show_current_list(List):
    """ This function takes a list as an input, then allows the user to view all the entries 
    in the current inputted list, ending with returning back the list. If the list is empty,
    the value returned is 'None'."""
    
    if len(List) == 0:
        print("This {List} is currently empty. Please add items into it using 'option 2' in the appropriate menu.")
        return None
    else:
        print("Inside your current list: \n ")
        for identification,item in enumerate(List):
            print(f"Identification number: {identification}, item info: {item}")
        return List
    

def create_new_product(List):
    """
    This function takes a list as an input, then
    allows the user to add a new entry into the list(product), and returns the updated list.
    """
    try:
        product_name = input("Please type in the name you'd like to add: ").title()
        product_price = float(input("Please type in the price of this new product: £ "))
        if product_name == "" or product_price == "": #Checks for empty string
            raise ValueError
        
    except ValueError:
        print("Error: Necessary information is missing from above, please try again.")
        
    except Exception as e:
        print(f"Error: {e}. An invalid character was detected in your product price.")
    else:
        new_product_dict = {"Product Name": product_name, "Product Price": product_price}
        List.append(new_product_dict)   
        print(f"The updated list is now:\n {List}")
        return List

def create_new_courier(List):
    """
    This function takes a list as an input, then
    allows the user to add a new entry into the list (courier), and returns the updated list.
    """
    
    try:
        courier_name = input("Please type in the name you'd like to add: ").title()
        courier_phone_number = input("Please type in the phone number of this courier: +44 ")
        
        if courier_name == "" or courier_phone_number == "": #Checks for empty strings
            raise ValueError
        elif  courier_phone_number.isdigit() == False or len(courier_phone_number) != 11: # checks to confirm if number entered is valid phone length and is all digits
            print("Error: An invalid phone number entry was detected.")
            raise ValueError
        
    except ValueError:
        print("Error: Necessary information is missing from above, please try again.")
    except Exception as e:
        print(f"Error: {e}.")
    else:
        new_product_dict = {"Courier's Name": courier_name, "Courier's Phone Number": courier_phone_number}
        List.append(new_product_dict)   
        print(f"The updated list is now:\n {List}")
        return List

def create_new_order(couriers, products, new_orders):
    """The purpose of this function is to take three lists, and append a dictionary of an order 
    (name, number, address, courier, status of order, items) into the last list, then return the return the last
    list."""
    try:
        customers_name = input("Please enter a name for the order: ").title()
        customers_address = input("Please enter an address for delivery: ").upper()
        customers_contact = input("Please enter a valid U.K number for us to contact you: +44 ")
        print("\n")
        
        if customers_name == "" or customers_address == "" or customers_contact == "": # Checks for empty strings in contact details
            raise ValueError
        elif customers_contact.isdigit() == False or len(customers_contact) != 11: # checks to confirm if number entered is valid phone length and is all digits
            print("An invalid phone number entry was detected.")
            raise ValueError
            
    except ValueError:
        print("Some details necessary for your order are missing, please try again.")   
    except Exception as e:
        print(f"Error: {e}. Please try again.")
    else:
        
        for placement, product in enumerate(products):
            print(placement, product)
            
        print("\n")
        product_selection = input("Enter the number(s) of the product(s) you wish purchase with each number separated by commas: ").split(",")
        print("\n")

        try:
            basket = [int(item) for item in product_selection]
            
        except Exception as e:
            print(f"Error: {e}. Non-integer was detected in item(s) selection.")
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
                print(f"Error: {e}. Please try again.")

            else:
                new_orders.append({"Customers' Name": customers_name, "Customers' Address": customers_address,\
                    "Customers' Phone Number": customers_contact, "Courier": courier_identification,\
                        "Status": "Preparing", "Items": basket})
                print("Your order has been placed.")
                
                return new_orders
        
def update_order_status(orders, orders_status):
    """The purpose of this function allows the user to update the status of their order. 
    It takes in two lists and returns the updated version of the orders list, if either of the lists are empty,
    the function returns 'None'."""
        
    if len(orders) == 0:
        print("This list called {orders} is currently empty. Please use 'Option 2' in 'Orders Menu' to create an order.")
        return None    
    elif len(orders_status) == 0:
        print("This list called {orders_status} is currently empty. Please use a list with values inside.")
        return None
            
    else:
        print("Your current orders are:")
        for location, order in enumerate(orders):
            print(location, order)
            print("\n")
            
        print("\n")
        order_index_value = input("Which order would you like to edit? Please enter a number listed above: ")
        
        print("Your options for status change are:")
        for space, order in enumerate(orders_status):
            print(space, order)
            print("\n")
            
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

def update_existing_item(List):
    """The purpose of this function is to allow the user to make updates to existing item in a list, it then returns
    the updated version of the list. If the list is empty, it will return 'None'.
    """
    if len(List) == 0:
        print("The {List} is currently empty. Please use 'Option 2' in the appropriate menu to create an entry.")
        return None
                
    else:
        for placement, item in enumerate(List):
            print(f"ID Number: {placement}, item: {item}.")
        print("\n")
            
        selected_list = input("Which item would you like to update? Please enter an ID Number: ")
        print("\n")
    
        try:
            if int(selected_list) > len(List) - 1 or  int(selected_list) < 0: #Checks user inputs index range 
                raise IndexError
            else:
                updated_list = List[int(selected_list)]
                    
        except IndexError:
            print("Error: Index error. Please try again.")
        except Exception as e:
            print(f"Error: {e}, Please try again.")
                
        else:
            # Bug: Can change values in list to anything
            for key, value in updated_list.items():
                print(f"Current Key: {key}, Current Value: {value}")
                print("\n")
                value_change = input("What would you like the new this new value to be?: ").title()
                if value_change == "":
                    print("\n")
                    print("You haven't inputted anything to change the value")
                else:
                    List[int(selected_list)][key] = value_change
            return List


def delete_existing_item(List):
    """The purpose of this function allows the user to input a list, then delete an entire element 
    from the list. If the list empty, it will return 'None', otherwise it returns the updated list."""
    
    if len(List) == 0:
        print("This {List} is currently empty, please use 'Option 2' in the appropriate menu to create an item.")
        return None   
    else:
        for placement, order in enumerate(List):
            print(placement, order)
            print("\n")
                
        print("\n")    

        remove_item = input("Enter the number of the order you'd like to delete: ")
            
        try:
            if int(remove_item) < 0 or int(remove_item) > len(List) - 1:
                raise IndexError
            else:
                del List[int(remove_item)]
                    
        except IndexError:
            print("Error: Index value error")
        except Exception as e:
            print(f"Error: {e}, please try again.")
                
        else:
            print("You've successfully removed the item.")
            print("\n")
            return List