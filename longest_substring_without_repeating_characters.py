class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sequence, start, length = set(), 0, 0

        for index, char in enumerate(s):
            while char in sequence:
                sequence.remove(s[start])
                start += 1

            sequence.add(char)
            length = max(length, index - start + 1)

        return length


if __name__ == '__main__':
    assert Solution().lengthOfLongestSubstring('aab') == 2
    assert Solution().lengthOfLongestSubstring('dvdf') == 3
    assert Solution().lengthOfLongestSubstring('abcabcbb') == 3
    assert Solution().lengthOfLongestSubstring('bbbbb') == 1
    assert Solution().lengthOfLongestSubstring('pwwkew') == 3
    assert Solution().lengthOfLongestSubstring('') == 0
