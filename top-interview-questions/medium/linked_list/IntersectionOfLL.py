import unittest
from typing import *


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def toList(self):
        l = list()
        c = self
        while c is not None:
            l.append(c.val)
            c = c.next
        return l

    def __eq__(self, __value) -> bool:
        if type(self) != type(__value):
            return False

        if self.val != __value.val:
            return False

        n1 = self.next
        n2 = __value.next

        return n1 == n2

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

    def __str__(self):
        if self.next:
            add = str(self.next)
        return f'ListNode({self.val}, next={add if self.next else "None"})'

    def __repr__(self) -> str:
        return str(self)


class Solution:
    def getIntersectionNode_nestedloop(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        if headA is headB:
            return headA

        curA = headA
        curB = headB
        while curA:
            while curB:
                if curA is curB:
                    return curA
                curB = curB.next
            curB = headB
            curA = curA.next

    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        visited = set()
        curA = headA
        while curA:
            visited.add(id(curA))
            curA = curA.next

        curB = headB
        while curB:
            if id(curB) in visited:
                return curB
            curB = curB.next

    def getIntersectionNode_optimal(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        l1, l2 = 0, 0

        curA = headA
        while curA:
            l1 += 1
            curA = curA.next

        curB = headB
        while headB:
            l2 += 1
            curB = curB.next

        d = l1 - l2

        if d < 0:
            d = -d
            headA, headB = headB, headA


class IntersectionTest(unittest.TestCase):
    def test_identical_heads(self):
        s = Solution()
        l = ListNode(1)
        intersection = s.getIntersectionNode(l, l)

        self.assertEqual(intersection, l)

    def test_different_heads(self):
        s = Solution()
        l1 = ListNode(1)
        l2 = ListNode(1)
        intersection = s.getIntersectionNode(l1, l2)

        self.assertIsNone(intersection)

    def test_chained_heads(self):
        s = Solution()
        l1 = ListNode(1)
        l2 = ListNode(2)
        l1.next = l2

        intersection = s.getIntersectionNode(l1, l2)
        self.assertIs(intersection, l2)

        # must be commutative
        intersection = s.getIntersectionNode(l2, l1)
        self.assertIs(intersection, l2)

    def test_common_single_tail(self):
        s = Solution()
        l1 = ListNode(1)
        l2 = ListNode(2)
        tail = ListNode(3)
        l1.next = tail
        l2.next = tail

        intersection = s.getIntersectionNode(l1, l2)
        self.assertIs(intersection, tail)

    def test_common_multi_tail(self):
        s = Solution()
        l1 = ListNode(1)
        l2 = ListNode(2)
        tail = ListNode(3, ListNode(4, ListNode(5)))

        l1.next = tail
        l2.next = tail

        intersection = s.getIntersectionNode(l1, l2)
        self.assertIs(intersection, tail)


if __name__ == "__main__":
    unittest.main()
