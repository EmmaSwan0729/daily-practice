import sqlite3

def find_streak_ranges(conn: sqlite3.Connection) -> list[tuple]:
    """
    Find the start and end date of each consecutive login streak per user.

    Args:
        conn: SQLite database connection.

    Returns:
        A list of tuples (user_id, start_date, end_date), ordered by user_id, start_date.
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
    WITH login_dates AS (
    SELECT user_id, login_date,
    ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY login_date) AS rn
    FROM user_logins
    ), islands AS (
    SELECT user_id, login_date,
        DATE(login_date, '-' || rn || ' days') AS grp
    FROM login_dates
    )
    SELECT user_id, MIN(login_date) AS start_date, MAX(login_date) AS end_date
    FROM (
    SELECT user_id, grp, login_date
    FROM islands
    )
    GROUP BY user_id, grp
    """

    return conn.execute(query).fetchall()


if __name__ == "__main__":
    with sqlite3.connect(":memory:") as conn:
        result = find_streak_ranges(conn)
        for row in result:
            print(row)
        
