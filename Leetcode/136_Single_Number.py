from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        res = 0  # n xor 0 = n
        for n in nums:
            res = res ^ n
        return res

obj = Solution()
result = obj.singleNumber([4,1,2,1,2])

print(result)