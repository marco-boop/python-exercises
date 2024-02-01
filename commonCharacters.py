strings = ["aaaa", "a"]

def commonCharacters(strings):
    dict = {}
    array = []

    print("The length of strings is: ",len(strings))

    shortestStringIndex = min(range(len(strings)), key=lambda i: len(strings[i]))
    
    print(shortestStringIndex)

    for chars in strings[shortestStringIndex]:
        dict[chars] = []

    print(dict)
    
    counter = 0

    while counter < len(strings):
        for chars in strings[counter]:
            print("Chars is: ", chars)
            if chars in dict and len(dict[chars]) <= counter:
                print("Length of dict[chars]: ",len(dict[chars]))
                dict[chars].append(counter)
        counter += 1
    
    print(dict)

    for values in dict:
        if len(dict[values]) == len(strings):
            array.append(values)

    print(array)

    return array

answer = commonCharacters(strings)
print(answer)