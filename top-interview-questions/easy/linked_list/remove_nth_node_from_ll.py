from typing import *

# TODO: implement single-traverse solution. Use "fast" and "slow" pointers and update it by N


class ListNode:
    '''
    Definition for a singly linked list.
    '''

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return '{val} {next}'.format(**{'val': self.val, 'next': self.next or 'END'})

    def __repr__(self) -> str:
        return str(self)


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # detect len
        listLength = 0
        detect_l_node = head
        while detect_l_node is not None:
            detect_l_node = detect_l_node.next
            listLength += 1

        if listLength < n:
            return None
        elif listLength == n:
            return head.next
        stop_l = listLength - n

        node = head
        for i in range(stop_l - 1):
            node = node.next

        node.next = None if node.next is None else node.next.next
        return head


if __name__ == '__main__':
    lists = [
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
        ListNode(1),
        ListNode(1, ListNode(2)),
        ListNode(1, ListNode(2))
    ]
    tests = (
        (lists[0], 2),
        (lists[1], 1),
        (lists[2], 1),
        (lists[3], 2)
    )

    for (head, n) in tests:
        h = Solution().removeNthFromEnd(head, n)
        print(h)
