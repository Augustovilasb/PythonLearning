first_number = int(input("Please, type the first number: "))

while first_number == 0:
    print("There is no division by 0.")
    first_number = int(input("Please, type the first number again: "))

second_number = int(input("Please, type the second number now: "))
remainder = second_number % first_number

if remainder == 0:
    print(f"The division of {second_number} by {first_number} is evenly, no remainder!")
else:
    print(f"The division of {second_number} by {first_number} has remainder.")
    print(f"The remainder is: {remainder}")
