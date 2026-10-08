alphabet = "abcdefghijklmnopqrstuvwxyz"

textMsg = input("Gimme the sentence:").lower()
key = int(input("Number between 0 - 25:"))

encryptedText = ""

for letter in textMsg:
    if letter in alphabet:
        indexLetter = alphabet.index(letter)
        encrypting = (indexLetter + key) % 26
        indexLetter = alphabet[encrypting]
        encryptedText += indexLetter
print(encryptedText)
