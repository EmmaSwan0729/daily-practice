import pandas as pd

orders = pd.DataFrame({
    'order_id': [1, 2, 3, 4, 5],
    'customer_id': [101, 102, 101, 103, 102],
    'amount': [250, 180, 320, 95, 410],
    'order_date': ['2024-01-05', '2024-01-07', '2024-01-10', '2024-01-12', '2024-01-15']
})

customers = pd.DataFrame({
    'customer_id': [101, 102, 103],
    'customer_name': ['Alice', 'Bob', 'Charlie'],
    'city': ['London', 'Paris', 'London']
})

df_customer_amount = customers.merge(right=orders, how='left',on='customer_id')

def get_customer_total_amount(orders:pd.DataFrame, customers:pd.DataFrame) -> pd.DataFrame:
    """
    Calculate total order amount per customer and return results sorted in descending order.

    Args:
        orders (pd.DataFrame): Order data containing 'customer_id' and 'amount'.
        customers (pd.DataFrame): Customer data containing 'customer_id' and 'customer_name'.

    Returns:
        pd.DataFrame: DataFrame with columns:
            - customer_name (str): Name of the customer
            - amount (float/int): Total order amount per customer, sorted descending
    """
    df_merged = customers.merge(right=orders, how='left',on='customer_id')
    df_result = df_merged.groupby('customer_name',as_index=False)['amount'].sum()
    df_result=df_result.sort_values(by='amount',ascending=False)
    return(df_result)

def get_high_value_customers(orders:pd.DataFrame, customers:pd.DataFrame) -> pd.DataFrame:
    """
    Retrieve customers whose total order amount exceeds 300.

    Args:
        orders (pd.DataFrame): Order data containing 'customer_id' and 'amount'.
        customers (pd.DataFrame): Customer data containing 'customer_id' and 'customer_name'.

    Returns:
        pd.DataFrame: DataFrame containing:
            - customer_name (str): Customers with total amount > 300
    """
    df_merged = customers.merge(right=orders, how='left',on='customer_id')
    df_grouped = df_merged.groupby('customer_name', as_index=False).sum().reset_index()
    # as_index=False 在groupby时就直接不把分组字段变成索引，直接是DataFrame（干净）
    # df_grouped = df_merged.groupby('customer_name').sum().reset_index()
    # .reset_index()在已经变成索引之后再把索引变回普通列，结果也对，但多一步

    df_result=df_grouped[df_grouped['amount']>300][['customer_name']]
    return(df_result)

def get_london_orders(orders:pd.DataFrame, customers:pd.DataFrame) -> pd.DataFrame:
    """
    Retrieve customers whose total order amount exceeds 300.

    Args:
        orders (pd.DataFrame): Order data containing 'customer_id' and 'amount'.
        customers (pd.DataFrame): Customer data containing 'customer_id' and 'customer_name'.

    Returns:
        pd.DataFrame: DataFrame containing:
            - customer_name (str): Customers with total amount > 300
    """
    df_merged = customers.merge(right=orders, how='left',on='customer_id')
    df_result =df_merged[df_customer_amount['city']=='London'][['customer_name','order_id','amount']]
    return(df_result)

print(get_customer_total_amount(orders, customers))
print(get_high_value_customers(orders, customers))
print(get_london_orders(orders, customers))