


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

# 顺便说一下 RANK() 和 DENSE_RANK() 的区别，面试经常会问：
# 函数相同薪资的排名下一个排名RANK()并列第2跳到第4DENSE_RANK()并列第2接着第3
# 比如这道题如果用 RANK()，Bob 和 Charlie 都是第2，下一个就是第4，没有第3。

