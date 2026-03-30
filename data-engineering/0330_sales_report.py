import pandas as pd

orders = pd.DataFrame({
    'order_id': [1, 2, 3, 4, 5],
    'customer_id': [101, 102, 101, 103, 102],
    'amount': [250, 180, 320, 150, 210]
})
customers = pd.DataFrame({
    'customer_id': [101, 102, 104],
    'name': ['Alice', 'Bob', 'Charlie']
})
# **任务：**
# 1. 把两个表 join 起来，只保留在 `customers` 里存在的客户的订单
# 2. 算出每个客户的总消费金额
# 3. 结果按总金额降序排列，列名用 `total_spent`

def sales_report(orders:pd.DataFrame, customers:pd.DataFrame) -> pd.DataFrame:
    """
    Generate a sales report showing total spending per customer.

    Args:
        orders: DataFrame with columns order_id, customer_id, amount.
        customers: DataFrame with columns customer_id, name.

    Returns:
        DataFrame with columns name and total_spent, sorted by total_spent descending.
        Only includes customers present in the customers DataFrame.
    """
    df_join = pd.merge(left=customers, right=orders,left_on='customer_id', right_on='customer_id', how='left')

    total_spent = df_join.groupby('name').agg(total_spent=('amount','sum')).sort_values('total_spent', ascending=False)

    return total_spent

    print(total_spent)