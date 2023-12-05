class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal and len(set(s)) < len(s):
            return True

        pairs = [(a, b) for a, b in zip(s, goal) if a != b]

        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]


if __name__ == '__main__':
    assert Solution().buddyStrings('ab', 'ba')
    assert not Solution().buddyStrings('ab', 'ab')
    assert Solution().buddyStrings('aa', 'aa')
