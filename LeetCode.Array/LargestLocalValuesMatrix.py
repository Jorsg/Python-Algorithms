# 2373. Largest Local Values in a Matrix
#You are given an n x n integer matrix grid.
#Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:
#* maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.
#In other words, we want to find the largest value in every contiguous 3 x 3 matrix in grid.
#Return the generated matrix.

#Example 1:

#Input: grid = [[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]]
#Output: [[9,9],[8,6]]
#Explanation: The diagram above shows the original matrix and the generated matrix.
#Notice that each value in the generated matrix corresponds to the largest value of a contiguous 3 x 3 matrix in grid.
#Example 2:

#Input: grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]
#Output: [[2,2,2],[2,2,2],[2,2,2]]
#Explanation: Notice that the 2 is contained within every contiguous 3 x 3 matrix in grid.
#
#Constraints:
#* n == grid.length == grid[i].length
#* 3 <= n <= 100
#* 1 <= grid[i][j] <= 100

def largest_local(grid):
    n = len(grid)
    max_Local = [[0] * (n - 2) for _ in range(n - 2)]

    for i in range(n - 2):
        for j in range(n - 2):
            max_val = 0
            for x in range(3):
                for y in range(3):
                    max_val = max(max_val, grid[i + x][j + y])
            max_Local[i][j] = max_val
    return max_Local

# Ejemplo de uso
grid = [
    [9, 9, 8, 1],
    [5, 6, 2, 6],
    [8, 2, 6, 4],
    [6, 2, 2, 2]
]
print(largest_local(grid))  # Output: [[9, 9], [8, 6]]    