from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        result = ListNode()
        pointer = result

        left, right = list1, list2

        while left or right:
            if left and not right:
                pointer.val = left.val
                left = left.next
            elif right and not left:
                pointer.val = right.val
                right = right.next
            else:
                if left.val <= right.val:
                    pointer.val = left.val
                    left = left.next
                else:
                    pointer.val = right.val
                    right = right.next

            if left or right:
                pointer.next = ListNode()
                pointer = pointer.next

        return result


if __name__ == '__main__':
    assert Solution().mergeTwoLists(ListNode(), ListNode()) == ListNode()
    assert Solution().mergeTwoLists(ListNode(), ListNode(0)) == [0]
    assert Solution().mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))) == [1, 1, 2, 3, 4]
