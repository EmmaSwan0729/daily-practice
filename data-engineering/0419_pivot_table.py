import pandas as pd

data = {
    "date": ["2024-01-01", "2024-01-01", "2024-01-01", "2024-01-01",
             "2024-01-02", "2024-01-02", "2024-01-02", "2024-01-02"],
    "region": ["East", "West", "East", "West", "East", "West", "East", "West"],
    "product": ["A", "A", "B", "B", "A", "A", "B", "B"],
    "sales": [100, 150, 200, 130, 110, 160, 210, 140],
}

df = pd.DataFrame(data)

def summarize_sales(df: pd.DataFrame) -> pd.DataFrame:
    """
    Creates a pivot table summarizing total sales by region and product.

    The function aggregates sales data using a pivot table where:
    - Rows represent regions
    - Columns represent products
    - Values represent the sum of sales

    Args:
        df (pd.DataFrame): Input DataFrame containing at least
            'region', 'product', and 'sales' columns.

    Returns:
        pd.DataFrame: Pivot table with total sales per region-product pair.
    """
    pivot_table = df.pivot_table(
        index = "region",
        columns = "product",
        values = "sales",
        aggfunc = "sum",
        fill_value = 0
    )

    return pivot_table

print(summarize_sales(df))