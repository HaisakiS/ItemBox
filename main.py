import sys
from menu import *

def main():
    while True:
        print_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            handle_register_purchase()
        elif choice == "2":
            handle_publish_for_sale()
        elif choice == "3":
            handle_record_sale()
        elif choice == "4":
            get_purchases()
        elif choice == "5":
            get_sales()
        elif choice == "6":
            get_sales_dashboard()
        elif choice == "7":
            print("\nThank you for using ItemBox. Goodbye!")
            sys.exit()
        else:
            print("\nInvalid option! Please type a number from 1 to 7.")

if __name__ == "__main__":
    main()