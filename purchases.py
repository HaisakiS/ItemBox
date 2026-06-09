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
        
def register_purchase(product, price, variant = "Unico", quantity=1, date = None, status = "In Transit"):
    conn = connect_db()
    if conn is None: return
    
    try:
        cursor = conn.cursor()
        
        if date:
            cursor.execute("""INSERT INTO purchases (product, variant, price, quantity, purchase_date,status) 
                VALUES (?, ?, ?, ?, ?, ?);""", (product, variant, price, quantity, date, status))
        else:
            cursor.execute("""INSERT INTO purchases (product, variant, price, quantity, status) 
                VALUES (?, ?, ?, ?, ?);""", (product, variant, price, quantity, status))
        
        conn.commit()
        print(f"Purchase registered {status} : {quantity}x {product} [{variant}] | ${price} per unit.")
        
    except sqlite3.Error as e:
        print(f"Error registering purchase: {e}")
    finally:
        conn.close()
        
        
def get_purchases():
    conn = connect_db()
    if conn is None: return
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, product, variant, price, quantity, sold, purchase_date, status FROM purchases ORDER BY id ASC;")
        purchases = cursor.fetchall()
        
        print("\n=== Purchases ===")
        if not purchases:
            return
          
        print("\n" + "=" * 65 + " Purchases & Logistics " + "=" * 65)
        print(f"{'ID':<4} | {'Product Name':<35} | {'Variant':<12} | {'Unit Price':<10} | {'Qty':<5} | {'Sold':<5} | {'Stock':<6} | {'Status':<11} | {'Purchase Date':<11}")
        print("=" * 150)
          
        for row in purchases:
            id_p, product, variant, price, quantity, sold, purchase_date, status = row
            
            stock = quantity - sold
            
            if stock == 0:
                status = "Out of Stock"
            
            print(f"{id_p:<4} | {product:<35} | {variant:<12} | ${price:<9.2f} | {quantity:<5} | {sold:<5} | {stock:<6} | {status:<12} | {purchase_date:<11}")
            
    except sqlite3.Error as e:
        print(f"Error fetching purchases: {e}")
    finally:
        conn.close()
        
        
def update_purchase_status(purchase_id):
    conn = connect_db()
    if conn is None: return
    
    try:
        cursor = conn.cursor()
        cursor.execute("""UPDATE purchases 
                       SET status = 'Received'
                       WHERE id = ? AND status = 'In Transit';""", (purchase_id,))
        
        if cursor.rowcount == 0:
            print(f"No changes made. Check if Purchase ID {purchase_id} exists and is currently 'In Transit'.")
            return
        
        conn.commit()
        print(f"Purchase with id {purchase_id} updated succesfully.")
    except sqlite3.Error as e:
        print(f"Error updating purchase: {e}")
    finally:
        conn.close()