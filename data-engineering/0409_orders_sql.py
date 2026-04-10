import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.executescript('''
    CREATE TABLE orders (
        order_id INTEGER,
        customer_id INTEGER,
        amount INTEGER,
        order_date TEXT
    );

    INSERT INTO orders VALUES
        (1, 101, 250, '2024-01-05'),
        (2, 102, 180, '2024-01-07'),
        (3, 101, 320, '2024-01-10'),
        (4, 103, 95,  '2024-01-12'),
        (5, 102, 410, '2024-01-15');

    CREATE TABLE customers (
        customer_id INTEGER,
        customer_name TEXT,
        city TEXT
    );

    INSERT INTO customers VALUES
        (101, 'Alice', 'London'),
        (102, 'Bob', 'Paris'),
        (103, 'Charlie', 'London');
''')

query1 = """
    SELECT c.customer_name, SUM(o.amount) AS total_amount
    FROM customers c
    LEFT JOIN orders o
    ON  c.customer_id = o.customer_id
    GROUP BY c.customer_name
    ORDER BY total_amount DESC
"""
for row in cursor.execute(query1):
    print(row)

query2 = """
    SELECT c.customer_name, SUM(o.amount) AS total_amount
    FROM customers c
    LEFT JOIN orders o
    ON  c.customer_id = o.customer_id
    GROUP BY c.customer_name
    HAVING SUM(o.amount) > 300
"""
for row in cursor.execute(query2):
    print(row)

query3 = """
    SELECT c.customer_name, o.order_id, o.amount
    FROM customers c
    LEFT JOIN orders o
    ON  c.customer_id = o.customer_id
    WHERE c.city = 'London'
"""
for row in cursor.execute(query3):
    print(row)