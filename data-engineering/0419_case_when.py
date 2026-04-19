import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE scores (
        student_id INTEGER,
        name TEXT,
        score INTEGER
    )
""")

cursor.executemany("INSERT INTO scores VALUES (?, ?, ?)", [
    (1, "Alice", 92),
    (2, "Bob", 75),
    (3, "Charlie", 58),
    (4, "Diana", 85),
    (5, "Eve", 45),
])

query = """
SELECT
    name,
    score,
    CASE 
        WHEN score >= 90 THEN 'A'
        WHEN score >=80 THEN 'B'
        WHEN score >=70 THEN 'C'
        WHEN score >=60 THEN 'D'
        ELSE 'F'
    END AS grade
FROM scores
ORDER BY name

"""

rows = cursor.execute(query).fetchall()
for row in rows:
    print(row)

conn.close()