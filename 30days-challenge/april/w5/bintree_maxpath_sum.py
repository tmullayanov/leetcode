import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root):
        self.max = float('-inf')

        def get_sum(root):
            if not root:
                return 0
            ls = max(get_sum(root.left), 0)
            rs = max(get_sum(root.right), 0)
            self.max = max(self.max, ls + rs + root.val)
            return max(ls, rs, 0) + root.val
        get_sum(root)
        return self.max


if __name__ == '__main__':
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    print(Solution().maxPathSum(root))

    print(Solution().maxPathSum(TreeNode(-3)))

    rootWA = TreeNode(1)
    rootWA.left = TreeNode(-2)
    rootWA.left.left = TreeNode(1, TreeNode(-1))
    rootWA.left.right = TreeNode(3)
    rootWA.right = TreeNode(-3, TreeNode(-2))
    print(Solution().maxPathSum(rootWA))
