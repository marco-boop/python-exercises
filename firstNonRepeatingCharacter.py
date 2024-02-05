string = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

def firstNonRepeatingCharacter(string):
    dict = {}
    for i in range(len(string)):
        if string[i] not in dict:
            dict[string[i]] = 1
        else:
            dict[string[i]] += 1
    print(dict)
    firstMatch = next(((key, value) for key, value in dict.items() if value == 1), None)
    if firstMatch == None:
        return -1
    else:
        result = string.index(firstMatch[0])
        
    print(result)
    return result



    #     print("-------------------Outside index",string[i])
    #     for j in range(len(string)):
    #         print(string[i],string[j])
    #         if i != j and string[i] == string[j]:
    #             break
    #         print("This is j",j)
    #         print("Length of the string always the same: ",len(string))
    #         print("String[i]",string[i])
    #         print("String[j]",string[j])
    #         if j == len(string) - 1:
    #             print("Found", string[i])
    #             return i
            
    # return -1

# This works but we could do it without the two loops

# def firstNonRepeatingCharacter(string):
#     for i in range(len(string)):
#         print("-------------------Outside index",string[i])
#         for j in range(len(string)):
#             print(string[i],string[j])
#             if i != j and string[i] == string[j]:
#                 break
#             print("This is j",j)
#             print("Length of the string always the same: ",len(string))
#             print("String[i]",string[i])
#             print("String[j]",string[j])
#             if j == len(string) - 1:
#                 print("Found", string[i])
#                 return i
            
#     return -1

answer = firstNonRepeatingCharacter(string)
print(answer)