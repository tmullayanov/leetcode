from typing import *


class TreeNode:
    '''Definition for a binary tree node.'''

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # other ideas: "bfs" using queue for each level of depth
        # or inorder traversal.
        return self.dfs(root, 0)

    def dfs(self, node: TreeNode, depth: int) -> int:
        if node is None:
            return depth
        left = self.dfs(node.left, depth+1)
        right = self.dfs(node.right, depth+1)
        return max(left, right)


if __name__ == '__main__':
    t1 = TreeNode(3, left=TreeNode(9), right=TreeNode(
        20, left=TreeNode(15), right=TreeNode(7)))
    t2 = TreeNode(0)
    print(f'ans={Solution().maxDepth(t1)}')
    print(f'ans={Solution().maxDepth(t2)}')
