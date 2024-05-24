import pytest
from typing import *


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return repr(self)

    def __repr__(self):
        s = f"""<Node val={self.val}>"""
        if not self.left and not self.right:
            return f"""<Node val={self.val}>"""

        left = "None" if not self.left else repr(self.left)
        right = "None" if not self.right else repr(self.right)

        return f"""<Node val={self.val}, left={left} right={right}>"""

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TreeNode):
            return False

        if self.val != other.val:
            return False

        return self.left == other.left and self.right == other.right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        root = cur = TreeNode(preorder[0])

        root_pos = inorder.index(preorder[0])
        left_branch_len = root_pos - 0

        root.left = self.buildTree(
            preorder[1 : 1 + left_branch_len], inorder[:root_pos]
        )
        root.right = self.buildTree(
            preorder[1 + left_branch_len :], inorder[root_pos + 1 :]
        )

        return root


s = Solution()


def test_create():
    r = s.buildTree([], [])
    assert r is None


def test_single_node():
    preorder = [1]
    inorder = [1]
    r = s.buildTree(preorder, inorder)
    au = TreeNode(1)
    assert r == au


def test_one_left():
    preorder = [1, 2]
    inorder = [2, 1]

    r = s.buildTree(preorder, inorder)
    au = TreeNode(1, left=TreeNode(2))

    assert r == au


def test_one_right():
    preorder = [1, 2]
    inorder = [1, 2]

    au = TreeNode(1, right=TreeNode(2))
    r = s.buildTree(preorder, inorder)

    assert r == au


def test_big_left_chain():
    preorder = [1, 2, 3, 4, 5]
    inorder = [5, 4, 3, 2, 1]

    au = TreeNode(
        1, left=TreeNode(2, left=TreeNode(3, left=TreeNode(4, left=TreeNode(5))))
    )

    r = s.buildTree(preorder, inorder)

    assert r == au


def test_both_children():
    inorder = [2, 1, 3]
    preorder = [1, 2, 3]

    au = TreeNode(1, left=TreeNode(2), right=TreeNode(3))
    r = s.buildTree(preorder, inorder)

    assert r == au


def test_leetcode_sample():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    au = TreeNode(
        3, left=TreeNode(9), right=TreeNode(20, left=TreeNode(15), right=TreeNode(7))
    )
    r = s.buildTree(preorder, inorder)

    assert r == au


if __name__ == "__main__":
    pytest.main()
