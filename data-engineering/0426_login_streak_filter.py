# 0426_login_streak_filter.py

import sqlite3

def find_users_with_long_streak(conn: sqlite3.Connection) -> list[tuple]:
    """
    Find users who have had a consecutive login streak of more than 3 days.

    Args:
        conn: SQLite database connection.

    Returns:
        A list of tuples (user_id,), ordered by user_id.
    """
    conn.execute("DROP TABLE IF EXISTS user_logins")
    conn.execute("""
        CREATE TABLE user_logins (
            user_id    INTEGER,
            login_date TEXT
        )
    """)
    conn.executemany("INSERT INTO user_logins VALUES (?, ?)", [
        (1, "2024-01-01"), (1, "2024-01-02"), (1, "2024-01-03"), (1, "2024-01-05"),
        (2, "2024-01-01"), (2, "2024-01-03"), (2, "2024-01-04"), (2, "2024-01-05"),
    ])

    query = """
    WITH ranked_logins AS (
    SELECT user_id, login_date,
    ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY login_date) AS rn
    FROM user_logins
    ),
    islands AS(
    SELECT user_id, login_date, 
    DATE(login_date, '-' || rn || ' days') AS grp
    FROM ranked_logins
    )
    SELECT user_id
    FROM (
    SELECT user_id, COUNT(*) AS streak_length
    FROM islands
    GROUP BY user_id, grp
    )
    WHERE streak_length >= 3
    ORDER BY user_id
    """

    return conn.execute(query).fetchall()


if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        result = find_users_with_long_streak(conn)
        for row in result:
            print(row)