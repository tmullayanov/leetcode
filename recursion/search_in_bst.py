class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'''<Node val={self.val}>'''

    def __str__(self, level=0):
        ret = '  ' * level + repr(self) + '\n'
        ret += '' if not self.left else self.left.__str__(level+1)
        ret += '' if not self.right else self.right.__str__(level+1)
        return ret


class Solution:
    def searchBST(self, root, val):
        if not root or root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(7)

    print(Solution().searchBST(root, 2))
