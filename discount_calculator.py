def calculate_price(original_price, discount_rate=0.10):
    discount_amount = original_price * discount_rate
    final_price = original_price - discount_amount

    return final_price


price = calculate_price(100)


print("Final price: $" + str(price))
# print(calculate_price(100, 0.20))