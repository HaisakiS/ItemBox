SELECT * FROM categories;

SELECT * FROM products;

SELECT * FROM price_tracker;

SELECT * FROM purchases;

SELECT * FROM sales;

SELECT product,price,quantity - sold as stock FROM purchases;