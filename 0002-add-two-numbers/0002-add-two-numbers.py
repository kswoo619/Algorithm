# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = ListNode(0)
        pointer = result

        while(l1 or l2 or carry):
            first = l1.val if l1 else 0
            second = l2.val if l2 else 0

            tmp = first + second + carry
            num = tmp % 10
            carry = tmp // 10

            pointer.next = ListNode(num)
            pointer = pointer.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return result.next