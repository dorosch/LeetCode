class Logger:
    def __init__(self):
        self.cache = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.cache:
            if timestamp - self.cache[message] >= 10:
                self.cache[message] = timestamp

                return True

            return False

        self.cache[message] = timestamp

        return True


if __name__ == "__main__":
    logger = Logger()
    assert logger.shouldPrintMessage(1, "foo")
    assert logger.shouldPrintMessage(2, "bar")
    assert not logger.shouldPrintMessage(3, "foo")
    assert not logger.shouldPrintMessage(8, "bar")
    assert not logger.shouldPrintMessage(10, "foo")
    assert logger.shouldPrintMessage(11, "foo")
