import pandas as pd

data = {
    "user_id":  [1, 1, 1, 2, 2, 3, 3, 3, 3],
    "action":   ["login", "view", "purchase", "login", "view", "login", "view", "view", "purchase"],
    "amount":   [None, None, 120.0, None, None, None, None, None, 85.0],
    "date":     ["2026-01-01", "2026-01-01", "2026-01-01",
                 "2026-01-02", "2026-01-02",
                 "2026-01-01", "2026-01-01", "2026-01-02", "2026-01-02"],
}
df = pd.DataFrame(data)

df["date"] = pd.to_datetime(df["date"])

action_count = df.groupby("user_id")["action"].count()

total_purchase = df[df["action"]=="purchase"].groupby("user_id")["amount"].sum().fillna(0)
total_purchase = total_purchase.reindex(df["user_id"].unique(), fill_value=0)

purchasers = df[df["action"]=="purchase"]["user_id"].unique()
df["is_purchaser"] = df["user_id"].map(lambda x: x in purchasers)

unique_user = df[df["action"]=="login"].groupby("date")["user_id"].nunique()

print(df)
print(f"\n {action_count}")
print(f"\n {total_purchase}")
print(f"\n {unique_user}")