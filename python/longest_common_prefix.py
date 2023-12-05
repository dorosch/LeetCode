from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ''

        for letters in zip(*strs):
            value = set(letters)

            if len(value) > 1:
                break

            result += value.pop()

        return result


if __name__ == '__main__':
    assert Solution().longestCommonPrefix(["flower", "flow", "flight"]) == 'fl'
    assert not Solution().longestCommonPrefix(["dog", "racecar", "car"])
