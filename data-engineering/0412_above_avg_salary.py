import sqlite3

def above_avg_salary() -> None:
    """
    Find employees earning above their department average salary.

    Returns:
        None: Prints results to stdout.
    """
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE employees (
            employee_id INTEGER,
            name TEXT,
            department TEXT,
            salary INTEGER
        )
    """)

    cursor.executemany("INSERT INTO employees VALUES (?, ?, ?, ?)", [
        (1, "Alice", "Eng", 9000),
        (2, "Bob",   "Eng", 7000),
        (3, "Carol", "HR",  6000),
        (4, "David", "HR",  8000),
        (5, "Eve",   "Eng", 9000),
        (6, "Frank", "HR",  5000),
    ])

    query = """
        WITH dep_avg_salary AS (
            SELECT department,
            AVG(salary) AS avg_salary
            FROM employees
            GROUP BY department
        )
        SELECT e.name, e.department, e.salary
        FROM employees e
        LEFT JOIN dep_avg_salary d
        ON e.department = d.department
        WHERE e.salary > d.avg_salary
    """

    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    conn.close()

above_avg_salary()