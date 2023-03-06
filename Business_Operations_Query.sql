-- Create a table for customers
CREATE TABLE customers (
    id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);

-- Create a table for addresses
CREATE TABLE addresses (
    id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    street_address VARCHAR(100) NOT NULL,
    city VARCHAR(50) NOT NULL,
    state VARCHAR(50) NOT NULL,
    zip_code VARCHAR(20) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

-- Create a table for products
CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT NOT NULL,
    price DECIMAL(10, 2) NOT NULL
);

-- Create a table for orders
CREATE TABLE orders (
    id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    total DECIMAL(10, 2) NOT NULL,
    status VARCHAR(50) NOT NULL,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);

-- Create a table for order items
CREATE TABLE order_items (
    id INT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Insert sample data into the customers table
INSERT INTO customers (id, first_name, last_name, email, password)
VALUES (1, 'John', 'Doe', 'johndoe@example.com', 'password'),
       (2, 'Jane', 'Doe', 'janedoe@example.com', 'password');

-- Insert sample data into the addresses table
INSERT INTO addresses (id, customer_id, street_address, city, state, zip_code)
VALUES (1, 1, '123 Main St', 'Anytown', 'CA', '12345'),
       (2, 2, '456 Maple Ave', 'Anycity', 'NY', '67890');

-- Insert sample data into the products table
INSERT INTO products (id, name, description, price)
VALUES (1, 'Product 1', 'Description for Product 1', 9.99),
       (2, 'Product 2', 'Description for Product 2', 19.99),
       (3, 'Product 3', 'Description for Product 3', 29.99);

-- Insert sample data into the orders table
INSERT INTO orders (id, customer_id, order_date, total, status)
VALUES (1, 1, '2022-01-01', 9.99, 'Completed'),
       (2, 2, '2022-01-02', 49.97, 'In Progress');

-- Insert sample data into the order items table
INSERT INTO order_items (id, order_id, product_id, quantity, price)
VALUES (1, 1, 1, 1, 9.99),
       (2, 2, 2, 2, 39.98);

-- Create a view to display order information with customer names
CREATE VIEW order_info AS
SELECT o.id, c.first_name, c.last_name, o.order_date, o.total, o.status
FROM orders o
JOIN customers c ON o.customer_id = c.id;

-- Create
-- Create a stored procedure to calculate the total revenue for a customer
CREATE PROCEDURE calculate_customer_revenue (IN customer_id INT, OUT total_revenue DECIMAL(10, 2))
BEGIN
SELECT SUM(oi.price * oi.quantity) INTO total_revenue
FROM order_items oi
JOIN orders o ON oi.order_id = o.id
WHERE o.customer_id = customer_id;
END;

-- Create a trigger to update the total for an order when an order item is added or updated
CREATE TRIGGER update_order_total
AFTER INSERT, UPDATE ON order_items
FOR EACH ROW
BEGIN
UPDATE orders SET total = (
SELECT SUM(price * quantity) FROM order_items WHERE order_id = NEW.order_id
) WHERE id = NEW.order_id;
END;
