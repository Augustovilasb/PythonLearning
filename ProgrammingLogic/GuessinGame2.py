password = "BTCSalvacao"
tries = 4
right = "WELL DONE, WE ARE RICH!!!"
fail = "WRONG, LESS ONE CHANCE!!!"
deleted = "!!!Wallet has been DELETED!!!"

while tries > 0:
    guess = input("Gimme a try: ")
    tries -= 1
    if guess == password:
        print(right)
        break
    else:
        if tries == 0:
            print("No more chances!!!")
            print(deleted)
        elif tries == 1:
            print(fail)
            print(tries,"chance now!!!\n")
        else:
            print(fail)
            print(tries,"chances now!!!\n")