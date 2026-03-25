import pandas as pd

data = {
    "emp_id":     [1, 2, 3, 4, 5, 6],
    "name":       ["Alice", "Bob", "Charlie", "Dave", "Eve", "Frank"],
    "department": ["Eng", "Eng", "HR", "HR", "Sales", "Sales"],
    "salary":     [90000, 85000, 60000, None, 70000, 75000],
    "score":      [4.5, 3.8, 4.2, 3.5, None, 4.8],
    "joined":     ["2020-03-01", "2019-06-15", "2021-09-01",
                   "2018-01-10", "2022-05-20", "2017-11-30"],
}
df = pd.DataFrame(data)

df["joined"] = pd.to_datetime(df["joined"])
df["years_work"] = (pd.Timestamp.today() - df["joined"]).dt.days //365

df["salary"] = df["salary"].fillna(df.groupby("department")["salary"].transform("mean"))
df["score"] = df["score"].fillna(df.groupby("department")["score"].transform("mean"))

avg_department = df.groupby("department").agg(
    avg_salary=("salary","mean"),
    avg_score=("score","mean"), 
    headcount=("emp_id","count")
    )

df["level"] = df["score"].apply(lambda x: "A" if x >= 4.5 else "B" if x >= 3.5 else "C")

print(df)
print(avg_department)