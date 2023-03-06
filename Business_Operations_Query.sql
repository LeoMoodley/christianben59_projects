CREATE TABLE customers (
  customer_id INT PRIMARY KEY,
  customer_name VARCHAR(50),
  email VARCHAR(50) UNIQUE,
  phone_number VARCHAR(20),
  shipping_address VARCHAR(200)
);

CREATE TABLE products (
  product_id INT PRIMARY KEY,
  product_name VARCHAR(50),
  description TEXT,
  price DECIMAL(10,2),
  stock_quantity INT
);
CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  order_date DATE,
  customer_id INT,
  order_status VARCHAR(20),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
CREATE TABLE order_items (
  order_id INT,
  product_id INT,
  quantity INT,
  price DECIMAL(10,2),
  PRIMARY KEY (order_id, product_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);
CREATE TABLE shipments (
  shipment_id INT PRIMARY KEY,
  order_id INT,
  shipment_status VARCHAR(20),
  FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
CREATE TABLE payment_methods (
  payment_method_id INT PRIMARY KEY,
  payment_method_name VARCHAR(50),
  payment_method_type VARCHAR(20)
);
CREATE TABLE payments (
  payment_id INT PRIMARY KEY,
  payment_date DATE,
  payment_method_id INT,
  payment_amount DECIMAL(10,2),
  FOREIGN KEY (payment_method_id) REFERENCES payment_methods(payment_method_id)
);
CREATE TABLE orders_payments (
  order_id INT,
  payment_id INT,
  PRIMARY KEY (order_id, payment_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (payment_id) REFERENCES payments(payment_id)
);
