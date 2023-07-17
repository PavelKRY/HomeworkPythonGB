def flip_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(i, len((matrix[i]))):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

predefined_matrix = [[10, 20, 30],
                     [40, 50, 60],
                     [70, 80, 90]]
print(*predefined_matrix, sep="\n")
flip_matrix(predefined_matrix)
print()
print(*predefined_matrix, sep="\n")



