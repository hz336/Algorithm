"""
Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

Example
Gieve s = lintcode,
dict = ["de", "ding", "co", "code", "lint"].

A solution is ["lint code", "lint co de"].
"""

""" Recursion with memoization
We can use memorization method, where we are making use of a hashmap to store the results in the form of a key:value pair. In this hashmap, 
the key used is the starting index of the string currently considered and the value contains all the sentences which can be formed using the 
substring from this starting index onwards. Thus, if we encounter the same starting index from different function calls, we can return the result 
directly from the hashmap rather than going for redundant function calls.

With memorization many redundant subproblems are avoided and recursion tree is pruned and thus it reduces the time complexity by a large factor.

Time complexity : O(n^3). Size of recursion tree can go up to n^2. The creation of list takes n time.
Space complexity : O(n^3).The depth of the recursion tree can go up to nn and each activation record can contains a string list of size nn.
"""


class Solution:
    """
    @param: s: A string
    @param: wordDict: A set of words.
    @return: All possible sentences.
    """

    def wordBreak(self, s, wordDict):
        # write your code here
        memo = {}
        results = self.dfs(s, wordDict, memo)

        return results

    def dfs(self, s, wordDict, memo):
        if s in memo:
            return memo[s]

        result = []

        if len(s) == 0:
            return result

        if s in wordDict:
            result.append(s)

        for i in range(1, len(s)):
            word = s[0: i]
            if word not in wordDict:
                continue
            suffix = s[i:]
            result_of_the_rest = self.dfs(suffix, wordDict, memo)

            for res in result_of_the_rest:
                item = word + " " + res
                result.append(item)

        memo[s] = result

        print(memo)

        return result


s = "lintcode"
word_dict = {"de", "ding", "co", 'd', 'e', "code", "lint"}
sol = Solution()
ans = sol.wordBreak(s, word_dict)
print(ans)
