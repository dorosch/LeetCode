from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = []
        current_node = self

        while current_node is not None:
            result.append(current_node.val)
            current_node = current_node.next

        return str(result)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        current_node = result

        overflow = 0

        while l1 or l2:
            a = getattr(l1, 'val', 0)
            b = getattr(l2, 'val', 0)

            c = a + b + overflow
            overflow = c // 10

            current_node.val = c % 10

            l1 = getattr(l1, 'next', None)
            l2 = getattr(l2, 'next', None)

            if l1 or l2:
                current_node.next = ListNode()
                current_node = current_node.next
            else:
                if overflow != 0:
                    current_node.next = ListNode(val=overflow)

        return result


if __name__ == '__main__':
    l1 = ListNode(val=2, next=ListNode(val=4, next=ListNode(val=3)))
    l2 = ListNode(val=5, next=ListNode(val=6, next=ListNode(val=4)))

    print(Solution().addTwoNumbers(l1, l2))

    assert str(Solution().addTwoNumbers(l1, l2)) == str([7, 0, 8])

    l1 = ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9)))))))
    l2 = ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9, next=ListNode(val=9))))

    assert str(Solution().addTwoNumbers(l1, l2)) == str([8, 9, 9, 9, 0, 0, 0, 1])
