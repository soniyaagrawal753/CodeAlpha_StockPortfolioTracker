# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 200,
    "MSFT": 300
}

total_investment = 0

print("================================")
print("   STOCK PORTFOLIO TRACKER")
print("================================")

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ₹{price}")

while True:
    stock_name = input("\nEnter stock name: ").upper()

    if stock_name not in stock_prices:
        print("❌ Stock not available.")
        continue

    quantity = int(input("Enter quantity: "))

    investment = stock_prices[stock_name] * quantity
    total_investment += investment

    print(f"✅ {stock_name}: ₹{investment}")

    choice = input("Do you want to add another stock? (yes/no): ").lower()

    if choice != "yes":
        break

print("\n================================")
print(f"Total Investment: ₹{total_investment}")
print("================================")