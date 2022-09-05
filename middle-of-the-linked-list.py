class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head

        while pointer and pointer.next:
            head = head.next
            pointer = pointer.next.next

        return head
