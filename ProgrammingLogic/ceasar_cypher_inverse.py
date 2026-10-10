alphabet = "abcdefghijklmnopqrstuvwxyz"

while True:
    print("Please, peak your choose:")
    menu = input("1 - Encrypt\n2 - Decrypt\n3 - Leave\n",)

    while menu != "1" and menu != "2" and menu != "3":
        print("Invalid input!")
        menu = input("1 - Encrypt\n2 - Decrypt\n3 - Leave\n")
    if menu == "3":
        print("Thank u!")
        break

    crypted_text = input("Enter your text: ").lower()
    key = int(input("Between 0 - 25: "))

    decrypt_text = ""

    if menu == "1":
        for letter in crypted_text:
            if letter in alphabet:
                indexLetter = alphabet.index(letter)
                decryption = (indexLetter + key) % 26
                indexDecryption = alphabet[decryption]
                decrypt_text += indexDecryption
            else:
                decrypt_text += letter
        print("Result = ",decrypt_text)
        print("")

    elif menu == "2":
        for letter in crypted_text:
            if letter in alphabet:
                indexLetter = alphabet.index(letter)
                decryption = (indexLetter - key) % 26
                indexDecryption = alphabet[decryption]
                decrypt_text += indexDecryption
            else:
                decrypt_text += letter
        print("Result = ",decrypt_text)
        print("")
    elif menu == "3":
        break