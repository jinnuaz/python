height = [1,8,6,2,5,4,8,3,7]

def maxArea(height):

    res   = 0
    left  = 0
    right = len(height)-1

    while (right > left):
        area = (right - left) * min(height[left], height[right])
        res = max(res, area)

        if height[left] < height[right]:
            left = left + 1

        elif height[right] < height[left]:
            right = right - 1

        else:
            right = right - 1

    return res

print(f"This is liner approch to find the Max Area - {maxArea(height)}")