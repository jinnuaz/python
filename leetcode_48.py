from typing import List

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
def rotate(matrix: List[List[int]]):

    left    = 0
    right   = len(matrix)-1

    while(left < right):
        for i in range(right - left):
            top     = left
            bottom  = right
            # Beacuse it is a square matrix

            # Save topleft value in the temp variable
            topleft = matrix[top][left + i]

            # Move bottomleft value to the topleft
            matrix[top][left + i] = matrix[bottom - i][left]

            # Move bottomright value to bottomleft
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # Move bottomright value to topright
            matrix[bottom][right - i] = matrix[top + i][right]

            # Move topright value to topleft
            matrix[top + i][right] = topleft

        left    += 1
        right   -= 1

    return matrix

print(rotate(matrix))