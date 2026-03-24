import pandas as pd

data = {
    "order_id":  [1, 2, 3, 4, 5, 6],
    "customer":  ["Alice", "Bob", "Alice", "Dave", "Bob", "Eve"],
    "category":  ["Electronics", "Clothing", "Electronics", "Food", "Clothing", "Food"],
    "price":     [999.0, 49.99, 299.0, None, 89.99, 15.0],
    "quantity":  [1, 2, 1, 3, None, 5],
    "date":      ["2026-01-05", "2026-01-05", "2026-01-06", "2026-01-06", "2026-01-07", "2026-01-07"],
}
df = pd.DataFrame(data)

df["date"]= pd.to_datetime(df["date"])

price_mean = df["price"].mean()
df["price"] = df["price"].apply(lambda x: price_mean if pd.isnull(x) else x)

df["quantity"] = df["quantity"].fillna(int(df["quantity"].mean()))

df["revenue"] = df["price"] * df["quantity"]
category_sales = df.groupby(df["category"])["revenue"].agg(["sum", "mean"])

top_customer = df.groupby("customer")["revenue"].sum().idxmax()

print(df)
print(f"\n {category_sales}")
print(f"\n {top_customer}")
