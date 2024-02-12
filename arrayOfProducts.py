array = [5, 1, 4, 2]

def arrayOfProducts(array):
    output = []
    for i in range(len(array)):
        left = 1
        right = 1
        for j in range(0,i):
            print("This is j: ",array[j])
            left = left * array[j]
        for k in range(i + 1, len(array)):
            print("This is k: ",array[k])
            right = right * array[k]
        print(left," and ",right)
        output.append(left * right)
    return output

# Brute force approach

# def arrayOfProducts(array):
#     output = []
#     for i in range(len(array)):
#         product = 1
#         for j in range(len(array)):
#             if i != j:
#                 product = product * array[j]
#         output.append(product)
#     print(output)


a = arrayOfProducts(array)
print(a)