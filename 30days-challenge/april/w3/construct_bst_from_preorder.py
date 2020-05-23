class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return f'''<Node val={self.val}>'''

    def __str__(self, level=0):
        ret = '  ' * level + repr(self) + '\n'
        ret += '' if not self.left else self.left.__str__(level+1)
        ret += '' if not self.right else self.right.__str__(level+1)
        return ret


class Solution:
    def bstFromPreorder(self, preorder):
        stack = []
        root = TreeNode(preorder[0])
        stack.append(root)
        for val in preorder[1:]:
            node = TreeNode(val)
            top = stack[-1]
            if val < top.val:
                top.left = node
                stack.append(node)
            else:
                while stack and stack[-1].val < val:
                    tmp = stack.pop()
                tmp.right = node
                stack.append(node)
        return root
