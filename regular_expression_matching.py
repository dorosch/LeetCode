class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def regex(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            if i >= len(s) and j >= len(p):
                return True

            if j >= len(p):
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if (j + 1) < len(p) and p[j + 1] == '*':
                cache[(i, j)] = (
                    regex(i, j + 2) or (match and regex(i + 1, j))
                )

                return cache[(i, j)]

            if match:
                cache[(i, j)] = regex(i + 1, j + 1)

                return cache[(i, j)]

            return False

        return regex(0, 0)


if __name__ == '__main__':
    assert not Solution().isMatch('aa', 'a')
    assert Solution().isMatch('aa', 'a.')
    assert Solution().isMatch('aa', 'a*')
    assert Solution().isMatch('ab', '.*')
    assert Solution().isMatch('ab', '..')
    assert not Solution().isMatch('ab', 'b*')
    assert Solution().isMatch('ab', 'ab*')
    assert Solution().isMatch('aab', 'c*a*b')
