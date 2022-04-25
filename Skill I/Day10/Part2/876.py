# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    import math
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        output = []
        LengthOfHead = 0
        newhead = head
        
        while head:
            LengthOfHead += 1
            head = head.next
        Start = math.ceil((LengthOfHead +1) / 2)
        LengthOfHead = 0
        
        # print(Start)
        # print(LengthOfHead)
        # print(newhead)
        
        while newhead:
            LengthOfHead += 1
            if Start == LengthOfHead:
                output.append(newhead.val)
                Start +=1
            newhead = newhead.next
            
        output.reverse()
        for x in output:
            # print(x)
            head = ListNode(x, next=head)
        return head