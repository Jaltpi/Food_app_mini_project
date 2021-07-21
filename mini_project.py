# mini_project

from module import main_menu, products_menu, couriers_menu, orders_menu, show_current_list
from module import create_new_product, create_new_courier, create_new_order, update_order_status, update_existing_item
from module import delete_existing_item

LOADING = "Loading Main Menu..."
INVALID = "Invalid selection, returning back to main menu."

# Load data from .cvs files  
with open("products.cvs") as products_list:
    products = [line.strip() for line in products_list]

with open("couriers.cvs") as couriers_list:
    couriers = [line.strip() for line in couriers_list]

with open("orders.cvs") as orders_list:
    orders = [line.strip() for line in orders_list]
    
orders_status = ["Order pending", "Preparing", "On it's way", "Delievered"]
    
application_on = True

while application_on:
    main_menu()
    
    main_menu_choice = input("What would you like todo?\nEnter a number listed above to proceed or enter 'Exit' to quit: ").title()
    
    if main_menu_choice == "0" or main_menu_choice == "Exit":
        # Exit Application and Save Data
        with open("products.cvs", "w") as updated_products:
            for item in products:
                updated_products.write("%s\n" % item)
        
        with open("couriers.cvs", "w") as updated_couriers:
            for item in couriers:
                updated_couriers.write("%s\n" % item)
                
        with open("orders.cvs", "w") as updated_orders:
            for item in orders:
                updated_orders.write("%s\n" % item)
                
        application_on = False
        print("Have a good day, thank you for using our app!")
        exit_consent = input("Please press 'Enter' to exit.")
        exit()
        
    elif main_menu_choice == "1":
        # PRODUCTS MENU
        products_menu()
        
        products_menu_choice = input("Please enter a number listed above: ")
        if products_menu_choice == "0":
            # Return to main menu
            print(LOADING)
            
        elif products_menu_choice == "1":
            # Shows current list
            show_current_list(products)
                
        elif products_menu_choice == "2":
            # Create a new entry in the list
            create_new_product(products)
            
        elif products_menu_choice == "3":
            # Edit an object in the list
            update_existing_item(products)
        
        elif products_menu_choice == "4":
            # Delete an object in the list
            delete_existing_item(products)
        
        else:
            print(INVALID)   
        
    elif main_menu_choice == "2":
        # COURIERS MENU
        couriers_menu()
        
        courier_menus_choice = input("Please enter a number listed above: ")
        
        if courier_menus_choice == "0":
            # Return to main menu
            print(LOADING)
            
        elif courier_menus_choice == "1":
            # Show current couriers list
            show_current_list(couriers)
            
        elif courier_menus_choice == "2":
            # Create new courier
            create_new_courier(couriers)
        
        elif courier_menus_choice == "3":
            # Update existing courier   
            update_existing_item(couriers)
        
        elif courier_menus_choice == "4":
            # Delete an existing courier
            delete_existing_item(couriers)
        
        else:
            print(INVALID)
                
    elif main_menu_choice == "3":
        # ORDERS' MENU
        orders_menu()   
        
        orders_menu_choice = input("Please enter a number listed above: ")
        
        if orders_menu_choice == "0":
            # Return to main menu
            print(LOADING)
            
        elif orders_menu_choice == "1":
            # Show current orders
            show_current_list(orders)
                            
        elif orders_menu_choice == "2":
            # Create an order
            create_new_order(couriers, products, orders)
        
        elif orders_menu_choice == "3":
            # Update existing order status
            update_order_status(orders, orders_status)

        elif orders_menu_choice == "4":
            # Update existing order
            update_existing_item(orders)
            
        elif orders_menu_choice == "5":
            # Delete an order
            delete_existing_item(orders)

        else:
            print(INVALID)
    else:
        print(INVALID)