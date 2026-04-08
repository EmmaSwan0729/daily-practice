import pandas as pd

orders = pd.DataFrame({
    'order_id': [1, 2, 3, 4, 5],
    'customer_id': [101, 102, 101, 103, 102],
    'amount': [250, 180, 320, 95, 410],
    'order_date':['2024-01-05', '2024-01-07', '2024-01-10', '2024-01-12', '2024-01-15']
})

def customer_total_amount(orders:pd.DataFrame) -> pd.DataFrame:
    """
    Calculate total amount of every customer.

    Args:
        pd.DataFrame

    Returns:
        pd.DataFrame
    """
    df = orders.groupby('customer_id')['amount'].sum()
    df = df.sort_values(ascending=False)
    return df

def amount_200_above(orders:pd.DataFrame) -> pd.DataFrame:
    """
    Filter amount which is 200 above.

    Args:
        pd.DataFrame

    Returns:
        pd.DataFrame
    """
    df = orders[orders['amount']>200]
    df_amount = df[['order_id','amount']]
    return df_amount

def amount_specific_date(order:pd.DataFrame) -> pd.DataFrame:
    """
    Filter amount which is after 2024-01-10.

    Args:
        pd.DataFrame

    Returns:
        pd.DataFrame
    """
    df_amount_date = order[order['order_date'] >= '2024-01-10']
    return df_amount_date