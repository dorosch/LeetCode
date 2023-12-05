from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        index = len(nums) - 1

        if not index:
            return [nums]

        results = []

        while index >= 0:
            value = nums[index]
            for result in self.permute(nums[:index] + nums[index + 1:]):
                results += [[value] + result]
            index -= 1

        return results


if __name__ == '__main__':
    assert Solution().permute([1]) == [
        [1]
    ]
    assert Solution().permute([0, 1]) == [
        [1, 0], [0, 1]
    ]
    assert Solution().permute([1, 2, 3]) == [
        [3, 2, 1], [3, 1, 2], [2, 3, 1], [2, 1, 3], [1, 3, 2], [1, 2, 3]
    ]
