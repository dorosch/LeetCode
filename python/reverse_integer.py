class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2 ** 31 - 1 or x <= -2 ** 31:
            return 0

        string = str(x)

        if x >= 0:
            result = string[::-1]
        else:
            temp = string[1:]
            temp2 = temp[::-1]
            result = "-" + temp2

        if int(result) >= 2 ** 31 - 1 or int(result) <= -2 ** 31:
            return 0

        return int(result)


if __name__ == '__main__':
    assert Solution().reverse(123) == 321
    assert Solution().reverse(-123) == -321
    assert Solution().reverse(120) == 21
    assert Solution().reverse(0) == 0
