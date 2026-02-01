# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:

        def reverse_list(start, end):
            node = start.next
            prev_node = None
            tail = start.next
            while node != end:
                next_node = node.next
                node.next = prev_node
                prev_node = node
                node = next_node

            start.next = prev_node
            if tail:
                tail.next = node
            return tail

        def mutate_list():
            dummy = ListNode(None, head)
            end = None
            start = dummy
            end = dummy
            diff = right - left
            count = 0
            while count < right + 1:

                if count < left - 1:
                    start = start.next
                if count < right + 1:
                    if end:
                        end = end.next
                count += 1

            reverse_list(start, end)

            return dummy.next

        def mutate_list():
            dummy = ListNode(None, head)
            count = 0
            prev = dummy
            while count < left - 1:
                prev = prev.next
                count += 1

            curr = prev.next
            print("curr", curr.val)
            for i in range(right - left):
                node_to_move = curr.next
                print("node_to_move", node_to_move.val, curr.val)
                curr.next = node_to_move.next
                node_to_move.next = prev.next
                prev.next = node_to_move

            return dummy.next

        def print_linked_list(head):
            print("------linked list")
            nums = []
            while head:
                nums.append(head.val)
                head = head.next
            print(nums)

        def mutate_list():
            dummy = ListNode(None, head)
            count = 0
            prev = dummy
            while count < left - 1:
                prev = prev.next
                count += 1

            curr = prev.next
            print("curr", curr.val)
            for i in range(right - left):
                print_linked_list(dummy)
                node_to_move = curr.next
                print("node_to_move", node_to_move.val, curr.val)
                curr.next = node_to_move.next
                node_to_move.next = prev.next
                prev.next = node_to_move
            print_linked_list(dummy)
            return dummy.next


        def mutate_list(left,right):
            dummy = ListNode(None, head)
            count = 0
            prev = dummy

            while count < left-1:
                prev = prev.next
                count+=1

            left_node = prev.next
            for i in range(right-left):
                right = left_node.next
                remaining = right.next
                right.next = prev.next
                left_node.next = remaining
                prev.next = right

            return dummy.next






        return mutate_list(left,right)
