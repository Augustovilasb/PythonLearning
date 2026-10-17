import random

password = "abcdefghijklmnopq"
length = len(password)
tries = 0

while tries < 3:
    cha_checked = []
    count = 0
    attempts = 0

    while attempts < 3:
        rnd = random.randint(1, length)

        while rnd in cha_checked:
            rnd = random.randint(1, length)

        character = input(f"Please input the Character {rnd}: ")
        if character == password[rnd - 1]:
            count += 1
        cha_checked.append(rnd)
        attempts += 1

    if count == 3:
        print("Access Granted!")
        break
    else:
        print("Access Denied!")
    tries += 1

    if tries == 3:
        print("Access LOCKED!")
        exit()

# MENU

CHECK_TEMPERATURE = 1
PURCHASE_REQUEST = 2
LOAD_BALANCE = 3
EXIT = 4
TEMP_OK_MIN = 18
TEMP_WARNING_MIN = 27
TEMP_CRITICAL_MIN = 35
LOWER_TEMP = -10
HIGHER_TEMP = 60

while True:

    print("MENU:")
    print("1 - CHECK TEMPERATURE")
    print("2 - PURCHASE REQUEST")
    print("3 - LOAD BALANCE")
    print("4 - EXIT")

    input_user = int(input("Please, select an option: "))

    if input_user == CHECK_TEMPERATURE:

        temp = float(input("Please, input the temperature (min -10 & max 60): "))

        while LOWER_TEMP > temp or temp > HIGHER_TEMP:
            print("Invalid temp, try again: ")
            temp = float(input("Please, input the temperature (min -10 & max 60): "))
        if temp < TEMP_OK_MIN:
            print("TOO COLD!!")
        elif temp < TEMP_WARNING_MIN:
            print("It's OK!")
        elif temp < TEMP_CRITICAL_MIN:
            print("It's a WARNING!")
        else:
            print("IT'S CRITICAL!")

    elif input_user == PURCHASE_REQUEST:
        print("Coming soon!")
    elif input_user == LOAD_BALANCE:
        print("Coming soon!")
    elif input_user == EXIT:
        print("Welcome!")
        break
    else:
        print("Invalid Option!")
