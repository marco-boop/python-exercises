array = [
    [4, 2, 3, 6, 7, 8, 1, 9, 5, 10],
    [12, 19, 15, 16, 20, 18, 13, 17, 11, 14]
  ]

# def spiralTraverse(array):
#     output = []
#     perimeterFill(array, 0,len(array) - 1,0, len(array[0])- 1, output)
#     return output

# def perimeterFill(array,beginCol,endCol,beginRow, endRow, output):
#         if beginCol > endCol or beginRow > endRow:
#             return
        
#         for col in range(beginCol,endCol + 1):
#             output.append(array[beginRow][col])

#         for row in range(beginRow + 1, endRow + 1):
#             output.append(array[row][endCol])

#         for col in reversed(range(beginCol, endCol)):
#             if beginRow == endRow:
#                 break
#             output.append(array[endRow][col])

#         for row in reversed(range(beginRow + 1, endRow)):
#             if beginCol == endCol:
#                 break
#             output.append(array[row][beginCol])
        
#         perimeterFill(array, beginCol + 1,endCol - 1, beginRow + 1, endRow - 1, output)
    
# answer = spiralTraverse(array)
# print(answer)

def spiralTraverse(array):
    output = []

    beginCol = 0
    endCol = len(array[0]) - 1
    beginRow = 0
    endRow = len(array) - 1

    while beginCol <= endCol and beginRow <= endRow:
        for col in range(beginCol,endCol + 1):
            output.append(array[beginRow][col])

        for row in range(beginRow + 1, endRow + 1):
            output.append(array[row][endCol])

        for col in reversed(range(beginCol, endCol)):
            if beginRow == endRow:
                break
            output.append(array[endRow][col])

        for row in reversed(range(beginRow + 1, endRow)):
            output.append(array[row][beginCol])
    
        beginCol +=1
        beginRow +=1
        endCol -= 1
        endRow -= 1

    return output

# def spiralTraverse(array):
#     output = []

#     beginCol = 0
#     endCol = len(array) - 1
#     beginRow = 0
#     endRow = len(array[0]) - 1

#     currentRow = beginRow
#     currentCol = beginCol

#     output.append(array[currentCol][currentRow])

#     while beginCol <= endCol and beginRow <= endRow:
#         print(output)
#         while currentRow < endRow:
#             print("Current column: ", currentCol)
#             print("Current row: ", currentRow)
#             currentRow += 1
#             output.append(array[currentCol][currentRow])
#             if currentRow == endRow:
#                 beginCol += 1
#                 break
#         while currentCol < endRow:
#             print("Current column: ", currentCol)
#             print("Current row: ", currentRow)
#             currentCol += 1
#             output.append(array[currentCol][currentRow])
#             if currentCol == endCol:
#                 endRow -= 1
#                 break
#         while currentRow > beginRow:
#             print("Current column: ", currentCol)
#             print("Current row: ", currentRow)
#             currentRow -= 1
#             output.append(array[currentCol][currentRow])
#             if currentRow == beginRow:
#                 endCol -= 1
#                 break
#         while currentCol > beginCol:
#             print("Current column: ", currentCol)
#             print("Current row: ", currentRow)
#             currentCol -= 1
#             output.append(array[currentCol][currentRow])
#             if currentCol == beginCol:
#                 beginRow += 1
#                 break
#     return output

# answer = spiralTraverse(array)
# print(answer)