import sqlite3
from database import connect_db, initialize_sys, print_purchases

def add_category(name):
    conn = connect_db()
    if conn is None: return
    
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO categories (name) VALUES (?);", (name,))
        conn.commit()
        print(f"Category '{name}' added succesfully.")
    except sqlite3.Error as e:
        print(f"Error adding category: {e}")
    finally:
        conn.close()
        
def add_product(name,category):
    conn = connect_db()
    if conn is None: return
    
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT OR IGNORE INTO products (name,category) VALUES (?,?);", (name,category))
        conn.commit()
        print(f"Product '{name}' with category '{category}' added succesfully.")
    except sqlite3.Error as e:
        print(f"Error adding product: {e}")
    finally:
        conn.close()
        
def register_purchase(product, price, variant = "Unico", quantity=1, date = None):
    conn = connect_db()
    if conn is None: return
    
    try:
        cursor = conn.cursor()
        
        if date:
            cursor.execute("""INSERT INTO purchases (product, variant, price, quantity, purchase_date) 
                VALUES (?, ?, ?, ?, ?);""", (product, variant, price, quantity, date))
        else:
            cursor.execute("""INSERT INTO purchases (product, variant, price, quantity) 
                VALUES (?, ?, ?, ?);""", (product, variant, price, quantity))
        
        conn.commit()
        print(f"Purchase registered: {quantity}x {product} [{variant}] | ${price} per unit.")
        
    except sqlite3.Error as e:
        print(f"Error registering purchase: {e}")
    finally:
        conn.close()
        
        
        
#Test Zone

if __name__ == "__main__":
    
    initialize_sys()
    
    
    print("--- Testing inventory database ---")
    
    #Add categories
    add_category("Perifericos")
    add_category("Cables")
    
    #Add products
    add_product("Ajazz AJ139 V2", "Perifericos")
    add_product("Ethernet CAT6 20M", "Cables")
    
    #Add purchases
    register_purchase("Ajazz AJ139 V2", 30, variant="Rojo", quantity=5)
    register_purchase("Ethernet CAT6 20M", 4, quantity=2)
    
    #Testing unregistered product, it must fail
    register_purchase("Fake product",10,quantity = 1)
    
    
    print_purchases()