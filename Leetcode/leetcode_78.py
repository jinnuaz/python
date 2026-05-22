
nums = [1,2,3]

def subsets(nums):

    res = []
    subset = []
    def dfs(i):
        if (i >= len(nums)):
            res.append(subset.copy())
            return

        # decision to include nums[i]
        subset.append(nums[i])
        dfs(i + 1)

    def(0)
    return res

result = subsets(nums)

for row in result:
    print(row)