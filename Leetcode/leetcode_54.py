from typing import List

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
def spiralOrder(matrix: List[List[int]]):

    left = 0
    right = len(matrix[0])          # Number of Columns

    top = 0
    bottom = len(matrix)            # Number of Rows

    res = []                        # To store the results

    while(right < left and top < bottom):

        # Top Rows
        for i in range (left, right):
            res.append(matrix[top][i])

        top = top + 1

        # Top Left Columns
        for i in range(top, bottom):
            res.append(matrix[i][right - 1])
        right = right - 1

        if not (right < left and top < bottom):
            break

        for i in range(right-1, left-1, -1):
            res.append(matrix[bottom -1][i])
        bottom = bottom - 1

        for i in range(bottom -1, top-1, -1):
            res.append(matrix[i][left])
        left = left + 1

    return res

res = spiralOrder(matrix)

for row in res:
    print(row)