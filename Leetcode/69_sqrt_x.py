class Solution:
    def mySqrt(self, x: int) -> int:

        left = 0
        right = x
        res = 0

        while left <= right:
            mid = left + ((right  - left) // 2)
            square = mid * mid
            if square > x:
                right = mid - 1

            elif square < x:
                left = mid + 1
                res = mid

            else:
                return mid

        return res

obj = Solution()
result = obj.mySqrt(26)
print(result)