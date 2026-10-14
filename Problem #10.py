# 10. Startup Pitch Deck Visualizer (ASCII Style)

# Projected revenue by year (in $ millions)
revenue = [3, 5, 8, 12, 17]

print("Projected Revenue by Year ($M)")

# Outer loop goes through each year
for i in range(len(revenue)):
    bar = ""
    # Inner loop adds one # for each $1M
    for j in range(revenue[i]):
        bar += "#"
    print(f"Year {i + 1}: {bar} ({revenue[i]})")