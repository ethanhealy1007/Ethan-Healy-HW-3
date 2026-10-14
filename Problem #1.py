# 1. Retail Checkout Simulation

prices = []  # list to store each item price

# Keep asking for prices until the user enters 0
price = float(input("Enter item price (0 to finish): "))
while price != 0:
    if price < 0:
        print("Price can't be negative. Try again.")
    else:
        prices.append(price)
    price = float(input("Enter item price (0 to finish): "))

# Calculate results
if len(prices) > 0:
    total = sum(prices)
    average = total / len(prices)
    print(f"Total purchase: ${total:,.2f}")
    print(f"Average item cost: ${average:,.2f}")
    print(f"Number of items: {len(prices)}")
else:
    print("No items purchased.")