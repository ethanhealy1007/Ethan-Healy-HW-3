# 6. Bank Loan Repayment Simulator

# Function to add one month of interest to the balance
def add_interest(balance, annual_rate):
    monthly_rate = annual_rate / 100 / 12
    return balance + balance * monthly_rate

loan = float(input("Enter loan amount: "))
rate = float(input("Enter annual interest rate (%): "))
payment = float(input("Enter monthly payment: "))

# Make sure the payment is bigger than the first month's interest
if payment <= loan * rate / 100 / 12:
    print("Payment is too small. The loan will never be paid off.")
else:
    balance = loan
    months = 0
    # Keep paying until the balance hits zero
    while balance > 0:
        balance = add_interest(balance, rate)
        balance -= payment
        months += 1
    print(f"It will take {months} months to pay off the loan.")