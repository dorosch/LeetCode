from typing import List


class Solution:
    data = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) < 2:
            return self.data.get(digits, [])

        values = [self.data[digit] for digit in digits]

        result = []
        pointer = len(digits) - 1

        while pointer > 0:
            temp = []
            left, right = values[pointer - 1], result or values[pointer]
            for l in left:
                for r in right:
                    temp.append(l + r)

            result = temp
            pointer -= 1

        return result


if __name__ == '__main__':
    assert Solution().letterCombinations('') == []
    assert Solution().letterCombinations('2') == ['a', 'b', 'c']
    assert Solution().letterCombinations('23') == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    assert Solution().letterCombinations('234') == ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei', 'bfg', 'bfh', 'bfi', 'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']
