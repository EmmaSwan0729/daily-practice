import pandas as pd

orders = pd.DataFrame({
    'order_id':    [1, 2, 3, 4, 5],
    'customer_id': [101, 102, 101, 103, 104],
    'amount':      [50, 30, 80, 20, 60]
})

customers = pd.DataFrame({
    'customer_id': [101, 102, 103],
    'name':        ['Alice', 'Bob', 'Charlie'],
    'city':        ['Edinburgh', 'Glasgow', 'Aberdeen']
})
# 要求：
# 把两张表按 customer_id 合并
# 保留所有订单，没有匹配到客户信息的显示为空
# 计算每个城市的总销售额，按降序排列

df = pd.merge(left=orders,right=customers,how='left',on='customer_id')

# df_agg = df.groupby(["city"])["amount"].sum().reset_index()
# df_agg = df_agg.sort_values(by="amount",ascending=False)

print(df)
print(df_agg)


# df_agg = df.groupby(["city"]).agg({"amount":"sum"}).sort_values(by="amount",ascending=False)
# .groupby().agg({})city 变成索引
# .groupby().sum().reset_index()city 变成普通列
# 如果后续还需要对 city 列做操作，用 reset_index() 更方便。如果只是展示结果，两种都行。