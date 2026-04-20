import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE articles (
        article_id INTEGER,
        author TEXT,
        category TEXT,
        views INTEGER
    )
""")

cursor.executemany("INSERT INTO articles VALUES (?, ?, ?, ?)", [
    (1, "Alice",   "tech",    300),
    (2, "Bob",     "finance", 150),
    (3, "Alice",   "finance", 200),
    (4, "Charlie", "tech",    400),
    (5, "Bob",     "tech",    500),
    (6, "Charlie", "finance", 100),
    (7, "Alice",   "tech",    250),
])

query = """
SELECT author, 
    COUNT (*) AS article_count,
    SUM(views) AS total_views
FROM articles
GROUP BY author
HAVING article_count >= 2 AND total_views > 500 
ORDER BY total_views DESC
"""

rows = cursor.execute(query).fetchall()
for row in rows:
    print(row)

conn.close()