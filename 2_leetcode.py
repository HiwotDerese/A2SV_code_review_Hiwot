# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        
        
        head = ListNode()
        dummy = head
        _sum = 0
        
        while l1 or l2 or _sum:
            if l1:
                _sum += l1.val
                l1 = l1.next
            if l2:
                _sum += l2.val
                l2 = l2.next
                
            head.next = ListNode(_sum % 10)
            head = head.next
            
            _sum = _sum // 10

        return dummy.next
        
