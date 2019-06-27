"""
Count characters in a string. Return a hash map which key is character and value is the occurrency of this character.

Example
Given str = "abca", return

{
  "a": 2,
  "b": 1,
  "c": 1
}
"""


class Solution:
    """
    @param: : a string
    @return: Return a hash map
    """

    def countCharacters(self, str):
        # write your code here
        results = {}
        for c in str:
            if c not in results:
                results[c] = 1
            else:
                results[c] += 1

        return results