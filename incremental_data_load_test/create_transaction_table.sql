CREATE TABLE IF NOT EXISTS transaction (
    order_id VARCHAR(255) PRIMARY KEY,
    user_id VARCHAR(255),
    product_id VARCHAR(255),
    quantity INT,
    amount DECIMAL(10, 2),
    order_date DATE
);