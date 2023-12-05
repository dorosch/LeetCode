from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        result = []
        left_a = left_b = 0

        while left_a + left_b < m + n:
            if left_a < m and left_b < n:
                a, b = nums1[left_a], nums2[left_b]

                if a <= b:
                    result.append(a)
                    left_a += 1
                else:
                    result.append(b)
                    left_b += 1
            elif left_a < m:
                result.append(nums1[left_a])
                left_a += 1
            elif left_b < n:
                result.append(nums2[left_b])
                left_b += 1

        nums1[:] = result


if __name__ == '__main__':
    a = [1, 2, 3, 0, 0, 0]
    b = [2, 5, 6]
    Solution().merge(a, 3, b, 3)

    assert a == [1, 2, 2, 3, 5, 6]
