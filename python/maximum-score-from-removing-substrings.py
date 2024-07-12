class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_substr(string, substr, points):
            score = 0
            stack = []
            left, right = substr[0], substr[1]

            for char in string:
                if stack and stack[-1] == left and char == right:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)

            return ''.join(stack), score

        if x > y:
            string, score_x = remove_substr(s, "ab", x)
            _, score_y = remove_substr(string, "ba", y)
        else:
            string, score_y = remove_substr(s, "ba", y)
            _, score_x = remove_substr(string, "ab", x)

        return score_x + score_y



if __name__ == "__main__":
    assert Solution().maximumGain(s = "cdbcbbaaabab", x = 4, y = 5) == 19
    assert Solution().maximumGain(s = "aabbaaxybbaabb", x = 5, y = 4) == 20
