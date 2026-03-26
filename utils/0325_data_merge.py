import pandas as pd

orders = pd.DataFrame({
    "order_id":   [1, 2, 3, 4, 5],
    "customer_id":[101, 102, 101, 103, 104],
    "product_id": [201, 202, 203, 201, 202],
    "quantity":   [2, 1, 3, 1, 2],
})

customers = pd.DataFrame({
    "customer_id": [101, 102, 103],
    "name":        ["Alice", "Bob", "Charlie"],
    "city":        ["London", "Paris", "Berlin"],
})

products = pd.DataFrame({
    "product_id": [201, 202, 203],
    "name":       ["Laptop", "Phone", "Tablet"],
    "price":      [999.0, 499.0, 299.0],
})
# 要求：
# 把三张表合并成一张完整的表
# 新增 revenue 列 = price × quantity
# 找出没有下单的客户（提示：customer_id 104 在 orders 里但不在 customers 里）
# 每个城市的总销售额
# 每个产品卖出了多少件，总收入是多少

order_cust = pd.merge(
    left=orders,
    right=customers,
    left_on="customer_id",
    right_on="customer_id",
    how='left'
)

order_cust_prod = pd.merge(
    left=order_cust,
    right=products,
    left_on="product_id",
    right_on="product_id",
    how='left'
)
order_cust_prod["revenue"] = order_cust_prod["price"] * order_cust_prod["quantity"]

cust_no_order = order_cust[order_cust["name"].isna()]["customer_id"]

total_sales_city = order_cust_prod.groupby("city")["revenue"].sum()

total_sales_prod = order_cust_prod.groupby("product_id").agg(prod_count=("quantity","sum"), prod_sale = ("revenue","sum"))

print(order_cust_prod)
print(cust_no_order)
print(total_sales_city)
print(total_sales_prod)