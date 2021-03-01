class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l3 = ListNode()
        carry = 0
        while carry or l1 or l2:
            val = carry
            if l1: l1, val = l1.next, l1.val + val
            if l2: l2, val = l2.next, l2.val + val
            carry, val = divmod(val, 10)
            l3.next = l3 = ListNode(val)
        return head.next
