"""
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Notice
Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.
"""

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution_v1:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """

    """ O(n) time complexity, O(n) space complexity """

    def closestKValues(self, root, target, k):
        # write your code here
        values = []
        self.traverse(root, values)

        for i in range(len(values)):
            if values[i] >= target:
                break

        left, right = i - 1, i
        results = []
        for i in range(k):
            if left < 0:
                results.append(values[right])
                right += 1
            elif right == len(values):
                results.append(values[left])
                left -= 1
            else:
                if target - values[left] <= values[right] - target:
                    results.append(values[left])
                    left -= 1
                else:
                    results.append(values[right])
                    right += 1

        return results

    def traverse(self, root, values):
        if root is None:
            return

        self.traverse(root.left, values)
        values.append(root.val)
        self.traverse(root.right, values)


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution_v2:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """

    """
    最优算法，时间复杂度 O(k + logn)O(k+logn)，空间复杂度 O(logn)O(logn)

    实现如下的子函数：

    getStack() => 在假装插入 target 的时候，看看一路走过的节点都是哪些，放到 stack 里，用于 iterate
    moveUpper(stack) => 根据 stack，挪动到 next node
    moveLower(stack) => 根据 stack, 挪动到 prev node
    有了这些函数之后，就可以把整个树当作一个数组一样来处理，只不过每次 i++ 的时候要用 moveUpper，i--的时候要用 moveLower
    """

    def closestKValues(self, root, target, k):
        # write your code here
        if root is None:
            return []

        values = []
        lower_stack = self.get_stack(root, target)
        upper_stack = lower_stack.copy()
        if target < lower_stack[-1].val:
            self.move_lower(lower_stack)
        else:
            self.move_upper(upper_stack)

        for i in range(k):
            if len(lower_stack) == 0:
                values.append(upper_stack[-1].val)
                self.move_upper(upper_stack)
            elif len(upper_stack) == 0:
                values.append(lower_stack[-1].val)
                self.move_lower(lower_stack)
            else:
                if target - lower_stack[-1].val <= upper_stack[-1].val - target:
                    values.append(lower_stack[-1].val)
                    self.move_lower(lower_stack)
                else:
                    values.append(upper_stack[-1].val)
                    self.move_upper(upper_stack)

        return values

    def get_stack(self, root, target):
        stack = []
        while root:
            stack.append(root)
            if target < root.val:
                root = root.left
            else:
                root = root.right

        return stack

    def move_lower(self, stack):
        node = stack[-1]
        if node.left is None:
            node = stack.pop()
            while stack and stack[-1].left == node:
                node = stack.pop()
            return

        node = node.left
        while node:
            stack.append(node)
            node = node.right

    def move_upper(self, stack):
        node = stack[-1]
        if node.right is None:
            node = stack.pop()
            while stack and stack[-1].right == node:
                node = stack.pop()
            return

        node = node.right
        while node:
            stack.append(node)
            node = node.left



















