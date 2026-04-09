# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = list1, list2 

        if not list2: 
            return list1 
        elif not list1: 
            return list2 
        #think about, the cases. 

        while l1 and l2:
            if l1.val <= l2.val: 
                while l1.next and l1.next.val <= l2.val: 
                    l1 = l1.next
                temp = l1.next 
                l1.next = l2
                l1 = temp 

            elif l1.val > l2.val: 
                while l2.next and l2.next.val <= l1.val: 
                    l2 = l2.next
                temp = l2.next 
                l2.next = l1 
                l2 = temp
        
        if list1.val <= list2.val: 
            return list1
        
        elif list1.val > list2.val: 
            return list2 


        #But. what about the case where, one of these is true yes, BUT. 
        #l1.next.val < l2.val what do we do then? 

        #Probably traverse l1 till this is no longer true? 

        [5]
        [0, 1]