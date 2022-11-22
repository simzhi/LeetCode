from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry = 0) -> Optional[ListNode]:

        val = l1.val + l2.val + carry
        print("val: ", val)
        carry = val // 10
        print("carry: ", carry)
        result = ListNode(val % 10)
        print("result: ", result.val, result.next)

        if (l1.next != None or l2.next != None or carry != 0):
            if l1.next == None:
                l1.next = ListNode(val=0)
            if l2.next == None:
                l2.next = ListNode(val=0)
            result.next = self.addTwoNumbers(l1.next, l2.next, carry)
        return result





l1 = ListNode(val=9, next = ListNode(val = 9, next = ListNode(val = 9, next = None)))
l2 = ListNode(val=5, next = ListNode(val = 6, next = ListNode(val = 4, next = None)))
print([l1.val, l1.next.val,l1.next.next.val])
print([l2.val, l2.next.val,l2.next.next.val])
carry = 0
res = Solution().addTwoNumbers(l1, l2, carry)
print([res.val, res.next.val, res.next.next.val, res.next.next.next.val, res.next.next.next.next])
