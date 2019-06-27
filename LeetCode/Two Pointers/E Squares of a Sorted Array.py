"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""

"""
Version 1: sort
Time Complexity: O(nlogn)
Space Complexity: O(n)
"""
class Solution_v1:
    def sortedSquares(self, A: 'List[int]') -> 'List[int]':
        A = [c ** 2 for c in A]
        A.sort()

        return A


"""
Version 2: two pointers
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution_v2:
    def sortedSquares(self, A: List[int]) -> List[int]:
        if A is None or len(A) == 0:
            return []

        results = [0] * len(A)
        index = len(A) - 1
        left, right = 0, len(A) - 1
        while left <= right:
            if A[left] * A[left] > A[right] * A[right]:
                results[index] = A[left] * A[left]
                left += 1
            else:
                results[index] = A[right] * A[right]
                right -= 1

            index -= 1

        return results


