CREATE TABLE IF NOT EXISTS user_transaction_amount (
    user_id TEXT,
    total_sales REAL,
    average_sales REAL
);

CREATE TABLE IF NOT EXISTS daily_transaction_amount (
    order_date TEXT,
    total_sales REAL,
    min_sales REAL,
    max_sales REAL,
    average_sales REAL,
    vat REAL
);

CREATE TABLE IF NOT EXISTS product_sales (
    product_id TEXT,
    number_of_transactions INTEGER,
    total_sales REAL
);

-- for task 3 
CREATE TABLE IF NOT EXISTS user_location_gender_sales (
    location TEXT,
    gender TEXT,
    total_sales REAL,
    min_sales REAL,
    max_sales REAL,
    average_sales REAL
);

CREATE TABLE IF NOT EXISTS top_sellers_chiangmai (
    order_date TEXT,
    product_id TEXT,
    sales REAL
);
