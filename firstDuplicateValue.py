array = [2, 1, 5, 2, 3, 3, 4]

def firstDuplicateValue(array):
    map = {}
    print(map)
    for i in range(len(array)):
        if array[i] in map:
            return array[i]
        else:
            map[array[i]] = True

a = firstDuplicateValue(array)
print(a)