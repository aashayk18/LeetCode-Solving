class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if (head == None):
            return head
        
        tmp = head
        
        while (tmp.next):
            if (tmp.val == tmp.next.val):
                tmp.next = tmp.next.next
            else:
                tmp = tmp.next
        
        return head
