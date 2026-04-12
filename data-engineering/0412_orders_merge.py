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

def cutomer_with_order(orders:pd.DataFrame, customers:pd.DataFrame) -> pd.DataFrame:
    df = orders.merge(right=customers,how='left',on='customer_id').sort_values('order_id',ascending=True)
    return df

print(cutomer_with_order(orders,customers))