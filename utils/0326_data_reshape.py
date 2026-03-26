import pandas as pd

data = {
    "region":  ["North", "South", "East"],
    "Q1_sales": [500, 300, 450],
    "Q2_sales": [600, 350, 400],
    "Q3_sales": [700, 400, 500],
    "Q4_sales": [800, 450, 600],
}
df = pd.DataFrame(data)
# 要求：
# 用 melt 把宽表转成长表（每行是一个 region + 一个季度的销售额）
# 从 variable 列里提取出季度名，比如 "Q1_sales" → "Q1"
# 找出每个 region 销售额最高的季度
# 找出每个季度销售额最高的 region

df_wide = pd.melt(df,id_vars="region", value_vars=["Q1_sales", "Q2_sales", "Q3_sales", "Q4_sales"],var_name="quarter", value_name="sales")
df_wide["quarter"] = df_wide["quarter"].str[:2]
top_quarter = df_wide.loc[df_wide.groupby("region")["sales"].idxmax(),"quarter"]
top_region = df_wide.loc[df_wide.groupby("quarter")["sales"].idxmax(),"region"]
print(df_wide)
print("\n每个region销售额最高的季度:")
print(top_quarter.values)  # ['Q4' 'Q4' 'Q4']
print("\n每个季度销售额最高的region:")
print(top_region.values)   # ['North' 'North' 'North' 'North']

# 不传 value_vars 的话，pandas 会自动把除 id_vars 之外的所有列都转成长表:
# df_long = pd.melt(df, id_vars="region", var_name="quarter", value_name="sales")
