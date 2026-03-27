import pandas as pd
import numpy as np

data = {
    "name":   ["Alice", "Bob", "Charlie", "Dave", "Eve", "Frank", "Grace", "Hank"],
    "age":    [15, 25, 35, 45, 55, 65, 75, 85],
    "salary": [20000, 45000, 60000, 80000, 95000, 110000, 130000, 150000],
    "score":  [45, 62, 71, 58, 88, 92, 79, 65],
}
df = pd.DataFrame(data)
# 要求：
# 用 cut 把 age 分成四个区间：0 - 18少年，19 - 35青年，36 - 60中年，61 + 老年，新增 age_group 列
# 用 qcut 把 salary 按四分位数分成4组，新增 salary_tier 列
# 统计每个 age_group 的平均 score
# 统计每个 salary_tier 的人数
bins = [0,18,35,60,100]
labels=["Teen","Young Adult","Middle age", "old"]
df["age_groups"] = pd.cut(
    df["age"], 
    bins=bins, 
    labels=labels, 
    include_lowest=True
)

df["salary_tier"] = pd.qcut(df["salary"], q=4)
print(df)

avg_score = df.groupby("age_groups", observed=True)["score"].mean().round(1)
print(avg_score)

head_count = df.groupby("salary_tier", observed=True)["name"].count().round(1)
print(head_count)
