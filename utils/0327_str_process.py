import pandas as pd

data = {
    "name":    ["  Alice Smith ", "BOB JONES", "charlie brown  ", "Dave-Wilson", "eve_davis"],
    "email":   ["Alice@Gmail.COM", "bob.jones@yahoo.com", "CHARLIE@hotmail.com", "dave@gmail.com", "eve@outlook.com"],
    "phone":   ["123-456-7890", "（020）12345678", "07700 900123", "1234567890", "+44-7700-900456"],
    "address": ["123 Main St, London", "456 High St, Paris", "789 Park Ave, Berlin", "321 Oak Rd, London", "654 Pine St, Paris"],
}
df = pd.DataFrame(data)
# 要求：
# name 去掉首尾空格，统一转成 Title Case（首字母大写）, 把 - 和 _ 替换成空格
# email 统一转成小写
# 从 address 里提取出城市名（逗号后面的部分）
# 统计每个城市有多少个用户

df["name"] = df["name"].str.strip()
df["name"] = df["name"].str.title()
df["name"] = df["name"].str.replace(r"[-_]", " ", regex=True)
df["email"] = df["email"].str.lower()
df["city"] = df["address"].str.split(",").str.get(1)
user_cnt = df.groupby("city")["name"].count()
print(df)
print(user_cnt)

