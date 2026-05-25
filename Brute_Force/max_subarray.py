def max_subarray_brute_force(nums):
    max_sum = float('-inf')  # Start with the smallest possible value
    n = len(nums)

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum

# Example usage:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_brute_force(nums)) # Output: 6
