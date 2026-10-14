# 2. Market Survey Analyzer

# Fake survey data
responses = ["coffee", "tea", "coffee", "soda"]

# Count how many people chose each product
counts = {}
for product in responses:
    if product in counts:
        counts[product] += 1
    else:
        counts[product] = 1

# Print market share for each product
print("Market Share Summary")
for product in counts:
    share = counts[product] / len(responses) * 100
    print(f"{product}: {share:.0f}%")