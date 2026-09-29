password = "Estudando1"

print("Lets play a game...")
print("I have 10 Bitcoins on my wallet...")
print("But somehow, im missing the passphrase...")
print("If you gess it, we share them!")
print("Care, its not too easy, we have 4 chances.. otherwise the wallet is deleted forever!!!")
print("BREAK LEGS!")

guess1 = input("U can start: ")
msg = "WELL DONE, WE ARE RICH!!! The passphrase is 'Estudando1'"
tries = 0

if guess1 == password:
    print(msg)
else:
    print("First dice: We have 10 characters!")
    tries = tries + 1
    guess2 = input("Try again...")
    if guess2 != password:
        print("Second dice: Ah! We also have a number on that!")
        tries = tries + 1
        guess3 = input("Try again...")
        if guess3 != password:
            print("Third and last dice: We have an upper letter on that!")
            tries = tries + 1
            guess4 = input("Try again...")
            if guess4 != password:
                tries = tries + 1
                print("U have been trying",tries,"th")
                print("The wallet has been DELETED!")
            else:
                print(msg)
        else:
            print(msg)
    else:
        print(msg)