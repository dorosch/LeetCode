from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1

        while left <= right:
            middle = left + (right - left) // 2

            if letters[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return letters[left % len(letters)]


if __name__ == '__main__':
    assert Solution().nextGreatestLetter(["a", "b"], "z") == "a"
    assert Solution().nextGreatestLetter(["c", "f", "j"], "a") == "c"
    assert Solution().nextGreatestLetter(["c", "f", "j"], "c") == "f"
    assert Solution().nextGreatestLetter(["c", "f", "j"], "d") == "f"
