# decrypts a Caesar encryption
def caesar(encryption):
    encryption = encryption.lower()
    for i in range(26):
        decryption = ""
        for char in encryption:
            charCode = ord(char)
            charPlace = charCode - 97
            newCharPlace = (charPlace + i) % 26
            newCharCode = newCharPlace + 97
            decryption = decryption + chr(newCharCode)
        print(decryption.upper() + "\n")
