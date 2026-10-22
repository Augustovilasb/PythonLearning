number_products = int(input("How many products has the purchase? "))
gold_costumer = input("Are u a gold costumer? (y/n)").lower()

product_price = 57.23
discount_a = 0.865
discount_b = 0.915
discount_gold = 0.965

total_cost = product_price * number_products

if gold_costumer == "y":
    if number_products >= 100:
        final_price_a = total_cost * discount_a
        print(f"The total purchase price is €: {round(final_price_a, 2)}")
    elif number_products >= 25:
        final_price_b = total_cost * discount_b
        print(f"The total purchase price is €: {round(final_price_b, 2)}")
    else:
        final_price_gold = total_cost * discount_gold
        print(f"The total purchase price is €: {round(final_price_gold, 2)}")
else:
    if number_products >= 100:
        final_price = total_cost * 0.90
    elif number_products >= 25:
        final_price = total_cost * 0.95
    else:
        final_price = total_cost
    print(f"The total purchase price is €: {round(final_price, 2)}")
