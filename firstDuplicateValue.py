# array = [2, 1, 5, 2, 3, 3, 4]
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Even better solution, go through array and for the index that matches the value:
# make that value negative, that way when you find it again, you'll know you
# saw it already

def firstDuplicateValue(array):
    map = {}
    if len(array) <= 1:
        return -1
    for i in range(len(array)):
        if array[i] in map:
            return array[i]
        else:
            map[array[i]] = True
    return -1

a = firstDuplicateValue(array)
print(a)