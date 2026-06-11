

class Solution:
    def findMedianSortedArrays(nums1, nums2):

        A = nums1           # A should be shorter array
        B = nums2

        if len(B) < len(A):
            A = B
            B = A

        total = len(A) + len(B)
        half  = total // 2

        left = 0
        right = len(A) - 1

        while True:
            middle_A = (left + right) // 2
            middle_B = half - middle_A - 2

            A_left  = A[middle_A] if middle_A >= 0 else float("-infinity")
            A_right = A[middle_A + 1] if middle_A + 1 < len(A) else float ("infinity")
            B_left  = B[middle_B] if middle_B >= 0 else float("-infinity")
            B_right = B[middle_B + 1]  if middle_B + 1 < len(B) else float ("infinity")

            if A_left <= B_right and B_left <= A_right:
                # Odd
                if total % 2 != 0:
                    return min(A_right, B_right)

                # Even
                return (max(A_left, B_left) + min(A_right, B_right) / 2)

            elif A_left > B_right:
                right = middle_A - 1

            else:
                left = middle_A + 1

sol = Solution()
result = sol.findMedianSortedArrays([1,2,3,4], [1,2,3,4,5,6,7,8])