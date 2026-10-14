# 9. Business Growth Projection

revenue = float(input("Enter initial revenue: "))
growth_rate = float(input("Enter growth rate (%): "))

print(f"\n{'Year':<6}{'Revenue':>15}")
print("-" * 21)

# Grow revenue each year for 10 years
for year in range(1, 11):
    revenue = revenue * (1 + growth_rate / 100)
    money = f"${revenue:,.2f}"
    print(f"{year:<6}{money:>15}")