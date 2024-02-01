string = "aA"

print(len(string))

def runLengthEncoding(string):
    outputArray = []

    def looking(string,pointer):
        if pointer >= len(string) - 1:
            return
        counter = 1
        print("At this point pointer is", pointer)
        while pointer is not len(string) - 1 and counter < 9 and string[pointer] == string[pointer + 1]:
            currentChar = string[pointer]
            if currentChar == string[pointer]:
                counter += 1
                pointer += 1
            print("Counter:", counter)
            print("Pointer:", pointer)
            print("Current character", currentChar)
        valueToAppend = str(counter) + str(currentChar)
        outputArray.append(valueToAppend)
        print(outputArray)
        return looking(string,pointer + 1)
        
    looking(string, 0)
    finalAnswer = ''.join(outputArray)
    return finalAnswer

answer = runLengthEncoding(string)
print(answer)