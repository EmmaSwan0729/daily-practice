import pandas as pd
import numpy as np

df = pd.DataFrame({
    "user_id":   range(100000),
    "country":   np.random.choice(["UK", "US", "France", "Germany"], 100000),
    "status":    np.random.choice(["active", "inactive", "pending"], 100000),
    "age":       np.random.randint(18, 80, 100000),
    "salary":    np.random.uniform(20000, 150000, 100000),
})
# 要求：
# 用 df.info(memory_usage="deep") 查看当前内存占用
# 把 country 和 status 转成 category 类型
# 把 age 从 int64 降级成 int8（范围 -128 到 127 够用）
# 把 salary 从 float64 降级成 float32
# 再次查看内存，打印优化前后的对比
print(df.dtypes)

mem_before = df.memory_usage(deep=True).sum() / 1024 ** 2  # bytes → MB
df["country"] = df["country"].astype("category")
df["status"] = df["status"].astype("category")
df["age"] = df["age"].astype("int8")
df["salary"] = df["salary"].astype("float32")
mem_after = df.memory_usage(deep=True).sum() / 1024 ** 2

print(f"优化前: {mem_before:.2f} MB")
print(f"优化后: {mem_after:.2f} MB")
print(f"节省了: {(1 - mem_after/mem_before)*100:.1f}%")