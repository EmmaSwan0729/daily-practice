import pandas as pd

df = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5, 6],
    "user_id":  [1, 1, 1, 2, 1, 2],
    "amount":   [500, 100, 300, 800, 300, 200]
})

def summarize_by_user(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate order data at the user level.

    This function groups the input DataFrame by `user_id` and computes:
    - total_amount: the sum of all order amounts per user
    - order_count: the number of orders per user
    - avg_amount: the average order amount per user

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame containing at least the following columns:
        - user_id : identifier for each user
        - amount : numeric value representing order amount

    Returns
    -------
    pd.DataFrame
        A DataFrame with one row per user, including:
        - user_id
        - total_amount
        - order_count
        - avg_amount
    """
    df = df.groupby(['user_id']).agg(
        total_amount = ("amount", "sum"),
        order_count = ("amount", "count"),
        avg_amount = ("amount", "mean")
    ).reset_index()
    
    df["avg_amount"] = df["avg_amount"].round(2)

    return df

print(summarize_by_user(df))

def add_user_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add user-level aggregated metrics to the original order-level DataFrame.

    This function uses groupby + transform to compute group-level statistics
    and align them back to each row without changing the original granularity.

    Specifically, it adds two new columns:
    - user_total: total order amount per user
    - pct_of_total: proportion of each order amount relative to the user's total
      (rounded to 2 decimal places)

    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame containing at least:
        - user_id : identifier for each user
        - amount : numeric value representing order amount

    Returns
    -------
    pd.DataFrame
        The original DataFrame with two additional columns:
        - user_total
        - pct_of_total
    """
    df["user_total"] = df.groupby('user_id')['amount'].transform("sum")
    df["pct_of_total"] = round((df["amount"] / df["user_total"]) * 100, 2)
    return df
print(add_user_stats(df))
