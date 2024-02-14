words = ["abcdefghijk", "aaa", "hello", "racecar", "kjihgfedcba"]

def semordnilap(words):
    output = []
    wordSet = set(words)
    for word in words:
        holder = []
        for i in reversed(range(len(word))):
            holder.append(word[i])
        string = "".join(holder)
        if word != string and string in wordSet:
            output.append([word,string])
            wordSet.remove(word)
            wordSet.remove(string)
        print(wordSet)
    return output
























# Simplified flipping the word around

# def semordnilap(words):
#     bigArray = []
#     word_set = set(words)
#     for word in words:
#         paliHolder = []
#         paliSearch = word[::-1]
#         if word != paliSearch and paliSearch in word_set:
#             bigArray.append([word,paliSearch])
#             word_set.remove(word)
#             word_set.remove(paliSearch)
#     return bigArray




# Tidier

# def semordnilap(words):
#     bigArray = []
#     word_set = set(words)
#     for word in words:
#         paliHolder = []
#         for i in range(len(word)-1, -1,-1):
#             paliHolder.append(word[i])
#         paliSearch = ''.join(paliHolder)
#         if word != paliSearch:
#             if paliSearch in word_set:
#                 bigArray.append([word,paliSearch])
#                 word_set.remove(word)
#     return bigArray

# Solution that works 

# def semordnilap(words):
#     bigArray = []
#     word_set = set(words)
#     for word in words:
#         paliHolder = []
#         for i in range(len(word)-1, -1,-1):
#             paliHolder.append(word[i])
#         paliSearch = ''.join(paliHolder)
#         print(paliSearch)
#         if word != paliSearch:
#             if paliSearch in word_set:
#                 print("Found")
#                 bigArray.append([word,paliSearch])
#                 word_set.remove(word)
#             else:
#                 print("Word not found")
#     print(bigArray)

answer = semordnilap(words)
print(answer)
