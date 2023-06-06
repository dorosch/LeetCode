from random import choices
from string import ascii_lowercase, digits


class Codec:
    urls = {}
    values = ascii_lowercase + digits

    def encode(self, longUrl: str) -> str:
        while (
            tiny := ''.join(
                choices(self.values, k=len(self.urls) // len(self.values) + 1)
            )
        ) in self.urls:
            continue

        self.urls[tiny] = longUrl

        return tiny

    def decode(self, shortUrl: str) -> str:
        return self.urls[shortUrl]


if __name__ == '__main__':
    tiny_url = Codec()
    url = 'https://leetcode.com/problems/design-tinyurl'
    assert tiny_url.decode(tiny_url.encode(url)) == url

    url1 = 'https://leetcode.com/problems/design-tinyurl1'
    assert tiny_url.decode(tiny_url.encode(url1)) == url1
