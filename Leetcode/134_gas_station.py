from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start = 0
        total = 0

        for i in range(len(gas)):
            total = total + gas[i] - cost[i]

            if total < 0:
                total = 0
                start = i + 1

        return start

obj = Solution()
result = obj.canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2])
print(result)

