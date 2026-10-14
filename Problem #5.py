# 5. Stock Portfolio Tracker
import random

portfolio = {
    "ABR": {"shares": 5, "price": 25},
    "GOOGL": {"shares": 8, "price": 180},
    "AMZN": {"shares": 4, "price": 130}
}

# Function to add up the value of every stock
def portfolio_value(portfolio):
    total = 0
    for stock in portfolio:
        total += portfolio[stock]["shares"] * portfolio[stock]["price"]
    return total

print(f"Starting portfolio value: ${portfolio_value(portfolio):,.2f}")

# Bonus: simulate 7 days of random price changes (between -5% and +5%)
for day in range(1, 8):
    for stock in portfolio:
        change = random.uniform(-0.05, 0.05)
        portfolio[stock]["price"] *= (1 + change)
    print(f"Day {day}: ${portfolio_value(portfolio):,.2f}")