from database import connect_db
from sales import publish_for_sale, record_sale, get_sales, get_sales_dashboard
from purchases import register_purchase, get_purchases

def print_menu():
    print("\n======================================")
    print("          itemBox SYSTEM v1.0         ")
    print("======================================")
    print("1. 📥 Register New Purchase")
    print("2. 📦 Publish Item for Sale")
    print("3. 💰 Record a Closed Sale")
    print("4. 📋 View Inventory Stock (Purchases)")
    print("5. 📈 View Sales History")
    print("6. 📊 View Financial Dashboard")
    print("7. ❌ Exit")
    print("======================================")


def handle_register_purchase():
    #Choice 1 Register purchase
    print("\n" + "*" * 38)
    print("        REGISTERING NEW PURCHASE      ")
    print("" * 38)
    
    product = input("Enter product name: ").strip()
    if not product:
        print("Error: Product name cannot be empty.")
        return

    variant = input("Enter variant (e.g., Color, Type) [Leave blank if none]: ").strip()
    if variant == "" : variant = "Único"

    try:
        price = float(input("Enter unit purchase price: $"))
        quantity = int(input("Enter quantity purchased: "))
        if price < 0 or quantity <= 0:
            print("Error: Price and Quantity must be greater than 0.")
            return
    except ValueError:
        print("Error: Invalid input type. Price must be a decimal and Quantity an integer.")
        return

    date_input = input("Enter purchase date (YYYY-MM-DD) [Leave blank for today]: ").strip()
    if date_input == "" : date_input = None

    register_purchase(product, price, variant, quantity, date_input)
    print("*" * 38)


def handle_publish_for_sale():
    #Choice 1 Publish product sale
    print("\n" + "*" * 38)
    print("         PUBLISH ITEM FOR SALE        ")
    print("" * 38)
    
    try:
        purchase_id = int(input("Enter the Purchase ID to list from: "))
        sell_price = float(input("Enter target selling price: $"))
        if sell_price < 0:
            print("Error: Selling price must be greater tha 0.")
            return
    except ValueError:
        print("Error: IDs must be integers and prices must be decimals.")
        return

    date_input = input("Enter publication date (YYYY-MM-DD) [Leave blank for today]: ").strip()
    if date_input == "" : date_input = None

    publish_for_sale(purchase_id, sell_price, date_input)
    print("*" * 38)


def handle_record_sale():
    #Choice 3: Change status of a sale to 'Sold'.
    print("\n" + "*" * 38)
    print("           RECORD CLOSED SALE         ")
    print("" * 38)
    
    try:
        sale_id = int(input("Enter the Sale ID that was sold: "))
        discount = input("Enter discount applied [Leave blank for $0]: ").strip()
        discount = float(discount) if discount != "" else 0.0
        if discount < 0:
            print("Error: Discount must be greater than 0.")
            return
    except ValueError:
        print("Error: ID or Discount is not valid.")
        return

    date_input = input("Enter sale date (YYYY-MM-DD) [Leave blank for today]: ").strip()
    if date_input == "" : date_input = None

    record_sale(sale_id, discount, date_input)
    print("*" * 38)