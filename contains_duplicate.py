from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_map = {}
        has_duplicates = False

        for num in nums:
            if num in hash_map:
                return True

            hash_map[num] = None

        return has_duplicates


if __name__ == '__main__':
    assert Solution().containsDuplicate([1, 2, 3, 1])
    assert not Solution().containsDuplicate([1, 2, 3, 4])
    assert Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
