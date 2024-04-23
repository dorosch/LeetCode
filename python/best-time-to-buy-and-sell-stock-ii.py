from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        profit = []

        for i in range(1, len(prices)):
            profit.append(max(0, prices[i] - prices[i-1]))

        return sum(profit)


if __name__ == "__main__":
    assert Solution().maxProfit([1]) == 0
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
    assert Solution().maxProfit([1, 2, 3, 4, 5]) == 4
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 7
