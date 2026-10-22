import random

password = "DataCentreTecTU5263"

length_password = len(password)
attempts = 0
count = 0
character_index = []

while attempts < 3:
    rnd = random.randint(1, length_password)

    while rnd in character_index:
        rnd = random.randint(1, length_password)

    character_index.append(rnd)
    character = input(f"Please input password character {rnd} (Case Sensitive): ")

    if character == password[rnd -1]:
        count += 1
    attempts += 1

if count == 3:
    print("You are logged in!")
else:
    print("Error, characters inputted don't match with the password!")
