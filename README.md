# 📦 ItemBox v1.0

A modular inventory and import logistics management system built with **Python** and **SQLite3**, designed to track stock by purchase batches, manage inbound shipments, and analyze business performance in real time through a lightweight command-line interface.

![Python](https://img.shields.io/badge/Python-3.x-blue)
![SQLite](https://img.shields.io/badge/SQLite-3-green)
![CLI](https://img.shields.io/badge/Interface-CLI-orange)

---

## 🚀 Key Features

* **Batch-Based Stock Control:** Track identical products purchased at different prices or on different dates independently.
* **Smart Logistics States:** Native tracking for imports through a two-phase pipeline: `In Transit` (locked from immediate sale) and `Received` (physically in stock).
* **Automated Data Integrity (SQLite Triggers):** Heavy use of database triggers to automatically calculate `sold` units and dynamic `Stock` changes during insertions, updates, or deletions.
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
```

---

## ⚙️ Installation & Usage

### 1. Requirements

- Python 3.x
- SQLite3 (included with Python's standard library)

No external dependencies are required.

### 2. Initialize the Database

Create the schema, triggers, and sample data:

```bash
python populate_db.py
```

### 3. Launch the Application

```bash
python main.py
```

---

## 📊 CLI Preview

```text
======================================
          itemBox SYSTEM v1.0
======================================

1. 📥 Register New Purchase
2. 🔄 Mark Purchase as Received
3. 📦 Publish Item for Sale
4. 💰 Record a Closed Sale
5. 📋 View Inventory Stock
6. 📈 View Sales History
7. 📊 View Financial Dashboard
8. ❌ Exit

======================================
Choose an option (1-8):
```
---

## 📄 License

This project was developed for educational purposes and to explore inventory management, relational database design, and automation using SQLite triggers.
