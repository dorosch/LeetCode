# Given an array of integers arr, return true if and
# only if it is a valid mountain array.
#
# Recall that arr is a mountain array if and only if:
#     arr.length >= 3
#     There exists some i with 0 < i < arr.length - 1 such that:
#         arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
#         arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        target_index = None

        for i in range(1, len(arr) - 1):
            if (i + 1) <= len(arr) - 1:
                if arr[i] == arr[i - 1]:
                    return False

                if arr[i-1] < arr[i] and arr[i] > arr[i + 1]:
                    target_index = i

        if target_index is None:
            return False

        for i in range(1, target_index + 1):
            if arr[i] < arr[i - 1]:
                return False

        for i in range(target_index + 1, len(arr)):
            if arr[i] > arr[i - 1]:
                return False

        return True


if __name__ == '__main__':
    assert not Solution().validMountainArray([2, 1])
    assert not Solution().validMountainArray([3, 5, 5])
    assert Solution().validMountainArray([0, 3, 2, 1])
