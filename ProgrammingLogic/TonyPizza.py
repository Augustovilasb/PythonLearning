pizza_price = 14.90
slices_one_pizza = 8

guessers_number = int(input("How many people will attend the party? "))
slices_number = int(input("How many slices of pizza each one will eat? "))

# how many pizzas we need to buy?
total_slices = guessers_number * slices_number
total_pizzas = (total_slices + 7) // slices_one_pizza

print("We will need to order", total_pizzas, "pizzas from Tony's Pizza.")

# how many slices will remainder
remainder = (total_pizzas * slices_one_pizza) - total_slices
print("We will have", remainder, "slices of pizza remainders.")

# the value of pizzas ordered
order_price = total_pizzas * pizza_price
print("The total order's price is: €",round(order_price, 2))

order_without_VAT = order_price / 1.135
VAT = order_without_VAT * 0.135
print("The VAT on the order is: €", round(VAT, 2))

tony_money = order_price - VAT
print("The total of the money going to Tony is: €",round(tony_money, 2))
