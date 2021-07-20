# mini_project_week_3

from module import main_menu, orders_menu, products_menu, couriers_menu, create_new_item, show_current_list, edit_existing_item, delete_existing_item, update_existing_order
from module import orders_menu, show_existing_orders, create_new_order, update_order_status, update_existing_order, delete_existing_order

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
            show_current_list(products)
                
        elif second_choice == "2":
            # Create a new entry in the list
            create_new_item(products)
            
        elif second_choice == "3":
            # Edit an object in the list
            edit_existing_item(products)
        
        elif second_choice == "4":
            # Delete an object in the list
            delete_existing_item(products)
        
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
            show_current_list(couriers)
            
        elif third_choice == "2":
            # Create new courier
            create_new_item(couriers)
        
        elif third_choice == "3":
            # Update existing courier   
            edit_existing_item(couriers)
        
        elif third_choice == "4":
            # Delete an existing courier
            delete_existing_item(couriers)
        
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
            show_existing_orders(orders_list)
                            
        elif fourth_choice == "2":
            # Create an order
            create_new_order(couriers, orders_list)
        
        elif fourth_choice == "3":
            # Update existing order status
            update_order_status(orders_list, orders_status)

        elif fourth_choice == "4":
            # Update existing order
            update_existing_order(orders_list)
            
        elif fourth_choice == "5":
            # Delete an order
            delete_existing_order(orders_list)

        else:
            print(INVALID)
    else:
        print(INVALID)