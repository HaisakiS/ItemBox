--TABLES

CREATE TABLE IF NOT EXISTS categories (
	name TEXT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS products (
	name TEXT PRIMARY KEY,
	category TEXT,
	FOREIGN KEY (category) REFERENCES categories (name)
);

CREATE TABLE IF NOT EXISTS purchases (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	product TEXT NOT NULL,
	variant TEXT DEFAULT 'Unico',
	price REAL NOT NULL,
	quantity INTEGER NOT NULL,
	sold INTEGER DEFAULT 0,
	purchase_date TEXT DEFAULT CURRENT_DATE,
	status TEXT DEFAULT 'In Transit',
	FOREIGN KEY (product) REFERENCES products (name)
);

CREATE TABLE IF NOT EXISTS sales (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_purchase INTEGER,
	price_sell REAL,
	publication_date TEXT DEFAULT CURRENT_DATE,
	sale_date TEXT,
	discount REAL DEFAULT 0,
	status TEXT DEFAULT 'Listed',
	FOREIGN KEY (id_purchase) REFERENCES purchases (id)
);

--TRIGGERS

CREATE TRIGGER IF NOT EXISTS stock_after_sale --Increase sold after a sale is insertes with status 'Sold' 
AFTER INSERT ON sales
FOR EACH ROW
WHEN NEW.status = 'Sold'
BEGIN
    UPDATE purchases SET sold = sold + 1 WHERE id = NEW.id_purchase;
END;

CREATE TRIGGER IF NOT EXISTS stock_update_sale --Increase sold after a sale is updated to status 'Sold'
AFTER UPDATE ON sales
FOR EACH ROW
WHEN OLD.status != 'Sold' AND NEW.status = 'Sold'
BEGIN
    UPDATE purchases SET sold = sold + 1 WHERE id = NEW.id_purchase;
END;

CREATE TRIGGER IF NOT EXISTS stock_delete_sale --Decrease sold after a sale with sattus 'Sold' is deleted
AFTER DELETE ON sales
FOR EACH ROW
WHEN OLD.status = 'Sold'
BEGIN
    UPDATE purchases SET sold = sold - 1 WHERE id = OLD.id_purchase;
END;