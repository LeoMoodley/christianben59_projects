SELECT 
    orders.order_id, 
    customers.customer_name, 
    products.product_name, 
    SUM(order_items.quantity * order_items.price) AS total_sale
FROM 
    orders
    INNER JOIN customers ON orders.customer_id = customers.customer_id
    INNER JOIN order_items ON orders.order_id = order_items.order_id
    INNER JOIN products ON order_items.product_id = products.product_id
WHERE 
    orders.order_date BETWEEN '2022-01-01' AND '2022-12-31'
    AND customers.country = 'United States'
GROUP BY 
    orders.order_id, 
    customers.customer_name, 
    products.product_name
ORDER BY 
    total_sale DESC
LIMIT 10;
