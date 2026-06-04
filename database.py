import sqlite3
from sqlite3 import Error

DB_NAME = "itemboxDB.db"
SCHEMA_FILE = "itembox.sql"

def connect_db():
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        conn.execute("PRAGMA foreign_keys = ON;")
        return conn
    except ERROR as e:
        print(f"Error connecting to database: {e}")
    return conn


def initialize_sys():
    conn = connect_db()
    if conn is None:
        return
    try:
        cursor = conn.cursor()
        
        with open(SCHEMA_FILE, "r", encoding="utf-8") as  f:
            sql_script = f.read()
           
        cursor.executescript(sql_script)
        
        conn.commit()
        print("Database initialized using schema.sql")
    except (Error, FileNotFoundError) as e:
        print(f"Error al inicializar el sistema: {e}")
    finally:
        conn.close()
        
    
def print_purchases():
    conn = connect_db()
    if conn is None: return
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM purchases;")
        
        compras = cursor.fetchall() #(id,porduct,variant,price,quantity,sold,purchase_date)
        
        print("\n=== Inventory ===")
        if not compras:
            return
            
        for row in compras:
            id_p, product, variant, price, quantity, sold, purchase_date = row
            stock = quantity - sold
            
            print(f"ID: {id_p} | {product} [{variant}]")
            print(f"  💰 Price: ${price:.2f} | 📦 Quantity: {quantity} | 🛒 Sold: {sold} | 🟢 Stock: {stock}")
            print("-" * 80)
            
    except sqlite3.Error as e:
        print(f"Error fetching purchases: {e}")
    finally:
        conn.close()
        
if __name__ == "__main__":
    initialize_sys()
    