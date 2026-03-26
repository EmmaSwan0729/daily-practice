import pandas as pd
import numpy as np

data = {
    "date":     ["2026-01-01", "2026-01-01", "2026-01-02", "2026-01-02",
                 "2026-01-03", "2026-01-03", "2026-01-03"],
    "region":   ["North", "South", "North", "South", "North", "South", "East"],
    "category": ["Electronics", "Clothing", "Clothing", "Electronics",
                 "Electronics", "Clothing", "Electronics"],
    "sales":    [500, 200, 150, 600, 800, 300, 450],
    "returns":  [50, 20, 0, 60, 80, 30, 45],
}
df = pd.DataFrame(data)
# 要求：
# 把 date 转成 datetime，新增 net_sales 列 = sales - returns
# 用 pivot_table 做一个透视表：行是 region，列是 category，值是 net_sales 的总和
# 在透视表里新增一列 total，是每个 region 所有 category 的总和
# 找出 net_sales 最高的 region-category 组合
# 哪个 region 的退货率最高（returns / sales）
df["date"] = pd.to_datetime(df["date"])
df["net_sales"] = df["sales"] - df["returns"]

df_pivot = pd.pivot_table(df, index="region", columns="category", values="net_sales", aggfunc="sum",fill_value=0,margins=True, margins_name="total")
print(df_pivot)

# top_net_sales = df_pivot["total"].max()
# print(top_net_sales)

# df["return_rate"] = df["returns"] / df["sales"]
# top_return_rate = df["return_rate"].max()
# print(top_return_rate)

top_idx = df.groupby(["region", "category"])["net_sales"].sum().idxmax()
print(top_idx)

region_return = df.groupby("region").agg(
    total_returns=("returns", "sum"),
    total_sales=("sales", "sum")
)
region_return["return_rate"] = region_return["total_returns"] / region_return["total_sales"]
top_return_region = region_return["return_rate"].idxmax()
print(top_return_region)
