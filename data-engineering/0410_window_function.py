import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.executescript("""
CREATE TABLE orders (
    order_id INTEGER,
    user_id  INTEGER,
    amount   INTEGER
);

INSERT INTO orders VALUES
(1, 1, 500),
(2, 1, 100),
(3, 1, 300),
(4, 2, 800),
(5, 1, 300),
(6, 2, 200);
""")

1
query_1 = """
    SELECT user_id,order_id,amount,
    RANK() OVER(PARTITION BY user_id ORDER BY amount DESC)as rank_in_user
    FROM orders
"""
rows_1 = cursor.execute(query_1).fetchall()
for row in rows_1:
    print(row)

# 2
query_2 = """
    SELECT user_id,order_id,amount,
    LAG(amount,1) OVER(PARTITION BY user_id ORDER BY user_id )as prev_amount
    FROM orders
"""
rows_2 = cursor.execute(query_2).fetchall()
for row in rows_2:
    print(row)

# 3
query_3 = """
    SELECT user_id,order_id,amount,
    ROUND(CAST(amount AS FLOAT) / SUM(amount) OVER(PARTITION BY user_id) * 100, 2) AS pct_of_user_total
    FROM orders
"""
rows_3 = cursor.execute(query_3).fetchall()
for row in rows_3:
    print(row)



conn.close()