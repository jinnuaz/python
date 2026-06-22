from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        res = 0  # n xor 0 = n
        for n in nums:
            res = res ^ n
        return res

obj = Solution()
result = obj.singleNumber([1,2,3,4,5,6,7,7,8,9])

print(result)