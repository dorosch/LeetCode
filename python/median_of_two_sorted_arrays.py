from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2

        if (len(A) > len(B)):
            A, B = B, A

        left, right = 0, len(A) - 1
        total_len = len(A) + len(B)
        half = total_len // 2

        while True:
            i = (left + right) // 2
            j = half - i - 2

            a_left = A[i] if i >= 0 else -float('inf')
            a_right = A[i + 1] if i + 1 < len(A) else float('inf')

            b_left = B[j] if j >= 0 else -float('inf')
            b_right = B[j + 1] if j + 1 < len(B) else float('inf')

            if a_left <= b_right and b_left < a_right:
                if total_len % 2:
                    return min(a_right, b_right)

                return (max(a_left, b_left) + min(a_right, b_right)) / 2

            elif a_left > b_right:
                right = i - 1
            else:
                left = i + 1


if __name__ == '__main__':
    assert Solution().findMedianSortedArrays([1, 2, 3, 4], [1, 2, 3, 4, 5, 6, 7, 8]) == 3.5
    assert Solution().findMedianSortedArrays([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8]) == 4.0
    assert Solution().findMedianSortedArrays([], [1]) == 1.0
    assert Solution().findMedianSortedArrays([], [1, 2, 3]) == 2.0
    assert Solution().findMedianSortedArrays([2], []) == 2
    assert Solution().findMedianSortedArrays([1, 3], [2]) == 2.0
    assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert Solution().findMedianSortedArrays([0, 0], [0, 0]) == 0
