# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
         #im gonna try another approach, fast and slow pointers? Potentially. 


         #The way its supposed to work is, slow will be before, the one to delete, 
         #fast should be, after the one to delete. 

         #I'm assuming,  we need the length of the linked list first no? 
        if not head: 
            return None 
        
        dummy = ListNode() 
        dummy.next = head 
        length = 0 


        while dummy.next: 
            dummy = dummy.next 
            length += 1 
        
        if length == 1 and n == 1:
            return None 


        #length = length of linked list. cool... now. 

        slow = ListNode() 
        slow.next = head

        fast = head.next 

        nodeToDelete = length - n 
        count = 0 

        if nodeToDelete == count:
            temp = head.next 
            head.next = None 
            head = temp 




        while True: 
            if count == nodeToDelete: 
                slow.next = fast 
                break 
            slow = slow.next 
            fast = fast.next 
            count += 1
        

        return head

