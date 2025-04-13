#SHOPPING DISCOUNT CALCULATOR

# 1. Initial Variables
purchase_amount = 120.00  # total shopping amount
is_loyalty_member = True
day_of_week = "Sunday"
is_holiday_season = True

# 2. Discount Calculation
original_amount = purchase_amount
total_discount = 0

print("Original Purchase Amount: $", original_amount)

# Base discount based on purchase amount
if purchase_amount > 100:
    discount = purchase_amount * 0.10
    print("10% discount for purchases over $100: $", round(discount, 2))
    total_discount += discount
elif purchase_amount > 50:
    discount = purchase_amount * 0.05
    print("5% discount for purchases over $50: $", round(discount, 2))
    total_discount += discount

# Loyalty member discount
if is_loyalty_member:
    discount = purchase_amount * 0.05
    print("5% loyalty discount: $", round(discount, 2))
    total_discount += discount

# Weekend discount
if day_of_week == "Saturday" or day_of_week == "Sunday":
    discount = purchase_amount * 0.02
    print("2% weekend discount: $", round(discount, 2))
    total_discount += discount

# Holiday season discount
if is_holiday_season:
    discount = purchase_amount * 0.08
    print("8% holiday season discount: $", round(discount, 2))
    total_discount += discount

# 3. Final Price
final_price = purchase_amount - total_discount
print("Total Discount: $", round(total_discount, 2))
print("Final Price to Pay: $", round(final_price, 2))
