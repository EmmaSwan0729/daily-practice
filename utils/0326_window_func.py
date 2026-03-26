import pandas as pd

data = {
    "date":       ["2026-01-01"] * 4 + ["2026-01-02"] * 4,
    "region":     ["North", "South", "East", "West"] * 2,
    "sales":      [500, 300, 450, 200, 600, 350, 400, 250],
}
df = pd.DataFrame(data)
# 要求：
# 新增 rank 列：每天内按 sales 从高到低排名（每天的排名独立计算）
# 新增 pct 列：每天内该 region 的销售额占当天总销售额的百分比
# 新增 cumsum 列：每天内按 sales 从高到低累计销售额
# 找出每天销售额第一名的 region
df["rank"] = df.groupby("date")["sales"].rank(ascending=False).astype(int)
df["pct"] = df["sales"] / df.groupby("date")["sales"].transform("sum")

df["cumsum"] = df.sort_values(["date", "sales"], ascending=[True,False]).groupby("date")["sales"].cumsum()
print(df)

top_region = df.loc[df.groupby("date")["sales"].idxmax(),["date","region","sales"]]
print(top_region)






# df = df.assign(rank=df["sales"].rank(ascending=False).astype(int))
# 在用 assign 的时候，如果新列名不是合法变量名（比如有空格）
# df.assign(**{"total sales": ...})