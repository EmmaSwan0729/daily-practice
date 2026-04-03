


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
    (3, 'Charlie', 'Engineering', 85000),
    (4, 'Diana',   'Marketing',   70000),
    (5, 'Eve',     'Marketing',   75000),
    (6, 'Frank',   'Marketing',   70000)
""")

# 3. query
query = """
    SELECT name,
    department,
    salary,
    DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank
    FROM employees
"""

df = pd.read_sql_query(query, conn)
print(df)
