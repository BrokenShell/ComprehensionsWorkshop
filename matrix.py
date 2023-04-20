""" Transpose a matrix in one line of code """

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[j][i])


arr = [[matrix[j][i] for j in range(len(matrix[i]))] for i in range(len(matrix))]
print(arr)
