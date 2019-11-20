"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Example
["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""


class Solution:
    """
    @param: tokens: The Reverse Polish Notation
    @return: the value
    """

    def evalRPN(self, tokens):
        # write your code here
        stack = []
        for c in tokens:
            if c not in ('+', '-', '*', '/'):
                stack.append(int(c))
            else:
                ope2 = stack.pop()
                ope1 = stack.pop()
                if c == '+':
                    stack.append(ope1 + ope2)
                elif c == '-':
                    stack.append(ope1 - ope2)
                elif c == '*':
                    stack.append(ope1 * ope2)
                else:
                    stack.append(int(ope1 / ope2))

        return stack[0]
