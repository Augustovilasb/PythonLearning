# Write a python program that encrypts a sentence. It encrypts a sentence using a Caesar shift.
# Thus the program requires the sentence as an input and the shift key (0-25).
# For the required Lab upload all letters will be in lower case and exactly 5 characters in length
# with no spaces. A sample output of the program is the encrypted sentence:

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
encryptedText = ""

textMessage = input("Please type the text to be encrypted: ").lower()
inputKey = int(input("Please, type any key (0-25): "))

for letter in textMessage:
    if letter in alphabet:
        indexLetter = alphabet.index(letter)
        encrypting = (indexLetter + inputKey) % 26
        newLetter = alphabet[encrypting]
        encryptedText = encryptedText + newLetter
    else:
        encryptedText = encryptedText + letter

print("Text msg encrypted :", encryptedText)