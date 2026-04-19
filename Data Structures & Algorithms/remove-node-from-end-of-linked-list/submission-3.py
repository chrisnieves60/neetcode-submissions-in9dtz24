# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next: 
            return None 

        def reverse(head): 
            prev = None  

            while head: 
                temp = head.next 
                head.next = prev 
                prev = head 
                head = temp 
            
            return prev


        head = reverse(head)


        dummy = ListNode() 
        dummy.next = head 
        count = 1 


        if n == 1: 
            temp = head 
            head = head.next  
            temp = None 
        
        while True:  
            if count == n:
                temp = dummy.next 
                dummy.next = dummy.next.next 
                temp = None 
                break   
            
            dummy = dummy.next
            count += 1

        


        head = reverse(head)


        return head 