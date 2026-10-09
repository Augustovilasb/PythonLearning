alphabet = "abcdefghijklmnopqrstuvwxyz"

crypted_text = input("Enter your text: ").lower()
key = int(input("Between 0 - 25: "))

decrypt_text = ""

for letter in crypted_text:
    if letter in alphabet:
        indexLetter = alphabet.index(letter)
        decryption = (indexLetter - key) % 26
        indexLetter = alphabet[decryption]
        decrypt_text += indexLetter
    else:
        decrypt_text += letter
print(decrypt_text)