# 📦 itemBox

**itemBox** is a smart inventory management, purchasing, and sales tracking system tailored for tech, peripherals, and collectibles resellers. 

This system goes beyond basic record-keeping by relationally connecting every sale to its specific purchase batch. This architecture allows you to calculate exact net profits, track real-time stock levels, and monitor historical lowest market prices.

---

## Key Features

* **Batch-Based Stock Control:** Track identical products purchased at different prices or on different dates independently.
* **Exact Financial Metrics:** Calculate real income and net profits by factoring in platform fees, shipping costs, or discounts in real time.
* **Price Tracker:** Prevents duplicate product-variant combinations and logs the lowest cost ever found in the market.

---

## Database Design (Relational Schema)

The database architecture is optimized for SQLite and consists of 5 interconnected tables:

1.  **`categories`**: Master table defining allowed item types (e.g., *Mando, Mouse, Peluche*).
2.  **`products`**: Master table for product models, linked directly to a category.
3.  **`price_tracker`**: A deal history tracker enforcing uniqueness on the combination of `product` and `variant`.
4.  **`purchases`**: The core of the inventory. It tracks costs, quantities acquired, and units sold (`sold`) to calculate current stock.
5.  **`sales`**: The outflow registry connecting directly to a `id_purchase` to audit the financial performance of each individual unit.


## Tech Stack

* **Database Engine:** SQLite 3
* **Language:** SQL (Relational Structure)

---

## ⚙️ Initial Setup

To set up the **itemBox** database, clone this repository and run the database creation scripts. Additionally you can test the databse using the inserts, drops and query files in the repository.
