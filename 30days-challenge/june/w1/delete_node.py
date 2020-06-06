class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while True:
            node.val = node.next.val
            if node.next.next is None:
                node.next = None
                return
            else:
                node = node.next
