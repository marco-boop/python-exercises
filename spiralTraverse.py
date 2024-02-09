array = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
  ]

# def spiralTraverse(array):
#     output = []

#     beginCol = 0
#     endCol = len(array) - 1
#     beginRow = 0
#     endRow = len(array[0]) - 1

#     def perimeter(array,beginCol,endCol,beginRow, endRow):
#         output.append(array[0][0])
#         current = beginRow
#         if beginRow < endRow:
#             output.append(array[beginRow][current])
#             current += 1
#             print(output)
        
#         return perimeter(array,beginCol + 1,endCol - 1,beginRow + 1, endRow - 1)

    

    # currentRow = beginRow
    # currentCol = beginCol

    # output.append(array[currentCol][currentRow])

    # while beginCol < endCol and beginRow < endRow:
    #     print(output)
    #     while currentRow < endRow:
    #         print("Current column: ", currentCol)
    #         print("Current row: ", currentRow)
    #         currentRow += 1
    #         output.append(array[currentCol][currentRow])
    #         if currentRow == endRow:
    #             beginCol += 1

    #     while currentCol < endRow:
    #         print("Current column: ", currentCol)
    #         print("Current row: ", currentRow)
    #         currentCol += 1
    #         output.append(array[currentCol][currentRow])
    #         if currentCol == endCol:
    #             endRow -= 1

    #     while currentRow > beginRow:
    #         print("Current column: ", currentCol)
    #         print("Current row: ", currentRow)
    #         currentRow -= 1
    #         output.append(array[currentCol][currentRow])
    #         if currentRow == beginRow:
    #             endCol -= 1

    #     while currentCol > beginCol:
    #         print("Current column: ", currentCol)
    #         print("Current row: ", currentRow)
    #         currentCol -= 1
    #         output.append(array[currentCol][currentRow])
    #         if currentCol == beginCol:
    #             beginRow += 1

    # return output

def spiralTraverse(array):
    output = []

    beginCol = 0
    endCol = len(array) - 1
    beginRow = 0
    endRow = len(array[0]) - 1

    currentRow = beginRow
    currentCol = beginCol

    output.append(array[currentCol][currentRow])

    while beginCol < endCol and beginRow < endRow:
        print(output)
        while currentRow < endRow:
            print("Current column: ", currentCol)
            print("Current row: ", currentRow)
            currentRow += 1
            output.append(array[currentCol][currentRow])
            if currentRow == endRow:
                beginCol += 1

        while currentCol < endRow:
            print("Current column: ", currentCol)
            print("Current row: ", currentRow)
            currentCol += 1
            output.append(array[currentCol][currentRow])
            if currentCol == endCol:
                endRow -= 1

        while currentRow > beginRow:
            print("Current column: ", currentCol)
            print("Current row: ", currentRow)
            currentRow -= 1
            output.append(array[currentCol][currentRow])
            if currentRow == beginRow:
                endCol -= 1

        while currentCol > beginCol:
            print("Current column: ", currentCol)
            print("Current row: ", currentRow)
            currentCol -= 1
            output.append(array[currentCol][currentRow])
            if currentCol == beginCol:
                beginRow += 1

    return output


answer = spiralTraverse(array)
print(answer)