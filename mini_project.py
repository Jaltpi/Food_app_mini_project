# mini_project_week_3

from module import main_menu, orders_menu, products_menu, couriers_menu, create_new, current_list, edit_item, deletion_item
from module import orders_menu

LOADING = "Loading Main Menu..."
INVALID = "Invalid selection, returning back to main menu."

# Load data from .txt files  
with open("products.txt") as products_list:
    products = [line.strip() for line in products_list]

with open("couriers.txt") as couriers_list:
    couriers = [line.strip() for line in couriers_list]
    
orders_status = ["Order pending", "Preparing", "On it's way", "Delievered"]
orders_list = []
    
application_on = True

while application_on:
    main_menu()
    
    first_choice = input("What would you like todo?\nEnter a number listed above to proceed or enter 'Exit' to quit: ").title()
    
    if first_choice == "0" or first_choice == "Exit":
        # Exit Application and Save Data
        with open("products.txt", "w") as updated_products:
            for item in products:
                updated_products.write("%s\n" % item)
        
        with open("couriers.txt", "w") as updated_couriers:
            for item in couriers:
                updated_couriers.write("%s\n" % item)
                
        application_on = False
        print("Have a good day, thank you for using our app!")
        exit_consent = input("Please press 'Enter' to exit.")
        exit()
        
    elif first_choice == "1":
        # PRODUCTS MENU
        products_menu()
        
        second_choice = input("Please enter a number listed above: ")
        if second_choice == "0":
            # Return to main menu
            print(LOADING)
            
        elif second_choice == "1":
            # Shows current list
            current_list(products)
                
        elif second_choice == "2":
            # Create a new entry in the list
            create_new(products)
            
        elif second_choice == "3":
            # Edit an object in the list
            edit_item(products)
        
        elif second_choice == "4":
            # Delete an object in the list
            deletion_item(products)
        
        else:
            print(INVALID)   
        
    elif first_choice == "2":
        # COURIERS MENU
        couriers_menu()
        
        third_choice = input("Please enter a number listed above: ")
        
        if third_choice == "0":
            # Return to main menu
            print(LOADING)
            
        elif third_choice == "1":
            # Show current couriers list
            current_list(couriers)
            
        elif third_choice == "2":
            # Create new courier
            create_new(couriers)
        
        elif third_choice == "3":
            # Update existing courier   
            edit_item(couriers)
        
        elif third_choice == "4":
            # Delete an existing courier
            deletion_item(couriers)
        
        else:
            print(INVALID)
                
    elif first_choice == "3":
        # ORDERS' MENU
        orders_menu()   
        
        fourth_choice = input("Please enter a number listed above: ")
        
        if fourth_choice == "0":
            # Return to main menu
            print(LOADING)
            
        elif fourth_choice == "1":
            # Show current orders
             if len(orders_list) == 0:
                    print("Your orders list is currently empty.")
             else:
                print(f"The current orders list is:")
                for placement, order in enumerate(orders_list):
                    print(placement, order)
                
        elif fourth_choice == "2":
            # Create an order
           try:
               customers_name = input("Please enter a name for the order: ").title()
               customers_address = input("Please enter an address for delivery: ").upper()
               customers_contact = input("Please enter a valid U.K number for us to contact you: ")
               
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
                    orders_list.append({"Customers' Name": customers_name, "Customers' Address": customers_address,\
                        "Customers' Phone Number": customers_contact, "Courier": courier_identification,\
                            "Status": "Preparing"})
                    print("Your order has been placed.")
        
        
        elif fourth_choice == "3":
            # Update existing order status
            
            for location, order in enumerate(orders_list):
                print(location, order)
            print("\n")
            order_index_value = input("Which order would you like to edit? Please enter a number listed above: ")
            
            for space, order in enumerate(orders_status):
                print(space, order)
            print("\n")
            orders_status_index = input("Please enter the number of the status you'd like to set: ")
            
            try:
                orders_list[int(order_index_value)]["Status"] = orders_status[int(orders_status_index)]
            except Exception as e:
                print(f"Error: {e}. Please try again.")
            else:
                print("Your orders' status has been updated. Here is your new order:")
                print(orders_list[int(order_index_value)])
                
        elif fourth_choice == "4":
            # Update existing order
            #pass
            for placement, order in enumerate(orders_list):
                print(placement, order)
            print("\n")
            
            selected_order = input("Which order would you like to update?: ").title()
            print("\n")
    
            try:
                updated_orders = orders_list[int(selected_order)]
                
            except Exception as e:
                print(f"Error: {e}, Please try again.")
                
            else:
                for key, value in updated_orders.items():
                    print(f"Curerent Key: {key}, Current Value: {value}")
                    print("\n")
                    value_change = input("What would you like the new this new value to be?: ")
                    if value_change == "":
                        print("\n")
                        print("You haven't inputted anything to change the value")
                    else:
                        orders_list[int(selected_order)][key] = value_change
            
        elif fourth_choice == "5":
            # Delete an order
            
            for placement, order in enumerate(orders_list):
                print(placement, order)
                
            print("\n")    
            remove_item = input("Enter the number of the order you'd like to delete: ")
            
            try:
                del orders_list[int(remove_item)]
                
            except Exception as e:
                print(f"Error: {e}, please try again.")
                
            else:
                print("You've successfully removed the order.")
                print("\n")
        else:
            print(INVALID)
    else:
        print(INVALID)