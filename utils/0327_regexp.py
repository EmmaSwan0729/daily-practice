import pandas as pd
import re

data = {
    "raw_text": [
        "Order #12345 placed by alice@gmail.com on 2026-01-15",
        "Invoice INV-2024-001 for bob@yahoo.com dated 01/20/2026",
        "Ref: ORD_98765 customer: charlie@hotmail.com date: 2026.01.25",
        "Transaction TX-00042 from dave@outlook.com 2026-02-01",
    ]
}
df = pd.DataFrame(data)
# 要求：
# 从每行提取出邮箱地址
# 从每行提取出数字编号（纯数字部分，比如 12345、001、98765、00042）
# 从每行提取出日期（格式可能是 2026-01-15 或 01/20/2026 或 2026.01.25）
# 全部用 str.extract() 或 str.findall() 完成 

df["email"] =  df["raw_text"].str.extract(r"([\w.]+@[\w.]+\.\w+)")


df["order_num"] = df["raw_text"].str.extract(r"(?:ORD_|INV-\d{4}-|TX-|#)(\d+)") # 这样泛化能力非常弱，但没别的办法
# df["order_num"] = df["raw_text"].str.extract(r"[#_-](\d+)") 这个输出不对
# df["order_num"] = df["raw_text"].str.findall(r"[#_-](\d+)").str[-1] 也不对
# df["order_num"] = df["raw_text"].str.extract(r"(\d+)(?!.*\d)")

pattern = r"(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|\d{4}\.\d{2}\.\d{2})"
df["date"] = df["raw_text"].str.extract(pattern)
print(df)
