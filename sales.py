import sqlite3
from database import connect_db


def publish_for_sale(id_purchase,sell_price,publication_date = None):
    conn = connect_db()
    if conn is None: return
    
    try:
        cursor = conn.cursor()
        
        cursor.execute("SELECT status FROM purchases WHERE id = ?;", (id_purchase,))
        result = cursor.fetchone()
        
        if not result:
            print(f"Error: Purchase ID {id_purchase} does not exist.")
            return
            
        if result[0] == 'In Transit':
            print(f"Logistics Block: Item with Purchase ID {id_purchase} is still 'In Transit'. You cannot publish it until it arrives!")
            return
        
        if publication_date:
            cursor.execute("""
                INSERT INTO sales (id_purchase, price_sell, publication_date)
                VALUES (?, ?, ?);
            """, (id_purchase, sell_price, publication_date))
        else:
            cursor.execute("""
                INSERT INTO sales (id_purchase, price_sell)
                VALUES (?, ?);
            """, (id_purchase, sell_price))

        conn.commit()
        print(f"Item with purchase id {id_purchase} successfully published at ${sell_price:.2f}")
    except sqlite3.Error as e:
        print(f"Error publishing for sale: {e}")
    finally:
        conn.close()
        
        
def record_sale(sale_id, discount=0, sale_date=None): #Updates existing sale to 'Sold'
    conn = connect_db()
    if conn is None: return
    
    try:
        cursor = conn.cursor()
            
        if sale_date is None:
            #Use today as default date
            from datetime import date
            sale_date = date.today().strftime("%Y-%m-%d")
        
        
        #Obtaining associated purchase to print product name
        cursor.execute("""
            SELECT s.id_purchase, pur.product 
            FROM sales s
            JOIN purchases pur ON s.id_purchase = pur.id
            WHERE s.id = ? AND s.status != 'Sold';
        """, (sale_id,))
        purchase_data = cursor.fetchone()
        
        #Update sale to 'Sold'
        cursor.execute("""
            UPDATE sales
            SET status = 'Sold', discount = ?, sale_date = ?
            WHERE id = ? AND status != 'Sold';
        """, (discount, sale_date, sale_id))
            
        if cursor.rowcount > 0: #verifies that a row was modified
            product_name = purchase_data[1]
            
            conn.commit()
            print(f"Item {product_name} with Sale ID {sale_id} successfully recorded. Stock updated.")
        else:
            print(f"Could not record sale. ID {sale_id} doesn't exist or is already sold.")
    except sqlite3.Error as e:
        print(f"Error recording sale in DB: {e}")
    finally:
        conn.close()
        
        
def get_sales():
    conn = connect_db()
    if conn is None: return
    
    try:
        cursor = conn.cursor()
        # JOIN to get product info for the sale
        cursor.execute("""
            SELECT s.id, pur.product, pur.variant, pur.price, s.price_sell, s.discount, s.sale_date, s.status
            FROM sales s
            JOIN purchases pur ON s.id_purchase = pur.id
            ORDER BY s.sale_date DESC, s.id DESC;
        """)
        
        sales = cursor.fetchall() # (id, product, variant, purchase_price, price_sell, discount, sale_date, status)
        if not sales:
            return
          
        print("\n" + "=" * 61 + " Sales " + "=" * 60)
        print(f"{'ID':<4} | {'Product Name':<40} | {'Variant':<8} | {'Cost':<7} | {'Price Sell':<11} | {'Discount':<8} | {'Sale Date':<11} | {'Status':<9} | {'Profit':<7}")
        print("=" * 128)
          
        for row in sales:
            sale_id, product, variant, purchase_price, price_sell, discount, sale_date, status = row
            
            #Default values if not sold
            if status != 'Sold':
                final_sell_price = 0.00
                profit = 0.00
                display_status = "Listed"
                display_date = "----"
            else:
                final_sell_price = price_sell - discount
                profit = final_sell_price - purchase_price
                display_status = "Sold"
                display_date = sale_date if sale_date else "----"
            
            print(f"""{sale_id:<4} | {product:<40} | {variant:<8} | {purchase_price:<7.2f} | {final_sell_price:<11.2f} | {discount:<8.2f} | {display_date:<11} | {display_status:<9} | {profit:<7.2f}""")
            
    except sqlite3.Error as e:
        print(f"Error fetching sales: {e}")
    finally:
        conn.close()
        
    
def get_sales_dashboard():
    conn = connect_db()
    if conn is None: return
    
    try:
        cursor = conn.cursor()
        
        #Count how many items have status 'Sold' and calculate the total revenue (sell_price - discount) and cost
        cursor.execute("""
            SELECT 
                COUNT(s.id) AS units_sold,
                SUM(s.price_sell - s.discount) AS total_revenue,
                SUM(pur.price) AS total_cost
            FROM sales s
            JOIN purchases pur ON s.id_purchase = pur.id
            WHERE s.status = 'Sold';
        """)
        
        result = cursor.fetchone()
        
        # If there are no sales, using SUM would return None, so make it default to 0
        units_sold = result[0] if result[0] else 0
        total_revenue = result[1] if result[1] else 0.0
        total_cost = result[2] if result[2] else 0.0
        
        net_profit = total_revenue - total_cost
        roi = (net_profit / total_cost * 100) if total_cost > 0 else 0.0
        
        print("\n==================================================")
        print("           📊 itemBox FINANCIAL DASHBOARD         ")
        print("==================================================")
        print(f" Total Units Sold        : {units_sold} units")
        print(f" Total Revenue           : ${total_revenue:<10.2f}")
        print(f" Cost of Goods Sold      : ${total_cost:<10.2f}")
        print("--------------------------------------------------")
        
        if net_profit >= 0:
            print(f" NET PROFIT ACCUMULATED  : ${net_profit:<10.2f} 🚀")
        else:
            print(f" NET LOSS ACCUMULATED    : ${net_profit:<10.2f} ⚠️")
            
        print(f" Return on Investment    : {roi:<6.2f}%")
        print("==================================================\n")
        
    except sqlite3.Error as e:
        print(f"Error generating dashboard: {e}")
    finally:
        conn.close()