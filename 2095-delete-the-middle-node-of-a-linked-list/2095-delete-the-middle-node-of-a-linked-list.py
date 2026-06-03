# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=low = head
        end = head

        if not head.next:
            return None

        while end and end.next:
            prev = low
            low = low.next
            end = end.next
            if end.next:
                end = end.next

        prev.next = low.next

        return head


class Solutionn:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return None

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

        return head

        