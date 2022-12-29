import unittest


class TimeMap:

    def __init__(self) -> None:
        self.store = {}

    def set(self, key, value, timestamp):
        if key in self.store:
            self.store[key].append((timestamp, value))
        else:
            self.store[key] = [(timestamp, value)]

    def get(self, key, timestamp):
        if key not in self.store:
            return ''
        value_log = self.store[key]
        # TODO: replace with binary search
        low, high = 0, len(value_log) - 1
        mid = (low + high) // 2
        while low != mid:
            (t, v) = value_log[mid]
            if timestamp == t:
                return v
            elif timestamp > t:  # mid happened earlier that timestamp.
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2

        (t_hi, v_hi) = value_log[high]
        (t_lo, v_lo) = value_log[low]
        if timestamp >= t_hi:
            return v_hi
        elif timestamp >= t_lo:
            return v_lo
        return ''


class TimeBasedKVStoreTest(unittest.TestCase):
    def test_instantiate(self):
        store = TimeMap()
        self.assertIsNotNone(store)

    def test_set_get_same_timestamp(self):
        store = TimeMap()
        key, value, timestamp = "foo", "bar", 1
        store.set(key, value, timestamp)
        self.assertEqual(value, store.get(key, timestamp))

    def test_set_now_get_later(self):
        store = TimeMap()
        key, value = "foo", "bar"
        set_timestamp, get_timestamp = 1, 2
        store.set(key, value, set_timestamp)
        self.assertEqual(value, store.get(key, get_timestamp))

    def test_set_now_get_in_past(self):
        store = TimeMap()
        key, value = "foo", "bar"
        set_timestamp, get_timestamp = 2, 1
        store.set(key, value, set_timestamp)
        self.assertEqual('', store.get(key, get_timestamp))

    def test_many_sets_get_latest(self):
        store = TimeMap()
        key, value = "foo", "bar"
        store.set(key, value, 1)
        store.set(key, value + value, 2)
        self.assertEqual(value + value, store.get(key, 2))

    def test_many_sets_get_first(self):
        store = TimeMap()
        key, value = "foo", "bar"
        store.set(key, value, 1)
        store.set(key, value + value, 2)
        self.assertEqual(value, store.get(key, 1))

    def test_set_many_keys(self):
        store = TimeMap()
        k1, v1 = "foo", "bar"
        k2, v2 = "foo2", "bar2"
        store.set(k1, v1, 1)
        store.set(k2, v2, 1)
        self.assertEqual(v2, store.get(k2, 2))


if __name__ == '__main__':
    USE_OWN_TRACE = False
    if not USE_OWN_TRACE:
        unittest.main()
    else:
        print('-------------')
        s = TimeMap()
        key = 'foo'
        values = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        for (idx, value) in enumerate(values):
            s.set(key, value, idx)
        print(f"{'Timestamp' :^15}|{'Expected' :^10}|{'Actual' :^10}|{'OK' :^8}")
        for (idx, value) in enumerate(values):
            found = s.get(key, idx)

            print(f'{idx:^15}|{value :^10}|{found :^10}| {str(found == value) :<8}')
