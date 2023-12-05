from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pointers = {item: item.val for item in lists if item}

        if not pointers:
            return None

        result = ListNode()
        pointer = result

        while pointers:
            min_pointer = min(pointers, key=pointers.get)
            pointer.val = min_pointer.val

            if min_pointer.next:
                del pointers[min_pointer]
                pointers[min_pointer.next] = min_pointer.next.val
            else:
                del pointers[min_pointer]

            if pointers:
                pointer.next = ListNode()
                pointer = pointer.next

        return result


if __name__ == '__main__':
    assert Solution().mergeKLists([None])
    assert Solution().mergeKLists([ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))])
