class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root, arr):
        if not root:
            return False
        stack = [(root, 0)]
        current_sequence = []
        while stack:
            node, pos = stack.pop()
            if not node or pos >= len(arr):
                continue

            if arr[pos] != node.val:
                continue

            # arr[pos] == node.val for the rest of cycle body
            if pos == len(arr) - 1 and node.left is None and node.right is None:
                return True

            stack.append((node.right, pos + 1))
            stack.append((node.left, pos + 1))
        return False


if __name__ == '__main__':
    t = TreeNode(0)
    t.right = TreeNode(0, TreeNode(0))
    t.left = TreeNode(1)
    t.left.left = TreeNode(0, right=TreeNode(1))
    t.left.right = TreeNode(1, left=TreeNode(0), right=TreeNode(0))

    print(Solution().isValidSequence(t, [0, 1, 0, 1]))
    print(Solution().isValidSequence(t, [0, 0, 1]))
    print(Solution().isValidSequence(t, [0, 1, 1]))

    wa = TreeNode(4)
    wa.right = TreeNode(2)
    wa.right.left = TreeNode(7, left=TreeNode(3), right=TreeNode(4))
    wa.right.right = TreeNode(5, left=TreeNode(4))
    print(Solution().isValidSequence(wa, [4, 2, 7, 4]))
