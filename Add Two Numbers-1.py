from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry = 0) -> Optional[ListNode]:

        val = l1.val + l2.val + carry
        carry = val // 10
        result = ListNode(val % 10)

        if (l1.next != None or l2.next != None or carry != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            result.next = self.addTwoNumbers(l1.next, l2.next, carry)
        return result





Liste = ListNode()
Solu = Solution()
l1 = [2,4,3]
l2 = [5,6,4]
carry = 0
print(Solu.addTwoNumbers(Optional[l1], Optional[l2], carry))