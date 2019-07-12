"""
Give you an array of 01. Find the minimum number of flipping steps so that the array meets the following rules:
The back of 1 can be either1 or 0, but0 must be followed by 0.

Example
Given array = [1,0,0,1,1,1], return 2.

Explanation:
Turn two 0s into 1s.
Given array = [1,0,1,0,1,0], return 2.

Explanation:
Turn the second 1 and the third 1 into 0.
"""

"""
Time Complexity: O(N)
Space Complexity: O(N) 
"""
class Solution_v1:
    """
    @param nums: the array
    @return: the minimum times to flip digit
    """

    def flipDigit(self, nums):
        # Write your code here
        if nums is None or len(nums) <= 1:
            return 0

        n = len(nums)
        f = [[math.inf for _ in range(2)] for _ in range(n + 1)]
        f[0][0] = f[0][1] = 0

        for i in range(1, n + 1):
            # A[i - 1] will be changed to curr_digit
            for curr_digit in range(2):
                # I(A[i - 1] != j)
                flip = 0
                if nums[i - 1] != curr_digit:
                    flip = 1

                # A[i - 2] will change to k
                for prev_digit in range(2):
                    if prev_digit == 0 and curr_digit == 1:
                        continue

                    f[i][curr_digit] = min(f[i][curr_digit], f[i - 1][prev_digit] + flip)

        return min(f[n][0], f[n][1])


"""
Time Complexity: O(N)
Space Complexity: O(1) 
"""
class Solution_v2:
    """
    @param nums: the array
    @return: the minimum times to flip digit
    """

    def flipDigit(self, nums):
        # Write your code here
        if nums is None or len(nums) <= 1:
            return 0

        n = len(nums)
        f = [[math.inf for _ in range(2)] for _ in range(2)]

        old, now = 0, 1
        f[now][0] = f[now][1] = 0

        for i in range(1, n + 1):
            old, now = now, old
            for curr_digit in range(2):
                f[now][curr_digit] = math.inf

                # I(A[i - 1] != j)
                flip = 0
                if nums[i - 1] != curr_digit:
                    flip = 1

                # A[i - 2] will change to k
                for prev_digit in range(2):
                    if prev_digit == 0 and curr_digit == 1:
                        continue

                    f[now][curr_digit] = min(f[now][curr_digit], f[old][prev_digit] + flip)

        return min(f[now][0], f[now][1])
