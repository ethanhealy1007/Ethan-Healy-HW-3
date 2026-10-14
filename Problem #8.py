# 8. Customer Loyalty Tiers

customers = {
    "Ethan": 800,
    "Evan": 1500,
    "Ryan": 8600,
    "Conrad": 3000,
    "Josh": 4899,
    "Luke": 4000
}

tier_counts = {"Bronze": 0, "Silver": 0, "Gold": 0}

# Assign each customer a tier
for name in customers:
    amount = customers[name]
    if amount < 1000:
        tier = "Bronze"
    elif amount < 5000:
        tier = "Silver"
    else:
        tier = "Gold"
    tier_counts[tier] += 1
    print(f"{name}: ${amount:,} -> {tier}")

print("\nTier Summary")
for tier in tier_counts:
    print(f"{tier}: {tier_counts[tier]} customers")