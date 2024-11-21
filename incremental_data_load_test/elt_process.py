import os
import pandas as pd
import sqlite3

DATABASE_PATH = 'incremental_data_load_test/transactions.db'
SALES_FOLDER = './ref/sales'

conn = sqlite3.connect(DATABASE_PATH)
cursor = conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS "transaction" (
    order_id TEXT PRIMARY KEY,
    user_id TEXT,
    product_id TEXT,
    quantity INTEGER,
    amount REAL,
    order_date TEXT
);
"""
cursor.execute(create_table_query)
conn.commit()

try:
    processed_orders = set(
        pd.read_sql_query("SELECT order_id FROM transaction", conn)['order_id'].tolist()
    )
except Exception as e:
    print(f"No existing data found. Starting fresh. Error: {e}")
    processed_orders = set()

for file_name in sorted(os.listdir(SALES_FOLDER)):
    if file_name.endswith('.csv'):
        file_path = os.path.join(SALES_FOLDER, file_name)
        print(f"Processing {file_path}...")

        data = pd.read_csv(file_path)

        # Ensure column names match the table schema
        data.columns = [col.strip() for col in data.columns]  # Trim whitespace
        required_columns = ['order_id', 'user_id', 'product_id', 'quantity', 'amount', 'order_date']

        # Validate columns in the CSV file
        if not all(col in data.columns for col in required_columns):
            raise ValueError(f"Missing required columns in {file_name}")

        new_data = data[~data['order_id'].astype(str).isin(processed_orders)]

        if not new_data.empty:
            # Insert new data into the database
            new_data.to_sql('transaction', conn, if_exists='append', index=False)
            print(f"Inserted {len(new_data)} new records from {file_name}.")

            # Update processed orders
            processed_orders.update(new_data['order_id'].astype(str).tolist())
        else:
            print(f"No new records found in {file_name}.")

print("ELT process completed successfully.")
conn.close()
