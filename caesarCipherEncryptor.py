# import string

# alphabet_string = string.ascii_lowercase
# print(alphabet_string)

string = "ovmqkwtujqmfkao"
key = 52


def caesarCipherEncryptor(string, key):
    array = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in string:
        positionInAlphabet = alphabet.find(i)
        shiftedPosition = positionInAlphabet + key
        newCharacter = alphabet[shiftedPosition % 26]
        print("New character is: ",newCharacter)
        array.append(newCharacter)
    output = "".join(array)
    print(output)
    return output

caesarCipherEncryptor(string, key)











# Modulo instead of while loop that subtracts 26
# def caesarCipherEncryptor(string, key):
#     alpha = "abcdefghijklmnopqrstuvwxyz"
#     shifted = []
#     for i in string:
#         position = alpha.find(i)
#         position += key
#         print("position is ,",position)
#         if position > 25:
#             position = position % 26
#             print("Looparond needed: ",position, alpha[position])
#         shifted.append(alpha[position])
#         print(shifted)
#         finalAnswer = ''.join(shifted)
#         print(finalAnswer)
#     return finalAnswer


# # Tidier version
# def caesarCipherEncryptor(string, key):
#     alpha = "abcdefghijklmnopqrstuvwxyz"
#     shifted = []
#     for i in string:
#         position = alpha.find(i)
#         position += key
#         if position > 25:
#             while position > 25:
#                 position -= 26
#             print("Looparond needed: ",alpha[position])
#         shifted.append(alpha[position])
#         print(shifted)
#         finalAnswer = ''.join(shifted)
#         print(finalAnswer)
#     return finalAnswer

# def caesarCipherEncryptor(string, key):
#     alpha = "abcdefghijklmnopqrstuvwxyz"
#     shifted = []
#     print(len(alpha))
#     print(alpha[25])
#     for i in string:
#         position = alpha.find(i)
#         print(position)
#         position += key
#         if position <= 25:
#             print("No looparond needed: ",alpha[position])
#         else:
#             while position > 25:
#                 position -= 26
#             print("Looparond needed: ",alpha[position])
#         shifted.append(alpha[position])
#         print(shifted)
#         finalAnswer = ''.join(shifted)
#         print(finalAnswer)
#     return finalAnswer

# caesarCipherEncryptor(string, key)