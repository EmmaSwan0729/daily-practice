import pandas as pd
import numpy as np

df = pd.DataFrame({
    "date":  pd.date_range("2026-01-01", periods=60, freq="D"),
    "sales": np.random.randint(100, 500, 60),
    "cost":  np.random.randint(50, 200, 60),
})
df = df.set_index("date")
# 要求：
# 按周重采样，计算每周总销售额
# 按月重采样，计算每月平均销售额和平均成本
# 找出销售额最高的那一周
# 新增 profit 列 = sales - cost，按周计算总利润

total_sales_week = df.resample("W")["sales"].sum()
print(total_sales_week)

avg_sales_cost_month = df.resample("ME")[["sales","cost"]].mean()
print(avg_sales_cost_month)

top_sale_week = total_sales_week.idxmax()
print(top_sale_week)

df["profit"] = df["sales"] - df["cost"]
profit_week = df.resample("W").sum()
print(profit_week)
                                                 