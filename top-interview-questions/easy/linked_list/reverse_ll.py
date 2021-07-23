from typing import *


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
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        cur = head
        prev = None
        while cur is not None:
            _next = cur.next
            cur.next = prev
            prev = cur
            cur = _next

        return prev

    def reverseListRecursively(self, head: ListNode, prev=None) -> ListNode:
        if head is None:
            return None
        elif head.next is None:
            head.next = prev
            return head
        else:
            new_tail = head.next
            head.next = prev
            new_head = self.reverseListRecursively(new_tail, prev=head)
            return new_head


if __name__ == '__main__':
    lists = [
        ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
        ListNode(1),
        ListNode(1, ListNode(2))
    ]
    for l in lists:
        print(f'{l=} ans={Solution().reverseListRecursively(l)}')
