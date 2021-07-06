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
        pass

