matrix = [[1,2],[3,4],[5, 6]]

# def transposeMatrix(matrix):
#     # print("matrix: ", matrix)
#     # print("len(matrix): ", len(matrix))
#     # print("matrix[0]: ", matrix[0])
#     # print("matrix[0][0]: ", matrix[0][0])
#     outMatrix = []
#     print(len(matrix))
#     rows = len(matrix)
#     print("rows is ",rows)
#     cols = len(matrix[0])
#     print("columns is ",cols)
#     for m in range(cols):
#         outMatrix.append([0]* rows)
#     print(outMatrix)
    
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             print("Looking at ",matrix[i][j])
#             outMatrix[j][i] = matrix[i][j]
#             print("New matrix is ",outMatrix)
#     return outMatrix

# def transposeMatrix(matrix):
#     # making our new matrix
#     outMatrix = []
#     rows = len(matrix)
#     cols = len(matrix[0])
#     for m in range(cols):
#         outMatrix.append([0]* rows)

#     # updating values
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             outMatrix[j][i] = matrix[i][j]

#     return outMatrix

# Book solution
# Didn't have to do all the setting up the matrix dimensions ahead of time
def transposeMatrix(matrix):
    # making our new matrix
    outMatrix = []
    # The next line tells us the length of each array which we call the columns and will become the # of rows in the output
    for i in range(len(matrix[0])):
        newRow = []
        # The next line is so for each row we have a number of elements equal to how long the original matrix was in length (aka the old number of rows).
        for j in range(len(matrix)):
            # We make each individual array
            newRow.append(matrix[j][i])
        #Then add the new array into the new matrix
        outMatrix.append(newRow)
    return outMatrix

answer = transposeMatrix(matrix)
print(answer)