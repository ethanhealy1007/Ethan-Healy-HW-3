# 7. Simple Supply Chain Tracker

warehouses = [
    {"name": "Warehouse A", "inventory": {"apples": 500, "bananas": 100}},
    {"name": "Warehouse B", "inventory": {"apples": 340, "bananas": 180}}
]

totals = {}

# Outer loop goes through each warehouse
for warehouse in warehouses:
    # Inner loop goes through each product in that warehouse
    for product in warehouse["inventory"]:
        amount = warehouse["inventory"][product]
        if product in totals:
            totals[product] += amount
        else:
            totals[product] = amount

print("Total Stock Across Supply Chain")
for product in totals:
    print(f"{product}: {totals[product]}")