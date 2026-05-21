height = [1,8,6,2,5,4,8,3,7]

def maxArea(self, height):

    res = 0

    for left in range(len(height)):
        for right in range(1+left, len(height)):
            area = (left - right)* min(height[left], height[right])
            res = max(res, area)

    return res

print(f"Maximum Area = {maxArea(height)}")