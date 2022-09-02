class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0

        for fast, value in enumerate(nums):
            if value != val:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

        return slow
