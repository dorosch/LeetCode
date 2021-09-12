class Node:
    __slots__ = 'start', 'end', 'left', 'right'

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None

    def insert(self, node) -> bool:
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True

            return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True

            return self.left.insert(node)

        return False


class MyCalendar(object):
    def __init__(self):
        self.root = None

    def book(self, start, end) -> bool:
        if self.root is None:
            self.root = Node(start, end)
            return True

        return self.root.insert(Node(start, end))


if __name__ == '__main__':
    calendar = MyCalendar()

    assert calendar.book(10, 20)
    assert calendar.book(50, 60)
    assert not calendar.book(5, 15)
    assert calendar.book(5, 10)
