# 📦 itemBox v1.0

**itemBox** is a robust, modular CLI inventory management, purchasing, and logistics tracking system tailored for tech, peripherals, and import-resellers. 

Unlike basic inventory apps that just count units, **itemBox** relationally connects every single sale to its specific purchase batch. This batch-based architecture allows the system to audit precise financial performance, manage complex shipping logistics, and calculate real-time metrics without data redundancy.

---

## 🚀 Key Features

* **Batch-Based Stock Control:** Track identical products purchased at different prices or on different dates independently.
* **Smart Logistics States:** Native tracking for imports through a two-phase pipeline: `In Transit` (locked from immediate sale) and `Received` (physically in stock).
* **Automated Data Integrity (SQLite Triggers):** Heavy use of database triggers to automatically calculate `sold` units and dynamic `Stock` changes during insertions, updates, or deletions.
* **Live Financial Dashboard:** Computes real-time financials including Total Revenue, Cost of Goods Sold (COGS), Accumulated Net Profit/Loss, and precise Return on Investment (ROI).
* **Input Blindfolding:** Robust error-handling in the CLI wrapper to prevent system crashes against invalid data types or format errors.

---

## 🛠️ Tech Stack

* **Language:** Python 3.x (Core logic and interactive CLI menu)
* **Database Engine:** SQLite 3 (Relational structure with active constraints)
* **Architecture:** Modular Backend-Frontend split (`main` ➔ `menu` ➔ `sales`/`purchases` ➔ `database`)

---

## 📐 Database Design & Relational Schema

The database architecture is optimized for SQLite with `FOREIGN KEY` constraints enforced at runtime:

1. **`categories`**: Master table defining allowed item families (e.g., *Peripherals*).
2. **`products`**: Catalog table mapping specific models to their parent categories.
3. **`purchases`**: The inventory core. Tracks individual batch costs, variants, quantities acquired, purchase dates, and current logistics status (`In Transit` vs `Received`).
4. **`sales`**: The outflow registry. Maps each sale listing directly to an item's `id_purchase` batch to dynamically audit financial performance.

### ⚡ Automated Database Triggers
* `stock_after_sale`: Increments the batch `sold` count immediately when a sale transitions to `'Sold'`.
* `stock_update_sale`: Manages conditional step-ups if a listing shifts status (e.g., from `'Listed'` to `'Sold'`).
* `stock_delete_sale`: Automatically restores stock counts if a closed sale is removed or rolled back.

---

## 📂 Project Structure

```text
itemBox/
├── database.py       # DB connection pool, PRAGMA setup & system initializer
├── itembox.sql       # Relational schema (Tables & Triggers)
├── main.py           # Core execution loop and app entry point
├── menu.py           # CLI interactive handlers and safe input wrappers
├── populate_db.py    # Hard-reset and automated seed script with real metrics
├── purchases.py      # Inventory core backend (Ingress, logistics updates)
├── reset_db.py       # File-level database wiping utility
└── sales.py          # Sales pipeline backend (Listings, closings, financial dashboard)
