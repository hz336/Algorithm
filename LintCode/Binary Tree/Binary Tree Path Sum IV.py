"""
If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.

For each integer in this list:
1. The hundreds digit represents the depth D of this node, 1 <= D <= 4.
2. The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the same as that in a full binary
tree.
3. The units digit represents the value V of this node, 0 <= V <= 9.
Given a list of ascending three-digits integers representing a binary with the depth smaller than 5. You need to return the sum of all paths from the
root towards the leaves.

Example
Given nums = [113, 215, 221], return 12.

Explanation:
The tree that the list represents is:
    3
   / \
  5   1

The path sum is (3 + 5) + (3 + 1) = 12.
Given nums = [113, 221], return 4.

Explanation:
The tree that the list represents is:
    3
     \
      1

The path sum is (3 + 1) = 4.
"""


class Solution:
    """
    @param nums: a list of integers
    @return: return an integer
    """

    def __init__(self):
        self.ans = 0

    def pathSum(self, nums):
        if nums is None or len(nums) == 0:
            return 0

        values = {x // 10: x % 10 for x in nums}
        root = nums[0] // 10
        self.dfs(values, root, 0)
        return self.ans

    def dfs(self, values, node, num_sum):
        if node not in values:
            return

        num_sum += values[node]
        depth, pos = node // 10, node % 10
        left = (depth + 1) * 10 + 2 * pos - 1
        right = left + 1

        if left not in values and right not in values:
            self.ans += num_sum
        else:
            self.dfs(values, left, num_sum)
            self.dfs(values, right, num_sum)
