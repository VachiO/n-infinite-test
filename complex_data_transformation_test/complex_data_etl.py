import sqlite3
import pandas as pd

DATABASE_PATH = 'incremental_data_load_test/transactions.db'

# Create SQLite connection
conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

print("Connect successfully")

# Load user_info.csv into the database
user_info_path = r'D:\n-infinite\n-infinite-test\ref\user_info.csv'
user_info_data = pd.read_csv(user_info_path)
user_info_data.to_sql('user_info', conn, if_exists='replace', index=False)
print("user_info table created and data loaded successfully.")

# 1. User Transaction Amount (Total and Average Sales by User)
user_query = """
    SELECT 
        user_id,
        SUM(quantity * amount) AS total_sales,
        AVG(quantity * amount) AS average_sales
    FROM "transaction"
    GROUP BY user_id;
"""
user_data = pd.read_sql_query(user_query, conn)
user_data.to_sql('user_transaction_amount', conn, if_exists='replace', index=False)

# 2. Daily Transaction Amount (Total, Min, Max, Average Sales, VAT by Day)
daily_query = """
    SELECT 
        order_date,
        SUM(quantity * amount) AS total_sales,
        MIN(quantity * amount) AS min_sales,
        MAX(quantity * amount) AS max_sales,
        AVG(quantity * amount) AS average_sales,
        SUM(quantity * amount) * 0.07 AS vat
    FROM "transaction"
    GROUP BY order_date;
"""
daily_data = pd.read_sql_query(daily_query, conn)
daily_data.to_sql('daily_transaction_amount', conn, if_exists='replace', index=False)

# 3. Product Sales (Number of Transactions and Total Sales per Product)
product_query = """
    SELECT 
        product_id,
        COUNT(*) AS number_of_transactions,
        SUM(quantity * amount) AS total_sales
    FROM "transaction"
    GROUP BY product_id;
"""
product_data = pd.read_sql_query(product_query, conn)
product_data.to_sql('product_sales', conn, if_exists='replace', index=False)

# 4. User Location and Gender Aggregation
location_gender_query = """
    SELECT 
        ui.location,
        ui.gender,
        SUM(t.quantity * t.amount) AS total_sales,
        MIN(t.quantity * t.amount) AS min_sales,
        MAX(t.quantity * t.amount) AS max_sales,
        AVG(t.quantity * t.amount) AS average_sales
    FROM user_info ui
    JOIN "transaction" t ON ui.user_id = t.user_id
    GROUP BY ui.location, ui.gender;
"""
location_gender_data = pd.read_sql_query(location_gender_query, conn)
location_gender_data.to_sql('user_location_gender_sales', conn, if_exists='replace', index=False)

# 5. Top 20 Best Sellers in Chiangmai by Day
top_sellers_query = """
    SELECT 
        t.order_date,
        t.product_id,
        SUM(t.quantity * t.amount) AS sales
    FROM "transaction" t
    JOIN user_info ui ON t.user_id = ui.user_id
    WHERE ui.location = 'Chiangmai'
    GROUP BY t.order_date, t.product_id
    ORDER BY t.order_date, sales DESC
    LIMIT 20;
"""
top_sellers_data = pd.read_sql_query(top_sellers_query, conn)
top_sellers_data.to_sql('top_sellers_chiangmai', conn, if_exists='replace', index=False)

print("ETL process completed.")
conn.close()
