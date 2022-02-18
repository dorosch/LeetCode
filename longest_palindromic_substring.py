class Solution:
    length = start = 0

    def longestPalindrome(self, s):
        for index in range(len(s)):
            self.expandFromCenter(s, index, index)
            self.expandFromCenter(s, index, index + 1)

        return s[self.start: self.start + self.length]

    def expandFromCenter(self, s, left, right):
        while left > -1 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        if self.length < right - left - 1:
            self.start = left + 1
            self.length = right - left - 1


if __name__ == '__main__':
    assert Solution().longestPalindrome('babad') == 'bab'
    assert Solution().longestPalindrome('cbbd') == 'bb'
