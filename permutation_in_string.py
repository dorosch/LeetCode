from collections import Counter, defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length = len(s1) - 1
        window = defaultdict(int)
        counter = dict(Counter(s1))

        for index, value in enumerate(s2):
            window[value] += 1

            if window == counter:
                return True

            if index >= length:
                key = s2[index - length]
                window[key] -= 1

                if window[key] == 0:
                    del window[key]

        return False


if __name__ == '__main__':
    assert Solution().checkInclusion('ab', 'cbad')
    assert Solution().checkInclusion('ab', 'eidbaooo')
    assert not Solution().checkInclusion('ab', 'eidboaoo')
