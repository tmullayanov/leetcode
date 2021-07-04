class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node: ListNode):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        '''
        my prior solution was to "shift" all nodes to the "left" by one:
        while True:
          node.val = node.next.val
          if node.next.next is None:
            node.next = None
            return
          node = node.next
        # don't mess with next unless we have to "cut" last element. just shift values
        '''
