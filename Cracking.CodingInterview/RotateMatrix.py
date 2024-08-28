# 1.7 Rotate Matrix" Given an imagen represented by an N x N matrix, where each pixel in the imagen is represented by an integer,
# write a method to rotate the image by 90 degree. Can you do this in place?

def rotate_matriz(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    # rotate image
    for i in range(n):
        for j in range(n // 2):
            arr[i][j], arr[i][n - 1 - j] = arr[i][n - 1 - j], arr[i][j]

    return arr        


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotada = rotate_matriz(matriz)
for fila in rotada:
    print(fila)