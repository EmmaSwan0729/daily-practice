import pandas as pd

df = pd.DataFrame({
    "order_id": [1, 2, 3, 4, 5, 6],
    "user_id":  [1, 1, 1, 2, 1, 2],
    "amount":   [500, 100, 300, 800, 300, 200]
})

def add_level(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add a categorical column 'level' based on order amount.

    The level is assigned as follows:
    - "high"   if amount >= 500
    - "medium" if 200 <= amount < 500
    - "low"    if amount < 200

    Args:
        df (pd.DataFrame): Input DataFrame containing an 'amount' column.

    Returns:
        pd.DataFrame: DataFrame with an additional 'level' column.
    """
    df['level'] = df['amount'].apply(lambda x: "high" if x>=500 else "medium" if 200<=x<500 else "low")

    return df

print(add_level(df))