class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        def solIsPalindrome(head, curr):
            if not curr:
                return False, None, None

            if not curr.next:
                if head.val == curr.val:
                    return True, head.next, True
                else:
                    return False, head.next, False

            bl, next_head, seek = solIsPalindrome(head, curr.next)

            if not seek: # cond 1
                return bl, None, None

            if next_head == curr or next_head.next == curr: # cond 2
                seek = False

            # code will runn successfully without condition 1 and 2

            if bl:
                if next_head.val == curr.val:
                    return True, next_head.next, seek
                else:
                    return False, next_head.next, False

            else:
                return False, None, None

        return solIsPalindrome(head, head)[0]