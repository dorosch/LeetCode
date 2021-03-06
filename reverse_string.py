from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


if __name__ == '__main__':
    string = ['h', 'e', 'l', 'l', 'o']
    Solution().reverseString(string)

    assert string == ['o', 'l', 'l', 'e', 'h']

    string = ['H', 'a', 'n', 'n', 'a', 'h']
    Solution().reverseString(string)

    assert string == ['h', 'a', 'n', 'n', 'a', 'H']
