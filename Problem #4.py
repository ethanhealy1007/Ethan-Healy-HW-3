# 4. Sales Commission Calculator

sales = {"Ethan": 5000, "Evan": 7000, "Conrad": 3000}

# Function that returns a 10% commission
def calculate_commission(amount):
    return amount * 0.10

# Calculate each employee's commission
commissions = {}
for name in sales:
    commissions[name] = calculate_commission(sales[name])

# Sort employees from highest to lowest commission
ranked = sorted(commissions, key=commissions.get, reverse=True)

print("Commission Leaderboard")
rank = 1
for name in ranked:
    print(f"{rank}. {name}: ${commissions[name]:,.2f}")
    rank += 1