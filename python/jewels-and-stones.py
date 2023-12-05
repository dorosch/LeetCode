class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(1 for stone in stones if stone in jewels)


if __name__ == '__main__':
    assert Solution().numJewelsInStones('z', 'ZZ') == 0
    assert Solution().numJewelsInStones('aA', 'aAAbbbb') == 3
