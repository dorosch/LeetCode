class Solution:
    def countVowelStrings(self, n: int) -> int:
        return ((n + 1) * (n + 2) * (n + 3) * (n + 4)) // 24


if __name__ == '__main__':
    assert Solution().countVowelStrings(1) == 5
    assert Solution().countVowelStrings(2) == 15
