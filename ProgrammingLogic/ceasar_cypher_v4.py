alphabet = "abcdefghijklmnopqrstuvwxyz"

textMsg = input("Enter the msg:").lower()
key = int(input("Between 0 - 25:"))
encryptedText = ""

for letter in textMsg:
    if letter in alphabet:
        indexLetter = alphabet.index(letter)
        encrypting = (indexLetter + key) % 26
        indexLetter = alphabet[encrypting]
        encryptedText += indexLetter
    else:
        encryptedText += letter
print(encryptedText)
