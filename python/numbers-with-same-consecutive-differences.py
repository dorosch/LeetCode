from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        results = []

        def recursion(number: int, level: int) -> int:
            numbers = []
            
            tail_digit = number % 10

            if 0 <= tail_digit + k <= 9:
                numbers.append(int(f'{number}{tail_digit + k}'))  

            if 0 <= tail_digit - k <= 9:
                numbers.append(int(f'{number}{tail_digit - k}'))

            if level == n:
                results.extend(set(numbers))
            else:
                for number in set(numbers):
                    recursion(number, level + 1)

        for i in range(1, 10):
            recursion(i, 2)

        return results


if __name__ == '__main__':
    assert Solution().numsSameConsecDiff(n=3, k=7) == [181, 292, 707, 818, 929]
