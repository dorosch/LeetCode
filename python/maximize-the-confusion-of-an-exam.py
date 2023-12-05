class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def solve(option: str) -> int:
            maximum = -1
            steps = 0
            index = 0

            for position, value in enumerate(answerKey):
                if value != option:
                    steps += 1

                while steps > k:
                    if answerKey[index] != option:
                        steps -= 1

                    index += 1

                maximum = max(position - index + 1, maximum)

            return maximum

        return max(solve('T'), solve('F'))


if __name__ == '__main__':
    assert Solution().maxConsecutiveAnswers('TFFT', 1) == 3
    assert Solution().maxConsecutiveAnswers('TTFF', 2) == 4
    assert Solution().maxConsecutiveAnswers('TTFTTFTT', 1) == 5
