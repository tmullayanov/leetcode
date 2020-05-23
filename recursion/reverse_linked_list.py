class ListNode:
    def __init__(self, val=0, nextNode=None):
        self.val = val
        self.next = nextNode


def printList(head):
    vals = []
    cur = head
    while cur:
        vals.append(cur.val)
        cur = cur.next
    print(' -> '.join(str(i) for i in vals))


class Solution:
    def reverseList(self, head):
        if not head:
            return None

        prev, cur, next = None, head, None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        return prev

    def reverseListRecur(self, head):
        if not head or not head.next:
            return head

        rest = self.reverseListRecur(head.next)
        head.next.next = head
        head.next = None

        return rest


if __name__ == '__main__':
    h = ListNode(5, ListNode(6, ListNode(7, ListNode(8))))
    printList(h)

    #new_h = Solution().reverseList(h)
    new_h = Solution().reverseListRecur(h)
    printList(new_h)
