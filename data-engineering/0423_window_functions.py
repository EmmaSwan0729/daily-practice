import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE employees (
        emp_id INTEGER,
        name TEXT,
        department TEXT,
        salary INTEGER
    )
""")

cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", [
    (1, "Alice",   "eng",       9000),
    (2, "Bob",     "eng",       7000),
    (3, "Charlie", "eng",       9000),
    (4, "Diana",   "marketing", 6000),
    (5, "Eve",     "marketing", 7500),
])

query = """
WITH ranked_employees AS (
    SELECT department, name, salary,
    RANK() OVER(PARTITION BY department ORDER BY salary DESC) AS rank
    FROM employees
)
SELECT department, name, salary
FROM ranked_employees
WHERE rank = 1
ORDER BY department

"""

rows = cursor.execute(query).fetchall()
for row in rows:
    print(row)

conn.close()