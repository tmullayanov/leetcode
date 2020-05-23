class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
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
    stack = []
    parents = []

    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.stack = []
        self.parents = []
        x_depth = self._dfs(root, x, 0)
        y_depth = self._dfs(root, y, 0)

        if x_depth is None or y_depth is None:
            return False
        if x_depth != y_depth:
            return False

        return self.parents[0] != self.parents[1] and self.parents[0] is not None and self.parents[1] is not None

    def _dfs(self, root, val, lvl=0):
        if not root:
            return None
        if root.val == val:
            parent = self.stack[-1] if self.stack else None
            self.parents.append(parent)
            return lvl

        self.stack.append(root)
        left = self._dfs(root.left, val, lvl+1)
        if left:
            self.stack.pop()
            return left

        right = self._dfs(root.right, val, lvl+1)
        if right:
            self.stack.pop()
            return right

        self.stack.pop()
        return None


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
    root.right = TreeNode(7, left=None, right=TreeNode(9))
    print(Solution().isCousins(root, 1, 9))
