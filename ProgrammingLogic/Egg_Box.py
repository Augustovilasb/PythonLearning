one_box = 12
one_box_price = 3.50
prize_box = 10

cakes = int(input("How many cake would u cook next week? "))
eggs_per_cake = int(input("How many eggs do u need for 1 cake? "))

# quantity of box Maria need to buy
total_eggs = cakes * eggs_per_cake
print("Total of eggs:", total_eggs)

eggbox_weekly = ((total_eggs + 11) // one_box)
print("U will need", eggbox_weekly, "boxes this week")

# eggs remainders weekly
eggs_remainder = ((eggbox_weekly * one_box) - total_eggs)
print("And will have", eggs_remainder," eggs remainders")

# buy 10 box and gain one fre
win_free_box = eggbox_weekly // prize_box
print("This week u have",win_free_box,"box fre")

# total price per order
total_price = eggbox_weekly * one_box_price
print("The eggs order will cost ", round(total_price, 2))

# price with prize
total_price_with_prize = eggbox_weekly - win_free_box
price_with_prize = total_price_with_prize * one_box_price
print("The final eggs order will cost ", round(price_with_prize, 2))
