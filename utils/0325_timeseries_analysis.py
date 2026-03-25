import pandas as pd
import numpy as np

data = {
    "date":  pd.date_range("2026-01-01", periods=20, freq="D"),
    "sales": [100, 120, None, 130, 110, 150, 160, None, 140, 170,
              180, None, 190, 200, 160, 210, None, 220, 230, 240],
}
df = pd.DataFrame(data)

# 要求：
# 用前向填充（用前一天的值）填充 sales 缺失值
# 新增 7day_rolling_avg 列：每一行的过去7天滚动平均
# 新增 growth 列：和前一天相比的销售额增长量
# 找出销售额最高的5天
# 统计哪个星期几（Monday/Tuesday...）平均销售额最高

# df["sales"] = df["sales"].fillna(method="ffill")
# df["7day_rolling_avg"] = df["sales"].rolling(7).mean()
# df["growth"] = df["sales"].diff()
# top5  = df.nlargest(5,"sales")[["date","sales"]]
df["weekday"] = df["date"].dt.day_name()
weekday_avg = df.groupby("weekday")["sales"].mean().sort_values(ascending=False)

print(weekday_avg)