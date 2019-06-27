"""
Implement strStr function in O(n + m) time.

strStr return the first index of the target string in a source string. The length of the target string is m and the length of the source string is n.
If target does not exist in source, just return -1.
"""


class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """

    def strStr2(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1

        target_len = len(target)
        if target_len == 0:
            return 0

        BASE = 1000000

        # 31 ^ target_len
        power = 1
        for i in range(target_len):
            power = (power * 31) % BASE

        # target hash code
        target_code = 0
        for i in range(target_len):
            target_code = (target_code * 31 + ord(target[i])) % BASE

        # source hash code
        source_code = 0
        for i in range(len(source)):
            source_code = (source_code * 31 + ord(source[i])) % BASE

            if i < target_len - 1:
                continue

            if i > target_len - 1:
                source_code = (source_code - ord(source[i - target_len]) * power) % BASE
                if source_code < 0:
                    source_code += BASE

            if source_code == target_code:
                if source[i - target_len + 1: i + 1] == target:
                    return i - target_len + 1

        return -1



