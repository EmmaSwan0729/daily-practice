import pandas as pd

data = {
    "timestamp": ["2026-01-01 08:00:00", "2026-01-01 08:05:00", "2026-01-01 09:00:00",
                  "2026-01-01 09:30:00", "2026-01-02 08:00:00", "2026-01-02 10:00:00"],
    "user_id":   [1, 1, 2, 1, 2, 3],
    "event":     ["login", "click", "login", "logout", "login", "login"],
    "duration":  [None, 5, None, 30, None, None],  # 只有 click/logout 有时长
}
df = pd.DataFrame(data)

df["date"] = pd.to_datetime(df["timestamp"])
df["hour"] = df["date"].dt.hour

# df["first_appear"] = df.groupby(df["user_id"])["date"].min()

# df["last_appear"] = df.groupby(df["user_id"])["date"].max()

first_last = df.groupby("user_id")["date"].agg(first="min",last="max")

hour_event = df.groupby(df["hour"])["event"].count()

avg_duration = df["duration"].fillna(0).groupby(df["user_id"]).agg("mean")

print(df)
print(first_last)
print(f"\n {hour_event}")
print(f"\n {avg_duration}")
