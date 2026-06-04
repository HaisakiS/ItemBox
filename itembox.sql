--TABLES

CREATE TABLE IF NOT EXISTS categories (
	name TEXT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS products (
	name TEXT PRIMARY KEY,
	category TEXT,
	FOREIGN KEY (category) REFERENCES categories (name)
);

CREATE TABLE IF NOT EXISTS price_tracker (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
	variant TEXT,
	lowest_price REAL,
	price_date TEXT DEFAULT CURRENT_DATE,
	FOREIGN KEY (product) REFERENCES products (name),
	
	UNIQUE (product, variant)
);

CREATE TABLE IF NOT EXISTS purchases (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	product TEXT,
	variant TEXT,
	price REAL,
	quantity INTEGER DEFAULT 1,
	sold INTEGER DEFAULT 0,
	purchase_date TEXT DEFAULT CURRENT_DATE,
	FOREIGN KEY (product) REFERENCES products (name)
);

CREATE TABLE IF NOT EXISTS sales (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_purchase INTEGER,
	price_sell REAL,
	publication_date TEXT DEFAULT CURRENT_DATE,
	sale_date TEXT,
	discount REAL DEFAULT 0,
	status TEXT DEFAULT 'Publicado',
	FOREIGN KEY (id_purchase) REFERENCES purchases (id)
);

--TRIGGERS

CREATE TRIGGER IF NOT EXISTS stock_after_sale --Increase sold after a sale is insertes with status 'Vendido' 
AFTER INSERT ON sales
FOR EACH ROW
WHEN NEW.status = 'Vendido'
BEGIN
    UPDATE purchases SET sold = sold + 1 WHERE id = NEW.id_purchase;
END;

CREATE TRIGGER IF NOT EXISTS stock_update_sale --Increase sold after a sale is updated to status 'Vendido'
AFTER UPDATE ON sales
FOR EACH ROW
WHEN OLD.status != 'Vendido' AND NEW.status = 'Vendido'
BEGIN
    UPDATE purchases SET sold = sold + 1 WHERE id = NEW.id_purchase;
END;

CREATE TRIGGER IF NOT EXISTS stock_delete_sale --Decrease sold after a sale with sattus 'Vendido' is deleted
AFTER DELETE ON sales
FOR EACH ROW
WHEN OLD.status = 'Vendido'
BEGIN
    UPDATE purchases SET sold = sold - 1 WHERE id = OLD.id_purchase;
END;
