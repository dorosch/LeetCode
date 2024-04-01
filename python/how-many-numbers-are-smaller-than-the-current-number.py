from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # One line solution:
        # return [sorted(nums).index(i) for i in nums]

        counter = {}

        for index, value in enumerate(sorted(nums)):
            if value not in counter:
                counter[value] = index

        return [counter[num] for num in nums]


if __name__ == "__main__":
    assert Solution().smallerNumbersThanCurrent([7, 7, 7, 7]) == [0, 0, 0, 0]
    assert Solution().smallerNumbersThanCurrent([6, 5, 4, 8]) == [2, 1, 0, 3]
    assert Solution().smallerNumbersThanCurrent([8, 1, 2, 2, 3]) == [4, 0, 1, 1, 3]
