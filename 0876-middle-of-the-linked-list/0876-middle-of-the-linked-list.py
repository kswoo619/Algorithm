# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        end = 0
        flag = 0
        pointer = head
        
        while pointer:
            pointer = pointer.next
            end += 1
        
        end //= 2
        
        pointer = head
        while pointer:
            if(flag == end):
                return pointer
            flag += 1
            pointer = pointer.next