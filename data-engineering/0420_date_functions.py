import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE users (
        user_id INTEGER,
        name TEXT,
        joined_date TEXT
    )
""")

cursor.executemany("INSERT INTO users VALUES (?, ?, ?)", [
    (1, "Alice",   "2024-01-15"),
    (2, "Bob",     "2024-01-28"),
    (3, "Charlie", "2024-02-03"),
    (4, "Diana",   "2024-02-20"),
    (5, "Eve",     "2024-03-05"),
    (6, "Frank",   "2024-03-18"),
    (7, "Grace",   "2024-03-22"),
])

query = """
SELECT 
strftime("%Y-%m", joined_date) AS month, 
COUNT(*) AS new_users
FROM users
GROUP BY month
ORDER BY month ASC

"""

rows = cursor.execute(query).fetchall()
for row in rows:
    print(row)

conn.close()