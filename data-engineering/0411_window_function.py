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

query_1 = """
    SELECT user_id, order_id,amount,
    SUM(amount) OVER (PARTITION BY user_id ORDER BY order_id) AS running_total
    FROM orders
"""
rows_1 = cursor.execute(query_1).fetchall()
for row in rows_1:
    print(row)

query_2 = """
    SELECT user_id, order_id,amount,
    DENSE_RANK() OVER (ORDER BY amount DESC) AS dense_rank
    FROM orders
"""
rows_2 = cursor.execute(query_2).fetchall()
for rows in rows_2:
    print(rows)

query_3 = """
    SELECT user_id, order_id,amount,
    NTILE(3) OVER (ORDER BY amount DESC) AS tile
    FROM orders
"""
rows_3 = cursor.execute(query_3).fetchall()
for rows in rows_3:
    print(rows)


conn.close()

