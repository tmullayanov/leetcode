import unittest
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


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        pointer1 = list1
        pointer2 = list2

        fakeHead = ListNode(float("-inf"))  # real head is fakeHead.next
        cur = fakeHead
        while pointer1 and pointer2:
            if pointer1.val > pointer2.val:
                cur.next = ListNode(pointer2.val)
                pointer2 = pointer2.next
            else:
                cur.next = ListNode(pointer1.val)
                pointer1 = pointer1.next
            cur = cur.next
        cur.next = pointer2 if pointer2 else pointer1

        return fakeHead.next


class MergeLLTest(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.s = Solution()

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

    def test_listnode_eql(self):
        n1 = ListNode(0)
        n2 = ListNode(0)
        self.assertTrue(n1 == n2)

        n1.next = ListNode(1)
        self.assertFalse(n1 == n2)

        n2.next = ListNode(1)
        self.assertTrue(n1 == n2)

        self.assertNotEqual(ListNode(0), ListNode(1))

    def test_ll_to_str(self):
        n1 = ListNode(0, ListNode(1))

        self.assertEqual(str(n1), "0, 1")

        self.assertEqual(str(ListNode(None)), "")

    def test_merge_empty_lists(self):
        empty1 = None
        empty2 = None

        res = self.s.mergeTwoLists(empty1, empty2)
        self.assertIsNone(res)

    def test_merge_with_empty(self):
        l1 = ListNode(0)
        empty = None

        self.assertEqual(self.s.mergeTwoLists(l1, empty), l1)
        self.assertEqual(self.s.mergeTwoLists(empty, l1), l1)

    def test_two_1element_lists(self):
        self.assertEqual(
            self.s.mergeTwoLists(ListNode(1), ListNode(2)).toList(), [1, 2]
        )
        self.assertEqual(
            self.s.mergeTwoLists(ListNode(2), ListNode(1)).toList(), [1, 2]
        )

    def test_2element_lists(self):
        self.assertEqual(
            self.s.mergeTwoLists(
                ListNode.fromList([1, 2]), ListNode.fromList([3])
            ).toList(),
            [1, 2, 3],
        )
        self.assertEqual(
            self.s.mergeTwoLists(
                ListNode.fromList([1, 2]), ListNode.fromList([3, 4])
            ).toList(),
            [1, 2, 3, 4],
        )

        self.assertEqual(
            self.s.mergeTwoLists(
                ListNode.fromList([1, 3]), ListNode.fromList([2])
            ).toList(),
            [1, 2, 3],
        )

        self.assertEqual(
            self.s.mergeTwoLists(
                ListNode.fromList([2, 3]), ListNode.fromList([1])
            ).toList(),
            [1, 2, 3],
        )

        self.assertEqual(
            self.s.mergeTwoLists(ListNode(10), ListNode.fromList([1, 2, 3])).toList(),
            [1, 2, 3, 10],
        )

        self.assertEqual(
            self.s.mergeTwoLists(
                ListNode(10), ListNode.fromList([1, 2, 3, 30])
            ).toList(),
            [1, 2, 3, 10, 30],
        )

    def test_random_lists(self):
        self.assertEqual(
            self.s.mergeTwoLists(
                ListNode.fromList([1, 3, 5, 6, 10]), ListNode.fromList([1, 2, 4, 5, 6])
            ).toList(),
            [1, 1, 2, 3, 4, 5, 5, 6, 6, 10],
        )


if __name__ == "__main__":
    unittest.main()
