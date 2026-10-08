
import csv
from collections import defaultdict

sales_by_product = defaultdict(float)
total_revenue = 0

with open("data/sales.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        quantity = int(row["quantity"])
        unit_price = float(row["unit_price"])
        revenue = quantity * unit_price

        sales_by_product[row["product"]] += revenue
        total_revenue += revenue

print("Total revenue:", total_revenue)
print("\nRevenue by product:")

for product, revenue in sorted(
    sales_by_product.items(),
    key=lambda item: item[1],
    reverse=True
):
    print(f"{product}: {revenue:.2f}")