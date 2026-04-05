


import sqlite3
import pandas as pd

conn = sqlite3.connect(":memory:")

# 1. create table
conn.execute("""
    CREATE TABLE employees (
        employee_id  INT,
        name         VARCHAR(50),
        department   VARCHAR(50),
        salary       DECIMAL
    )
""")

# 2. insert data
conn.execute("""
    INSERT INTO employees VALUES
    (1, 'Alice',   'Engineering', 90000),
    (2, 'Bob',     'Engineering', 85000),
    (3, 'Charlie', 'Engineering', 70000),
    (4, 'Diana',   'Marketing',   70000),
    (5, 'Eve',     'Marketing',   75000),
    (6, 'Frank',   'Marketing',   65000)
""")

# 3. query
query = """
    WITH dept_avg AS(
        SELECT d.department, AVG(d.salary) AS avg_salary
        FROM employees d
        GROUP BY d.department
    ) 
    SELECT e.name,e.department,e.salary,d.avg_salary
    FROM employees e
    JOIN dept_avg d ON e.department = d.department
    Where e.salary > d.avg_salary
"""

df = pd.read_sql_query(query, conn)
print(df)

