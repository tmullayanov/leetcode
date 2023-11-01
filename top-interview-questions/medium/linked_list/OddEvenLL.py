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


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        odds_head = head
        odd = odds_head

        evens_head = None
        even = evens_head

        is_odd = True

        _next = head.next

        while _next:
            if is_odd:
                if not evens_head:
                    evens_head = _next
                    even = _next
                else:
                    even.next = _next
                    even = even.next
            else:
                odd.next = _next
                odd = odd.next

            is_odd = not is_odd
            _next = _next.next

        if even:
            even.next = None
        odd.next = evens_head

        return odds_head


class OddEvenLL(unittest.TestCase):
    def test_ll_to_list(self):
        one = ListNode(1)
        self.assertEqual(one.toList(), [1])
        ll = ListNode(1, ListNode(2))
        self.assertEqual(ll.toList(), [1, 2])

    def test_make_ll_from_list(self):
        l0 = [1]
        self.assertEqual(ListNode.fromList(l0), ListNode(1))
        l1 = [1, 2]
        expected = ListNode(1, ListNode(2))
        self.assertEqual(ListNode.fromList(l1), expected)

    def test_ll_preserves_list(self):
        l1 = [1, 2, 3]
        self.assertEqual(l1, ListNode.fromList(l1).toList())

    def test_none(self):
        s = Solution()
        self.assertIsNone(s.oddEvenList(None))

    def test_single_elem(self):
        s = Solution()
        h = ListNode(1)
        self.assertEqual(s.oddEvenList(h), h)

    def test_two_nodes(self):
        s = Solution()
        h = ListNode.fromList([1, 2])
        self.assertEquals([1, 2], s.oddEvenList(h).toList())

    def test_three_nodes(self):
        s = Solution()
        input = [1, 2, 3]
        au = [1, 3, 2]
        self.assertEquals(au, s.oddEvenList(ListNode.fromList(input)).toList())

    def test_random_lists(self):
        s = Solution()

        input = list(range(10))
        au = list(range(0, 10, 2)) + list(range(1, 10, 2))

        self.assertEqual(au, s.oddEvenList(ListNode.fromList(input)).toList())


if __name__ == "__main__":
    unittest.main()
