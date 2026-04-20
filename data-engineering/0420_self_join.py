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
    (3, "Charlie", "eng",       8000),
    (4, "Diana",   "marketing", 6000),
    (5, "Eve",     "marketing", 7500),
])

query = """
SELECT e.name AS lower_name, s.name AS higher_name, e.department, 
    (s.salary - e.salary) AS diff
FROM employees e
INNER JOIN employees s ON e.emp_id != s.emp_id 
AND e.department = s.department
WHERE e.salary < s.salary 
ORDER BY diff DESC

"""

rows = cursor.execute(query).fetchall()
for row in rows:
    print(row)

conn.close()