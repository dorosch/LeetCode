class Solution:
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900
    }

    def romanToInt(self, s: str) -> int:
        result = 0
        position = len(s) - 1

        while position >= 0:
            symbol = s[position]

            if position > 0:
                if (symbol in ('V', 'X') and s[position - 1] == 'I') or \
                        (symbol in ('L', 'C') and s[position - 1] == 'X') or \
                        (symbol in ('D', 'M') and s[position - 1] == 'C'):
                    result += self.roman[s[position - 1: position + 1]]
                    position -= 2
                else:
                    result += self.roman[symbol]
                    position -= 1
            else:
                result += self.roman[symbol]
                break

        return result


if __name__ == '__main__':
    assert Solution().romanToInt('III') == 3
    assert Solution().romanToInt('LVIII') == 58
    assert Solution().romanToInt('MCMXCIV') == 1994
