import pandas as pd
import numpy as np

# 原始数据（模拟真实脏数据）
data = {
    'order_id':   [1, 2, 3, 4, 5, 6, 7, 8],
    'customer_id':[101, 102, 101, 103, 102, 101, None, 104],
    'product':    ['Apple', 'Banana', 'apple', 'Cherry', 'BANANA', 'Apple', 'Cherry', 'banana'],
    'amount':     [50.0, 30.0, -10.0, 80.0, 30.0, None, 40.0, 20.0],
    'date':       ['2024-01-01', '2024-01-01', '2024-01-02', 'invalid_date',
                   '2024-01-02', '2024-01-03', '2024-01-03', '2024-01-03']
}
df = pd.DataFrame(data)
# **要求：**
# 1. 清洗 `product` 列，统一转为首字母大写（`Apple` / `Banana` / `Cherry`）
# 2. 删除 `customer_id` 为空的行
# 3. 删除 `amount` 为负数或空值的行
# 4. 将 `date` 转为 datetime 类型，无法解析的设为 `NaT`，然后删除这些行
# 5. 按 `product` 分组，计算每种产品的**总销售额**和**订单数量**，结果按总销售额降序排列

df["product"] = df["product"].str.title()

df = df.dropna(subset=["customer_id"])

df = df[df["amount"]>0]

df["date"] = pd.to_datetime(df["date"], errors='coerce') # coerce强制、胁迫,这里强制转换成NaT
df = df.dropna(subset=["date"])

df_sales = df.groupby("product").agg(
    total_amount = ("amount", "sum"),
    order_count = ("order_id","count")
).sort_values("total_amount", ascending=False)

print(df)
print(df_sales)

