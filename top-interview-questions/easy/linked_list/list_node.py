from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, __value) -> bool:
        if type(self) != type(__value):
            return False

        if self.val != __value.val:
            return False

        n1 = self.next
        n2 = __value.next

        return n1 == n2

    def __str__(self) -> str:
        if self.val is None:
            return ""
        if self.next is None:
            return f"{self.val}"
        return f"{self.val}, {str(self.next)}"

    def toList(self):
        l = list()
        c = self
        while c is not None:
            l.append(c.val)
            c = c.next
        return l

    @staticmethod
    def fromList(lst: [Any]):
        head = None
        prev = None
        for i in lst:
            n = ListNode(i)
            if head is None:
                head = n
            if prev:
                prev.next = n
            prev = n

        return head
