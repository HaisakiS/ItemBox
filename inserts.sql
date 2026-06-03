PRAGMA foreign_keys = ON;

-- INSERTS IN CATEGORIES
INSERT OR IGNORE INTO categories (name) VALUES 
    ('Mando'),
    ('Mouse'),
    ('Peluche'),
    ('Accesorio');

-- INSERTS IN PRODUCTS
-- PRODUCTS MUST BELONG TO A CATEGORY
INSERT OR IGNORE INTO products (name, category) VALUES  --IGNORE TO AVOID ERRRORS ON DUPLICATES
    ('FonkiiDokii Controller Switch', 'Mando'),
    ('EasySMX X05 Pro', 'Mando'),
    ('Gamesir Supernova', 'Mando'),
    ('Gamesir X5 Lite', 'Mando'),
    ('Gamesir Tegenaria Lite', 'Mando'),
    ('Ajazz AJ139 V2', 'Mouse'),
    ('FonkiiDokii Controller G6', 'Mando'),
    ('EasySMX D05', 'Mando'),
    ('Gamesir Cyclone 2', 'Mando'),
    ('Attack Shark X11', 'Mouse'),
    ('Gamesir Nova Lite 2', 'Mando'),
    ('Gamesir Nova Lite', 'Mando'),
    ('EasySMX M20', 'Mando'),
    ('NYXI Echtpower', 'Mando'),
    ('Base de carga mandos PS5', 'Accesorio'),
    ('Silksong Eira Plushie', 'Peluche'),
    ('Silksong Sherma Plushie', 'Peluche'),
    ('FonkiiDokii Telescopic Controller', 'Mando'),
    ('Mando Wukong', 'Mando'),
    ('Peluche Ajolote', 'Peluche'),
    ('Flydigi Dunefox', 'Mando'),
    ('FonkiiDokii Controller', 'Mando'),
    ('Perro Mecanico', 'Accesorio'),
    ('Acegamer Pocket', 'Mando'),
    ('Gamesir G8+', 'Mando'),
    ('EasySMX D10', 'Mando'),
    ('Gamesir G7 Pro', 'Mando'),
    ('Echtpower Switch Controller (GC)', 'Mando');


-- INSERT IN PURCHASES
INSERT INTO purchases (product, variant, price, quantity) VALUES 
    ('FonkiiDokii Controller Switch', 'Negro', 18.00, 1),
    ('EasySMX X05 Pro', 'Negro', 32.00, 1),
    ('Gamesir Supernova', 'Azul', 66.00, 1),
    ('Gamesir X5 Lite', 'Negro', 30.00, 1),
    ('Gamesir Tegenaria Lite', 'Blanco', 20.00, 1),
    ('Ajazz AJ139 V2', 'Rojo', 30.00, 1),
    ('FonkiiDokii Controller G6', 'Negro', 20.00, 1),
    ('EasySMX D05', 'Negro', 50.00, 1),
    ('Gamesir Cyclone 2', 'Blanco', 80.00, 1),
    ('Attack Shark X11', 'Rojo', 27.00, 1),
    ('Gamesir X5 Lite', 'Verde', 33.00, 1),
    ('Gamesir Nova Lite 2', 'Blanco', 18.00, 1),
    ('EasySMX X05 Pro', 'Negro', 38.00, 1), 
    ('Gamesir Supernova', 'Azul', 62.00, 1),
    ('Gamesir Nova Lite', 'Negro', 25.00, 1),
    ('EasySMX M20', NULL, 90.00, 1),
    ('NYXI Echtpower', NULL, 35.00, 1),
    ('EasySMX X05 Pro', 'Blanco', 28.00, 1),
    ('Gamesir Nova Lite 2', 'Blanco', 45.00, 1);


-- INSERTS IN PRICE_TRACKER
-- COMBINATION "PRODUCT-VARIANT" MUST BE UNIQUE, ELSE IT WILL UPDATE THE PRICE (*solve, updates even if higher price registered)
INSERT OR REPLACE INTO price_tracker (product, variant, lowest_price) VALUES --REPLACE TO UPDATE NEW LOWEST PRICE
    ('Base de carga mandos PS5', 'Rojo', 16.80),
    ('Gamesir Tegenaria Lite', 'Negro/Blanco', 30.00),
    ('Attack Shark X11', 'Negro/Blanco/Rojo', 42.00),
    ('Silksong Eira Plushie', NULL, 17.00),
    ('Silksong Sherma Plushie', NULL, 12.00),
    ('FonkiiDokii Telescopic Controller', 'Blanco', 26.00),
    ('Base de carga mandos PS5', 'Blanco', 13.00),
    ('Mando Wukong', NULL, 45.00),
    ('Peluche Ajolote', NULL, 7.00),
    ('Flydigi Dunefox', 'Rosa', 63.00),
    ('FonkiiDokii Controller', 'Negro/Blanco', 28.00),
    ('Perro Mecanico', 'Naranja', 10.00),
    ('Gamesir Nova Lite 2', 'Negro/Blanco', 48.00),
    ('Gamesir X5 Lite', 'Negro/Verde', 40.00),
    ('Acegamer Pocket', 'Negro/Blanco', 28.00),
    ('Gamesir Supernova', 'Azul/Rosa', 75.00),
    ('EasySMX D05', NULL, 75.00),
    ('Gamesir Cyclone 2', 'Negro/Blanco', 111.00),
    ('Gamesir Nova Lite', 'Negro/Blanco/Rosa/Gris', 50.00),
    ('EasySMX X05 Pro', 'Negro/Blanco', 54.00),
    ('Gamesir G8+', NULL, 165.00),
    ('EasySMX D10', NULL, 94.00),
    ('Gamesir G7 Pro', NULL, 225.00),
    ('Echtpower Switch Controller (GC)', NULL, 48.00),
    ('EasySMX M20', NULL, 130.00);
	
	
-- INSERTS IN SALES
INSERT INTO sales (id_purchase, price_sell, publication_date, sale_date, discount, status) VALUES
	(3, 145.00, '2026-06-03', '2026-06-05', 0.00, 'Vendido'),
	(4, 100.00, '2026-06-03', '2026-06-05', 5.00, 'Vendido'),
	(6, 70.00, '2026-06-05', '2026-06-07', 10.00, 'Vendido');

--STOCK UPDATE ON SALES (*look for an automated method)
UPDATE purchases 
SET sold = sold + 1 
WHERE id = 3 OR id = 4 OR id = 6