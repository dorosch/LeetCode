from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_value = None
        min_value = prices[0]

        for price in prices[1:]:
            if max_value is None or price > max_value:
                max_value = price

            if price < min_value:
                min_value = price
                max_value = None

            if max_value is not None:
                if (max_value - min_value) > profit:
                    profit = max_value - min_value

        if max_value is not None:
            if (max_value - min_value) > profit:
                profit = max_value - min_value

        return profit


if __name__ == '__main__':
    assert Solution().maxProfit([2, 4, 1]) == 2
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert Solution().maxProfit([2, 1, 2, 1, 0, 1, 2]) == 2
