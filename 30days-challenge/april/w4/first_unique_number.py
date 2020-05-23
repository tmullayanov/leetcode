class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

    def remove(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __bool__(self):
        return self.head is not None and self.tail is not None

    def add(self, node):
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def remove(self, node):
        if self.head == node:
            self.head = node.next
        else:
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
        if self.tail == node:
            self.tail = node.prev


class FirstUnique:
    def __init__(self, nums):
        self.inDLL = {}
        self.repeated = {}
        self.dll = DLL()
        for n in nums:
            self.add(n)

    def showFirstUnique(self):
        if self.dll:
            return self.dll.head.val
        return -1

    def add(self, value):
        if self.repeated.get(value, False):
            return

        if not self.inDLL.get(value, False):
            # self.repeated[value] = false or None, we see element for the 1st time
            node = ListNode(value)
            self.dll.add(node)
            self.inDLL[value] = node
        else:
            self.dll.remove(self.inDLL[value])
            self.repeated[value] = True


if __name__ == '__main__':
    firstUnique = FirstUnique([7, 7, 7, 7, 7, 7])
    print(firstUnique.showFirstUnique())  # return -1
    firstUnique.add(7)  # the queue is now [7,7,7,7,7,7,7]
    firstUnique.add(3)  # the queue is now [7,7,7,7,7,7,7,3]
    print(firstUnique.showFirstUnique())  # return 3
    firstUnique.add(3)  # the queue is now [7,7,7,7,7,7,7,3,3]
    firstUnique.add(7)  # the queue is now [7,7,7,7,7,7,7,3,3,7]
    firstUnique.add(17)  # the queue is now [7,7,7,7,7,7,7,3,3,7,17]
    print(firstUnique.showFirstUnique())  # return 17
