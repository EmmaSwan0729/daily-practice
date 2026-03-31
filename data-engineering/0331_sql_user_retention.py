import sqlite3
import pandas as pd

conn = sqlite3.connect(":memory:")  # 内存数据库，不生成文件

conn.execute("""
    CREATE TABLE user_logins (
        user_id INT,
        login_date DATE
    )
""")

conn.execute("""
    INSERT INTO user_logins VALUES
    (1, '2024-01-01'), (1, '2024-01-02'),
    (2, '2024-01-01'), (3, '2024-01-01'),
    (3, '2024-01-03'), (4, '2024-01-02')
""")

# 把你的答案写在这里
query = """
    SELECT a.login_date,
    ROUND(COUNT(b.user_id) * 1.0 / COUNT(a.user_id), 2) AS retention_rate
    FROM user_logins a
    LEFT JOIN user_logins b
        ON a.user_id = b.user_id
        AND b.login_date = date(a.login_date, '+1 day')
    GROUP BY a.login_date
"""

df = pd.read_sql_query(query, conn)
print(df)

# 27 行：SQLite 里日期是字符串，不能直接 + 1，要用 date() 函数：AND b.login_date = date(a.login_date, '+1 day')  -- ✅ SQLite 的日期加法，