# use functools.lru_cache in real world
import collections


class LRUCache0:

    def __init__(self, capacity):
        self.capacity = capacity
        self.keysDeque = []
        self.store = {}

    def get(self, key):
        if key in self.store:
            self.keysDeque.remove(key)
            self.keysDeque.append(key)
            return self.store[key]
        return -1

    def put(self, key, value):
        if key in self.store:
            self.keysDeque.remove(key)

        if len(self.keysDeque) >= self.capacity:
            last = self.keysDeque.pop(0)
            self.store.pop(last)
        self.keysDeque.append(key)
        self.store[key] = value


class LRUCache:
    def __init__(self, capacity):
        self.store = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        val = self.store.get(key)
        if val:
            self.store.move_to_end(key)
            return val
        return -1

    def put(self, key, val):
        if self.store.get(key):
            self.store.move_to_end(key)
        elif len(self.store) == self.capacity:
            self.store.popitem(last=False)
        self.store[key] = val


if __name__ == '__main__':
    obj = LRUCache(2)
    obj.put(1, 1)
    obj.put(2, 2)
    print(obj.get(1))  # expected 1
    obj.put(3, 10)
    print(obj.get(2))  # expected -1

    obj.put(5, 1)
    obj.put(5, 2)
    print(obj.get(5))
