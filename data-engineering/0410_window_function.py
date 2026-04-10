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

query = """
    SELECT user_id,order_id,amount,
    RANK() OVER(PARTITION BY user_id ORDER BY amount DESC)as rank_in_user
    FROM orders
"""

rows = cursor.execute(query).fetchall()
for row in rows:
    print(row)

conn.close()