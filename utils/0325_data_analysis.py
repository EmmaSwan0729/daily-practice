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