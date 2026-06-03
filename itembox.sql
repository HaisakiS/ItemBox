PRAGMA foreign_keys = ON;

CREATE TABLE categories (
	name TEXT PRIMARY KEY
);

CREATE TABLE products (
	name TEXT PRIMARY KEY,
	category TEXT,
	FOREIGN KEY (category) REFERENCES categories (name)
);

CREATE TABLE price_tracker (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
	variant TEXT,
	lowest_price REAL,
	price_date TEXT DEFAULT CURRENT_DATE,
	FOREIGN KEY (product) REFERENCES products (name),
	
	UNIQUE (product, variant)
);

CREATE TABLE purchases (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	product TEXT,
	variant TEXT,
	price REAL,
	quantity INTEGER DEFAULT 1,
	sold INTEGER DEFAULT 0,
	purchase_date TEXT DEFAULT CURRENT_DATE,
	FOREIGN KEY (product) REFERENCES products (name)
);

CREATE TABLE sales (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	id_purchase INTEGER,
	price_sell REAL,
	publication_date TEXT DEFAULT CURRENT_DATE,
	sale_date TEXT,
	discount REAL DEFAULT 0,
	status TEXT DEFAULT 'Publicado',
	FOREIGN KEY (id_purchase) REFERENCES purchases (id)
);