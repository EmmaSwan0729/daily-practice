import pandas as pd

data = {
    "date":     ["2026-01-01", "2026-01-01", "2026-01-02", "2026-01-02", "2026-01-03"],
    "product":  ["A", "B", "A", "C", "B"],
    "region":   ["North", "South", "North", "South", "North"],
    "sales":    [100, 200, 150, 300, 250],
    "quantity": [2, 4, 3, 6, 5],
}
df = pd.DataFrame(data)

df["date"] = pd.to_datetime(df["date"])
product_sales = df.groupby("product")["sales"].sum()
avg_sales_region = df.groupby(['region','date'])['sales'].mean()
top_sale = df.loc[df["sales"].idxmax()]

print("=== total sales by product ===")
print(product_sales)

print("\n === Average daily sales by region ===")
print(avg_sales_region)

print("\n=== Top sales record ===")
print(top_sale)