import pandas as pd

data = {
    "user_id": [1, 2, 3],
    "name":    ["Alice", "Bob", "Charlie"],
    "tags":    [["python", "pandas", "sql"],
                ["spark", "python", "scala"],
                ["sql", "airflow", "kafka"]],
    "scores":  [[85, 90, 78],
                [92, 88, 95],
                [70, 85, 80]],
}
df = pd.DataFrame(data)
# 要求：
# 用 explode 把 tags 展开成多行
# 统计每个 tag 出现了多少次，从高到低排列
# 找出哪些 tag 只有一个用户用过
# 同时展开 tags 和 scores（每个 tag 对应一个 score

df_explode = df.explode("tags")
print(df_explode)

tag_count = df_explode.groupby("tags")["tags"].count().sort_values(ascending=False)
print(tag_count)

# tag_once = df.loc[df.groupby("tag")["tag"].count()==1, "tag_once"]
tag_once = tag_count[tag_count==1].index.tolist()
print(tag_once)

tags_scores_explode = df.explode(["tags","scores"])
print(tags_scores_explode)
