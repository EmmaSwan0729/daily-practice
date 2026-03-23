import pandas as pd
import numpy as np


def inspect_csv(filepath: str) -> None:
    df = pd.read_csv(filepath)
    df_rows = len(df)
    df_columns = len(df.columns)
    df_duplicated = df.duplicated().sum()

    print(f"==== CSV Inspector ===")
    print(f"Rows: {df_rows} | Columns: {df_columns}")

    for col in df.columns:
        dtype = df[col].dtype
        missing_count = df[col].isna().sum()
        missing_pct = missing_count / df_rows * 100
        print(f"  {col:<12} {str(dtype):<10} missing: {missing_count:>3} ({missing_pct:.1f}%)")

    print(f"Duplicate rows: {df_duplicated}")


if __name__ == "__main__":
    df = pd.DataFrame({
        "name":   ["Alice", "Bob", None, "Alice", "Eve"],
        "age":    [25, None, 30, 25, 40],
        "salary": [50000.0, 60000.0, None, 50000.0, 80000.0],
        "city":   ["London", "Paris", "London", "London", None],
    })
    df.to_csv("utils/test.csv", index=False)
    inspect_csv("utils/test.csv")