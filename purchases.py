import sqlite3
from database import connect_db, initialize_sys

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
        
        
def get_purchases():
    conn = connect_db()
    if conn is None: return
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM purchases ORDER BY id ASC;")
        purchases = cursor.fetchall()
        
        print("\n=== Purchases ===")
        if not purchases:
            return
          
        print("=" * 60 + " Purchases " + "=" * 60)
        print(f"{'ID':<4} | {'Product Name':<40} | {'Variant':<8} | {'Unit Price':<10} | {'Qty':<5} | {'Sold':<5} | {'Stock':<6} | {'Total Cost':<11} | {'Purchase Date':<9}")
        print("=" * 131)
          
        for row in purchases:
            id_p, product, variant, price, quantity, sold, purchase_date = row
            
            stock = quantity - sold
            total_investment = price * quantity
            display_date = purchase_date if purchase_date else "----"
            
            print(f"""{id_p:<4} | {product:<40} | {variant:<8} | ${price:<9.2f} | {quantity:<5} | {sold:<5} | {stock:<6} | ${total_investment:<10.2f} | {display_date:<9}""")
            
    except sqlite3.Error as e:
        print(f"Error fetching purchases: {e}")
    finally:
        conn.close()