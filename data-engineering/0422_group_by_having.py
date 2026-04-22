import sqlite3

def get_high_value_customers(conn: sqlite3.Connection) -> list[tuple]:
    """
    Find customers whose total spending exceeds 500.

    Args:
        conn: SQLite database connection

    Returns:
        List of (customer_id, total_amount, order_count) tuples,
        ordered by total_amount descending
    """
    query = """
    SELECT customer_id,
    ROUND(SUM(amount), 2) AS total_amount,
    COUNT(*) AS order_count
    FROM orders
    GROUP BY customer_id
    HAVING total_amount > 500
    ORDER BY total_amount DESC
    """
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()


# -------- 测试数据 --------
conn = sqlite3.connect(":memory:")
conn.execute("""
    CREATE TABLE orders (
        order_id   INTEGER PRIMARY KEY,
        customer_id INTEGER,
        amount      REAL,
        order_date  TEXT
    )
""")
conn.executemany("INSERT INTO orders VALUES (?, ?, ?, ?)", [
    (1,  101, 200.00, "2024-01-05"),
    (2,  101, 150.00, "2024-01-20"),
    (3,  101, 180.00, "2024-02-03"),
    (4,  102,  80.00, "2024-01-10"),
    (5,  102,  90.00, "2024-02-15"),
    (6,  103, 600.00, "2024-01-08"),
    (7,  104, 250.00, "2024-01-22"),
    (8,  104, 300.00, "2024-02-28"),
])
conn.commit()

print(get_high_value_customers(conn))