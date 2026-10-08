# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            # 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from operator import index

# both alphabet works perfectly on index
alphabet = "abcdefghijklmnopqrstuvwxyz"

textMessage = input("Please, enter the message you would like to encrypt:")
key = int(input("Gimme the product key:"))
encryptedText = ""

for letter in textMessage:
    if  letter in alphabet:
        indexLetter = alphabet.index(letter)
        encrypting = (indexLetter + key) % 26
        indexLetter = alphabet[encrypting]
        encryptedText += indexLetter
print(encryptedText)