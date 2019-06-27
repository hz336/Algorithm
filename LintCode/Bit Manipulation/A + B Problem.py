"""
Write a function that add two numbers A and B. You should not use + or any arithmetic operators.

Clarification
Are a and b both 32-bit integers?

Yes.
Can I use bit operation?

Sure you can.
"""


class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b
    """

    """
    主要利用异或运算来完成，异或运算有一个别名叫做：不进位加法
    那么a ^ b就是a和b相加之后，该进位的地方不进位的结果
    然后下面考虑哪些地方要进位，自然是a和b里都是1的地方
    a & b就是a和b里都是1的那些位置，a & b << 1 就是进位
    之后的结果。所以：a + b = (a ^ b) + (a & b << 1)
    令a' = a ^ b, b' = (a & b) << 1
    可以知道，这个过程是在模拟加法的运算过程，进位不可能
    一直持续，所以b最终会变为0。因此重复做上述操作就可以
    求得a + b的值。
        
    Python 有个问题是 int 超过 0x7FFFFFFF 之后会自动转成 long 
    所以在 (a & b) << 1 时会就这么不断的往前进位，跳不出循环
    对应的思路是每次越界(超过 0x7FFFFFFF * 2 + 1, 所有 int 个数)就 and 一次
    """

    def aplusb(self, a, b):
        # write your code here
        while b != 0:
            a, b = (a ^ b) & 0x7FFFFFFF, (a & b) << 1

        return a


sol = Solution()
ans = sol.aplusb(1, 2)
print(ans)
