class Solution:
    roman_symbols_values = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }

    def intToRoman(self, num: int) -> str:
        roman_numeral = ""

        for symbol, value in self.roman_symbols_values.items():
            while num >= value:
                roman_numeral += symbol
                num -= value

        return roman_numeral


if __name__ == "__main__":
    assert Solution().intToRoman(3) == "III"
    assert Solution().intToRoman(58) == "LVIII"
    assert Solution().intToRoman(1994) == "MCMXCIV"
