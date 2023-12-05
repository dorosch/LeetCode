class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(map(lambda x: x[::-1], s.split(' ')))


if __name__ == '__main__':
    assert Solution().reverseWords(
        "Let's take LeetCode contest"
    ) == "s'teL ekat edoCteeL tsetnoc"
    assert Solution().reverseWords("God Ding") == "doG gniD"
