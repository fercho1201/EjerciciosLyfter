price = float(input("Enter the price of the item: "))
discount = 0
if price >= 100:
    discount = (price * 0.05)
else:
    discount = (price * 0.02)
final_price = price - discount
print("The final price after discount is: ", final_price)