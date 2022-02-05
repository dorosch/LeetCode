from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k

        while left < right:
            middle = (left + right) // 2

            if x - arr[middle] > arr[middle + k] - x:
                left = middle + 1
            else:
                right = middle

        return arr[left: left + k]


if __name__ == '__main__':
    assert Solution().findClosestElements([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]
    assert Solution().findClosestElements([1, 2, 3, 4, 5], 4, -1) == [1, 2, 3, 4]
    assert Solution().findClosestElements([1], 1, 1) == [1]
    assert Solution().findClosestElements([0, 1, 1, 1, 2, 3, 6, 7, 8, 9], 9, 4) == [0, 1, 1, 1, 2, 3, 6, 7, 8]
