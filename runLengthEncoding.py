string = "W"


def runLengthEncoding(string):
    outputArray = []
    counter = 1

    if len(string) == 1:
        valueToAppend = "1" + string[0]
        outputArray.append(valueToAppend)

    for i in range(1, len(string)):
        current = string[i]
        previous = string[i - 1]
        if current != previous or counter == 9:
            valueToAppend = str(counter) + previous
            outputArray.append(valueToAppend)
            print(outputArray)
            counter = 0
        counter += 1
        if i == len(string) - 1:
            valueToAppend = str(counter) + current
            outputArray.append(valueToAppend)
            print("Last one: ",outputArray)
    
    finalAnswer = ''.join(outputArray)
    return finalAnswer


    # def looking(string,pointer):
    #     if pointer >= len(string) - 1:
    #         return
    #     counter = 1
    #     print("At this point pointer is", pointer)
    #     while pointer is not len(string) - 1 and counter < 9 and string[pointer] == string[pointer + 1]:
    #         currentChar = string[pointer]
    #         if currentChar == string[pointer]:
    #             counter += 1
    #             pointer += 1
    #         print("Counter:", counter)
    #         print("Pointer:", pointer)
    #         print("Current character", currentChar)
    #     valueToAppend = str(counter) + str(currentChar)
    #     outputArray.append(valueToAppend)
    #     print(outputArray)
    #     return looking(string,pointer + 1)
        
    # looking(string, 0)
    # finalAnswer = ''.join(outputArray)
    # return finalAnswer


# def runLengthEncoding(string):
#     outputArray = []

#     def looking(string,pointer):
#         if pointer >= len(string) - 1:
#             return
#         counter = 1
#         print("At this point pointer is", pointer)
#         while pointer is not len(string) - 1 and counter < 9 and string[pointer] == string[pointer + 1]:
#             currentChar = string[pointer]
#             if currentChar == string[pointer]:
#                 counter += 1
#                 pointer += 1
#             print("Counter:", counter)
#             print("Pointer:", pointer)
#             print("Current character", currentChar)
#         valueToAppend = str(counter) + str(currentChar)
#         outputArray.append(valueToAppend)
#         print(outputArray)
#         return looking(string,pointer + 1)
        
#     looking(string, 0)
#     finalAnswer = ''.join(outputArray)
#     return finalAnswer

answer = runLengthEncoding(string)
print(answer)