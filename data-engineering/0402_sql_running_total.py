
import sqlite3
import pandas as pd

conn = sqlite3.connect(":memory:")

# 1. create table
conn.execute("""
    CREATE TABLE orders (
        order_id   INT,
        order_date DATE,
        amount     DECIMAL
    )
""")

# 2. insert data
conn.execute("""
    INSERT INTO orders VALUES
    (1, '2024-01-01', 100),
    (2, '2024-01-02', 200),
    (3, '2024-01-03', 150),
    (4, '2024-01-04', 300)
""")

# 3. query
query = """
    SELECT order_date,
    amount,
    SUM(amount) OVER (ORDER BY order_date asc) AS running_total
    FROM orders

"""

df = pd.read_sql_query(query, conn)
print(df)