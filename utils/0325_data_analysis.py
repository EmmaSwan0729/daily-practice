import pandas as pd
import numpy as np

data = {
    "user_id":  [1, 2, 2, 3, 4, 5, 5],
    "email":    ["alice@gmail.com", "BOB@GMAIL.COM", "bob@gmail.com",
                 "charlie@", "dave@yahoo.com", None, "eve@gmail.com"],
    "age":      [25, 30, 30, -5, 200, 28, 28],
    "country":  ["UK", "us", "us", "Germany", "UK", "france", "france"],
    "salary":   [50000, 60000, 60000, 70000, 80000, 55000, 55000],
}
df = pd.DataFrame(data)
# 要求：
# 用前向填充（用前一天的值）填充 sales 缺失值
# 新增 7day_rolling_avg 列：每一行的过去7天滚动平均
# 新增 growth 列：和前一天相比的销售额增长量
# 找出销售额最高的5天
# 统计哪个星期几（Monday/Tuesday...）平均销售额最高

df_before = len(df)

df = df.drop_duplicates()

df["email"] = df["email"].str.lower()
df = df[
    df["email"].notna() 
    & df["email"].str.contains("@") 
    & df["email"].str.contains("\\.")
    ] 

df["age"] = df["age"].apply(lambda x: np.nan if (x <= 0 or x > 100) else x)

df["country"] = df["country"].str.capitalize()

df_after = len(df)

print(df_before,f"\n {df_after}")