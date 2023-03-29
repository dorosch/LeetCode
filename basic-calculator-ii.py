class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        number = 0
        operation = '+'

        for symbol in s + '+':
            if symbol.isspace():
                continue
            elif symbol.isdigit():
                number = (number * 10) + int(symbol)
            else:
                if operation == '-':
                    stack.append(-number)
                elif operation == '+':
                    stack.append(number)
                elif operation == '*':
                    stack.append(stack.pop() * number)
                elif operation == '/':
                    stack.append(int(stack.pop() / number))

                number, operation = 0, symbol

        return sum(stack)


if __name__ == '__main__':
    assert Solution().calculate('3+2*2') == 7
    assert Solution().calculate(' 3/2 ') == 1
    assert Solution().calculate(' 3+5 / 2 ') == 5
