class Solution:
    def isValid(self, s: str) -> bool:
        expected = []

        for symbol in s:
            if symbol in ('(', '[', '{'):
                expected.append(symbol)
            else:
                if symbol == ')':
                    symbol = '('
                elif symbol == ']':
                    symbol = '['
                elif symbol == '}':
                    symbol = '{'

                if not expected or symbol != expected.pop():
                    return False

        return not expected


if __name__ == '__main__':
    assert Solution().isValid('()')
    assert not Solution().isValid('([')
    assert Solution().isValid('()[]{}')
    assert Solution().isValid('([{}])')
    assert not Solution().isValid(']')
    assert not Solution().isValid('([)]')
