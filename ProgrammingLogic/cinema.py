price_child = 7.00
price_teen = 9.00
price_adult = 12.50
price_elderly = 8.00

age_child = 12
age_teen = 17
age_adult = 64
age_elderly = 65

age = int(input("Please, input your age: "))
day = input("Please, input the week day: ").lower()

if age < 0:
    print("Age invalid, please input a positive value!")
else:
    if age < age_child:
        price = price_child
    elif age <= age_teen:
        price = price_teen
    elif age <= age_adult:
        price = price_adult
    else:
        price = price_elderly

    if day == "tuesday" and price == price_adult:
        price = price/2
    print("The price is:", price)