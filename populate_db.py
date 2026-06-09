import sqlite3
from database import connect_db
from reset_db import reset_database

def populate_real_data():
    
    reset_database()
    
    conn = connect_db()
    if conn is None:
        print("Could not connect to the database.")
        return
        
    try:
        cursor = conn.cursor()
        
        # 1. INSERT CATEGORIES
        print("Inserting categories...")
        cursor.execute("INSERT INTO categories (name) VALUES ('Peripherals');")
        
        # 2. INSERT UNIQUE PRODUCTS INTO CATALOG
        print("Populating product catalog...")
        catalog_products = [
            ('FonkiiDokii Controller Switch', 'Peripherals'),
            ('EasySMX X05 Pro', 'Peripherals'),
            ('Gamesir Supernova', 'Peripherals'),
            ('Gamesir X5 Lite', 'Peripherals'),
            ('Gamesir Tegenaria Lite', 'Peripherals'),
            ('Ajazz AJ139 V2', 'Peripherals'),
            ('FonkiiDokii Controller G6', 'Peripherals'),
            ('EasySMX D05', 'Peripherals'),
            ('Gamesir Cyclone 2', 'Peripherals'),
            ('Attack Shark X11', 'Peripherals'),
            ('Gamesir Nova Lite 2', 'Peripherals'),
            ('Gamesir Nova Lite', 'Peripherals'),
            ('EasySMX M20', 'Peripherals'),
            ('NYXI Echtpower', 'Peripherals'),
            ('Acegamer Switch Controller x2', 'Peripherals')
        ]
        cursor.executemany("INSERT OR IGNORE INTO products (name, category) VALUES (?, ?);", catalog_products)

        # 3. INSERT INTO PURCHASES
        #    (id, product, variant, price, quantity, sold, purchase_date, status)
        print("Registering all purchases (including items in transit)...")
        purchases_data = [
            (1, 'FonkiiDokii Controller Switch', 'Negro', 18.00, 1, 0, '2026-05-06', 'Received'),
            (2, 'EasySMX X05 Pro', 'Negro', 32.00, 1, 0, '2026-05-06', 'Received'),
            (3, 'Gamesir Supernova', 'Azul', 66.00, 1, 0, '2026-05-06', 'Received'),
            (4, 'Gamesir X5 Lite', 'Negro', 30.00, 1, 0, '2026-05-06', 'Received'),
            (5, 'Gamesir Tegenaria Lite', 'Blanco', 20.00, 1, 0, '2026-05-12', 'Received'),
            (6, 'Ajazz AJ139 V2', 'Rojo', 30.00, 1, 0, '2026-05-12', 'Received'),
            (7, 'FonkiiDokii Controller G6', 'Negro', 20.00, 1, 0, '2026-05-20', 'Received'),
            (8, 'EasySMX D05', 'Negro', 50.00, 1, 0, '2026-06-04', 'Received'),
            (9, 'Gamesir Cyclone 2', 'Blanco', 80.00, 1, 0, '2026-06-04', 'Received'),
            (10, 'Attack Shark X11', 'Rojo', 27.00, 1, 0, '2026-06-04', 'Received'),
            (11, 'Gamesir X5 Lite', 'Verde', 33.00, 1, 0, '2026-06-04', 'Received'),
            (12, 'Gamesir Nova Lite 2', 'Blanco', 18.00, 1, 0, '2026-06-04', 'Received'),
            (13, 'EasySMX X05 Pro', 'Negro', 38.00, 1, 0, '2026-06-04', 'Received'),
            (14, 'Gamesir Supernova', 'Azul', 62.00, 1, 0, '2026-06-04', 'Received'),
            
            (15, 'Gamesir Nova Lite', 'Negro', 25.00, 1, 0, '2026-06-05', 'In Transit'),
            (16, 'EasySMX M20', 'Unico', 90.00, 1, 0, '2026-06-05', 'In Transit'),
            (17, 'NYXI Echtpower', 'Unico', 35.00, 1, 0, '2026-06-06', 'In Transit'),
            (18, 'EasySMX X05 Pro', 'Blanco', 28.00, 1, 0, '2026-06-06', 'In Transit'),
            (19, 'Gamesir Nova Lite 2', 'Blanco', 45.00, 1, 0, '2026-06-07', 'In Transit'),
            (20, 'Gamesir X5 Lite', 'Gris', 30.00, 1, 0, '2026-06-07', 'In Transit'),
            (21, 'Acegamer Switch Controller x2', 'Blanco/Negro', 43.00, 1, 0, '2026-06-07', 'In Transit')
        ]
        
        cursor.executemany("""
            INSERT INTO purchases (id, product, variant, price, quantity, sold, purchase_date, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """, purchases_data)

        # 4. INSERT INTO SALES
        print("Publishing active listings and locking closed sales...")
        sales_data = [
            #(id_purchase, price_sell, status, discount, publication_date, sale_date)
            (1, 35.00, 'Sold', 0.00, '2026-05-06', '2026-05-14'),
            (2, 80.00, 'Sold', 5.00, '2026-05-06', '2026-05-14'),
            (3, 140.00, 'Sold', 0.00, '2026-05-06', '2026-05-15'),
            (4, 90.00, 'Sold', 0.00, '2026-05-06', '2026-05-10'),
            (5, 50.00, 'Sold', 10.00, '2026-05-12', '2026-05-29'),
            (6, 70.00, 'Sold', 10.00, '2026-05-12', '2026-06-01'),
            (7, 40.00, 'Sold', 5.00, '2026-05-20', '2026-05-21'),
            (8, 110.00, 'Listed', 0.00, '2026-06-04', None),
            (9, 190.00, 'Sold', 0.00, '2026-06-04', '2026-06-08'),
            (10, 60.00, 'Sold', 4.00, '2026-06-04', '2026-06-05'),
            (11, 90.00, 'Listed', 0.00, '2026-06-04', None),
            (12, 110.00, 'Listed', 0.00, '2026-06-04', None),
            (13, 90.00, 'Listed', 0.00, '2026-06-04', None),
            (14, 140.00, 'Listed', 0.00, '2026-06-04', None)
        ]
        
        cursor.executemany("""
            INSERT INTO sales (id_purchase, price_sell, status, discount, publication_date, sale_date)
            VALUES (?, ?, ?, ?, ?, ?);
        """, sales_data)
        
        conn.commit()
        print("\nDatabase successfully wiped and re-populated with fresh logistics metrics!")
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    populate_real_data()