characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"
# characters = "ehoLL"
# document = "heLLo"
# document = ""

def generateDocument(characters, document):
    map = {}
    for character in characters:
        if character not in map:
            map[character] = 1
        else:
            map[character] += 1
    for character in document:
        print("Looking for: ",character)
        print("Remaining characters: ",map)
        if character in map:
            if map[character] > 0:
                map[character] -= 1
            if map[character] == 0:
                del map[character]
        else:
            return False
    return True

answer = generateDocument(characters, document)
print(answer)






























# def generateDocument(characters, document):
#     check = True
#     if document == "":
#         return check
#     print(characters)
#     print(document)
#     table = {}
#     for character in characters:
#         if character in table:
#             table[character] += 1
#         else:
#             table[character] = 1
#     print(table)
#     for character in document:
#         print(character)
#         print(table)
#         if character in table:
#             if table[character] == 1:
#                 del table[character]
#             else:
#                 table[character] -= 1
#         else:
#             check = False
#     return check


# answer = generateDocument(characters, document)
# print(answer)