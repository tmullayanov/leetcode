class Solution:
    def change(self, amount, coins):
        dp = [[0] * (amount + 1) for coin_idx in range(len(coins) + 1)]
        for coin_idx in range(len(coins) + 1):
            for cur_amount in range(amount + 1):
                if cur_amount == 0:
                    # one way to represent zero with any coins
                    dp[coin_idx][cur_amount] = 1
                elif coin_idx == 0:
                    # no way to represent any amount with no coins
                    dp[coin_idx][cur_amount] = 0

        for coin_idx in range(1, len(coins) + 1):
            for cur_amount in range(1, amount + 1):
                if coins[coin_idx - 1] <= cur_amount:
                    dp[coin_idx][cur_amount] = dp[coin_idx - 1][cur_amount] + \
                        dp[coin_idx][cur_amount-coins[coin_idx - 1]]
                else:
                    dp[coin_idx][cur_amount] = dp[coin_idx - 1][cur_amount]
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().change(5, [1, 2, 5]))  # 4
    print(Solution().change(3, [2]))  # 0
    print(Solution().change(10, [10]))  # 1
    print(Solution().change(0, []))  # 1
    print(Solution().change(500, [3, 5, 7, 8, 9, 10, 11]))
