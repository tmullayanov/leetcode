import unittest
from typing import *
from list_node import ListNode


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return True

        n = 0
        cur = head

        while cur:
            n += 1
            cur = cur.next

        stack = []

        cur = head
        i = 0

        while cur:
            # 0 < i < n // 2 -> append
            # n is odd AND i == n // 2 + 1 - skip
            # n // 2 < i - pop and compare
            if i < n // 2:
                stack.append(cur)
            if i > n // 2 or (i == n // 2 and n % 2 == 0):
                top = stack.pop()
                if top.val != cur.val:
                    return False
            cur = cur.next
            i += 1

        return True

    def ll_length(self, l: ListNode) -> int:
        if l is None:
            return 0

        length = 0
        cur = l

        while cur:
            length += 1
            cur = cur.next

        return length


class LL_LengthTest(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_empty(self):
        l = ListNode.fromList([])
        self.assertEqual(0, self.s.ll_length(l))

    def test_lists(self):
        lists = [[1], [1, 2], [1, 2, 3], list(range(20))]

        for l in lists:
            self.assertEqual(len(l), self.s.ll_length(ListNode.fromList(l)))


class PalindromeTest(unittest.TestCase):

    def setUp(self) -> None:
        self.s = Solution()

    def test_empty(self):
        l = ListNode.fromList([])
        self.assertTrue(self.s.isPalindrome(l))

    def test_single_elem(self):
        l = ListNode.fromList([1])
        self.assertTrue(self.s.isPalindrome(l))

    def test_two_elem(self):
        falsy_list = ListNode.fromList([1, 2])
        self.assertFalse(self.s.isPalindrome(falsy_list))

        truthy_list = ListNode.fromList([1, 1])
        self.assertTrue(self.s.isPalindrome(truthy_list))

    def test_three_elem(self):
        non_palindrome = ListNode.fromList([1, 2, 3])
        self.assertFalse(self.s.isPalindrome(non_palindrome))

        palindrome = ListNode.fromList([0, 1, 0])
        self.assertTrue(self.s.isPalindrome(palindrome))

    def test_random_lists(self):
        test_data = [
            ([1, 2, 5, 4, 2], False),
            ([5, 4, 1, 2], False),
            ([1, 0, 1, 0, 1], True),
            ([1, 2, 2, 1], True),
        ]

        for raw_list, isPalindrome in test_data:
            head = ListNode.fromList(raw_list)
            self.assertEqual(isPalindrome, self.s.isPalindrome(head))


if __name__ == "__main__":
    unittest.main()
