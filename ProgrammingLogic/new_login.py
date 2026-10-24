import random

password = "Dublin2026"
tries = 0

while tries < 3:
    attempts = 0
    count = 0
    character_password = []
    tries += 1

    while attempts < 3:
        rnd = random.randint(1, len(password))

        while rnd in character_password:
            rnd = random.randint(1, len(password))

        character_password.append(rnd)
        character = (input(f"Please input the letter {rnd}:")).lower()
        attempts += 1

        if character == password[rnd - 1]:
            count += 1

    if count == 3:
        print("Access Granted!")
        break
    else:
        print("Access Denied!")

if count != 3:
    print("Access BLOCKED!")

