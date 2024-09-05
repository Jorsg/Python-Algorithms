# 1.8 Zero Matrix
# Write an algorithm such that if an element in an M x N matrix is 0, its entire row and column are set to 0

def zero_matriz(arr):
    #Num rows and colums
    rows = len(arr)
    columns = len(arr[0])
   #Create sets to tracking rows and columns

    zero_rows = set()
    zero_columns = set()

    for i in range(rows):
        for j in range(columns):
            if arr[i][j] == 0:
                zero_rows.add(i)
                zero_columns.add(j)

    # rows to 0
    for i in zero_rows:
        for j in range(columns):
            arr[i][j] = 0

    for j in zero_columns:
        for i in range(rows):
            arr[i][j] = 0

    return arr


matriz = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

result = zero_matriz(matriz)
for row in result:
    print(row)

