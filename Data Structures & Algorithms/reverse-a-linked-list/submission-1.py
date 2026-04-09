# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 

        def reverse(head: Optional[ListNode]): 
            if not head: 
                return 
            nonlocal prev 


            temp = head.next 
            head.next = prev 
            prev = head 
            head = temp 
            
            reverse(head)
        

        reverse(head)
        return prev 