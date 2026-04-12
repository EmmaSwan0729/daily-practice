import pandas as pd

orders = pd.DataFrame({
    "order_id":   [1, 2, 3, 4, 5],
    "customer_id":[101, 102, 101, 103, 104],
    "amount":     [250, 150, 300, 200, 100]
})

customers = pd.DataFrame({
    "customer_id": [101, 102, 103],
    "name":        ["Alice", "Bob", "Carol"]
})

def customer_with_order(orders:pd.DataFrame, customers:pd.DataFrame) -> pd.DataFrame:
    """
    Return all orders with corresponding customer names, including customers not present in the customers table.

    Performs a left join from orders to customers on 'customer_id':
    - Keeps all records from orders.
    - Fills missing customer names with NaN if no match is found.

    The result is sorted by 'order_id' in ascending order.

    Args:
        orders (pd.DataFrame): DataFrame containing order details, including 'order_id', 'customer_id', and 'amount'.
        customers (pd.DataFrame): DataFrame containing customer information, including 'customer_id' and 'name'.

    Returns:
        pd.DataFrame: Merged DataFrame with columns 'order_id', 'customer_id', 'amount', and 'name'.
    """
    df = orders.merge(right=customers,how='left',on='customer_id').sort_values('order_id',ascending=True)
    return df

print(customer_with_order(orders,customers))