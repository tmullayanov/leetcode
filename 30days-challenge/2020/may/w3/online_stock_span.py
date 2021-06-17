class StockSpanner:

    def __init__(self):
        self.values = []
        self.indices_stack = []
        self.counter = 0

    def next(self, price: int) -> int:
        self.counter += 1

        while self.indices_stack and price >= self.values[self.indices_stack[-1] - 1]:
            self.indices_stack.pop()

        res = self.counter if not self.indices_stack else self.counter - \
            self.indices_stack[-1]
        self.values.append(price)
        self.indices_stack.append(self.counter)

        return res


if __name__ == '__main__':
    span = StockSpanner()
    print(span.next(100))
    print(span.next(80))
    print(span.next(60))
    print(span.next(70))
    print(span.next(60))
    print(span.next(75))
    print(span.next(85))
