"""
Given n books and the ith book has A[i] pages. You are given k people to copy the n books.

n books list in a row and each person can claim a continous range of the n books. For example one copier can copy the books from ith to jth
continously, but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).

They start copying books at the same time and they all cost 1 minute to copy 1 page of a book. What's the best strategy to assign books so that the
slowest copier can finish at earliest time?

Example
Given array A = [3,2,4], k = 2.
Return 5( First person spends 5 minutes to copy book 1 and book 2 and second person spends 4 minutes to copy book 3. )
"""

""" 
Time Complexity: nlog(total pages) 
"""
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # write your code here
        if pages is None or len(pages) == 0:
            return 0

        start, end = min(pages), sum(pages)
        while start + 1 < end:
            mid = start + (end - start) // 2
            checker = self.check(pages, mid, k)
            if checker:
                end = mid
            else:
                start = mid

        if self.check(pages, start, k):
            return start
        else:
            return end

    def check(self, pages, limit, k):
        left = 0
        num = 0
        for i in range(len(pages)):
            if pages[i] > limit:
                return False

            if pages[i] > left:
                num += 1
                left = limit

            left -= pages[i]

        return num <= k
