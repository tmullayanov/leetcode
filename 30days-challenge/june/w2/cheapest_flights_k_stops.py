class Solution:
    def findCheapestPrice(self, n, flights, src, dst, stops):
        prices = [float('inf') for _ in range(n)]
        hops = [0 for _ in range(n)]
        prices[src] = 0
        # bellman-ford
        for _ in range(stops + 1):
            old_prices = prices[::]
            for (_from, _to, _price) in flights:
                if prices[_to] > old_prices[_from] + _price:
                    prices[_to] = old_prices[_from] + _price
        return prices[dst] if prices[dst] != float('inf') else -1


if __name__ == '__main__':
    print(Solution().findCheapestPrice(
        3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
        0, 2, 1
    ))  # 200
    print(Solution().findCheapestPrice(
        3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]],
        0, 2, 0
    ))  # 500
    print(Solution().findCheapestPrice(
        4, [[0, 1, 100], [1, 2, 100], [0, 2, 500], [2, 3, 100]],
        0, 2, 0
    ))  # 500
    print(Solution().findCheapestPrice(
        4,
        [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]],
        src=0,
        dst=3,
        stops=1
    ))
