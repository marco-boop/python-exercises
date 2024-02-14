array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 5]

def isValidSubsequence(array, sequence):
    if len(sequence) > len(array):
        return False
    arrayPointer = 0
    sequencePointer = 0
    while sequencePointer < len(sequence) and arrayPointer < len(array):
        print(sequence[sequencePointer])
        if sequence[sequencePointer] == array[arrayPointer]:
            print("Found: ",sequence[sequencePointer])
            sequencePointer += 1
            arrayPointer += 1
            if sequencePointer == len(sequence):
                return True
        else: 
            arrayPointer += 1
    return False
    

answer = isValidSubsequence(array, sequence)
print(answer)

# def isValidSubsequence(array, sequence):
#     validation = False
#     print("len(sequence) is ", len(sequence))
#     if len(sequence) > len(array):
#         return validation
#     i = 0
#     for num in range(len(array)):
#         print(sequence[i], array[num])
#         if sequence[i] != array[num]:
#             validation = False
#             print(validation)
#         elif sequence[i] == array[num]:
#             i = i + 1
#             print("Now i is ",i)
#             print(validation)
#             if i == len(sequence):
#                 validation = True
#                 break
#     return validation
            
        # else:
        #     validation = False
        # return validation

    #     look for num in array
    #         if you get to the end of the array and don't find
    #             validation = false
    #         if you find in:
    #             validation = true
    #             remove from the front of the array anything up to and including num
    #     move on to next number in sequence with remaining array

# def isValidSubsequence(array, sequence):
#     validation = False
#     if len(sequence) > len(array):
#         return validation
#     i = 0
#     for num in range(len(array)):
#         if sequence[i] != array[num]:
#             validation = False
#         elif sequence[i] == array[num]:
#             i = i + 1
#             if i == len(sequence):
#                 validation = True
#                 break
#     return validation

# answer = isValidSubsequence(array, sequence)
# print(answer)